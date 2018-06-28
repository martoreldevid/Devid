from django.shortcuts import render

# Create your views here.


from datetime import datetime

from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .forms import addValutaForm,addCCIAAForm,addDipendenteForm,addRestituzioneForm,addMotPrestitoForm,addTassoInteresseForm,addTipoProvvedimentoForm,addPrestitoForm

from CDC.models import TipoMoneta,CCIA,Dipendente,Restituzione,MotPrestito,TassoInteresse,TipoProvvedimento,Prestito
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
		listaMonete = TipoMoneta.objects.all()
		context = {
			'listaMonete': listaMonete,
			'form':form,		
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

		form = addDipendenteForm()
	
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

			restituzione = Restituzione(Tipo=tipo,Descrizione=descrizione)
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


def eliminaMotPrestito(request):

	varMot = request.POST.get('motivazione')
		
	MotPrestito.objects.filter(Motivazione=varMot).delete()

	request.method="GET"

	return addMotPrestitoView(request)



def addTassoInteresseView(request):
	
	if request.method == 'POST':

		form = addTassoInteresseForm(request.POST)
		
		if form.is_valid():		
			#PERFORM DATA

			tipo = form.cleaned_data['tipo']
			percentuale = form.cleaned_data['percentuale']
			inizio = request.POST.get('inizio')
			fine = request.POST.get('fine')

			tasso = TassoInteresse(Tipo=tipo,Percentuale=percentuale,Inizio=inizio,Fine=fine)
			
			try:
				tasso.save()
			except IntegrityError:
				pass
				
			request.method="GET"

			return addTassoInteresseView(request)
	
	else:

		form = addTassoInteresseForm()
	
		listaTassi = TassoInteresse.objects.all()
		context = {
			'listaTassi': listaTassi,
			'form':form,		
		}
		
		return render(request, 'CDC/addTassoInteresseView.html',context)


def eliminaTassoInteresse(request):

	varTipo = request.POST.get('tipo')
		
	TassoInteresse.objects.filter(Tipo=varTipo).delete()

	request.method="GET"

	return addTassoInteresseView(request)


def addTipoProvvedimentoView(request):
	
	if request.method == 'POST':

		form = addTipoProvvedimentoForm(request.POST)
			
		if form.is_valid():		
			#PERFORM DATA

			tipo  = form.cleaned_data['tipo']
			descrizione = form.cleaned_data['descrizione']
			
			tipoProvvedimento = TipoProvvedimento(Tipo=tipo,Descrizione=descrizione)
			try:
				tipoProvvedimento.save()
			except IntegrityError:
				pass
				
			request.method="GET"

			return addTipoProvvedimentoView(request)
	
	else:

		form = addTipoProvvedimentoForm()
	
		listaProvvedimenti = TipoProvvedimento.objects.all()
		context = {
			'listaProvvedimenti': listaProvvedimenti,
			'form':form,		
		}
		
		return render(request, 'CDC/addTipoProvvedimentoView.html',context)


def eliminaTipoProvvedimento(request):

	varTipo = request.POST.get('tipo')
		
	TipoProvvedimento.objects.filter(Tipo=varTipo).delete()

	request.method="GET"
	
	return addTipoProvvedimentoView(request)



def addPrestitoView(request):
	
	if request.method == 'POST':
		form = addPrestitoForm(request.POST)
		if form.is_valid():
			cf = request.POST.get('cf')			
			cciaa = request.POST.get('cciaa')
			tipoProvvedimento = request.POST.get('tipoProvvedimento')
			numero = form.cleaned_data['numero']
			dataProvvedimento = request.POST.get('dataProvvedimento')
			ammontare = form.cleaned_data['ammontare']
			valuta = request.POST.get('valuta')
			numeroMandato = form.cleaned_data['numeroMandato']
			dataMandatoPagamento = request.POST.get('dataMandatoPagamento')
			meseAnnoCedolino = request.POST.get('meseAnnoCedolino')
			motivazione = request.POST.get('motivazione')
			modRestituzione = request.POST.get('modRestituzione')
			tasso = requst.POST.get('tasso')
			dataCessazione = request.POST.get('dataCessazione')
			prestito = Prestito(CF=cf,CCIA=cciaa,TipoProvvedimento=tipoProvvedimento,Numero=numero,DataProvvedimento=dataProvvedimento,Ammontare=ammontare,Valuta=valuta,NumeroMandato=numeroMandato,DataMandatoPagamento=dataMandatoPagamento,MeseAnnoCedolino=meseAnnoCedolio,Motivazione=motivazione,ModRestituzione=modRestituzione,Tasso=tasso,InEssere=False,DataCessazione=dataCessazione)
			try:
				prestito.save()
			except IntegrityError:
				pass
			request.method="GET"
			return addPrestitoView(request)

	else:
		form = addPrestitoForm()	
		listaCf = Dipendente.objects.all()
		listaCCIAA = CCIA.objects.all()
		listaProv = TipoProvvedimento.objects.all()
		listaValuta = TipoMoneta.objects.all()
		listaMotivazioni = MotPrestito.objects.all()
		listaModRest = Restituzione.objects.all()
		listaTassi = TassoInteresse.objects.all()
		listaPrestiti = Prestito.objects.all()
		context = {
			'listaCf': listaCf,
			'listaCCIAA': listaCCIAA,
			'listaProv': listaProv,
			'listaValuta': listaValuta,
			'listaMotivazioni': listaMotivazioni,
			'listaModRest': listaModRest,
			'listaTassi': listaTassi,
			'form': form,
			'listaPrestiti': listaPrestiti,		
		}
		return render(request, 'CDC/addPrestitoView.html',context)


def eliminaPrestito(request):

	varId = request.POST.get('id')
		
	Prestito.objects.filter(id=varID).delete()

	request.method="GET"
	
	return addPrestitoView(request)



def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
    return next_month - datetime.timedelta(days=next_month.day)


def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def PrestitoElaborato(request):

	idPrestito = request.POST.get('id')
	dataInizioCalcolo = request.POST.get('inizioCalcolo')	
	dataFineCalcolo = request.POST.get('fineCalcolo')
	
	prestito =Prestito.objects.filter(id=idPrestito)

	cf = prestito.CF
	
	dipendente = Dipendente.objects.filter(CF=cf)
	Nome = dipendente.Nome
	Cognome = dipendente.Cognome
	
	valuta = prestito.Valuta
	tipoMoneta = TipoMoneta.objects.filter(Tipo=valuta)
	Tipo = tipoMoneta.Tipo
	Simbolo = tipoMoneta.Simbolo
	
	tasso = prestito.Tasso
	tassoInteresse = TassoInteresse.objects.filter(Tipo=tasso)
	Percentuale = tassoInteresse.Percentuale
	tipoTasso = tassoInteresse.Tipo

	if( prestito.MeseAnnoCedolino >0):
		
		dataInizioAnticipo=last_day_of_month(prestito.MeseAnnoCedolino)
		dataInizioAnticipo=dataInizioAnticipo+1		
	
	else: dataInizioAnticipo=prestito.DataMandatoPagamento

	dataFineAnticipo=dataFineCalcolo

	Ammontare = prestito.Ammontare
	
	if( prestito.DataCessazione == None): dataCessataAnticipazione=DataFineCalcolo
	else: dataCessataAnticipazione = prestito.DataCessazione


	dataInizioFasciaU=datetime.date(2014,12,9)
	dataFineFasciaU=datetime.date(2900,12,31)	

	if( dataInizioCalcolo>dataInizioFasciaU and dataInizioCalcolo<dataFineFasciaU):
		interessiMensiliFascia = ((Ammontare*5)/100)/12
		mesiAppartenentiU = days_between(dataInizioCalcolo,dataFineCalcolo)/30
	
	



	context = {
			'prestito': prestito,
			'Nominativo': Cognome,
			'Tipo': Tipo,
			'Nome': Nome,
			'Simbolo': Simbolo,
			'InizioCalcolo':dataInizioAnticipo,
			'FineCalcolo': dataFineCalcolo,
			'InteressiFascia1': interessiMensiliFasciaU,
		}
		
	return render(request, 'CDC/viewPrestitoElaborato.html',context)
	
