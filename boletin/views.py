# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .forms import UsuarioForm, usuarioModelForm, programaModelForm, lineaProgramaModelForm,datosPadreModelForm
from .forms import datosApoderadoModelForm, datosMedicosModelForm, curriculumModelForm, usuarioBeneficiarioModelForm
from .forms import EtapaProgresionModelForm, PuntajeModelForm, CambiarContrasenaModelForm
from .forms import usuarioDirigenteModelForm, SeccionModelForm, PatrullaModelForm, NoticiaModelForm
from .forms import ProvinciaModelForm, LocalidadModelForm, GrupoModelForm, PreguntaNoticiaModelForm
from .forms import PreguntaNoticia2ModelForm
from .models import Usuario, Programa, LineaPrograma, Seccion, Noticia, Categoria, ObjetoBiblioteca, Patrulla
from .models import DatosPadres, DatosApoderado, DatosMedicos,Curriculum, Asistencia, Prueba
from .models import EtapaProgresion, GrupoScout, PruebaViews, Puntaje, PuntajeTotal,tipoScout
from .models import Provincia, Localidad, tipoDirigente, PreguntaNoticia
# Create your views here.

from django.http import HttpResponse
import time


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

def inicio(request):
	titulo = "Hola"
	if request.user.is_authenticated():
		titulo = "Bienvenido %s" % (request.user)
	else:
		form = UsuarioForm(request.POST or None)
		context ={

		"titulo" : titulo,
		"el_form": form,
		}
		
	return render (request, "inicio.html", context)

def index(request):
	usuario = Usuario.objects.get(user=request.user.id)
	noticias = Noticia.objects.filter(Grupo=usuario.Grupo.id).order_by('fecha')[::-1]
	preguntas = PreguntaNoticia.objects.all()
	if request.method == 'POST':
		form = PreguntaNoticiaModelForm(request.POST)
		if form.is_valid():
			guardar = form.save(commit=False)
			guardar.Noticia = noticia
			guardar.user = usuario.nombre+ " "+ usuario.apellido
			guardar.save()
			return redirect(request.build_absolute_uri())
	else:
		form = PreguntaNoticiaModelForm()
	contexto = {'noticias':noticias, 'usuario': usuario, 'preguntas': preguntas, 'form':form}
	return render(request, 'noticias.html', contexto)

def preguntaNoticia(request, id_noticia):
	usuario = Usuario.objects.get(user=request.user.id)
	noticia = Noticia.objects.get(id=id_noticia)
	preguntas = PreguntaNoticia.objects.all()

	if request.method == 'POST':
		form = PreguntaNoticiaModelForm(request.POST)
		if form.is_valid():
			guardar = form.save(commit=False)
			guardar.Noticia = noticia
			guardar.user = usuario.nombre+ " "+ usuario.apellido
			guardar.save()
			return redirect(request.build_absolute_uri())
	else:
		form = PreguntaNoticiaModelForm()

	contexto = {'usuario': usuario, 'form':form, 'noticia': noticia, 'preguntas': preguntas}
	return render(request, 'noticia.html', contexto)

def respuestaNoticia(request, id_pregunta):
	usuario = Usuario.objects.get(user=request.user.id)
	pregunta = PreguntaNoticia.objects.get(id=id_pregunta)
	noticia = Noticia.objects.get(id=pregunta.Noticia.id)

	if request.method == 'POST':
		form = PreguntaNoticia2ModelForm(request.POST)
		if form.is_valid():
			guardar = form.save(commit=False)
			pregunta.respuesta = guardar.pregunta
			pregunta.save()
			return redirect(request.build_absolute_uri())
	else:
		form = PreguntaNoticia2ModelForm()

	contexto = {'usuario': usuario, 'form':form, 'noticia': noticia, 'pregunta': pregunta}
	return render(request, 'respuestaNoticia.html', contexto)

