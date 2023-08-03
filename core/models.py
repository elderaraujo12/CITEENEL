from django.db import models

# Create your models here.
from django.db import models

class Participante(models.Model):
    nome = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True, null=False)
    instituicao_empresa = models.CharField(max_length=200, null=False)
    conhecimento_choices = [
        ('redes_sociais', 'Redes sociais'),
        ('email', 'Email'),
        ('colegas', 'Colegas de trabalho'),
        ('edicoes_anteriores', 'Edições anteriores'),
        ('outros', 'Outros'),
    ]
    como_conheceu = models.CharField(max_length=50, choices=conhecimento_choices)

    def __str__(self):
        return self.nome
