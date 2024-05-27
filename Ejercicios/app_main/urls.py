from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('1', views.mcd, name='mcd'),
    path('maximo-comun-divisor', views.mcd, name='mcd'),
    path('2', views.mcm, name='mcm'),
    path('miimo-comun-multiplo', views.mcm, name='mcm'),
    path('3', views.contar_palabras, name='contar_palabras'),
    path('contar-palabras', views.contar_palabras, name='contar_palabras'),
    path('4', views.palabra_popular, name='palabra_popular'),
    path('palabra-popular', views.palabra_popular, name='palabra_popular'),
    path('5', views.value_error, name='value_error'),
    path('value-error', views.value_error, name='value_error'),
    path('6', views.persona, name='persona'),
    path('persona', views.persona, name='persona'),
    path('7', views.cuenta, name='cuenta'),
    path('cuenta', views.cuenta, name='cuenta'),
    path('8', views.cuenta_joven, name='cuenta_joven'),
    path('cuenta_joven', views.cuenta_joven, name='cuenta_joven'),
]