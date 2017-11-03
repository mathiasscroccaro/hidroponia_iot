from django.utils import timezone
from django import forms
import datetime

class Formulario(forms.Form):
	comentarios = forms.CharField(widget=forms.Textarea)

class BuscarForm(forms.Form):
	data_inicial = forms.DateField(initial=timezone.now())
	data_final = forms.DateField(initial=timezone.now())	

class ControleForm(forms.Form):
	ph_setpoint = forms.FloatField()
        