def biblioteca(request):
	usuario = Usuario.objects.get(user=request.user.id)
	categorias = Categoria.objects.all().order_by('nombre')
	contexto = {'categorias':categorias, 'usuario': usuario}
	return render(request, 'biblioteca.html', contexto)

def verCategoria(request, id_categoria):
	usuario = Usuario.objects.get(user=request.user.id)
	archivos = ObjetoBiblioteca.objects.filter(categoria=id_categoria).order_by('nombre')
	contexto = {'archivos':archivos, 'usuario': usuario}
	return render(request, 'verCategoria.html', contexto)

def verSeccion(request):
	usuario = Usuario.objects.get(user=request.user.id)
	patrullas = Patrulla.objects.filter(Seccion=usuario.Seccion.id).order_by('nombre')
	beneficiarios = Usuario.objects.filter(Seccion=usuario.Seccion.id).filter(tipoScout=2)
	contexto = {'patrullas':patrullas, 'beneficiarios':beneficiarios, 'usuario': usuario}
	return render(request, 'miSeccion.html', contexto)

def verMiProgresion(request):
	usuario = Usuario.objects.get(user=request.user.id)
	pruebas = Prueba.objects.filter(etapa=usuario.etapa.id).order_by('descripcion')
	pruebasMias = usuario.pruebas.all()

	lista = []

	for prueba in pruebas:
		num = 0
		pv = PruebaViews()
		pv.descripcion = prueba.descripcion
		pv.url = prueba.id
		for pruebaMia in pruebasMias:
			if prueba == pruebaMia:
				num = 1
				pv.estado = 1
		if num == 0:
			pv.estado=0
		lista.append(pv)
	
	contexto = {'usuario': usuario, 'pruebas':lista}
	return render(request, 'miProgresion.html', contexto)

def verCurriculum(request, id_user):
	usuario = Usuario.objects.get(user=request.user.id)
	user = Usuario.objects.get(id=id_user)
	curriculum = Curriculum.objects.filter(usuario=id_user).order_by('fecha')

	if request.method == 'POST':
		form = curriculumModelForm(request.POST)
		if form.is_valid():
			guardar = form.save(commit=False)
			guardar.usuario=user
			guardar.save()
		return redirect(request.build_absolute_uri())
	else:
		form = curriculumModelForm()

	contexto = {'usuario': usuario, 'curris':curriculum, 'form':form, 'iduser': id_user,}
	return render(request, 'curriculumScout.html', contexto)

#views para jefe de seccion
def crearUsuario(request):
	usuario = Usuario.objects.get(user=request.user.id)
	pruebas = Prueba.objects.all()
	tipo = tipoScout.objects.get(id=2)

	if request.method == 'POST':
		form = usuarioModelForm(request.POST)
		if form.is_valid():
			guardar = form.save(commit=False)
			guardar.Seccion = usuario.Seccion
			guardar.tipoScout = tipo
			guardar.Grupo = usuario.Grupo
			dp = DatosPadres()
			dp.fundacionPadre='2018-06-20'
			dp.fundacionMadre = '2018-06-20'
			da = DatosApoderado()
			da.fundacion = '2018-06-20'
			da.viveConEl=1
			dm = DatosMedicos()
			dm.varicela = 0
			dm.sarampion = 0
			dm.meringitis = 0
			dm.rubeola = 0
			dm.paperas = 0
			dm.tifoidea = 0
			dm.hepatitis = 0
			dm.hanta = 0
			dm.apendicitis = 0
			dm.escarlinata = 0
			dm.convulcion = 0
	
			dm.parasetamol = 0
			dm.ibuprofeno = 0
			dm.clorfenamina = 0
			dm.loratadina = 0
			dm.viadil = 0
			dm.amoxisilina = 0

			dm.alergiaAlimentaria = 0
			dm.alergiaMedicamento = 0
			dm.utilizaLentes = 0
			dm.esguince = 0
			dm.fractura = 0
			dm.operado = 0
			dm.columna = 0
			dm.piePlano = 0
			dm.pieAtleta = 0
			dm.movilidadReducida = 0
			dm.hernias = 0

			dm.diabetes = 0
			dm.hipertension = 0
			dm.epilepsia = 0
			dm.asma = 0
			dm.insuficienciaRenal = 0
			dm.insifucienciaCardiaca = 0
			dm.anemia = 0
			dm.obesidad = 0
			dm.apetito = 0
			dm.reflujo = 0
			dp.save()
			da.save()
			dm.save()
			user = User()
			user.password=guardar.rut
			user.username=guardar.rut
			user.save()
			guardar.user=user
			guardar.da=da
			guardar.dp=dp
			guardar.dm=dm
			user.set_password(guardar.rut)
			user.save()
			form.save()
		return redirect('miSeccion')
	else:
		form = usuarioModelForm()
	contexto = {'usuario': usuario, 'form':form}
	return render(request, 'nuevoUsuario.html', contexto)

