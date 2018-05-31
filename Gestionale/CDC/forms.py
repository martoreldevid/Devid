from django import forms

class addValutaForm(forms.Form):
	tipo = forms.CharField(label='Tipo', max_length=20)
	simbolo = forms.CharField(label='Simbolo', max_length=1)
	descrizione = forms.CharField(label='Descrizione', max_length=45)

class eliminaMonetaForm(forms.Form):
	tipo = forms.CharField(label='Tipo', max_length=20)
