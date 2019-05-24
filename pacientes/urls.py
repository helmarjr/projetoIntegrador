from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pacientes, name='lista_pacientes'),
    path('paciente/<int:pk>', views.detalhe_paciente, name='detalhe_paciente'),
    path('paciente/novo/', views.novo_paciente, name='novo_paciente'),
]