def nuevoBeneficiario(request):
	usuario = Usuario.objects.get(user=request.user.id)
	pruebas = Prueba.objects.all()
	tipo = tipoScout.objects.get(id=2)

	if request.method == 'POST':
		form = usuarioBeneficiarioModelForm(request.POST)
		if form.is_valid():
			guardar = form.save(commit=False)
			guardar.tipoScout = tipo
			guardar.Grupo = usuario.Grupo
			dp = DatosPadres()
			dp.fundacionPadre='2018-06-20'
			dp.fundacionMadre = '2018-06-20'
			da = DatosApoderado()
			da.fundacion = '2018-06-20'
			da.viveConEl=1
			dm = DatosMedicos()
			dm.varicela = 0
			dm.sarampion = 0
			dm.meringitis = 0
			dm.rubeola = 0
			dm.paperas = 0
			dm.tifoidea = 0
			dm.hepatitis = 0
			dm.hanta = 0
			dm.apendicitis = 0
			dm.escarlinata = 0
			dm.convulcion = 0
	
			dm.parasetamol = 0
			dm.ibuprofeno = 0
			dm.clorfenamina = 0
			dm.loratadina = 0
			dm.viadil = 0
			dm.amoxisilina = 0

			dm.alergiaAlimentaria = 0
			dm.alergiaMedicamento = 0
			dm.utilizaLentes = 0
			dm.esguince = 0
			dm.fractura = 0
			dm.operado = 0
			dm.columna = 0
			dm.piePlano = 0
			dm.pieAtleta = 0
			dm.movilidadReducida = 0
			dm.hernias = 0

			dm.diabetes = 0
			dm.hipertension = 0
			dm.epilepsia = 0
			dm.asma = 0
			dm.insuficienciaRenal = 0
			dm.insifucienciaCardiaca = 0
			dm.anemia = 0
			dm.obesidad = 0
			dm.apetito = 0
			dm.reflujo = 0
			dp.save()
			da.save()
			dm.save()
			user = User()
			user.password=guardar.rut
			user.username=guardar.rut
			user.save()
			guardar.user=user
			guardar.da=da
			guardar.dp=dp
			guardar.dm=dm
			user.set_password(guardar.rut)
			user.save()
			form.save()
		return redirect('miSeccion')
	else:
		form = usuarioBeneficiarioModelForm()
		form.fields["Patrulla"].queryset = Patrulla.objects.filter(Grupo=usuario.Seccion.Grupo.id)
		form.fields["Seccion"].queryset = Seccion.objects.filter(Grupo=usuario.Seccion.Grupo.id)

	contexto = {'usuario': usuario, 'form':form}
	return render(request, 'nuevoUsuario.html', contexto)

