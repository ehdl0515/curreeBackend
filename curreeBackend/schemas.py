from drf_spectacular.utils import OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from django.utils import timezone
from curreeBackend import serializers
from curreeBackend.models import *

CURRENCY_CODE_PARAM_EXAMPLE = OpenApiParameter(
	name="code",
	type=OpenApiTypes.STR,
	location=OpenApiParameter.PATH,
	description="화폐 코드",
)


PROFILE_NO_PARAM_EXAMPLE = OpenApiParameter(
	name="profileNo",
	type=OpenApiTypes.INT,
	location=OpenApiParameter.PATH,
	description="프로파일 번호",
)


CONVERT_CURRENCY_PARAM_EXAMPLE = OpenApiParameter(
	name="convertCurrency",
	type=OpenApiTypes.STR,
	enum=CURRENCIES,
	location=OpenApiParameter.PATH,
	description="변환 통화",
)

CONVERT_CURRENCY_DATE_PARAM_EXAMPLE = OpenApiParameter(
	name="convertDate",
	type=OpenApiTypes.DATE,
	location=OpenApiParameter.PATH,
	description="환율 적용 일자",
)

"""
CURRENCY_CODE
"""

CURRENCY_CODE_LIST_PARAM_EXAMPLES = [
	OpenApiParameter(
		name='code',
		type=OpenApiTypes.STR,
		description="화폐 코드",
		required=False,
	),
	OpenApiParameter(
		name="name",
		type=OpenApiTypes.STR,
		description="화폐명",
		required=False,
	),
	OpenApiParameter(
		name="nation",
		type=OpenApiTypes.STR,
		description="국가명",
		required=False,
	),
	OpenApiParameter(
		name="unit",
		type=OpenApiTypes.INT,
		description="화폐 단위",
		required=False,
	),
]

CURRENCY_CODE_CREATE_BODY_EXAMPLES = [
	OpenApiExample(
		summary="신규화폐 등록",
		name="신규화폐 등록",
		value={
			"code": "TES",
			"name": "테스트",
			"nation": "테스터",
		},
		request_only=True,
	),
]

CURRENCY_CODE_UPDATE_BODY_EXAMPLES = [
	OpenApiExample(
		summary="화폐 단위 변경",
		name="단위 변경",
		value={
			"unit": 100,
		},
		request_only=True,
	),
]


"""
PROFILE
"""

PROFILE_LIST_PARAM_EXAMPLES = [
	OpenApiParameter(
		name='profileNo',
		type=OpenApiTypes.INT,
		description="프로파일 번호",
		required=False,
	),
	OpenApiParameter(
		name="deviceId",
		type=OpenApiTypes.STR,
		description="기기 아이디",
		required=False,
	),
	OpenApiParameter(
		name="subCurrency",
		type=OpenApiTypes.STR,
		description="보조 통화",
		enum=CURRENCIES,
		required=False,
	),
	OpenApiParameter(
		name="exchangeMinimum",
		type=OpenApiTypes.INT,
		description="주 통화 최소금액",
		enum=[k[1] for k in EXCHANGE_MINIMUMS],
		required=False,
	),
	OpenApiParameter(
		name="exchangeMaximum",
		type=OpenApiTypes.INT,
		description="주 통화 최대금액",
		enum=[k[1] for k in EXCHANGE_MAXIMUMS],
		required=False,
	),
	OpenApiParameter(
		name="exchangeIncreaseUnit",
		type=OpenApiTypes.INT,
		description="주 통화 증가폭",
		enum=[k[1] for k in EXCHANGE_INCREASE_UNITS],
		required=False,
	),
]

PROFILE_CREATE_BODY_EXAMPLES = [
	OpenApiExample(
		summary="신규프로파일 등록",
		name="신규프로파일 등록",
		value={
			"deviceId": "tester",
			"subCurrency": CURRENCIES[1],
			"exchangeMinimum": EXCHANGE_MINIMUMS[1][1],
			"exchangeMaximum": EXCHANGE_MAXIMUMS[2][1],
			"exchangeIncreaseUnit": EXCHANGE_INCREASE_UNITS[1][1],
		},
		request_only=True,
	),
]

PROFILE_UPDATE_BODY_EXAMPLES = [
	OpenApiExample(
		summary="할당된 profileNo 변경",
		name="할당된 profileNo 변경",
		value={
			"profileNo": 3,
		},
		request_only=True,
	),
]


"""
CURRENCY_RATE_HIST
"""

CURRENCY_RATE_HIST_LIST_PARAM_EXAMPLES = [
	OpenApiParameter(
		name="round",
		type=OpenApiTypes.INT,
		description="고시회차",
		required=False,
	),
	OpenApiParameter(
		name="standard",
		type=OpenApiTypes.STR,
		description="기준",
		required=False,
	),
	OpenApiParameter(
		name="convertDate",
		type=OpenApiTypes.DATE,
		description="환율 고시 일자",
		required=False,
	),
	OpenApiParameter(
		name="convertTime",
		type=OpenApiTypes.TIME,
		description="환율 고시 시각",
		required=False,
	),
	OpenApiParameter(
		name="baseCurrency",
		type=OpenApiTypes.STR,
		description="베이스 통화",
		default=CURRENCIES[0],
		required=True,
	),
	OpenApiParameter(
		name="convertCurrency",
		type=OpenApiTypes.STR,
		description="변환 통화",
		enum=CURRENCIES,
		required=False,
	),
	OpenApiParameter(
		name="rate",
		type=OpenApiTypes.DECIMAL,
		description="적용 환율",
		required=False,
	),
]

CURRENCY_RATE_HIST_CREATE_BODY_EXAMPLES = [
	OpenApiExample(
		summary="신규 환율 정보 등록",
		name="신규 환율 정보 등록",
		value={
			"round": 234,
			"standard": "하나은행",
			"convertTime": timezone.now(),
			"baseCurrency": CURRENCIES[0],
			"convertCurrency": CURRENCIES[1],
			"rate": 1000.5,
		},
		request_only=True,
	),
]
