from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Subject, Sugang_Student
# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from mysite.views import OwnerOnlyMixin
from .forms import SugangtoInlineFormSet


class StudentCV(LoginRequiredMixin, CreateView):
    model = Sugang_Student
    fields = ('student_id', 'name', 'image', 'subject',)
    success_url = reverse_lazy('sugang:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class StudentChangeLV(LoginRequiredMixin, ListView):
    model = Sugang_Student
    template_name = 'sugang/sugang_student_change_list.html'

    def get_queryset(self):
        return Sugang_Student.objects.filter(owner=self.request.user)


class StudentUV(OwnerOnlyMixin, UpdateView):
    model = Sugang_Student
    fields = ('student_id', 'name', 'image', 'subject',)
    success_url = reverse_lazy('sugang:index')


class StudentDelV(OwnerOnlyMixin, DeleteView):
    model = Sugang_Student
    success_url = reverse_lazy('sugang:index')

# Subject 에 관한 View


class SubjectChangeLV(LoginRequiredMixin, ListView):
    model = Subject
    template_name = 'sugang/subject_change_list.html'

    def get_queryset(self):
        return Subject.objects.filter(owner=self.request.user)


class SubjectDelV(OwnerOnlyMixin, DeleteView):
    model = Subject
    success_url = reverse_lazy('sugang:index')


class SubjectStudentCV(LoginRequiredMixin, CreateView):
    model = Subject
    fields = ('subject_id', 'name', 'point', 'max_student',
              'class_time', 'pd_name', 'class_room')
    success_url = reverse_lazy('sugang:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = SugangtoInlineFormSet(
                self.request.POST, self.request.FILES)
        else:
            context['formset'] = SugangtoInlineFormSet()
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        context = self.get_context_data()
        formset = context['formset']
        for photoform in formset:
            photoform.instance.owner = self.request.user
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class SubjectStudentUV(OwnerOnlyMixin, UpdateView):
    model = Subject
    fields = ('subject_id', 'name', 'point', 'max_student',
              'class_time', 'pd_name', 'class_room',)
    success_url = reverse_lazy('sugang:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = SugangtoInlineFormSet(
                self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['formset'] = SugangtoInlineFormSet(instance=self.object)
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
