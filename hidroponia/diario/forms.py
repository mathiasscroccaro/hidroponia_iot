from django import forms

class Formulario(forms.Form):
	comentarios = forms.CharField(widget=forms.Textarea)
	
