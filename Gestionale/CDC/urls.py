from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('index',views.index,name='index'),
	path('addValutaView',views.addValutaView,name='addValutaView'),
	path('eliminaMoneta',views.eliminaMoneta,name='eliiminaMoneta'),
	path('addCCIAAView', views.addCCIAAView,name='addCCIAAView'),
	path('eliminaCCIAA', views.eliminaCCIAA,name='eliminaCCIAA'),
	path('addDipendenteView', views.addDipendenteView,name='addDipendenteView'),
	path('eliminaDipendente', views.eliminaDipendente,name='eliminaDipendente'),
	path('addRestituzioneView', views.addRestituzioneView,name='addRestituzioneView'),
	path('eliminaRestituzione', views.eliminaRestituzione,name='eliminaRestituzione'),
	path('addMotPrestito', views.addMotPrestito,name='addMotPrestito'),
	path('eliminaMotPrestito', views.eliminaMotPrestito,name='eliminaMotPrestito'),
	path('addTassoInteresse', views.addTassoInteresse,name='addTassoInteresse'),
	path('eliminaTassoInteresse', views.eliminaTassoInteresse,name='eliminaTassoInteresse'),
	path('addTipoProvvedimento', views.addTipoProvvedimento,name='addTipoProvvedimento'),
	path('eliminaTipoProvvedimento', views.eliminaTipoProvvedimento,name='eliminaTipoProvvedimento'),
	path('addPrestitoView', views.addPrestitoView,name='addPrestitoView'),
	path('eliminaPrestito', views.eliminaCCIAA,name='eliminaPrestito'),
]
