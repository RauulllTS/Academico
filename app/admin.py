from django.contrib import admin
from .models import (
    Cidade, Instituicao, AreaSaber, Ocupacao, Pessoas, Cursos,
    PeriodoCurso, Disciplinas, Matricula, Avaliacoes, Frequencia,
    Turmas, Ocorrencias, DiciplinaCurso, TipoAvaliacao
)

# 1) Ocupação → Pessoas
class PessoaInline(admin.TabularInline):
    model = Pessoas
    extra = 1

class OcupacaoAdmin(admin.ModelAdmin):
    inlines = [PessoaInline]

# 2) Instituição → Cursos
class CursoInline(admin.TabularInline):
    model = Cursos
    extra = 1

class InstituicaoAdmin(admin.ModelAdmin):
    inlines = [CursoInline]

# 3) Área do Saber → Cursos
class CursoAreaSaberInline(admin.TabularInline):
    model = Cursos
    extra = 1

class AreaSaberAdmin(admin.ModelAdmin):
    inlines = [CursoAreaSaberInline]

# 4) Cursos → DiciplinaCurso
class DisciplinaCursoInline(admin.TabularInline):
    model = DiciplinaCurso
    extra = 1

class CursosAdmin(admin.ModelAdmin):
    inlines = [DisciplinaCursoInline]

# 5) Disciplinas → Avaliações
class AvaliacaoInline(admin.TabularInline):
    model = Avaliacoes
    extra = 1

class DisciplinasAdmin(admin.ModelAdmin):
    inlines = [AvaliacaoInline]

# 6) Pessoas → Frequência e Ocorrências
class FrequenciaInline(admin.TabularInline):
    model = Frequencia
    extra = 1

class OcorrenciaInline(admin.TabularInline):
    model = Ocorrencias
    extra = 1

# 7) Cidade → Pessoas
class CidadePessoaInline(admin.TabularInline):
    model = Pessoas
    extra = 1

class CidadeAdmin(admin.ModelAdmin):
    inlines = [CidadePessoaInline]

# 8) Pessoas → Matrícula
class MatriculaInline(admin.TabularInline):
    model = Matricula
    extra = 1

# 9) Pessoa → Avaliações indiretas (por Frequência e Ocorrências já cobrimos bem)
class PessoasAdmin(admin.ModelAdmin):
    inlines = [MatriculaInline, FrequenciaInline, OcorrenciaInline]

# Registros com inlines
admin.site.register(Ocupacao, OcupacaoAdmin)
admin.site.register(Instituicao, InstituicaoAdmin)
admin.site.register(AreaSaber, AreaSaberAdmin)
admin.site.register(Cursos, CursosAdmin)
admin.site.register(Disciplinas, DisciplinasAdmin)
admin.site.register(Pessoas, PessoasAdmin)
admin.site.register(Cidade, CidadeAdmin)

# Registros simples
admin.site.register(PeriodoCurso)
admin.site.register(Matricula)
admin.site.register(Avaliacoes)
admin.site.register(Frequencia)
admin.site.register(Turmas)
admin.site.register(Ocorrencias)
admin.site.register(DiciplinaCurso)
admin.site.register(TipoAvaliacao)
