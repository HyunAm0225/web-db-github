from django.forms import inlineformset_factory
from .models import Participant, PartyName

ParticipantInlineFormSet = inlineformset_factory(
    PartyName, Participant, fields=['image', 'nickname', 'age'], extra=2)
