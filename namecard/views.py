from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from .models import Namecard_TBL

from .forms import NameCardSearchForm
from django.db.models import Q

from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin


# Create your views here.
class NamecardLV(ListView):
    model = Namecard_TBL


class NamecardDV(DetailView):
    model = Namecard_TBL


class SearchFormView(FormView):
    form_class = NameCardSearchForm
    template_name = 'namecard/namecard_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        Namecard_list = Namecard_TBL.objects.filter(Q(name__icontains=searchWord) |
                                                    Q(tel__icontains=searchWord) |
                                                    Q(company__icontains=searchWord) |
                                                    Q(email__icontains=searchWord) |
                                                    Q(group__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = Namecard_list

        # No Redirection
        return render(self.request, self.template_name, context)


class NamecardCreateView(LoginRequiredMixin, CreateView):
    model = Namecard_TBL
    fields = ['name', 'tel', 'company', 'email', 'group', 'birth_dt']
    success_url = reverse_lazy('namecard:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class NamecardChangeLV(LoginRequiredMixin, ListView):
    template_name = 'namecard/namecard_change_list.html'

    def get_queryset(self):
        return Namecard_TBL.objects.filter(owner=self.request.user)


class NamecardUpdateView(OwnerOnlyMixin, UpdateView):
    model = Namecard_TBL
    fields = ['name', 'tel', 'company', 'email', 'group', 'birth_dt']
    success_url = reverse_lazy('namecard:index')


class NamecardDeleteView(OwnerOnlyMixin, DeleteView):
    model = Namecard_TBL
    success_url = reverse_lazy('namecard:index')
