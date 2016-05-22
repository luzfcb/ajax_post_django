from django.core.validators import MinValueValidator
from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    idade = models.PositiveIntegerField(default=18, validators=[MinValueValidator(18)])
