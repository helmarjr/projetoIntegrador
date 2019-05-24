from django import forms
from .models import Paciente, Responsavel


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ('nome', 'responsavel')



