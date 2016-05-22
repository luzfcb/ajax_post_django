from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$',
        views.PessoaListView.as_view(),
        name='list'
        ),
    url(r'^criar/',
        views.PessoaCreateView.as_view(),
        name='criar'
        ),
    url(r'^editar/(?P<pk>\d+)/$',
        views.PessoaEditView.as_view(),
        name='editar'
        ),
]
