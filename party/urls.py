from django.urls import path
from .models import Participant, PartyName
from . import views
from django.views.generic import ListView, DetailView

app_name = 'party'
urlpatterns = [
    path('', ListView.as_view(model=PartyName), name='index'),
    path('partyname', ListView.as_view(model=PartyName), name='partyname_list'),
    path('partyname/<int:pk>/', DetailView.as_view(model=PartyName),
         name='partyname_detail'),
    path('participant/<int:pk>/', DetailView.as_view(model=Participant),
         name='participant_detail'),

    path('partyname/add/', views.PartyNameParticipantCV.as_view(),
         name='partyname_add'),
    path('partyname/change/', views.PartyNameChangeLV.as_view(),
         name='partyname_change'),
    path('partyname/<int:pk>/update/',
         views.PartyNameParticipantUV.as_view(), name='partyname_update'),
    path('partyname/<int:pk>/delete/',
         views.PartyNameDelV.as_view(), name='partyname_delete'),
    path('participant/add/', views.ParticipantCV.as_view(), name='participant_add'),
    path('participant/change/', views.ParticipantChangeLV.as_view(),
         name='participant_change'),
    path('participant/<int:pk>/update/',
         views.ParticipantUV.as_view(), name='participant_update'),
    path('participant/<int:pk>/delete/',
         views.ParticipantDelV.as_view(), name='participant_delete'),

]
