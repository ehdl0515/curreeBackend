from django.db.models import Max, F
from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.response import Response
from curreeBackend.schemas import *
from curreeBackend.serializers import *
from curreeBackend.models import *
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter, OpenApiExample


# Create your views here.
def index(request):
	return render(request, 'templates/index.html')


class CurrencyCodeFilter(filters.FilterSet):
	# lookup_expr: startswith, endswith, lte, gte, range, in, exact
	code = filters.CharFilter(field_name='code', lookup_expr='exact')
	name = filters.CharFilter(field_name='name', lookup_expr='exact')
	nation = filters.CharFilter(field_name='nation', lookup_expr='exact')
	unit = filters.NumberFilter(field_name='unit', lookup_expr='exact')

	class Meta:
		model = CurrencyCode
		fields = ['code', 'name', 'nation', 'unit']


class CurrencyCodeList(generics.ListCreateAPIView):
	queryset = CurrencyCode.objects.all()
	serializer_class = CurrencyCodeSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filterset_class = CurrencyCodeFilter

	@extend_schema(
		tags=["화폐"],
		summary="화폐 조회",
		parameters=CURRENCY_CODE_LIST_PARAM_EXAMPLES,
	)
	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	@extend_schema(
		tags=["화폐"],
		summary="화폐 추가",
		examples=CURRENCY_CODE_CREATE_BODY_EXAMPLES,
	)
	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


class CurrencyCodeDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = CurrencyCode.objects.all()
	serializer_class = CurrencyCodeSerializer

	@extend_schema(
		tags=["화폐"],
		summary="화폐 조회 (code)",
		parameters=[CURRENCY_CODE_PARAM_EXAMPLE],
	)
	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	@extend_schema(
		tags=["화폐"],
		summary="화폐 정보 일괄 변경",
		parameters=[CURRENCY_CODE_PARAM_EXAMPLE],
		examples=CURRENCY_CODE_UPDATE_BODY_EXAMPLES,
	)
	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	@extend_schema(
		tags=["화폐"],
		summary="화폐 정보 일부 변경",
		parameters=[CURRENCY_CODE_PARAM_EXAMPLE],
		examples=CURRENCY_CODE_UPDATE_BODY_EXAMPLES,
	)
	def patch(self, request, *args, **kwargs):
		return self.partial_update(request, *args, **kwargs)

	@extend_schema(
		tags=["화폐"],
		summary="화폐 삭제",
		parameters=[CURRENCY_CODE_PARAM_EXAMPLE],
	)
	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)


class ProfileFilter(filters.FilterSet):
	profileNo = filters.NumberFilter(field_name='profileNo', lookup_expr='exact')
	deviceId = filters.CharFilter(field_name='deviceId', lookup_expr='exact')
	subCurrency = filters.CharFilter(field_name='subCurrency', lookup_expr='exact')
	exchangeMinimum = filters.ChoiceFilter(choices=EXCHANGE_MINIMUMS, field_name='exchangeMinimum', lookup_expr='exact')
	exchangeMaximum = filters.ChoiceFilter(choices=EXCHANGE_MAXIMUMS, field_name='exchangeMaximum', lookup_expr='exact')
	exchangeIncreaseUnit = filters.ChoiceFilter(choices=EXCHANGE_INCREASE_UNITS, field_name='exchangeIncreaseUnit', lookup_expr='exact')

	class Meta:
		model = Profile
		fields = ['profileNo', 'deviceId', 'subCurrency', 'exchangeMinimum', 'exchangeMaximum', 'exchangeIncreaseUnit']


class ProfileList(generics.ListCreateAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filterset_class = ProfileFilter

	@extend_schema(
		tags=["프로파일"],
		summary="프로파일 조회",
		parameters=PROFILE_LIST_PARAM_EXAMPLES,
	)
	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	@extend_schema(
		tags=["프로파일"],
		summary="프로파일 추가",
		examples=PROFILE_CREATE_BODY_EXAMPLES,
	)
	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer

	@extend_schema(
		tags=["프로파일"],
		summary="프로파일 조회 (profileNo)",
		parameters=[PROFILE_NO_PARAM_EXAMPLE],
	)
	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	@extend_schema(
		tags=["프로파일"],
		summary="프로파일 정보 일괄 변경",
		parameters=[PROFILE_NO_PARAM_EXAMPLE],
		examples=PROFILE_UPDATE_BODY_EXAMPLES,
	)
	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	@extend_schema(
		tags=["프로파일"],
		summary="프로파일 정보 일부 변경",
		parameters=[PROFILE_NO_PARAM_EXAMPLE],
		examples=PROFILE_UPDATE_BODY_EXAMPLES,
	)
	def patch(self, request, *args, **kwargs):
		return self.partial_update(request, *args, **kwargs)

	@extend_schema(
		tags=["프로파일"],
		summary="프로파일 삭제",
		parameters=[PROFILE_NO_PARAM_EXAMPLE],
	)
	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)


