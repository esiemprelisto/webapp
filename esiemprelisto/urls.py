"""esiemprelisto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login
from boletin import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', views.inicio, name='registrar')
    url(r'^accounts/login', login, {'template_name':'inicio.html'}, name='login'),
    url(r'^$', logout_then_login, name='logout'),
    url(r'^menu/', login_required(views.index), name='menu'),
    url(r'^biblioteca/', views.biblioteca, name='biblioteca'),
    url(r'^vercategoria/(?P<id_categoria>\d+)/$', views.verCategoria, name='verCategoria'),
    url(r'^vercurriculum/(?P<id_user>\d+)/$', views.verCurriculum, name='verCurriculum'),
    url(r'^nuevousuario/', views.crearUsuario, name='nuevoUsuario'),
    url(r'^programas/', views.listaProgramas, name='listaProgramas'),
    url(r'^nuevanoticia/', views.nuevaNoticia, name='nuevaNoticia'),
    url(r'^nuevanoticiaNN/', views.nuevaNoticiaNivelNacional, name='nuevaNoticiaNN'),

    url(r'^nuevaprovincia/', views.nuevaProvincia, name='nuevaProvincia'),
    url(r'^nuevalocalidad/', views.nuevaLocalidad, name='nuevaLocalidad'),
    url(r'^nuevogrupo/', views.nuevaGrupo, name='nuevoGrupo'),

    url(r'^preguntanoticia/(?P<id_noticia>\d+)/$', views.preguntaNoticia, name='preguntaNoticia'),
    url(r'^respuestanoticia/(?P<id_pregunta>\d+)/$', views.respuestaNoticia, name='respuestaNoticia'),

    url(r'^programasgrupo/', views.listaProgramasJefeGrupo, name='listaProgramasGrupo'),
    url(r'^usuariosgrupo/', views.listaUsuariosJefeGrupo, name='usuariosGrupo'),
    url(r'^seccionesgrupo/', views.listaSeccionJefeGrupo, name='verSecciones'),
    url(r'^patrullasgrupo/', views.listaPatrullasJefeGrupo, name='verPatrullas'),
    url(r'^miprogresion/', views.verMiProgresion, name='verMiProgresion'),
    url(r'^nuevoprogramas/', views.nuevoProgramas, name='nuevoProgramas'),
    url(r'^nuevobeneficiario/', views.nuevoBeneficiario, name='nuevoBeneficiario'),
    url(r'^nuevodirigente/', views.nuevoDirigente, name='nuevoDirigente'),
    url(r'^editarasistencia/(?P<id_programa>\d+)/$', views.editarAsistencia, name='editarAsistencia'),
    url(r'^asistio/(?P<id_asistencia>\d+)/$', views.asistio, name='asistio'),
    url(r'^nuevopuntaje/(?P<id_linea>\d+)/$', views.nuevoPuntaje, name='nuevoPuntaje'),
    url(r'^editarusuario/(?P<id_usuario>\d+)/$', views.editarUsuario, name='editarUsuario'),
    url(r'^editarprogramas/(?P<id_programa>\d+)/$', views.editarPrograma, name='editarPrograma'),
    url(r'^editarpassword/', views.editarPassword, name='editarPassword'),
    url(r'^editarLineaPrograma/(?P<id_linea>\d+)/$', views.editarLineaPrograma, name='editarLineaPrograma'),
    url(r'^editardatospadre/(?P<id_dp>\d+)/$', views.editarDatosPadre, name='editarDatosPadre'),
    url(r'^editardatosapoderado/(?P<id_da>\d+)/$', views.editarDatosApoderado, name='editarDatosApoderado'),
    url(r'^editardatosmedicos/(?P<id_dm>\d+)/$', views.editarDatosMedicos, name='editarDatosMedicos'),
    url(r'^verprogramas/(?P<id_programa>\d+)/$', views.verPrograma, name='verPrograma'),
    url(r'^editaretapaprogresion/(?P<id_user>\d+)/$', views.editarEtapaProgresion, name='verEtapaProgresion'),
    url(r'^eliminarprogramas/(?P<id_programa>\d+)/$', views.eliminarPrograma, name='eliminarPrograma'),
    url(r'^eliminarLineaPrograma/(?P<id_linea>\d+)/$', views.eliminarLineaPrograma, name='eliminarLineaPrograma'),
    url(r'^miseccion/', views.verSeccion, name='miSeccion'),
    url(r'^cambiarurl/(?P<web_id>\d+)/$', views.cambiarUrl, name='cambiarUrl'),
]

