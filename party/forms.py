from django.forms import inlineformset_factory
from .models import Participant, PartyName
from django import forms


ParticipantInlineFormSet = inlineformset_factory(
    PartyName, Participant, fields=['image', 'nickname', 'age'], extra=2)


class PartyNameSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Party')


class ParticipantSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Participant')
