from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .forms import addValutaForm,eliminaMonetaForm

from CDC.models import TipoMoneta,CCIA
from django.db import IntegrityError

def index(request):
	template = loader.get_template('CDC/index.html')
	return HttpResponse(template.render())


def addValutaView(request):
	
	if request.method == 'POST':

		form = addValutaForm(request.POST)
		
		if form.is_valid():		
			#PERFORM DATA

			tipo = form.cleaned_data['tipo']
			simbolo = form.cleaned_data['simbolo']
			descrizione = form.cleaned_data['descrizione']

			moneta=TipoMoneta(Tipo=tipo,Simbolo=simbolo,Descrizione=descrizione)
			try:
				moneta.save()
			except IntegrityError:
				pass
				
			request.method="GET"

			return addValutaView(request)
	
	else:

		form = addValutaForm()
		formElimina = eliminaMonetaForm()
		listaMonete = TipoMoneta.objects.all()
		context = {
			'listaMonete': listaMonete,
			'form':form,		
			'formElimina':formElimina,
		}
		
		return render(request, 'CDC/addValutaView.html',context)

def eliminaMoneta(request):

	varTipo = request.POST.get('tipo')
		
	TipoMoneta.objects.filter(Tipo=varTipo).delete()

	request.method="GET"

	return addValutaView(request)



def addCCIAAView(request):
	
	if request.method == 'POST':

		form = addCCIAAForm(request.POST)
		
		if form.is_valid():		
			#PERFORM DATA

			sede  = form.cleaned_data['sede']
			descrizione = form.cleaned_data['descrizione']

			cciaa = CCIA(Sede=sede,Descrizione=descrizione)
			try:
				cciaa.save()
			except IntegrityError:
				pass
				
			request.method="GET"

			return addCCIAAView(request)
	
	else:

		form = addCCIAAForm()
	
		listacciaa = CCIA.objects.all()
		context = {
			'listaCCIAA': listacciaa,
			'form':form,		
		}
		
		return render(request, 'CDC/addCCIAAView.html',context)
