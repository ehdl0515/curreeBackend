from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


CURRENCIES = [
	"KRW",
	"USD",
	"JPY",
	"CNY",
	"EUR",
]

EXCHANGE_MINIMUMS = (
	(0, 0),
	(10, 10),
	(50, 50),
	(100, 100),
	(500, 500),
	(1000, 1000),
	(5000, 5000),
	(10000, 10000),
)

EXCHANGE_MAXIMUMS = (
	(100, 100),
	(500, 500),
	(1000, 1000),
	(2000, 2000),
	(5000, 5000),
	(10000, 10000),
)

EXCHANGE_INCREASE_UNITS = (
	(5, 5),
	(10, 10),
	(50, 50),
	(100, 100),
	(500, 500),
	(1000, 1000),
	(2000, 2000),
	(5000, 5000),
	(10000, 10000),
)


class BaseModel(models.Model):
	createTime = models.DateTimeField(auto_now_add=True)
	updateTime = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class CurrencyCode(BaseModel):
	code = models.CharField(max_length=10, primary_key=True)
	name = models.CharField(max_length=20)
	nation = models.CharField(max_length=50)
	unit = models.PositiveSmallIntegerField(default=1)
	createTime = BaseModel.createTime
	updateTime = BaseModel.updateTime

	class Meta:
		ordering = ['code', 'name', 'nation', 'unit']


class Profile(BaseModel):
	profileNo = models.AutoField(primary_key=True)
	deviceId = models.CharField(max_length=200, default="", unique=True)
	subCurrency = models.CharField(max_length=20, default=2)
	exchangeMinimum = models.PositiveIntegerField(choices=EXCHANGE_MINIMUMS, default=EXCHANGE_MINIMUMS[0][1])
	exchangeMaximum = models.PositiveIntegerField(choices=EXCHANGE_MAXIMUMS, default=EXCHANGE_MAXIMUMS[0][1])
	exchangeIncreaseUnit = models.PositiveIntegerField(choices=EXCHANGE_INCREASE_UNITS, default=EXCHANGE_INCREASE_UNITS[0][1])
	createTime = BaseModel.createTime
	updateTime = BaseModel.updateTime

	def __str__(self):
		return f"{self.profileNo} - {self.deviceId}, {self.subCurrency} - {self.exchangeMinimum, self.exchangeMaximum, self.exchangeIncreaseUnit}"


class CurrencyRateHist(models.Model):
	histNo = models.AutoField(primary_key=True)
	round = models.PositiveIntegerField()
	standard = models.CharField(max_length=20)
	convertDate = models.DateField(default=timezone.now)
	convertTime = models.TimeField(default=timezone.now)
	baseCurrency = models.CharField(max_length=20, default=CURRENCIES[0])
	convertCurrency = models.CharField(max_length=20)
	rate = models.FloatField()

	def __str__(self):
		return f"{self.histNo, self.round, self.convertDate, self.convertTime, self.standard, self.baseCurrency, self.convertCurrency, self.rate}"
