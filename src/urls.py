"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title='HireHive',
        default_version='V1',
        contact=openapi.Contact(email='hirehive2@gmail.com'),
    ),
    public=True,

)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('swagger/', schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path('redoc/', schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path('api/', include("src.api_urls"))

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
