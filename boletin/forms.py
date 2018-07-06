from django import forms
from .models import Usuario
from .models import Seccion
from .models import Patrulla, Provincia, Localidad
from .models import tipoScout
from .models import Programa
from .models import LineaPrograma
from .models import DatosPadres
from .models import DatosApoderado
from .models import DatosMedicos, PreguntaNoticia
from .models import Curriculum, PruebaViews, Puntaje, PasswordFalse, Noticia, GrupoScoutFalse
from django.contrib.admin import widgets
from django.contrib.auth.models import User

BIRTH_YEAR_CHOISE = ('2018', '2017', '2016', '2015', '2014', '2013')

#model para usuario jefe de seccion
class usuarioModelForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = [
			'nombre', 
			'apellido', 
			'fundacion',
			'rut',
			'email',
			'Patrulla',
			'etapa',
			'direccion',
			'comuna',
			'region',
			'telefono',
			'grupoAnterior',
			'nacionalidad',
		]
		labels = {
			'nombre' : 'Nombre', 
			'apellido' : 'Apellido', 
			'fundacion' : 'Fecha de Nacimiento',
			'rut' : 'R.U.T.',
			'email' : 'E-mail',
			'Patrulla' : 'Patrulla',
			'etapa' : 'Etapa Actual Rendiendo',
			'direccion' : 'Direcion',
			'comuna' : 'Comuna',
			'region' : 'Region',
			'telefono' : 'Telefono',
			'grupoAnterior' : 'Grupo Anterior',
			'nacionalidad' : 'Nacionalidad',
		}
		widgets = {
			'nombre' : forms.TextInput(attrs={'class':'form-control'}), 
			'apellido' : forms.TextInput(attrs={'class':'form-control'}),
			'fundacion' : forms.SelectDateWidget(attrs={'class':'form-control'}),
			'rut' : forms.TextInput(attrs={'class':'form-control'}),
			'email' : forms.TextInput(attrs={'class':'form-control'}),
			'Patrulla' : forms.Select(attrs={'class':'form-control'}),
			'etapa' : forms.Select(attrs={'class':'form-control'}),
			'direccion' : forms.TextInput(attrs={'class':'form-control'}),
			'comuna' : forms.TextInput(attrs={'class':'form-control'}),
			'region' : forms.TextInput(attrs={'class':'form-control'}),
			'telefono' : forms.TextInput(attrs={'class':'form-control'}),
			'grupoAnterior' : forms.TextInput(attrs={'class':'form-control'}),
			'nacionalidad' : forms.TextInput(attrs={'class':'form-control'}),
		}

class usuarioBeneficiarioModelForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = [
			'nombre', 
			'apellido', 
			'fundacion',
			'rut',
			'email',
			'Patrulla',
			'etapa',
			'direccion',
			'comuna',
			'region',
			'telefono',
			'grupoAnterior',
			'nacionalidad',
			'Seccion'
		]
		labels = {
			'nombre' : 'Nombre', 
			'apellido' : 'Apellido', 
			'fundacion' : 'Fecha de Nacimiento',
			'rut' : 'R.U.T.',
			'email' : 'E-mail',
			'Patrulla' : 'Seisena/Patrulla/Equipo',
			'etapa' : 'Etapa Actual Rendiendo',
			'direccion' : 'Direcion',
			'comuna' : 'Comuna',
			'region' : 'Region',
			'telefono' : 'Telefono',
			'grupoAnterior' : 'Grupo Anterior',
			'nacionalidad' : 'Nacionalidad',
			'Seccion': 'Seccion',
		}
		widgets = {
			'nombre' : forms.TextInput(attrs={'class':'form-control'}), 
			'apellido' : forms.TextInput(attrs={'class':'form-control'}),
			'fundacion' : forms.SelectDateWidget(attrs={'class':'form-control'}),
			'rut' : forms.TextInput(attrs={'class':'form-control'}),
			'email' : forms.TextInput(attrs={'class':'form-control'}),
			'etapa' : forms.Select(attrs={'class':'form-control'}),
			'Seccion' : forms.Select(attrs={'class':'form-control'}),
			'Patrulla' : forms.Select(attrs={'class':'form-control'}),
			'etapa' : forms.Select(attrs={'class':'form-control'}),
			'direccion' : forms.TextInput(attrs={'class':'form-control'}),
			'comuna' : forms.TextInput(attrs={'class':'form-control'}),
			'region' : forms.TextInput(attrs={'class':'form-control'}),
			'telefono' : forms.TextInput(attrs={'class':'form-control'}),
			'grupoAnterior' : forms.TextInput(attrs={'class':'form-control'}),
			'nacionalidad' : forms.TextInput(attrs={'class':'form-control'}),
		}

class usuarioDirigenteModelForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = [
			'nombre', 
			'apellido', 
			'fundacion',
			'rut',
			'email',
			'etapa',
			'direccion',
			'comuna',
			'region',
			'telefono',
			'grupoAnterior',
			'nacionalidad',
			'Seccion',
			'tipoDirigente',
		]
		labels = {
			'nombre' : 'Nombre', 
			'apellido' : 'Apellido', 
			'fundacion' : 'Fecha de Nacimiento',
			'rut' : 'R.U.T.',
			'email' : 'E-mail',
			'Patrulla' : 'Patrulla',
			'etapa' : 'Etapa Actual Rendiendo',
			'direccion' : 'Direcion',
			'comuna' : 'Comuna',
			'region' : 'Region',
			'telefono' : 'Telefono',
			'grupoAnterior' : 'Grupo Anterior',
			'nacionalidad' : 'Nacionalidad',
			'Seccion': 'Seccion',
			'tipoDirigente' : 'Cargo del Dirigente',
		}
		widgets = {
			'nombre' : forms.TextInput(attrs={'class':'form-control'}), 
			'apellido' : forms.TextInput(attrs={'class':'form-control'}),
			'fundacion' : forms.SelectDateWidget(attrs={'class':'form-control'}),
			'rut' : forms.TextInput(attrs={'class':'form-control'}),
			'email' : forms.TextInput(attrs={'class':'form-control'}),
			'etapa' : forms.Select(attrs={'class':'form-control'}),
			'Seccion' : forms.Select(attrs={'class':'form-control'}),
			'etapa' : forms.Select(attrs={'class':'form-control'}),
			'direccion' : forms.TextInput(attrs={'class':'form-control'}),
			'comuna' : forms.TextInput(attrs={'class':'form-control'}),
			'region' : forms.TextInput(attrs={'class':'form-control'}),
			'telefono' : forms.TextInput(attrs={'class':'form-control'}),
			'grupoAnterior' : forms.TextInput(attrs={'class':'form-control'}),
			'nacionalidad' : forms.TextInput(attrs={'class':'form-control'}),
			'tipoDirigente' : forms.Select(attrs={'class':'form-control'}),
		}

class curriculumModelForm(forms.ModelForm):
	class Meta:
		model = Curriculum
		fields = [
			'categoria', 
			'fecha', 
			'suceso',
			'descripcion',
		]
		labels = {
			'categoria': 'Categoria', 
			'fecha': 'Fecha', 
			'suceso': 'Suceso',
			'descripcion': 'Descripcion',

		}
		widgets = {
			'categoria' : forms.Select(attrs={'class':'form-control'}),
			'fecha' : forms.SelectDateWidget(attrs={'class':'form-control'}),
			'suceso' : forms.TextInput(attrs={'class':'form-control'}),
			'descripcion' : forms.TextInput(attrs={'class':'form-control'}),
		}

