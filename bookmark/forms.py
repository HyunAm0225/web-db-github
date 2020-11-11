from django import forms

class BookMarkSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')