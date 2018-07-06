# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Usuario
from .models import Seccion
from .models import Patrulla
from .models import Programa
from .models import LineaPrograma
from .models import tipoScout
from .models import tipoDirigente
from .models import Noticia
from .models import Categoria
from .models import ObjetoBiblioteca
from .models import CategoriaCurriculum
from .models import Curriculum
from .models import EtapaProgresion
from .models import Prueba, GrupoScout, nivelCuenta

from .forms import usuarioModelForm
from .forms import seccionModelForm
from .forms import patrullaModelForm
from .forms import tipoScoutModelForm
from .forms import tipoDirigenteModelForm

class AdminUsuario(admin.ModelAdmin):
	list_display = ["nombre", "email", "tipoScout"]
	list_display_links = ["nombre"]
	form = usuarioModelForm
	class Meta:
		model = Usuario

class AdminTipoScout(admin.ModelAdmin):
	list_display = ["tipo"]
	list_display_links = ["tipo"]
	form = tipoScoutModelForm
	class Meta:
		model = tipoScout

class AdminTipoDirigente(admin.ModelAdmin):
	list_display = ["tipo"]
	list_display_links = ["tipo"]
	form = tipoDirigenteModelForm
	class Meta:
		model = tipoDirigente

class AdminSeccion(admin.ModelAdmin):
	list_display = ["nombre"]
	list_display_links = ["nombre"]
	form = seccionModelForm
	class Meta:
		model = Seccion

class AdminNoticia(admin.ModelAdmin):
	list_display = ["user", "fecha", "titulo", "body"]
	list_display_links = ["nombre"]
	form = patrullaModelForm
	class Meta:
		model = Noticia	

admin.site.register(Usuario, AdminUsuario)
admin.site.register(Seccion)
admin.site.register(Patrulla)
admin.site.register(tipoScout, AdminTipoScout)
admin.site.register(tipoDirigente, AdminTipoDirigente)
admin.site.register(Noticia)
admin.site.register(Programa)
admin.site.register(LineaPrograma)
admin.site.register(Categoria)
admin.site.register(ObjetoBiblioteca)
admin.site.register(CategoriaCurriculum)
admin.site.register(Curriculum)
admin.site.register(EtapaProgresion)
admin.site.register(Prueba)
admin.site.register(GrupoScout)
admin.site.register(nivelCuenta)