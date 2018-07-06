# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

# Create your models here.
class nivelCuenta(models.Model):
	nombre = models.CharField(max_length=100)

#Views solo para rescatar datos
class PasswordFalse(models.Model):
	passwordNueva  = models.CharField(max_length=15)
	passwordNueva2  = models.CharField(max_length=15)
	passwordAntigua  = models.CharField(max_length=15)

class Provincia(models.Model):
	nombre  = models.CharField(max_length=100)
	fundacion = models.DateField()

	def __str__(self):
		return '{}'.format(self.nombre)

class Localidad(models.Model):
	nombre  = models.CharField(max_length=100)
	fundacion = models.DateField()
	provincia= models.ForeignKey(Provincia, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return '{}'.format(self.nombre)

class GrupoScout(models.Model):
	nombre  = models.CharField(max_length=100)
	fundacion = models.DateField()
	localidad= models.ForeignKey(Localidad, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return '{}'.format(self.nombre)

#Views solo para rescatar datos
class GrupoScoutFalse(models.Model):
	nombre  = models.CharField(max_length=100)
	fundacion = models.DateField()
	localidad= models.ForeignKey(Localidad, null=True, blank=True, on_delete=models.CASCADE)
	nombreJefe  = models.CharField(max_length=100)
	apellidoJefe  = models.CharField(max_length=100)
	rutJefe  = models.CharField(max_length=100)

class EtapaProgresion(models.Model):
	nombre  = models.CharField(max_length=100)

	def __str__(self):
		return '{}'.format(self.nombre)

class Prueba(models.Model):
	grupo= models.ForeignKey(GrupoScout, null=True, blank=True, on_delete=models.CASCADE)
	descripcion  = models.CharField(max_length=10000)
	etapa = models.ForeignKey(EtapaProgresion, null=True, blank=True, on_delete=models.CASCADE)
	url  = models.CharField(max_length=10000)

	def __str__(self):
		return '{} : {}'.format(self.etapa,self.descripcion)

class DatosPadres(models.Model):
	NombrePadre = models.CharField(max_length=100)
	rutPadre = models.CharField(max_length=100)
	telefonoPadre = models.CharField(max_length=100)
	telefono2Padre = models.CharField(max_length=100)
	fundacionPadre = models.DateField()
	NombreMadre = models.CharField(max_length=100)
	rutMadre = models.CharField(max_length=100)
	telefonoMadre = models.CharField(max_length=100)
	telefono2Madre = models.CharField(max_length=100)
	fundacionMadre = models.DateField()

class DatosApoderado(models.Model):
	Nombre = models.CharField(max_length=100)
	rut = models.CharField(max_length=100)
	telefono = models.CharField(max_length=100)
	telefono2 = models.CharField(max_length=100)
	fundacion = models.DateField()
	parentesco = models.CharField(max_length=100)
	viveConEl = models.BooleanField(choices=((False,"No"),(True,"Si")))

class DatosMedicos(models.Model):

	telefonoEmergencia = models.CharField(max_length=100)
	telefonoEmergencia2 = models.CharField(max_length=100)
	estatura = models.CharField(max_length=100)
	peso = models.CharField(max_length=100)
	sistemaSalud = models.CharField(max_length=100)
	grupoSanguineo = models.CharField(max_length=100)
	factorRH = models.CharField(max_length=100)
	varicela = models.BooleanField(choices=((False,"No ha padecido"),(True,"Si ha padecido")))
	sarampion = models.BooleanField(choices=((False,"No ha padecido"),(True,"Si ha padecido")))
	meringitis = models.BooleanField(choices=((False,"No ha padecido"),(True,"Si ha padecido")))
	rubeola = models.BooleanField(choices=((False,"No ha padecido"),(True,"Si ha padecido")))
	paperas = models.BooleanField(choices=((False,"No ha padecido"),(True,"Si ha padecido")))
	tifoidea = models.BooleanField(choices=((False,"No ha padecido"),(True,"Si ha padecido")))
	hepatitis = models.BooleanField(choices=((False,"No ha padecido"),(True,"Si ha padecido")))
	hanta = models.BooleanField(choices=((False,"No ha padecido"),(True,"Si ha padecido")))
	apendicitis = models.BooleanField(choices=((False,"No ha padecido"),(True,"Si ha padecido")))
	escarlinata = models.BooleanField(choices=((False,"No ha padecido"),(True,"Si ha padecido")))
	convulcion = models.BooleanField(choices=((False,"No ha padecido"),(True,"Si ha padecido")))
	
	parasetamol = models.BooleanField(choices=((False,"Sin reacción Adversa"),(True,"Con reacción Adversa")))
	ibuprofeno = models.BooleanField(choices=((False,"Sin reacción Adversa"),(True,"Con reacción Adversa")))
	clorfenamina = models.BooleanField(choices=((False,"Sin reacción Adversa"),(True,"Con reacción Adversa")))
	loratadina = models.BooleanField(choices=((False,"Sin reacción Adversa"),(True,"Con reacción Adversa")))
	viadil = models.BooleanField(choices=((False,"Sin reacción Adversa"),(True,"Con reacción Adversa")))
	amoxisilina = models.BooleanField(choices=((False,"Sin reacción Adversa"),(True,"Con reacción Adversa")))

	alergiaAlimentaria = models.BooleanField(choices=((False,"No Presenta"),(True,"Si Presenta")))
	alergiaMedicamento = models.BooleanField(choices=((False,"No Presenta"),(True,"Si Presenta")))
	alergiaOtros = models.CharField(max_length=1000)
	utilizaLentes = models.BooleanField(choices=((False,"No Presenta"),(True,"Si Presenta")))
	esguince = models.BooleanField(choices=((False,"No ha presentado"),(True,"Si ha presentado")))
	fractura = models.BooleanField(choices=((False,"No ha presentado"),(True,"Si ha presentado")))
	operado = models.BooleanField(choices=((False,"No ha presentado"),(True,"Si ha presentado")))
	columna = models.BooleanField(choices=((False,"No ha presentado"),(True,"Si ha presentado")))
	piePlano = models.BooleanField(choices=((False,"No Presenta"),(True,"Si Presenta")))
	pieAtleta = models.BooleanField(choices=((False,"No Presenta"),(True,"Si Presenta")))
	movilidadReducida = models.BooleanField(choices=((False,"No Presenta"),(True,"Si Presenta")))
	hernias = models.BooleanField(choices=((False,"No Presenta"),(True,"Si Presenta")))

	diabetes = models.BooleanField(choices=((False,"No Presenta"),(True,"Si Presenta")))
	hipertension = models.BooleanField(choices=((False,"No Presenta"),(True,"Si Presenta")))
	epilepsia = models.BooleanField(choices=((False,"No Presenta"),(True,"Si Presenta")))
	asma = models.BooleanField(choices=((False,"No Presenta"),(True,"Si Presenta")))
	insuficienciaRenal = models.BooleanField(choices=((False,"No Presenta"),(True,"Si Presenta")))
	insifucienciaCardiaca = models.BooleanField(choices=((False,"No Presenta"),(True,"Si Presenta")))
	anemia = models.BooleanField(choices=((False,"No Presenta"),(True,"Si Presenta")))
	obesidad = models.BooleanField(choices=((False,"No Presenta"),(True,"Si Presenta")))
	apetito = models.BooleanField(choices=((False,"No Presenta"),(True,"Si Presenta")))
	reflujo = models.BooleanField(choices=((False,"No Presenta"),(True,"Si Presenta")))
	otra = models.CharField(max_length=100)
	otra2 = models.CharField(max_length=100)
	otra3 = models.CharField(max_length=100)
	medicamentos = models.CharField(max_length=10000)

class tipoScout(models.Model):
	tipo = models.CharField(max_length=100)

	def __str__(self):
		return '{}'.format(self.tipo)

class tipoDirigente(models.Model):
	tipo = models.CharField(max_length=100)

	def __str__(self):
		return '{}'.format(self.tipo)

class Seccion(models.Model):
	nombre = models.CharField(max_length=100)
	fundacion = models.DateField()
	Grupo= models.ForeignKey(GrupoScout, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return '{}'.format(self.nombre)


class Patrulla(models.Model):
	Seccion= models.ForeignKey(Seccion, null=True, blank=True, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=100)
	fundacion = models.DateField()
	Grupo= models.ForeignKey(GrupoScout, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return '{}'.format(self.nombre)

class PruebaViews(models.Model):
	descripcion  = models.CharField(max_length=100)
	estado = models.BooleanField(choices=((False,"No Rendida"),(True,"Aprobada")))
	url  = models.CharField(max_length=10000)

	def __str__(self):
		return '{}'.format(self.descripcion)

class Usuario(models.Model):
	Patrulla = models.ForeignKey(Patrulla, null=True, blank=True, on_delete=models.CASCADE)
	Seccion = models.ForeignKey(Seccion, null=True, blank=True, on_delete=models.CASCADE)
	Grupo = models.ForeignKey(GrupoScout, null=True, blank=True, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	tipoScout = models.ForeignKey(tipoScout, null=True, blank=True, on_delete=models.CASCADE)
	tipoDirigente = models.ForeignKey(tipoDirigente, null=True, blank=True, on_delete=models.CASCADE)
	email = models.EmailField()
	fundacion = models.DateField()
	rut = models.CharField(max_length=100)
	user= models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	direccion = models.CharField(max_length=100)
	comuna = models.CharField(max_length=100)
	region = models.CharField(max_length=100)
	telefono = models.CharField(max_length=100)
	grupoAnterior = models.CharField(max_length=100)
	nacionalidad = models.CharField(max_length=100)
	dp = models.ForeignKey(DatosPadres, null=True, blank=True, on_delete=models.CASCADE)
	da = models.ForeignKey(DatosApoderado, null=True, blank=True, on_delete=models.CASCADE)
	dm = models.ForeignKey(DatosMedicos, null=True, blank=True, on_delete=models.CASCADE)
	etapa = models.ForeignKey(EtapaProgresion, null=True, blank=True, on_delete=models.CASCADE)
	pruebas = models.ManyToManyField(Prueba)
	nivelCuenta = models.ForeignKey(nivelCuenta, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self): #python 3
		return '{} {}'.format(self.nombre, self.apellido)


class Programa(models.Model):
	lugar = models.CharField(max_length=100)
	fecha = models.DateField()
	observacion = models.CharField(max_length=100)
	Seccion= models.ForeignKey(Seccion, null=True, blank=True, on_delete=models.CASCADE)
	grupo= models.ForeignKey(GrupoScout, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return '{}'.format(self.fecha)

class Asistencia(models.Model):
	usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
	programa = models.ForeignKey(Programa, null=True, blank=True, on_delete=models.CASCADE)
	fecha = models.DateField()
	asistio = models.BooleanField(choices=((False,"Ausente"),(True,"Presente")))

	def __str__(self):
		return '{}'.format(self.usuario)

class LineaPrograma(models.Model):
	Programa = models.ForeignKey(Programa, null=True, blank=True, on_delete=models.CASCADE)
	hora  = models.CharField(max_length=100)
	duracion  = models.CharField(max_length=100)
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=100)
	encargado = models.CharField(max_length=100)
	materiales = models.CharField(max_length=100)
	observacion = models.CharField(max_length=100)

class Categoria(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=10000)

class ObjetoBiblioteca(models.Model):
	nombre  = models.CharField(max_length=100)
	urlImagen  = models.CharField(max_length=100)
	urlArchivo  = models.CharField(max_length=100)
	descripcion  = models.CharField(max_length=100)
	categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)

class Noticia(models.Model):
	user = models.CharField(max_length=100)
	Grupo = models.ForeignKey(GrupoScout, null=True, blank=True, on_delete=models.CASCADE)
	fecha = models.DateField()
	titulo = models.CharField(max_length=100)
	body = models.CharField(max_length=100000)

class PreguntaNoticia(models.Model):
	user = models.CharField(max_length=100)
	pregunta = models.CharField(max_length=10000)
	respuesta = models.CharField(max_length=10000)
	Noticia = models.ForeignKey(Noticia, null=True, blank=True, on_delete=models.CASCADE)

class CategoriaCurriculum(models.Model):
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return '{}'.format(self.nombre)

class Curriculum(models.Model):
	categoria = models.ForeignKey(CategoriaCurriculum, null=True, blank=True, on_delete=models.CASCADE)
	usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
	fecha = models.DateField()
	suceso = models.CharField(max_length=1000)
	descripcion = models.CharField(max_length=10000)

class Puntaje(models.Model):
	lineaPrograma = models.ForeignKey(LineaPrograma, null=True, blank=True, on_delete=models.CASCADE)
	patrulla = models.ForeignKey(Patrulla, null=True, blank=True, on_delete=models.CASCADE)
	puntos = models.IntegerField()

class PuntajeTotal(models.Model):
	lineaPrograma = models.ForeignKey(LineaPrograma, null=True, blank=True, on_delete=models.CASCADE)
	patrulla = models.ForeignKey(Patrulla, null=True, blank=True, on_delete=models.CASCADE)
	puntos = models.IntegerField()