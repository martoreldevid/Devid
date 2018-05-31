from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('index',views.index,name='index'),
	path('addValutaView',views.addValutaView,name='addValutaView'),
	path('eliminaMoneta/<str:tipo>',views.eliminaMoneta,name='eliiminaMoneta'),
]