def nuevoDirigente(request):
	usuario = Usuario.objects.get(user=request.user.id)
	pruebas = Prueba.objects.all()
	tipo = tipoScout.objects.get(id=1)

	if request.method == 'POST':
		form = usuarioBeneficiarioModelForm(request.POST)
		if form.is_valid():
			guardar = form.save(commit=False)
			guardar.tipoScout = tipo
			guardar.Grupo = usuario.Grupo
			dp = DatosPadres()
			dp.fundacionPadre='2018-06-20'
			dp.fundacionMadre = '2018-06-20'
			da = DatosApoderado()
			da.fundacion = '2018-06-20'
			da.viveConEl=1
			dm = DatosMedicos()
			dm.varicela = 0
			dm.sarampion = 0
			dm.meringitis = 0
			dm.rubeola = 0
			dm.paperas = 0
			dm.tifoidea = 0
			dm.hepatitis = 0
			dm.hanta = 0
			dm.apendicitis = 0
			dm.escarlinata = 0
			dm.convulcion = 0
	
			dm.parasetamol = 0
			dm.ibuprofeno = 0
			dm.clorfenamina = 0
			dm.loratadina = 0
			dm.viadil = 0
			dm.amoxisilina = 0

			dm.alergiaAlimentaria = 0
			dm.alergiaMedicamento = 0
			dm.utilizaLentes = 0
			dm.esguince = 0
			dm.fractura = 0
			dm.operado = 0
			dm.columna = 0
			dm.piePlano = 0
			dm.pieAtleta = 0
			dm.movilidadReducida = 0
			dm.hernias = 0

			dm.diabetes = 0
			dm.hipertension = 0
			dm.epilepsia = 0
			dm.asma = 0
			dm.insuficienciaRenal = 0
			dm.insifucienciaCardiaca = 0
			dm.anemia = 0
			dm.obesidad = 0
			dm.apetito = 0
			dm.reflujo = 0
			dp.save()
			da.save()
			dm.save()
			user = User()
			user.password=guardar.rut
			user.username=guardar.rut
			user.save()
			guardar.user=user
			guardar.da=da
			guardar.dp=dp
			guardar.dm=dm
			user.set_password(guardar.rut)
			user.save()
			form.save()
		return redirect('miSeccion')
	else:
		form = usuarioDirigenteModelForm()
		form.fields["Seccion"].queryset = Seccion.objects.filter(Grupo=usuario.Seccion.Grupo.id)

	contexto = {'usuario': usuario, 'form':form}
	return render(request, 'nuevoUsuario.html', contexto)

def nuevaNoticia(request):
	usuario = Usuario.objects.get(user=request.user.id)

	if request.method == 'POST':
		form = NoticiaModelForm(request.POST)
		if form.is_valid():
			guardar = form.save(commit=False)
			guardar.fecha = time.strftime("%Y-%m-%d")
			guardar.Grupo = usuario.Grupo
			guardar.user = usuario.nombre+ " " +usuario.apellido
			form.save()
		return redirect('menu')
	else:
		form = NoticiaModelForm()

	return render(request, 'nuevaNoticia.html',{'form':form, 'usuario': usuario})

#Views para Cuenta nivel nacional
def nuevaNoticiaNivelNacional(request):
	usuario = Usuario.objects.get(user=request.user.id)
	grupos = GrupoScout.objects.all()

	if request.method == 'POST':
		form = NoticiaModelForm(request.POST)

		if form.is_valid():
			for grupo in grupos:
				guardar = form.save(commit=False)
				noticia = Noticia()
				noticia.titulo = guardar.titulo
				noticia.body = guardar.body
				noticia.fecha = time.strftime("%Y-%m-%d")
				noticia.Grupo = grupo
				noticia.user = usuario.nombre+ " " +usuario.apellido
				noticia.save()
		return redirect('menu')
	else:
		form = NoticiaModelForm()
	contexto = {'form':form, 'usuario': usuario}
	return render(request, 'nuevaNoticia.html', contexto)

def nuevaProvincia(request):
	usuario = Usuario.objects.get(user=request.user.id)
	provincias = Provincia.objects.all()
	localidades = Localidad.objects.all()
	if request.method == 'POST':
		form = ProvinciaModelForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('nuevaProvincia')
	else:
		form = ProvinciaModelForm()
	contexto = {'form':form, 'usuario': usuario, 'provincias': provincias, 'localidades': localidades}
	return render(request, 'nuevaProvincia.html', contexto)

