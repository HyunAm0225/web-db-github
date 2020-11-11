from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from .models import Student
# Create your views here.
from .forms import StudentSearchForm
from django.db.models import Q


from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin


class StudentLV(ListView):
    model = Student


class StudentDV(DetailView):
    model = Student


class SearchFormView(FormView):
    form_class = StudentSearchForm
    template_name = 'student/student_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        Student_list = Student.objects.filter(Q(name__icontains=searchWord)
                                              | Q(student_id__icontains=searchWord)
                                              | Q(department__icontains=searchWord)
                                              | Q(tel__icontains=searchWord)
                                              | Q(email__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = Student_list

        # No Redirection
        return render(self.request, self.template_name, context)


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    fields = ['student_id', 'name', 'department', 'tel', 'email', 'birth_dt']
    success_url = reverse_lazy('student:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class StudentChangeLV(LoginRequiredMixin, ListView):
    template_name = 'student/student_change_list.html'

    def get_queryset(self):
        return Student.objects.filter(owner=self.request.user)


class StudentUpdateView(OwnerOnlyMixin, UpdateView):
    model = Student
    fields = ['student_id', 'name', 'department', 'tel', 'email', 'birth_dt']
    success_url = reverse_lazy('student:index')


class StudentDeleteView(OwnerOnlyMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('student:index')


# ['student_id', 'name', 'department', 'tel', 'email', 'birth_dt']
