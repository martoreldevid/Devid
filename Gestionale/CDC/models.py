import datetime

from django.db import models

from django.utils import timezone

# Create your models here.

class Valuta(models.Model):
	Descrizione = models.CharField(max_length=200)

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	
	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		return self.pub_date >= timezone.now()-datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class CCIA(models.Model):
	Sede = models.CharField(max_length=45)
	Descrizione = models.CharField(max_length=200)

class Dipendente(models.Model):
	CF = models.CharField(max_length=30)
	Cognome = models.CharField(max_length=45)
	Nome = models.CharField(max_length=45)

class Restituzione(models.Model):
	Tipo = models.CharField(max_length=45)
	Descrizione = models.CharField(max_length=45)

class MotPrestito(models.Model):
	Motivazione = models.CharField(max_length=45)
	Descrizione = models.CharField(max_length=45)

class TassoInteresse(models.Model):
	Tipo = models.CharField(max_length=45)
	Percentuale = models.DecimalField(max_digits=5, decimal_places=2)
	Inizio = models.DateField(auto_now=False, auto_now_add=False,null=True)
	Fine = models.DateField(auto_now=False, auto_now_add=False,null=True)


class TipoMoneta(models.Model):
	Tipo = models.CharField(max_length=20)
	Simbolo = models.CharField(max_length=1)
	Descrizione = models.CharField(max_length=45)


class TipoProvvedimento(models.Model):
	Tipo = models.CharField(max_length=45)
	Descrizione = models.CharField(max_length=45)


class Prestito(models.Model):
	CF = models.ForeignKey(Dipendente, on_delete=models.DO_NOTHING,null=True)
	CCIA = models.ForeignKey(CCIA, on_delete=models.DO_NOTHING,null=True)
	TipoProvvedimento = models.ForeignKey(TipoProvvedimento, on_delete=models.DO_NOTHING,null=True)
	Numero = models.PositiveIntegerField(null=True)
	DataProvvedimento = models.DateField(auto_now=False, auto_now_add=False,null=True)
	Ammontare = models.DecimalField(max_digits=5, decimal_places=2,null=True)
	Valuta = models.ForeignKey(TipoMoneta, on_delete=models.DO_NOTHING,null=True)
	NumeroMandato = models.PositiveIntegerField(null=True)
	DataMandatoPagamento = models.DateField(auto_now=False, auto_now_add=False,null=True)
	MeseAnnoCedolino = models.DateField(auto_now=False,auto_now_add=False,null=True)
	Motivazione = models.ForeignKey(MotPrestito, on_delete=models.DO_NOTHING,null=True)
	ModRestituzione = models.ForeignKey(Restituzione, on_delete=models.DO_NOTHING,null=True)
	Tasso = models.ForeignKey(TassoInteresse, on_delete=models.DO_NOTHING,null=True)
	InEssere = models.NullBooleanField(null=True)
	DataCessazione = models.DateField(auto_now=False, auto_now_add=False,null=True)
	
