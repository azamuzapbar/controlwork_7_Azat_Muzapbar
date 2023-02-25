from django import forms
from django.forms import widgets
class ArticleForm(forms.Form):
    title = forms.CharField(max_length=100, required=True, label='title')
    text = forms.CharField(max_length=3000, required=True, label='text', widget=widgets.Textarea )
    mail = forms.EmailField(max_length=3500, required=True, label='mail')