def nuevaLocalidad(request):
	usuario = Usuario.objects.get(user=request.user.id)
	localidades = Localidad.objects.all()
	if request.method == 'POST':
		form = LocalidadModelForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('nuevaLocalidad')
	else:
		form = LocalidadModelForm()
	contexto = {'form':form, 'usuario': usuario, 'localidades': localidades}
	return render(request, 'nuevaLocalidad.html', contexto)

def nuevaGrupo(request):
	usuario = Usuario.objects.get(user=request.user.id)
	grupos = GrupoScout.objects.all()
	if request.method == 'POST':
		form = GrupoModelForm(request.POST)
		if form.is_valid():
			guardar = form.save(commit=False)
			grupo = GrupoScout()
			grupo.nombre=guardar.nombre
			grupo.fundacion= guardar.fundacion
			grupo.localidad = guardar.localidad
			grupo.save()
			user = Usuario()
			user.nombre=guardar.nombreJefe
			user.apellido=guardar.apellidoJefe
			user.fundacion='2018-06-20'

			user.tipoScout = tipoScout.objects.get(id=1)
			user.tipoDirigente = tipoDirigente.objects.get(id=1)
			guardar.Grupo = grupo
			dp = DatosPadres()
			dp.fundacionPadre='2018-06-20'
			dp.fundacionMadre = '2018-06-20'
			da = DatosApoderado()
			da.fundacion = '2018-06-20'
			da.viveConEl=1
			dm = DatosMedicos()
			dm.varicela = 0
			dm.sarampion = 0
			dm.meringitis = 0
			dm.rubeola = 0
			dm.paperas = 0
			dm.tifoidea = 0
			dm.hepatitis = 0
			dm.hanta = 0
			dm.apendicitis = 0
			dm.escarlinata = 0
			dm.convulcion = 0
	
			dm.parasetamol = 0
			dm.ibuprofeno = 0
			dm.clorfenamina = 0
			dm.loratadina = 0
			dm.viadil = 0
			dm.amoxisilina = 0

			dm.alergiaAlimentaria = 0
			dm.alergiaMedicamento = 0
			dm.utilizaLentes = 0
			dm.esguince = 0
			dm.fractura = 0
			dm.operado = 0
			dm.columna = 0
			dm.piePlano = 0
			dm.pieAtleta = 0
			dm.movilidadReducida = 0
			dm.hernias = 0

			dm.diabetes = 0
			dm.hipertension = 0
			dm.epilepsia = 0
			dm.asma = 0
			dm.insuficienciaRenal = 0
			dm.insifucienciaCardiaca = 0
			dm.anemia = 0
			dm.obesidad = 0
			dm.apetito = 0
			dm.reflujo = 0
			dp.save()
			da.save()
			dm.save()
			userSys = User()
			userSys.password=guardar.rutJefe
			userSys.username=guardar.rutJefe
			userSys.save()
			user.user=userSys
			user.da=da
			user.dp=dp
			user.dm=dm
			userSys.set_password(guardar.rutJefe)
			userSys.save()
			user.save()
		return redirect('nuevoGrupo')
	else:
		form = GrupoModelForm()
	contexto = {'form':form, 'usuario': usuario, 'grupos': grupos}
	return render(request, 'nuevoGrupo.html', contexto)

def listaProgramas(request):
	usuario = Usuario.objects.get(user=request.user.id)
	programas = Programa.objects.filter(Seccion = usuario.Seccion.id).order_by('fecha')[::-1]
	contexto = {'programas':programas, 'usuario': usuario}
	return render(request, 'programas.html', contexto)

def listaProgramasJefeGrupo(request):
	usuario = Usuario.objects.get(user=request.user.id)
	programas = Programa.objects.filter(grupo=usuario.Grupo.id).order_by('fecha')[::-1]
	contexto = {'programas':programas, 'usuario': usuario}
	return render(request, 'programaGrupo.html', contexto)

