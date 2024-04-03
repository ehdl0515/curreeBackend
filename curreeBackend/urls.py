from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
	# path('', views.index, name='index'),
	path('profile', views.ProfileList.as_view(), name='profile-list'),
	path('profile/<int:pk>', views.ProfileDetail.as_view(), name='profile-detail'),
	path('currency', views.CurrencyCodeList.as_view(), name='currency-list'),
	path('currency/<str:pk>', views.CurrencyCodeDetail.as_view(), name='currency-detail'),
	path('currencyRate', views.CurrencyRateHistList.as_view(), name='currency-rate-list'),
	path('currencyRateLatest', views.CurrencyRateHistLatest.as_view(), name='currency-rate-latest'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
