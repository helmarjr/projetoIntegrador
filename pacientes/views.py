from django.shortcuts import render, redirect
from .models import Paciente
from .forms import PacienteForm


# Create your views here.
def lista_pacientes(request):

    pacientes = Paciente.objects.all()

    return render(request, 'pacientes/pacientes_list.html', {'pacientes': pacientes})


def detalhe_paciente(request, pk):
    paciente = Paciente.objects.get(pk=pk)

    return render(request, 'pacientes/pacientes_detail.html', {'paciente': paciente})


def novo_paciente(request):

    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.save()
            return redirect('lista_pacientes')
    else:
        form = PacienteForm()

    return render(request, 'pacientes/pacientes_edit.html', {'form': form})






