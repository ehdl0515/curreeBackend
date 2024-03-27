from datetime import datetime

from django.core.management.base import BaseCommand
import logging
import requests
from bs4 import BeautifulSoup

from curreeBackend.models import CurrencyCode, CurrencyRateHist

logger = logging.getLogger(__name__)


class Command(BaseCommand):
	help = 'Run batch task'

	def handle(self, *args, **kwargs):
		try:
			response = requests.get("https://finance.naver.com/marketindex")
			soup = BeautifulSoup(response.text, "html.parser")

			get_datetime = soup.select_one("span.date").get_text(strip=True)
			convert_date, convert_time = get_datetime.split(" ")
			convert_date = convert_date.replace(".", "-")
			standard = soup.select_one("span.standard").get_text(strip=True).split(" ")[0]
			round = int(soup.select_one("span.round").get_text(strip=True)[4:-1])

			print(convert_date, convert_time, standard, round)

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
					# print(f"CurrencyCode] save complete - {obj}")

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
					print(f"CurrencyRateHist] save complete - {obj}")
				except Exception as e:
					print(e)
		except Exception as e:
			print(e)

