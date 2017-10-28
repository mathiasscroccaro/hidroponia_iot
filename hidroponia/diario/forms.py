from django import forms
import datetime

class Formulario(forms.Form):
	comentarios = forms.CharField(widget=forms.Textarea)

class BuscarForm(forms.Form):
	data_inicial = forms.DateField(initial=datetime.date.today)
	data_final = forms.DateField(initial=datetime.date.today)	