class programaModelForm(forms.ModelForm):
	class Meta:
		model = Programa
		fields = [
			"lugar", 
			"fecha", 
			"observacion",
		]
		labels = {
			'lugar' : 'Lugar', 
			'fecha' : 'Fecha', 
			'observacion' : 'Observacion',
		}
		widgets = {
			'lugar' : forms.TextInput(attrs={'class':'form-control'}), 
			'fecha' : forms.TextInput(attrs={'class':'form-control'}), 
			'observacion' : forms.TextInput(attrs={'class':'form-control'}),
		}

class SeccionModelForm(forms.ModelForm):
	class Meta:
		model = Seccion
		fields = [
			'nombre',
			'fundacion',
		]
		labels = {
			'nombre': 'Nombre de la Nueva Seccion',
			'fundacion': 'Fecha de Fundacion',
		}
		widgets = {
			'nombre' : forms.TextInput(attrs={'class':'form-control'}), 
			'fundacion' : forms.SelectDateWidget(years = BIRTH_YEAR_CHOISE,attrs={'class':'form-control'}),
		}

class PatrullaModelForm(forms.ModelForm):
	class Meta:
		model = Patrulla
		fields = [
			'nombre',
			'fundacion',
			'Seccion',
		]
		labels = {
			'nombre': 'Nombre de la Nueva Seccion',
			'fundacion': 'Fecha de Fundacion',
			'Seccion' : 'Seccion',
		}
		widgets = {
			'nombre' : forms.TextInput(attrs={'class':'form-control'}), 
			'fundacion' : forms.SelectDateWidget(years = BIRTH_YEAR_CHOISE,attrs={'class':'form-control'}),
			'Seccion' : forms.Select(attrs={'class':'form-control'}),
		}

class lineaProgramaModelForm(forms.ModelForm):
	class Meta:
		model = LineaPrograma
		fields = [
			"hora", 
			"duracion", 
			"nombre",
			"descripcion",
			"encargado",
			"materiales",
			"observacion",
		]
		labels = {
			'hora' : 'Hora',
			'duracion' : 'Duracion',
			'nombre' : 'Nombre de la Actividad',
			'descripcion' : 'Descripcion',
			'encargado' : 'Encargado',
			'materiales' : 'Materiales',
			'observacion' : 'Observacion',
		}
		widgets = {
			'hora' : forms.TextInput(attrs={'class':'form-control'}),
			'duracion' : forms.TextInput(attrs={'class':'form-control'}),
			'nombre' : forms.TextInput(attrs={'class':'form-control'}),
			'descripcion' : forms.TextInput(attrs={'class':'form-control'}),
			'encargado' : forms.TextInput(attrs={'class':'form-control'}),
			'materiales' : forms.TextInput(attrs={'class':'form-control'}),
			'observacion' : forms.TextInput(attrs={'class':'form-control'}),
		}

class EtapaProgresionModelForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = [
			'pruebas',
		]
		labels = {
			'pruebas': 'Estado',
		}
		widgets = {
			'pruebas' : forms.CheckboxSelectMultiple(),
		}

class PreguntaNoticiaModelForm(forms.ModelForm):
	class Meta:
		model = PreguntaNoticia
		fields = [
			'pregunta',
		]
		labels = {
			'pregunta': '',	
		}
		widgets = {
			'pregunta' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Haz tu pregunta o deja un comentario'}),
		}
#respuesta desde el jefe de grupo
class PreguntaNoticia2ModelForm(forms.ModelForm):
	class Meta:
		model = PreguntaNoticia
		fields = [
			'pregunta',
		]
		labels = {
			'pregunta': '',	
		}
		widgets = {
			'pregunta' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Respuesta o Edicion'}),
		}

class CambiarContrasenaModelForm(forms.ModelForm):
	class Meta:
		model = PasswordFalse
		fields = [
			'passwordAntigua',
			'passwordNueva',
			'passwordNueva2',
			
		]
		labels = {
			'passwordAntigua': 'Ingrese su Password Actual',
			'passwordNueva': 'Ingrese la Password Nueva',
			'passwordNueva2': 'Ingrese nuevamente la Password Nueva',
		}
		widgets = {
			'passwordAntigua': forms.TextInput(attrs={'class':'form-control'}),
			'passwordNueva': forms.TextInput(attrs={'class':'form-control'}),
			'passwordNueva2': forms.TextInput(attrs={'class':'form-control'}),
		}

