"""
URL configuration for curreeBackend_config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from drf_spectacular.views import SpectacularJSONAPIView, SpectacularRedocView, SpectacularSwaggerView, SpectacularYAMLAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("curreeBackend.urls")),
    path("api/", include("rest_framework.urls")),
]


if settings.DEBUG:
    urlpatterns += [
        # Open API 자체를 조회 : json, yaml,
        path("docs/json/", SpectacularJSONAPIView.as_view(), name="schema-json"),
        path("docs/yaml/", SpectacularYAMLAPIView.as_view(), name="swagger-yaml"),
        # Open API Document UI로 조회: Swagger, Redoc
        path("docs/swagger/", SpectacularSwaggerView.as_view(url_name="schema-json"), name="swagger-ui"),
        path("docs/redoc/", SpectacularRedocView.as_view(url_name="schema-json"), name="redoc", ),
    ]