class CurrencyRateHistFilter(filters.FilterSet):
	round = filters.NumberFilter(field_name="round", lookup_expr="exact")
	standard = filters.CharFilter(field_name='standard', lookup_expr='exact')
	convertDate = filters.DateFilter(field_name="convertDate", lookup_expr="gte")
	convertTime = filters.TimeFilter(field_name="convertTime", lookup_expr="gte")
	baseCurrency = filters.CharFilter(field_name='baseCurrency', lookup_expr='exact')
	convertCurrency = filters.CharFilter(field_name='convertCurrency', lookup_expr='exact')
	rate = filters.NumberFilter(field_name="rate", lookup_expr="exact")

	class Meta:
		model = CurrencyRateHist
		fields = ['round', 'standard', 'convertDate', 'convertTime', 'baseCurrency', 'convertCurrency', 'rate']


class CurrencyRateHistList(generics.ListCreateAPIView):
	queryset = CurrencyRateHist.objects.all()
	serializer_class = CurrencyRateHistSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filterset_class = CurrencyRateHistFilter

	@extend_schema(
		tags=["환율"],
		summary="환율 조회",
		parameters=CURRENCY_RATE_HIST_LIST_PARAM_EXAMPLES,
	)
	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	@extend_schema(
		tags=["환율"],
		summary="환율 정보 추가",
		examples=CURRENCY_RATE_HIST_CREATE_BODY_EXAMPLES,
	)
	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

# class CurrencyRateHistDetail(generics.RetrieveAPIView):
# 	queryset = CurrencyRateHist.objects.all()
# 	serializer_class = CurrencyRateHistSerializer
# 	lookup_field = 'convertCurrency'
#
# 	@extend_schema(
# 		tags=["환율"],
# 		summary="환율 조회",
# 		parameters=[CONVERT_CURRENCY_PARAM_EXAMPLE],
# 	)
# 	def get(self, request, *args, **kwargs):
# 		return self.retrieve(request, *args, **kwargs)
#
#
# class CurrencyRateHistDateDetail(generics.RetrieveAPIView):
# 	queryset = CurrencyRateHist.objects.all()
# 	serializer_class = CurrencyRateHistSerializer
# 	lookup_field = 'convertDate'
#
# 	@extend_schema(
# 		tags=["환율"],
# 		summary="환율 조회",
# 		parameters=[CONVERT_CURRENCY_DATE_PARAM_EXAMPLE],
# 	)
# 	def get(self, request, *args, **kwargs):
# 		return self.retrieve(request, *args, **kwargs)


class CurrencyRateHistLatestFilter(filters.FilterSet):
	round = filters.NumberFilter(field_name="round", lookup_expr="exact")
	standard = filters.CharFilter(field_name='standard', lookup_expr='exact')
	convertDate = filters.DateFilter(field_name="convertDate", lookup_expr="gte")
	convertTime = filters.TimeFilter(field_name="convertTime", lookup_expr="gte")
	baseCurrency = filters.CharFilter(field_name='baseCurrency', lookup_expr='exact')
	convertCurrency = filters.CharFilter(field_name='convertCurrency', lookup_expr='exact')
	rate = filters.NumberFilter(field_name="rate", lookup_expr="exact")

	class Meta:
		model = CurrencyRateHist
		fields = ['convertCurrency']

	def filter_queryset(self, queryset):
		base_currency = self.request.query_params.get('baseCurrency')
		convert_currency = self.request.query_params.get('convertCurrency')
		latest_records = queryset.filter(
			baseCurrency=base_currency,
			convertCurrency=convert_currency,
		).annotate(
			# max_convert_datetime=Max(F('convertDate') + F('convertTime'), output_field=models.DateTimeField())
			max_convert_date=Max('convertDate'),
			max_convert_time=Max('convertTime'),
		# ).order_by('-max_convert_datetime')
		).order_by('-max_convert_date', '-max_convert_time')[:2]
		return latest_records


class CurrencyRateHistLatest(generics.ListAPIView):
	queryset = CurrencyRateHist.objects.all()
	serializer_class = CurrencyRateHistSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filterset_class = CurrencyRateHistLatestFilter

	@extend_schema(
		tags=["환율"],
		summary="최신, 이전 환율 조회",
		parameters=CURRENCY_RATE_HIST_LIST_PARAM_EXAMPLES,
	)
	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)
