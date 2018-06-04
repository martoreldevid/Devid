from django import forms

class addValutaForm(forms.Form):
	tipo = forms.CharField(label='Tipo', max_length=20)
	simbolo = forms.CharField(label='Simbolo', max_length=1)
	descrizione = forms.CharField(label='Descrizione', max_length=45)

class eliminaMonetaForm(forms.Form):
	tipo = forms.CharField(label='Tipo', max_length=20)



class addCCIAAForm(forms.Form):
	sede = forms.CharField(label='Sede', max_length=45)
	descrizione = forms.CharField(label='Descrizione', max_length=45)


class addDipendenteForm(forms.Form):
	cf = forms.CharField(label='CF', max_length=30)
	cognome = forms.CharField(label='Cognome', max_length=45)
	nome = forms.CharField(label='Nome', max_length=45)

class addRestituzioneForm(forms.Form):
	tipo  = forms.CharField(label='Tipo', max_length=45)
	descrizione = forms.CharField(label='Descrizione', max_length=45)

class addMotPrestitoForm(forms.Form):
	motivazione = forms.CharField(label='Motivazione', max_length=45)
	descrizione = forms.CharField(label='Descrizione', max_length=45)

class addTassoInteresseForm(forms.Form):
	tipo = forms.CharField(label='Tipo', max_length=45)
	percentuale  = forms.DecimalField(label='Descrizione', max_digits=5,decimal_places=2)
	inizio = forms.DateField(label='Inizio')
	fine = forms.DateField(label='Fine')

class addTipoProvvedimentoForm(forms.Form):
	tipo = forms.CharField(label='Tipo', max_length=45)
	descrizione = forms.CharField(label='Descrizione', max_length=45) 

class addPrestitoForm(forms.Form):
	sede = forms.CharField(label='Sede', max_length=45)
	descrizione = forms.CharField(label='Descrizione', max_length=45)
	tipo = forms.CharField(label='Tipo', max_length=20)
	tipo = forms.CharField(label='Tipo', max_length=20)
	tipo = forms.CharField(label='Tipo', max_length=20)
	tipo = forms.CharField(label='Tipo', max_length=20)
	tipo = forms.CharField(label='Tipo', max_length=20)
	tipo = forms.CharField(label='Tipo', max_length=20)
	tipo = forms.CharField(label='Tipo', max_length=20)
	tipo = forms.CharField(label='Tipo', max_length=20)
	tipo = forms.CharField(label='Tipo', max_length=20)
	tipo = forms.CharField(label='Tipo', max_length=20)
	tipo = forms.CharField(label='Tipo', max_length=20)
	tipo = forms.CharField(label='Tipo', max_length=20)
	tipo = forms.CharField(label='Tipo', max_length=20)
	
