from django.urls import path

from . import views

urlpatterns = [
	path('', views.login, name='viewLogin'),
	path('logoutView', views.logoutView, name='logoutView'),
	path('viewLogin',views.login, name='viewLogin'),
	path('index',views.index,name='index'),
	path('addValutaView',views.addValutaView,name='addValutaView'),
	path('eliminaMoneta',views.eliminaMoneta,name='eliiminaMoneta'),
	path('addCCIAAView', views.addCCIAAView,name='addCCIAAView'),
	path('eliminaCCIAA', views.eliminaCCIAA,name='eliminaCCIAA'),
	path('addDipendenteView', views.addDipendenteView,name='addDipendenteView'),
	path('eliminaDipendente', views.eliminaDipendente,name='eliminaDipendente'),
	path('addRestituzioneView', views.addRestituzioneView,name='addRestituzioneView'),
	path('eliminaRestituzione', views.eliminaRestituzione,name='eliminaRestituzione'),
	path('addMotPrestitoView', views.addMotPrestitoView,name='addMotPrestitoView'),
	path('eliminaMotPrestito', views.eliminaMotPrestito,name='eliminaMotPrestito'),
	path('addTassoInteresseView', views.addTassoInteresseView,name='addTassoInteresseView'),
	path('eliminaTassoInteresse', views.eliminaTassoInteresse,name='eliminaTassoInteresse'),
	path('addTipoProvvedimentoView', views.addTipoProvvedimentoView,name='addTipoProvvedimentoView'),
	path('eliminaTipoProvvedimento', views.eliminaTipoProvvedimento,name='eliminaTipoProvvedimento'),
	path('addPrestitoView', views.addPrestitoView,name='addPrestitoView'),
	path('eliminaPrestito', views.eliminaPrestito,name='eliminaPrestito'),
	path('viewPrestito', views.PrestitoElaborato,name='PrestitoElaborato'),
	path('dataDaElaborare', views.dataDaElaborare,name='dataDaElaborare'),
]