class PuntajeModelForm(forms.ModelForm):
	class Meta:
		model = Puntaje
		fields = [
			'patrulla',
			'puntos',
		]
		labels = {
			'patrulla': 'Patrulla',
			'puntos': 'Puntos',
		}
		widgets = {
		'patrulla' : forms.Select(attrs={'class':'form-control'}),
		'puntos' : forms.TextInput(attrs={'class':'form-control'}),
		}

class NoticiaModelForm(forms.ModelForm):
	class Meta:
		model = Noticia
		fields = [
			'titulo',
			'body',
		]
		labels = {
			'titulo': 'Titulo de la Noticia',
			'body': 'Cuerpo de la Noticia',
		}
		widgets = {
		'titulo' : forms.TextInput(attrs={'class':'form-control'}),
		'body' : forms.TextInput(attrs={'class':'form-control'}),
		}

class ProvinciaModelForm(forms.ModelForm):
	class Meta:
		model = Provincia
		fields = [
			'nombre',
			'fundacion',
		]
		labels = {
			'nombre': 'Nombre de la Nueva Provincia',
			'fundacion': 'fecha de Fundacion de la Provincia',
		}
		widgets = {
		'nombre' : forms.TextInput(attrs={'class':'form-control'}),
		'fundacion' : forms.SelectDateWidget(attrs={'class':'form-control'}),
		}

class LocalidadModelForm(forms.ModelForm):
	class Meta:
		model = Localidad
		fields = [
			'nombre',
			'fundacion',
			'provincia',
		]
		labels = {
			'nombre': 'Nombre de la Nueva Localidad',
			'fundacion': 'Fecha de Fundacion de la Localidad',
			'provincia' : 'Provincia',
		}
		widgets = {
		'nombre' : forms.TextInput(attrs={'class':'form-control'}),
		'fundacion' : forms.SelectDateWidget(attrs={'class':'form-control'}),
		'provincia' : forms.Select(attrs={'class':'form-control'}),
		}

class GrupoModelForm(forms.ModelForm):
	class Meta:
		model = GrupoScoutFalse
		fields = [
			'nombre',
			'fundacion',
			'localidad',
			'nombreJefe',
			'apellidoJefe',
			'rutJefe',
		]
		labels = {
			'nombre': 'Nombre del Grupo Scout',
			'fundacion': 'Fecha de Fundacion del Grupo Scout',
			'localidad' : 'Localidad',
			'nombreJefe': 'Nombre del Jefe de Grupo',
			'apellidoJefe': 'Apellido del Jefe de Grupo',
			'rutJefe' : 'Rut Jefe de Grupo',
		}
		widgets = {
		'nombre' : forms.TextInput(attrs={'class':'form-control'}),
		'fundacion' : forms.SelectDateWidget(attrs={'class':'form-control'}),
		'localidad' : forms.Select(attrs={'class':'form-control'}),
		'nombreJefe': forms.TextInput(attrs={'class':'form-control'}),
		'apellidoJefe': forms.TextInput(attrs={'class':'form-control'}),
		'rutJefe': forms.TextInput(attrs={'class':'form-control'}),
		}

class seccionModelForm(forms.ModelForm):
	class Meta:
		model = Seccion
		fields = ["nombre","fundacion"]

class patrullaModelForm(forms.ModelForm):
	class Meta:
		model = Patrulla
		fields = ["nombre"]

class tipoScoutModelForm(forms.ModelForm):
	class Meta:
		model = tipoScout
		fields = ["tipo"]

class tipoDirigenteModelForm(forms.ModelForm):
	class Meta:
		model = tipoScout
		fields = ["tipo"]		

