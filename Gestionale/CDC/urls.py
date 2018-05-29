from django.urls import path

from . import views

urlpatterns = [
	path('mostra', views.index, name='index'),
	path('add',views.addValutaView,name='addValutaView'),
]
