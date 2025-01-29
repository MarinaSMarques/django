from django.db import models

# Create your models here.

class Membro(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Equipe(models.Model):
    nome = models.CharField(max_length=200)
    membros = models.ManyToManyField(Membro, related_name="equipes")

    def __str__(self):
        return self.nome

class Atividade(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField()
    membro_responsavel = models.ForeignKey(Membro, on_delete=models.CASCADE, related_name="atividades")

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    equipe = models.OneToOneField(Equipe, on_delete=models.CASCADE)
    atividades = models.ManyToManyField(Atividade, related_name="projetos")

    def __str__(self):
        return self.nome
