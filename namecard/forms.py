from django import forms

class NameCardSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')