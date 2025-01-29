from django.contrib import admin

# Register your models here.
from .models import Membro, Equipe, Atividade, Projeto

class AtividadeInline(admin.TabularInline):
    model = Projeto.atividades.through
    extra = 1

class MembroInline(admin.TabularInline):
    model = Equipe.membros.through
    extra = 1

class ProjetoAdmin(admin.ModelAdmin):
    inlines = [AtividadeInline]

class EquipeAdmin(admin.ModelAdmin):
    inlines = [MembroInline]

admin.site.register(Membro)
admin.site.register(Equipe, EquipeAdmin)
admin.site.register(Atividade)
admin.site.register(Projeto, ProjetoAdmin)
