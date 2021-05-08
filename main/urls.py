from django.urls import path
from . import views

app_name = "main"


urlpatterns = [
    path('', views.home, name="home"),
    path('home.html', views.home, name='home'),
    path('simulation.html', views.simulation, name="simulation"),

    # Urls de servicos
    path('merca_lib_ener.html', views.merca_lib_ener, name="merca_lib_ener"),
    path('bater_conde.html', views.bater_conde, name="bater_conde"),
    path('autit_cert_ener.html', views.autit_cert_ener, name="autit_cert_ener"),
    path('ilumina_led.html', views.ilumina_led, name="ilumina_led"),
    path('autoconsumo_foto.html', views.autoconsumo_foto, name="autoconsumo_foto"),
    path('carrega_viatu_eletric.html', views.carrega_viatu_eletric, name="carrega_viatu_eletric"),
    path('sistem_monito_energ.html', views.sistem_monito_energ, name="sistem_monito_energ"),

]
