from django.urls import path, include
from .views import ip_lookup, download_csv, limpiar_resultados
urlpatterns = [
    path('', ip_lookup, name='ip_lookup'),
    path('download_csv/', download_csv, name='download_csv'),
    path('limpiar_resultados/', limpiar_resultados, name='limpiar_resultados')
]