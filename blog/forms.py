from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms

class ContactForm(forms.Form):
	email = forms.EmailField()
	name = forms.CharField(max_length=140)
	subject = forms.CharField(max_length=140)
	message = forms.CharField(widget = forms.Textarea)

