from django.urls import path
from .models import Subject, Sugang_Student
from django.views.generic import ListView, DetailView
from . import views

app_name = 'sugang'
urlpatterns = [
    path('', ListView.as_view(model=Subject), name='index'),
    # path('subject', ListView.as_view(model=Subject), name='subject_list'),
    path('subject/<int:pk>/', DetailView.as_view(model=Subject),
         name='subject_detail'),
    path('sugang_student/<int:pk>/', DetailView.as_view(model=Sugang_Student),
         name='student_detail'),
    path('subject/add/', views.SubjectStudentCV.as_view(), name='subject_add'),
    path('subject/change/', views.SubjectChangeLV.as_view(), name='subject_change'),
    path('subject/<int:pk>/update/',
         views.SubjectStudentUV.as_view(), name='subject_update'),
    path('subject/<int:pk>/delete/',
         views.SubjectDelV.as_view(), name='subject_delete'),
    path('sugang_student/add/', views.StudentCV.as_view(),
         name='sugang_student_add'),
    path('sugang_student/change/', views.StudentChangeLV.as_view(),
         name='sugang_student_change'),
    path('sugang_student/<int:pk>/update/',
         views.StudentUV.as_view(), name='sugang_student_update'),
    path('sugang_student/<int:pk>/delete/',
         views.StudentDelV.as_view(), name='sugang_student_delete'),

]
