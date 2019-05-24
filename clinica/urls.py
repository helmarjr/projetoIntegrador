from django.contrib import admin
from django.urls import path, include
from pacientes import urls as pacientes_url
from home import urls as home_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(home_url), name='home'),
    path('pacientes/', include(pacientes_url), name='pacientes'),
]
