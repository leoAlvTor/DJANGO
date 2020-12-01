from django.conf.urls import url
from mi_app import views

urlpatterns = [
    url(r'^$', views.Main.open_index),
    url(r'^registro', views.Main.open_registro),
    url(r'^administrar', views.Main.open_administrar),
    url(r'^predecir/', views.Logica.predecir_imagen),
    url(r'^crear_usuario/', views.Logica.crear_usuario),
    url(r'^iniciar_sesion/', views.Logica.iniciar_sesion),
    url(r'^controlador_administrador', views.Logica.controlador_administrador)
]
