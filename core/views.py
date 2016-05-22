from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from django.views import generic
from . import models
from . import forms


class FormActionMixin(object):
    form_action = None

    def get_form_action(self):
        return self.form_action

    def get_context_data(self, **kwargs):
        contexto = super(FormActionMixin, self).get_context_data(**kwargs)
        contexto.update(
            {
                'form_action': self.get_form_action()
            }
        )
        return contexto


class BasePessoa(object):
    model = models.Pessoa
    form_class = forms.PessoaCreateForm

    def get_context_data(self, **kwargs):
        contexto = super(BasePessoa, self).get_context_data(**kwargs)
        contexto.update(
            {
                'variavel_a_mais': "Hahahha"
            }
        )
        return contexto
    

class PessoaCreateView(LoginRequiredMixin, FormActionMixin, BasePessoa, generic.CreateView):
    template_name = 'core/pessoa_form.html'
    success_url = reverse_lazy('core:list')
    form_action = reverse_lazy('core:criar')

    def get_context_data(self, **kwargs):
        contexto = super(PessoaCreateView, self).get_context_data(**kwargs)
        return contexto


class PessoaEditView(FormActionMixin, BasePessoa, generic.UpdateView):
    template_name = 'core/pessoa_form.html'
    success_url = reverse_lazy('core:list')

    def get_form_action(self):
        return reverse_lazy('core:editar',
                            kwargs={'pk': self.object.pk}
                            )


class PessoaListView(generic.ListView):
    model = models.Pessoa
    template_name = 'core/pessoa_list.html'
