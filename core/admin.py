from django.contrib import admin

from . import models


@admin.register(models.Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', )
