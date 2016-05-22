from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
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


class PessoaCreateView(FormActionMixin, BasePessoa, generic.CreateView):
    template_name = 'core/pessoa_form.html'
    success_url = reverse_lazy('core:list')
    form_action = reverse_lazy('core:criar')

    def get_context_data(self, **kwargs):
        contexto = super(PessoaCreateView, self).get_context_data(**kwargs)
        return contexto

    def form_valid(self, form):
        if self.request.is_ajax():
            d = {
                'mensagem': 'Salvo com sucesso',
                'erros': None
            }
            return JsonResponse(data=d, status=200)
        return super(PessoaCreateView, self).form_valid(form)

    def form_invalid(self, form):
        if self.request.is_ajax():
            d = {
                'mensagem': 'Houve erros',
                'erros': form.errors
            }
            return JsonResponse(data=d, status=400)
        return super(PessoaCreateView, self).form_invalid(form)


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