def listaUsuariosJefeGrupo(request):
	usuario = Usuario.objects.get(user=request.user.id)
	usuarios = Usuario.objects.filter(Grupo=usuario.Grupo.id).order_by('Seccion').order_by('Patrulla')
	contexto = {'usuarios':usuarios, 'usuario': usuario}
	return render(request, 'usuariosGrupo.html', contexto)

def listaSeccionJefeGrupo(request):
	usuario = Usuario.objects.get(user=request.user.id)
	secciones = Seccion.objects.filter(Grupo=usuario.Grupo.id)

	if request.method == 'POST':
		form = SeccionModelForm(request.POST)
		if form.is_valid():
			guardar = form.save(commit=False)
			guardar.Grupo = usuario.Grupo
			guardar.save()
		return redirect('verSecciones')
	else:
		form = SeccionModelForm()
		

	contexto = {'form':form,'secciones':secciones, 'usuario': usuario}
	return render(request, 'verSeccionesGrupo.html', contexto)

def listaPatrullasJefeGrupo(request):
	usuario = Usuario.objects.get(user=request.user.id)
	patrullas = Patrulla.objects.filter(Grupo=usuario.Grupo.id).order_by('Seccion')

	if request.method == 'POST':
		form = PatrullaModelForm(request.POST)
		if form.is_valid():
			guardar = form.save(commit=False)
			guardar.Grupo = usuario.Grupo
			guardar.save()
		return redirect('verPatrullas')
	else:
		form = PatrullaModelForm()
		form.fields["Seccion"].queryset = Seccion.objects.filter(Grupo=usuario.Seccion.Grupo.id)

	contexto = {'form':form,'patrullas':patrullas, 'usuario': usuario}
	return render(request, 'verPatrullasGrupo.html', contexto)

def editarAsistencia(request, id_programa):
	usuario = Usuario.objects.get(user=request.user.id)
	fecha = Programa.objects.get(id=id_programa).fecha
	asistencias = Asistencia.objects.filter(programa=id_programa).order_by('usuario__nombre')

	return render(request, 'editarAsistencia.html', {'asistencias':asistencias, 'usuario': usuario, 'fecha':fecha})

def editarPassword(request):
	usuario = Usuario.objects.get(user=request.user.id)
	user = User.objects.get(id=request.user.id)
	if request.method=='GET':
		form = CambiarContrasenaModelForm()
	else:
		form = CambiarContrasenaModelForm(request.POST)
		if form.is_valid():
			guardar = form.save(commit=False)
			user.set_password(guardar.passwordNueva)
			user.save()
		return redirect('menu')
	return render(request, 'editarPassword.html', {'form':form, 'usuario': usuario})

def asistio(request, id_asistencia):
	usuario = Usuario.objects.get(user=request.user.id)
	asistencia = Asistencia.objects.get(id=id_asistencia)
	id_programa = asistencia.programa.id
	asistencias = Asistencia.objects.filter(programa=id_programa).order_by('usuario__nombre')
	fecha = Programa.objects.get(id=id_programa).fecha
	if asistencia.asistio:
		asistencia.asistio=0
	else:
		asistencia.asistio=1
	asistencia.save()
	return render(request, 'editarAsistencia.html', {'asistencias':asistencias, 'usuario': usuario, 'fecha':fecha})

def editarEtapaProgresion(request, id_user):
	usuario = Usuario.objects.get(user=request.user.id)
	user = Usuario.objects.get(id=id_user)
	if request.method=='GET':
		form = EtapaProgresionModelForm(instance=user)
	else:
		form = EtapaProgresionModelForm(request.POST, instance=user)
		if form.is_valid():
			form.save()
		return redirect('miSeccion')
	return render(request, 'editarEtapaProgresion.html', {'form':form, 'usuario': usuario, 'iduser':id_user})

