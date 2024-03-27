from rest_framework import serializers
from curreeBackend.models import *


class CurrencyCodeSerializer(serializers.ModelSerializer):
	class Meta:
		model = CurrencyCode
		fields = '__all__'
		extra_kwargs = {
			'code': {'required': False},
			'name': {'required': False},
			'nation': {'required': False},
			'unit': {'required': False},
		}


class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = '__all__'


class CurrencyRateHistSerializer(serializers.ModelSerializer):
	class Meta:
		model = CurrencyRateHist
		fields = '__all__'



