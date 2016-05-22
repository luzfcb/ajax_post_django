from django import forms
from . import models


class PessoaCreateForm(forms.ModelForm):
    class Meta:
        model = models.Pessoa
        fields = '__all__'
