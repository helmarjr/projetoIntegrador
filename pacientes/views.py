from django.shortcuts import render

# Create your views here.


def lista_pacientes(request):
    return render(request, 'pacientes/pacientes_list.html')


