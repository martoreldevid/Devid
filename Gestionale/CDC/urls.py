from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('index',views.index,name='index'),
	path('addValutaView',views.addValutaView,name='addValutaView'),
	path('eliminaMoneta',views.eliminaMoneta,name='eliiminaMoneta'),
]
