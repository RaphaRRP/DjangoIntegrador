from django.contrib import admin
from django.urls import path, include
from django.urls import re_path


urlpatterns = [
    path('api/v1/', include('core.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
]

urlpatterns += [
    path('api/v1/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
]