def editarUsuario(request, id_usuario):
	usuario = Usuario.objects.get(user=request.user.id)
	user = Usuario.objects.get(id=id_usuario)
	iddp=user.dp.id
	idda=user.da.id
	iddm=user.dm.id
	nombreB = user.nombre + " " +user.apellido

	if request.method=='GET':
		form = usuarioModelForm(instance=user)
	else:
		form = usuarioModelForm(request.POST, instance=user)
		if form.is_valid():
			form.save()
		return redirect('menu')
	return render(request, 'editarUsuario.html', {'form':form, 'usuario': usuario, 'iddp':iddp, 'idda':idda, 'iddm':iddm, 'iduser':id_usuario, 'nombreB':nombreB})

def editarDatosPadre(request, id_dp):
	usuario = Usuario.objects.get(user=request.user.id)
	user = Usuario.objects.get(dp=id_dp)
	iduser = user.id
	nombreB = user.nombre + " " + user.apellido

	dp = DatosPadres.objects.get(id=id_dp)
	if request.method=='GET':
		form = datosPadreModelForm(instance=dp)
	else:
		form = datosPadreModelForm(request.POST, instance=dp)
		if form.is_valid():
			form.save()
		return redirect('miSeccion')
	return render(request, 'editarDatosPadre.html', {'form':form, 'usuario': usuario, 'iduser':iduser, 'nombreB':nombreB})

def editarDatosApoderado(request, id_da):
	usuario = Usuario.objects.get(user=request.user.id)
	user = Usuario.objects.get(da=id_da)
	iduser = user.id
	nombreB = user.nombre + " " + user.apellido

	da = DatosApoderado.objects.get(id=id_da)
	if request.method=='GET':
		form = datosApoderadoModelForm(instance=da)
	else:
		form = datosApoderadoModelForm(request.POST, instance=da)
		if form.is_valid():
			form.save()
		return redirect('miSeccion')
	return render(request, 'editarDatosApoderado.html', {'form':form, 'usuario': usuario, 'iduser':iduser, 'nombreB':nombreB})

def editarDatosMedicos(request, id_dm):
	usuario = Usuario.objects.get(user=request.user.id)
	user = Usuario.objects.get(dm=id_dm)
	iduser = user.id
	nombreB = user.nombre + " " + user.apellido

	dm = DatosMedicos.objects.get(id=id_dm)
	if request.method=='GET':
		form = datosMedicosModelForm(instance=dm)
	else:
		form = datosMedicosModelForm(request.POST, instance=dm)
		if form.is_valid():
			form.save()
		return redirect('miSeccion')
	return render(request, 'editarDatosMedicos.html', {'form':form, 'usuario': usuario, 'iduser':iduser, 'nombreB':nombreB})

def editarPrograma(request, id_programa):
	usuario = Usuario.objects.get(user=request.user.id)
	lineas = LineaPrograma.objects.filter(Programa=id_programa)
	programa = Programa.objects.get(id=id_programa)
	if request.method=='GET':
		form = programaModelForm(instance=programa)
	else:
		form = programaModelForm(request.POST, instance=programa)
		if form.is_valid():
			form.save()
		return redirect('listaProgramas')
	return render(request, 'editarPrograma.html', {'form':form, 'lineas':lineas, 'usuario': usuario})

def editarLineaPrograma(request, id_linea):
	usuario = Usuario.objects.get(user=request.user.id)
	linea = LineaPrograma.objects.get(id=id_linea)
	if request.method=='GET':
		form = lineaProgramaModelForm(instance=linea)
	else:
		form = lineaProgramaModelForm(request.POST, instance=linea)
		if form.is_valid():
			form.save()
		return redirect('listaProgramas')
	return render(request, 'editarLineaPrograma.html', {'form':form, 'usuario': usuario,'linea':linea})

