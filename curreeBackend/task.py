import logging
import requests
from apscheduler.triggers.cron import CronTrigger
from bs4 import BeautifulSoup

from curreeBackend.models import CurrencyRateHist
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

logger = logging.getLogger(__name__)


def run():
	try:
		logger.debug("TASK START")
		response = requests.get("https://finance.naver.com/marketindex")
		soup = BeautifulSoup(response.text, "html.parser")

		get_datetime = soup.select_one("span.date").get_text(strip=True)
		convert_date, convert_time = get_datetime.split(" ")
		convert_date = convert_date.replace(".", "-")
		standard = soup.select_one("span.standard").get_text(strip=True).split(" ")[0]
		round = int(soup.select_one("span.round").get_text(strip=True)[4:-1])

		logger.debug(convert_date, convert_time, standard, round)

		response = requests.get("https://finance.naver.com/marketindex/exchangeList.naver")
		soup = BeautifulSoup(response.text, "html.parser")

		rows = soup.select(" tbody > tr")

		exchange_rates = dict()
		for row in rows:
			currency = row.select_one("td.tit").get_text(strip=True)
			rate = row.select_one("td.sale").get_text(strip=True)
			exchange_rates[currency] = rate

		for key, value in exchange_rates.items():
			if key == "일본 JPY (100엔)":
				nation, code, unit = map(str, key.split(" "))
				unit = unit[1:-2]
			elif key in ["베트남 VND 100", "인도네시아 IDR 100"]:
				nation, code, unit = map(str, key.split(" "))
			else:
				nation, code = map(str, key.rsplit(" ", maxsplit=1))
				unit = 1

			rate = float(value.replace(",", ""))

			try:
				# obj = CurrencyCode(nation=nation, code=code, name="", unit=unit)
				# obj.save()
				# logger.debug(f"CurrencyCode] save complete - {obj}")

				obj = CurrencyRateHist(
					round=round,
					standard=standard,
					convertDate=convert_date,
					convertTime=convert_time,
					baseCurrency="KRW",
					convertCurrency=code,
					rate=rate,
				)
				obj.save()
				logger.debug(f"CurrencyRateHist] save complete - {obj}")
			except Exception as e:
				logger.debug(e)
	except Exception as e:
		logger.error(e)


cron_expression = "*/10 9-18 * * 1-5"
trigger = CronTrigger.from_crontab(cron_expression)
scheduler.add_job(run, trigger, id="run")
logger.debug(f"add_job run {cron_expression}")
