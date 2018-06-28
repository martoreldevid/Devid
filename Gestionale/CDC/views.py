from django.shortcuts import render

# Create your views here.
from decimal import Decimal
from datetime import datetime,timedelta
from dateutil import relativedelta

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as auth_login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .forms import addValutaForm,addCCIAAForm,addDipendenteForm,addRestituzioneForm,addMotPrestitoForm,addTassoInteresseForm,addTipoProvvedimentoForm,addPrestitoForm

from CDC.models import TipoMoneta,CCIA,Dipendente,Restituzione,MotPrestito,TassoInteresse,TipoProvvedimento,Prestito
from django.db import IntegrityError


def login(request):

	if request.method == 'POST':	

		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			auth_login(request,user)
			return index(request)
	else:
		context={}
		return render(request, 'CDC/viewLogin.html',context)

def logoutView(request):
	logout(request)
	context={}
	return render(request, 'CDC/viewLogin.html',context)

@login_required
def index(request):
	context={}
	return render(request, 'CDC/index.html',context)

@login_required
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

@login_required
def eliminaMoneta(request):

	varTipo = request.POST.get('tipo')
		
	TipoMoneta.objects.filter(Tipo=varTipo).delete()

	request.method="GET"

	return addValutaView(request)


@login_required
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


@login_required
def eliminaCCIAA(request):

	varSede = request.POST.get('sede')
		
	CCIA.objects.filter(Sede=varSede).delete()

	request.method="GET"

	return addCCIAAView(request)



@login_required
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

@login_required
def eliminaDipendente(request):

	varCF = request.POST.get('cf')
		
	Dipendente.objects.filter(CF=cf).delete()

	request.method="GET"
	
	return addDipendenteView(request)


@login_required
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

@login_required
def eliminaRestituzione(request):

	varTipo = request.POST.get('tipo')
		
	Restituzione.objects.filter(Tipo=varTipo).delete()

	request.method="GET"

	return addCCIAAView(request)

@login_required
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

@login_required
def eliminaMotPrestito(request):

	varMot = request.POST.get('motivazione')
		
	MotPrestito.objects.filter(Motivazione=varMot).delete()

	request.method="GET"

	return addMotPrestitoView(request)


@login_required
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

@login_required
def eliminaTassoInteresse(request):

	varTipo = request.POST.get('tipo')
		
	TassoInteresse.objects.filter(Tipo=varTipo).delete()

	request.method="GET"

	return addTassoInteresseView(request)

@login_required
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

@login_required
def eliminaTipoProvvedimento(request):

	varTipo = request.POST.get('tipo')
		
	TipoProvvedimento.objects.filter(Tipo=varTipo).delete()

	request.method="GET"
	
	return addTipoProvvedimentoView(request)


@login_required
def addPrestitoView(request):	
	if request.method == 'POST':

		form = addPrestitoForm(request.POST)

		if form.is_valid():

			dip = request.POST.get('cf')
			cf = Dipendente.objects.filter(CF=dip)[0]
			cciaaapp = request.POST.get('cciaa')
			cciaa = CCIA.objects.filter(Sede=cciaaapp)[0]
			tipoProvvedimentoapp = request.POST.get('prov')
			tipoProvvedimento = TipoProvvedimento.objects.filter(Tipo=tipoProvvedimentoapp)[0]
			numero = form.cleaned_data['numero']
			dataProvvedimento = request.POST.get('dataProvvedimento')
			ammontare = form.cleaned_data['ammontare']
			valutaapp = request.POST.get('valuta')
			valuta = TipoMoneta.objects.filter(Simbolo=valutaapp)[0]
			numeroMandato = form.cleaned_data['numeroMandato']
			dataMandatoPagamento = request.POST.get('dataMandatoPagamento')
			meseAnnoCedolino = request.POST.get('meseAnnoCedolino')
			motivazioneapp = request.POST.get('motivazione')
			motivazione = MotPrestito.objects.filter(Motivazione=motivazioneapp)[0]
			modRestituzioneapp = request.POST.get('modRestituzione')
			modRestituzione = Restituzione.objects.filter(Tipo=modRestituzioneapp)[0]
			tassoapp = request.POST.get('tasso')
			tasso = TassoInteresse.objects.filter(Tipo=tassoapp)[0]
			dataCessazione = request.POST.get('dataCessazione')

			prestito = Prestito(CF=cf,CCIA=cciaa,TipoProvvedimento=tipoProvvedimento,Numero=numero,DataProvvedimento=dataProvvedimento,Ammontare=ammontare,Valuta=valuta,NumeroMandato=numeroMandato,DataMandatoPagamento=dataMandatoPagamento,MeseAnnoCedolino=meseAnnoCedolino,Motivazione=motivazione,ModRestituzione=modRestituzione,Tasso=tasso,InEssere=False,DataCessazione=dataCessazione)

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

@login_required
def eliminaPrestito(request):

	varId = request.POST.get('id')
		
	Prestito.objects.filter(id=varID).delete()

	request.method="GET"
	
	return addPrestitoView(request)



def last_day_of_month(any_day):
	next_month = any_day.replace(day=28) + timedelta(days=4)  # this will never fail
	return next_month - timedelta(days=next_month.day)


def days_between(d1, d2):
	return abs((d2 - d1).days)


@login_required
def PrestitoElaborato(request):

	idPrestito = request.POST.get('id')
	#dataInizioCalcolo = request.POST.get('inizioCalcolo')	
	#dataFineCalcolo = request.POST.get('fineCalcolo')
	
	dataInizioCalcolo= datetime(2015,1,1)
	dataFineCalcolo =  datetime(2017,12,31)

	prestito =Prestito.objects.filter(id=idPrestito)[0]

	cf = prestito.CF
	
	Nome = cf.Nome
	Cognome = cf.Cognome
	
	valuta = prestito.Valuta

	Tipo = valuta.Tipo
	Simbolo = valuta.Simbolo
	
	tasso = prestito.Tasso

	Percentuale = tasso.Percentuale
	tipoTasso = tasso.Tipo

	if( prestito.MeseAnnoCedolino != None):
		
		dataInizioAnticipo=last_day_of_month(prestito.MeseAnnoCedolino)
		dataInizioAnticipo=dataInizioAnticipo+timedelta(days=1)		
	
	else: dataInizioAnticipo=prestito.DataMandatoPagamento

	dataFineAnticipo=dataFineCalcolo

	Ammontare = prestito.Ammontare
	
	if( prestito.DataCessazione == None): dataCessataAnticipazione=DataFineCalcolo
	else: dataCessataAnticipazione = prestito.DataCessazione


	dataInizioFasciaU=datetime(2014,12,9)
	dataFineFasciaU=datetime(2900,12,31)	

	if( dataInizioCalcolo>dataInizioFasciaU and dataInizioCalcolo<dataFineFasciaU):
		interessiMensiliFasciaU = ((Ammontare*15)/1000)/12
		datadiff = relativedelta.relativedelta(dataFineCalcolo, dataInizioCalcolo)	
		mesiAppartenentiU = (datadiff.months + (datadiff.years*12))-4
		interessiPeriodo = mesiAppartenentiU*interessiMensiliFasciaU
		dataInizioMese = dataFineCalcolo
		dataInizioMese = dataInizioMese.replace(day=1)
		datadiffine = relativedelta.relativedelta(dataFineCalcolo,dataInizioMese).days+1
		dataFineMese = last_day_of_month(dataInizioMese)
		giorniMese = relativedelta.relativedelta(dataFineMese,dataInizioMese).days+1
		interessiMeseFinale = Decimal((interessiMensiliFasciaU/giorniMese)*datadiffine)
		interessiMeseFinale = round(interessiMeseFinale,2)		

	context = {
			'prestito': prestito,
			'Cognome': Cognome,
			'Tipo': Tipo,
			'Nome': Nome,
			'Simbolo': Simbolo,
			'InizioCalcolo':dataInizioAnticipo,
			'FineCalcolo': dataFineCalcolo,
			'InteressiFascia1': interessiMensiliFasciaU,
			'MesiAppartenentiU': mesiAppartenentiU,
			'InteressiPeriodo': interessiPeriodo,
			'interessiMeseFinale': interessiMeseFinale,
		}
		
	return render(request, 'CDC/viewPrestitoElaborato.html',context)
	
