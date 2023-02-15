from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('registrarMarca/', views.registrarMarca),
    path('edicionMarca/<id_marca>', views.edicionMarca),
    path('editarMarca/', views.editarMarca),
    path('eliminarMarca/<id_marca>', views.eliminarMarca)
]
