from django.contrib import admin
from .models import Participant, PartyName
# Register your models here.


class ParticipantInLine(admin.StackedInline):
    model = Participant
    extra = 2


@admin.register(PartyName)
class PartyNameAdmin(admin.ModelAdmin):
    inlines = (ParticipantInLine,)
    list_display = ('id', 'name', 'description', 'place', 'opendate')


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'age', 'join_dt')