def verPrograma(request, id_programa):
	usuario = Usuario.objects.get(user=request.user.id)
	lineas = LineaPrograma.objects.filter(Programa=id_programa)
	programa = Programa.objects.get(id=id_programa)
	if request.method == 'POST':
		form = lineaProgramaModelForm(request.POST)
		if form.is_valid():
			guardar = form.save(commit=False)
			guardar.Programa = programa
			guardar.save()
		return redirect('listaProgramas')
	else:
		form = lineaProgramaModelForm()

	return render(request, 'verPrograma.html', {'programa':programa, 'usuario': usuario,'lineas':lineas,'form':form})

def nuevoProgramas(request):
	usuario = Usuario.objects.get(user=request.user.id)
	usuarios = Usuario.objects.filter(Seccion=usuario.Seccion.id)
	if request.method == 'POST':
		form = programaModelForm(request.POST)
		if form.is_valid():
			guardar = form.save(commit=False)
			guardar.Seccion = usuario.Seccion
			guardar.save()
			for di in usuarios:
				asis = Asistencia(usuario =di, fecha = guardar.fecha, asistio=1, programa=guardar)
				asis.save()
			guardar.save()
		return redirect('listaProgramas')
	else:
		form = programaModelForm()
	contexto = {'form':form, 'usuario':nombre, 'usuario': usuario}
	return render(request, 'nuevoPrograma.html', contexto)

def nuevoPuntaje(request, id_linea):
	usuario = Usuario.objects.get(user=request.user.id)
	linea = LineaPrograma.objects.get(id=id_linea)
	puntaje = Puntaje.objects.filter(lineaPrograma=id_linea)
	patrullas = Patrulla.objects.filter(Seccion=usuario.Seccion)
	titulo = linea.nombre

	maximo=0
	contador=0
	idPa=1
	idsir=1
	for patrulla in patrullas:
		bar =0
		for pu in puntaje:
			if pu.patrulla==patrulla:
				contador=contador+1
				bar =bar + pu.puntos
				idsir=pu.patrulla.id
		totales = PuntajeTotal.objects.filter(lineaPrograma=id_linea)
		var =0
		for tot in totales:
			if tot.patrulla.id == idsir:
				tot.puntos=bar
				tot.save()
				var =1
		if var == 0:
			pt = PuntajeTotal()
			pt.lineaPrograma=linea
			pt.patrulla = Patrulla.objects.get(id=idsir)
			pt.puntos =bar
			pt.save()

		if contador > maximo:
			maximo = contador
			idPa=patrulla.id
		contador =0

	puntaje2 = Puntaje.objects.filter(patrulla=idPa)
	maximo = 0
	totales = PuntajeTotal.objects.filter(lineaPrograma=id_linea)
	if request.method == 'POST':
		form = PuntajeModelForm(request.POST)
		if form.is_valid():
			guardar = form.save(commit=False)
			guardar.lineaPrograma = linea
			guardar.save()
		return redirect(request.build_absolute_uri())
	else:
		form = PuntajeModelForm()
		form.fields["patrulla"].queryset = Patrulla.objects.filter(Seccion=usuario.Seccion.id)
	contexto = {'totales':totales,'titulo':titulo,'form':form, 'puntajes':puntaje, 'patrullas':patrullas, 'maximo':maximo, 'maximoP':puntaje2, 'usuario': usuario}
	return render(request, 'nuevoPuntaje.html', contexto)

def eliminarPrograma(request, id_programa):
	programa=Programa.objects.get(id=id_programa)
	if request.method == 'POST':
		programa.delete()
		return redirect('listaProgramas')
	return render(request, 'eliminarPrograma.html',{'programa':programa, 'usuario': usuario})

def eliminarLineaPrograma(request, id_linea):
	programa=LineaPrograma.objects.get(id=id_linea)
	if request.method == 'POST':
		programa.delete()
		return redirect('listaProgramas')
	return render(request, 'eliminarLineaPrograma.html',{'programa':programa, 'usuario': usuario})

def cambiarUrl(request, web_id):
    return redirect(Prueba.objects.get(id=web_id).url)