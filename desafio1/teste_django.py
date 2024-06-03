from django.db import models
from django.shortcuts import render


class Autor(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    publicado = models.DateField()


def index(request):
    livros = Livro.objects.all()
    return render(request, 'teste.html', {'livros': livros})
