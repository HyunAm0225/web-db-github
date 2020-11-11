from django.forms import inlineformset_factory
from .models import Subject, Sugang_Student

SugangtoInlineFormSet = inlineformset_factory(Subject, Sugang_Student, fields=[
                                              'student_id', 'name', 'image', 'subject'], extra=1)