class UsuarioForm(forms.Form):
	nombre = forms.CharField(max_length=100)
	apellido = forms.CharField(max_length=100)
	nombreApoderado = forms.CharField(max_length=100)
	tipoScout = forms.CharField(max_length=100)
	email = forms.EmailField()
	contrasena = forms.CharField(max_length=100)

class datosPadreModelForm(forms.ModelForm):
	class Meta:
		model = DatosPadres
		fields = [
			'NombrePadre',
			'rutPadre',
			'telefonoPadre',
			'telefono2Padre',
			'fundacionPadre',
			'NombreMadre',
			'rutMadre',
			'telefonoMadre',
			'telefono2Madre',
			'fundacionMadre',
		]
		labels = {
			'NombrePadre' : 'Nombre del Padre',
			'rutPadre' : 'R.U.T. del Padre',
			'telefonoPadre' : 'Telefono 1 del Padre',
			'telefono2Padre' : 'Telefono 2 del Padre',
			'fundacionPadre' : 'Fechac Nacimiento del Padre',
			'NombreMadre' : 'Nombre de la Madre',
			'rutMadre' : 'R.U.T. de la Madre',
			'telefonoMadre' : 'Telefono 1 de la Madre',
			'telefono2Madre' : 'Telefono 2 de la Madre',
			'fundacionMadre' : 'Fecha Nacimiento de la Madre',

		}
		widgets = {
			'NombrePadre' : forms.TextInput(attrs={'class':'form-control'}), 
			'rutPadre' : forms.TextInput(attrs={'class':'form-control'}), 
			'telefonoPadre' : forms.TextInput(attrs={'class':'form-control'}),
			'telefono2Padre' : forms.TextInput(attrs={'class':'form-control'}), 
			'fundacionPadre' : forms.SelectDateWidget(attrs={'class':'form-control'}),
			'NombreMadre' : forms.TextInput(attrs={'class':'form-control'}), 
			'rutMadre' : forms.TextInput(attrs={'class':'form-control'}), 
			'telefonoMadre' : forms.TextInput(attrs={'class':'form-control'}), 
			'telefono2Madre' : forms.TextInput(attrs={'class':'form-control'}), 
			'fundacionMadre' : forms.SelectDateWidget(attrs={'class':'form-control'}),	
		}

class datosApoderadoModelForm(forms.ModelForm):
	class Meta:
		model = DatosApoderado
		fields = [
			'Nombre',
			'rut',
			'telefono',
			'telefono2',
			'fundacion',
			'parentesco',
			'viveConEl',
		]
		labels = {
			'Nombre' : 'Nombre del Apoderado',
			'rut' : 'R.U.T. del Apoderado',
			'telefono' : 'Telefono 1 del Apoderado',
			'telefono2' : 'Telefono 2 del Apoderado',
			'fundacion' : ' Fecha de Nacimiento del Apoderado',
			'parentesco' : 'Parentesco con el muchacho',
			'viveConEl' : 'Vive con el muchacho',
		}
		widgets = {
			'Nombre' : forms.TextInput(attrs={'class':'form-control'}),
			'rut' : forms.TextInput(attrs={'class':'form-control'}),
			'telefono' : forms.TextInput(attrs={'class':'form-control'}),
			'telefono2' : forms.TextInput(attrs={'class':'form-control'}),
			'fundacion' : forms.SelectDateWidget(attrs={'class':'form-control'}),
			'parentesco' : forms.TextInput(attrs={'class':'form-control'}),
			'viveConEl' : forms.Select(attrs={'class':'form-control'}),
		}

