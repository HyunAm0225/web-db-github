from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# 필요한 모델
# 학번, 이름, 학과, 전화번호, 이메일, 생년월일


class Student(models.Model):
    student_id = models.IntegerField(verbose_name="학번", null=True)
    name = models.CharField('이름', max_length=100, blank=False)
    department = models.CharField('학과', max_length=50, blank=True)
    tel = models.CharField('전화번호', max_length=50, blank=False)
    email = models.EmailField('이메일', max_length=50, blank=True)
    birth_dt = models.DateTimeField('생일', auto_now=False)
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('student_id', 'name',)
