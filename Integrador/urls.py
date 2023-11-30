from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from core.urls import router
from django.conf.urls.static import static
from django.conf import settings
from core.views import MovimentacaoViewSet


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('api/v1/cliente/<int:codigo>/movimentacao/', MovimentacaoViewSet.as_view({'get': 'obter_movimentacoes_usuario'}), name='cliente-movimentacoes'),
]

urlpatterns += [
    path('api/v1/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls


