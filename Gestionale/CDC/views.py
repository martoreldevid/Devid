from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .forms import addValutaForm,eliminaMonetaForm

from CDC.models import TipoMoneta


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
			moneta.save()

			return HttpResponseRedirect('/')
	
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

	tipo = request.GET.get('tipo', None)	
	monete = TipoMoneta.objects.filter(Tipo=tipo).delete()

	return addValutaView(request)
