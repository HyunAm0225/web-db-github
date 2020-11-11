from django.contrib import admin
from .models import Subject, Sugang_Student
# Register your models here.


class StudentInLine(admin.StackedInline):
    model = Sugang_Student
    extra = 1


@admin.register(Subject)
class AlbumAdmin(admin.ModelAdmin):
    inlines = (StudentInLine,)
    list_display = ('subject_id', 'name', 'pd_name', 'class_room')


@admin.register(Sugang_Student)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name')
