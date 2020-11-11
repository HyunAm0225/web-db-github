from django.db import models
from django.urls import reverse
from sugang.fields import ThumbnailImageField
# Create your models here.


# 수강 과목
class Subject(models.Model):
    subject_id = models.CharField('학수번호', max_length=15, blank=True)  # 헉수 번호
    name = models.CharField('과목이름', max_length=30, blank=True)
    point = models.IntegerField('학점', blank=True)
    max_student = models.CharField('정원', max_length=15, blank=True)
    class_time = models.CharField('강의시간', max_length=30, blank=True)
    pd_name = models.CharField('교수', max_length=15, blank=True)
    class_room = models.CharField('강의실', max_length=15, blank=True)
    owner = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("sugang:subject_detail", args=(self.id,))

# 수강 학생


class Sugang_Student(models.Model):
    student_id = models.CharField('학번', max_length=15, blank=True)  # 헉수 번호
    name = models.CharField('이름', max_length=30, blank=True)
    image = ThumbnailImageField('IMAGE', upload_to='sugang/%Y/%m')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    owner = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("sugang:student_detail", args=(self.id,))