class datosMedicosModelForm(forms.ModelForm):
	class Meta:
		model = DatosMedicos
		fields = [
			'telefonoEmergencia',
			'telefonoEmergencia2',
			'estatura',
			'peso',
			'sistemaSalud',
			'grupoSanguineo',
			'factorRH',
			'varicela',
			'sarampion',
			'meringitis',
			'rubeola',
			'paperas',
			'tifoidea',
			'hepatitis',
			'hanta',
			'apendicitis',
			'escarlinata',
			'convulcion',
	
			'parasetamol',
			'ibuprofeno',
			'clorfenamina',
			'loratadina',
			'viadil',
			'amoxisilina',

			'alergiaAlimentaria',
			'alergiaMedicamento',
			'alergiaOtros',
			'utilizaLentes',
			'esguince',
			'fractura',
			'operado',
			'columna',
			'piePlano',
			'pieAtleta',
			'movilidadReducida',
			'hernias',

			'diabetes',
			'hipertension',
			'epilepsia',
			'asma',
			'insuficienciaRenal',
			'insifucienciaCardiaca',
			'anemia',
			'obesidad',
			'apetito',
			'reflujo',
			'otra',
			'otra2',
			'otra3',
			'medicamentos',
		]
		labels = {
			'telefonoEmergencia' : 'Telefono de Emergencia 1',
			'telefonoEmergencia2' : 'Telefono de Emergencia 2',
			'estatura' : 'Estatura',
			'peso' : 'Peso',
			'sistemaSalud' : 'Sistema de Salud',
			'grupoSanguineo' : 'Grupo Sanguineo',
			'factorRH' : 'Factor RH',
			'varicela' : 'Ha padecido Varicela',
			'sarampion' : 'Ha padecido Sarampion',
			'meringitis' : 'Ha padecido Meringuitis',
			'rubeola' : 'Ha padecido Rubeola',
			'paperas' : 'Ha padecido Paperas',
			'tifoidea' : 'Ha padecido Tifoidea',
			'hepatitis' : 'Ha padecido Hapatitis',
			'hanta' : 'Ha padecido Virus Hanta',
			'apendicitis' : 'Ha padecido Apendicitis',
			'escarlinata' : 'Ha padecido Escarlinata',
			'convulcion' : 'Ha padecido Convulciones',
	
			'parasetamol' :'Reaccion al consumir Parasetamol',
			'ibuprofeno' :'Reaccion al consumir Ibuprofeno',
			'clorfenamina' :'Reaccion al consumir Clorfenamina',
			'loratadina' :'Reaccion al consumir Loratadina',
			'viadil' :'Reaccion al consumir Viadil',
			'amoxisilina' :'Reaccion al consumir Amoxisilina',

			'alergiaAlimentaria' : 'Presenta Alergia Alimentaria',
			'alergiaMedicamento' : 'Presenta a Medicamentos',
			'alergiaOtros' : 'Presenta otras Alergias',
			'utilizaLentes' :'Utiliza Lentes',
			'esguince' : 'Ha sufrido de Esguince',
			'fractura' : 'Ha sufrido de Fractura',
			'operado' : 'Ha sido Operado',
			'columna' : 'Problema en la Columna',
			'piePlano' : 'Presenta Pie Plano',
			'pieAtleta' : 'Presenta Pie de Atleta',
			'movilidadReducida' : 'Presenta Movilidad Reducida',
			'hernias' : 'Presenta Hernias',

			'diabetes' : 'Presenta Diabetes',
			'hipertension' : 'Presenta Hipertension',
			'epilepsia' : 'Presenta Epilepsia',
			'asma' : 'Presenta Asma',
			'insuficienciaRenal' : 'Presenta Insuficiencia Renal',
			'insifucienciaCardiaca' : 'Presenta Insuficiencia Cardiaca',
			'anemia' : 'Presenta Anemia',
			'obesidad' : 'Presenta Obesidad',
			'apetito' : 'Presenta Falta de Apetito',
			'reflujo' : 'Presenta Reflujo',
			'otra' : 'Presenta alguna otra patologia',
			'otra2' : 'Presenta alguna otra patologia',
			'otra3' : 'Presenta alguna otra patologia',
			'medicamentos' : 'Consume los siguientes Medicamentos',
		}
		widgets = {
			'telefonoEmergencia' : forms.TextInput(attrs={'class':'form-control'}),
			'telefonoEmergencia2' : forms.TextInput(attrs={'class':'form-control'}),
			'estatura' : forms.TextInput(attrs={'class':'form-control'}),
			'peso' : forms.TextInput(attrs={'class':'form-control'}),
			'sistemaSalud' : forms.TextInput(attrs={'class':'form-control'}),
			'grupoSanguineo' : forms.TextInput(attrs={'class':'form-control'}),
			'factorRH' : forms.TextInput(attrs={'class':'form-control'}),
			'varicela' : forms.Select(attrs={'class':'form-control'}),
			'sarampion' : forms.Select(attrs={'class':'form-control'}),
			'meringitis' : forms.Select(attrs={'class':'form-control'}),
			'rubeola' : forms.Select(attrs={'class':'form-control'}),
			'paperas' : forms.Select(attrs={'class':'form-control'}),
			'tifoidea' : forms.Select(attrs={'class':'form-control'}),
			'hepatitis' : forms.Select(attrs={'class':'form-control'}),
			'hanta' : forms.Select(attrs={'class':'form-control'}),
			'apendicitis' : forms.Select(attrs={'class':'form-control'}),
			'escarlinata' : forms.Select(attrs={'class':'form-control'}),
			'convulcion' : forms.Select(attrs={'class':'form-control'}),
	
			'parasetamol' : forms.Select(attrs={'class':'form-control'}),
			'ibuprofeno' : forms.Select(attrs={'class':'form-control'}),
			'clorfenamina' : forms.Select(attrs={'class':'form-control'}),
			'loratadina' : forms.Select(attrs={'class':'form-control'}),
			'viadil' : forms.Select(attrs={'class':'form-control'}),
			'amoxisilina' : forms.Select(attrs={'class':'form-control'}),

			'alergiaAlimentaria' : forms.Select(attrs={'class':'form-control'}),
			'alergiaMedicamento' : forms.Select(attrs={'class':'form-control'}),
			'alergiaOtros' : forms.TextInput(attrs={'class':'form-control'}),
			'utilizaLentes' : forms.Select(attrs={'class':'form-control'}),
			'esguince' : forms.Select(attrs={'class':'form-control'}),
			'fractura' : forms.Select(attrs={'class':'form-control'}),
			'operado' : forms.Select(attrs={'class':'form-control'}),
			'columna' : forms.Select(attrs={'class':'form-control'}),
			'piePlano' : forms.Select(attrs={'class':'form-control'}),
			'pieAtleta' : forms.Select(attrs={'class':'form-control'}),
			'movilidadReducida' : forms.Select(attrs={'class':'form-control'}),
			'hernias' : forms.Select(attrs={'class':'form-control'}),

			'diabetes' : forms.Select(attrs={'class':'form-control'}),
			'hipertension' : forms.Select(attrs={'class':'form-control'}),
			'epilepsia' : forms.Select(attrs={'class':'form-control'}),
			'asma' : forms.Select(attrs={'class':'form-control'}),
			'insuficienciaRenal' : forms.Select(attrs={'class':'form-control'}),
			'insifucienciaCardiaca' : forms.Select(attrs={'class':'form-control'}),
			'anemia' : forms.Select(attrs={'class':'form-control'}),
			'obesidad' : forms.Select(attrs={'class':'form-control'}),
			'apetito' : forms.Select(attrs={'class':'form-control'}),
			'reflujo' : forms.Select(attrs={'class':'form-control'}),
			'otra' : forms.TextInput(attrs={'class':'form-control'}),
			'otra2' : forms.TextInput(attrs={'class':'form-control'}),
			'otra3' : forms.TextInput(attrs={'class':'form-control'}),
			'medicamentos' : forms.TextInput(attrs={'class':'form-control'}),
		}