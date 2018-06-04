from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .forms import addValutaForm,eliminaMonetaForm,addCCIAAForm

from CDC.models import TipoMoneta,CCIA,Dipendente
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
	
		listaCCIAA = CCIA.objects.all()
		context = {
			'listaCCIAA': listaCCIAA,
			'form':form,		
		}
		
		return render(request, 'CDC/addCCIAAView.html',context)


def eliminaCCIAA(request):

	varSede = request.POST.get('sede')
		
	CCIA.objects.filter(Sede=varSede).delete()

	request.method="GET"

	return addCCIAAView(request)




def addDipendenteView(request):
	
	if request.method == 'POST':

		form = addDipendenteForm(request.POST)
			
		if form.is_valid():		
			#PERFORM DATA

			cf  = form.cleaned_data['cf']
			cognome = form.cleaned_data['cognome']
			nome = form.cleaned_data['nome']

			dipendente = Dipendente(CF=cf,Cognome=cognome,Nome=nome)
			try:
				dipendente.save()
			except IntegrityError:
				pass
				
			request.method="GET"

			return addDipendenteView(request)
	
	else:

		form = addDipenenteForm()
	
		listaDipendenti = Dipendente.objects.all()
		context = {
			'listaDipendenti': listaDipendenti,
			'form':form,		
		}
		
		return render(request, 'CDC/addDipendenteView.html',context)


def eliminaDipendente(request):

	varCF = request.POST.get('cf')
		
	Dipendente.objects.filter(CF=cf).delete()

	request.method="GET"
	
	return addDipendenteView(request)



def addRestituzioneView(request):
	
	if request.method == 'POST':

		form = addRestituzioneForm(request.POST)
		
		if form.is_valid():		
			#PERFORM DATA

			tipo  = form.cleaned_data['tipo']
			descrizione = form.cleaned_data['descrizione']

			restituzione = Restituzione(Tipo=Tipo,Descrizione=descrizione)
			try:
				restituzione.save()
			except IntegrityError:
				pass
				
			request.method="GET"

			return addRestituzioneView(request)
	
	else:

		form = addRestituzioneForm()
	
		listaRestituzioni = Restituzione.objects.all()
		context = {
			'listaRestituzioni': listaRestituzioni,
			'form':form,		
		}
		
		return render(request, 'CDC/addRestituzioneView.html',context)


def eliminaRestituzione(request):

	varTipo = request.POST.get('tipo')
		
	Restituzione.objects.filter(Tipo=varTipo).delete()

	request.method="GET"

	return addCCIAAView(request)


def addMotPrestitoView(request):
	
	if request.method == 'POST':

		form = addMotPrestitoForm(request.POST)
		
		if form.is_valid():		
			#PERFORM DATA

			motivazione  = form.cleaned_data['motivazione']
			descrizione = form.cleaned_data['descrizione']

			mot = MotPrestito(Motivazione=motivazione,Descrizione=descrizione)
			try:
				mot.save()
			except IntegrityError:
				pass
				
			request.method="GET"

			return addMotPrestitoView(request)
	
	else:

		form = addMotPrestitoForm()
	
		listaMotivazioni = MotPrestito.objects.all()
		context = {
			'listaMotivazioni': listaMotivazioni,
			'form':form,		
		}
		
		return render(request, 'CDC/addMotPrestitoView.html',context)


def eliminaCCIAA(request):

	varMot = request.POST.get('motivazione')
		
	MotPrestito.objects.filter(Motivazione=varMot).delete()

	request.method="GET"

	return addMotPrestitoView(request)
