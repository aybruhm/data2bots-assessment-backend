# Django Imports
from django.contrib import admin
from django.urls import path, include, re_path

# Rest Framework Imports
from rest_framework import permissions

# DRF Yasg Imports``
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# schema definition
schema_view = get_schema_view(
   openapi.Info(
      title="Data2bots Assessment API",
      default_version='v1',
      contact=openapi.Contact(email="israelvictory87@gmail.com"),
      license=openapi.License(name="CC0-1.0 license"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # authentication endpoints
    path("api/v1/auth/", include("accounts.urls")),
    
    # api docs
    re_path(r'^generate_api_documentation(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='api_docs'),
]
