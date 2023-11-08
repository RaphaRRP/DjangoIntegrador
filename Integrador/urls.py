from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from core.urls import router


urlpatterns = [
    #path('api/v1/', include('core.urls')),
    path('api/v2/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
]

urlpatterns += [
    path('api/v2/', include('djoser.urls')),
    path('api/v2/auth/', include('djoser.urls.authtoken')),
    path('api/v2/auth/', include('djoser.urls.jwt')),
]


