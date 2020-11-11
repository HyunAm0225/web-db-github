from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Participant, PartyName
from django.views.generic import ListView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from mysite.views import OwnerOnlyMixin
from .forms import ParticipantInlineFormSet


class ParticipantCV(LoginRequiredMixin, CreateView):
    model = Participant
    fields = ('party', 'nickname', 'age', 'image',)
    success_url = reverse_lazy('party:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ParticipantChangeLV(LoginRequiredMixin, ListView):
    model = Participant
    template_name = 'party/participant_change_list.html'

    def get_queryset(self):
        return Participant.objects.filter(owner=self.request.user)


class ParticipantUV(OwnerOnlyMixin, UpdateView):
    model = Participant
    fields = ('party', 'nickname', 'age', 'image',)
    success_url = reverse_lazy('party:index')


class ParticipantDelV(OwnerOnlyMixin, DeleteView):
    model = Participant
    success_url = reverse_lazy('party:index')


class PartyNameChangeLV(LoginRequiredMixin, ListView):
    model = PartyName
    template_name = 'party/partyname_change_list.html'

    def get_queryset(self):
        return PartyName.objects.filter(owner=self.request.user)


class PartyNameDelV(OwnerOnlyMixin, DeleteView):
    model = PartyName
    success_url = reverse_lazy('party:index')


class PartyNameParticipantCV(LoginRequiredMixin, CreateView):
    model = PartyName
    fields = ('name', 'place', 'description', 'opendate', 'openday')
    success_url = reverse_lazy('party:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = ParticipantInlineFormSet(
                self.request.POST, self.request.FILES)
        else:
            context['formset'] = ParticipantInlineFormSet()
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        context = self.get_context_data()
        formset = context['formset']
        for participantform in formset:
            participantform.instance.owner = self.request.user
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class PartyNameParticipantUV(OwnerOnlyMixin, UpdateView):
    model = PartyName
    fields = ('name', 'place', 'description', 'opendate', 'openday')
    success_url = reverse_lazy('party:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = ParticipantInlineFormSet(
                self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['formset'] = ParticipantInlineFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))
