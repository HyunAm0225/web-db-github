from django.db import models
from django.urls import reverse
from datetime import datetime

from .fields import ThumbnailImageField
# Create your models here.


class PartyName(models.Model):
    name = models.CharField('파티 이름', max_length=20)
    place = models.CharField('파티 장소', max_length=50)
    description = models.TextField('파티 설명')
    openday = models.DateTimeField('개최 날짜', default=datetime.now)
    opendate = models.TimeField('개최 시간')
    owner = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, verbose_name='등록자', blank=True, null=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("party:partyname_detail", args=(self.id,))


class Participant(models.Model):
    party = models.ForeignKey(PartyName, on_delete=models.CASCADE)
    nickname = models.CharField('이름(별명)', max_length=20)
    age = models.IntegerField('나이', blank=True, default=20)
    image = ThumbnailImageField('이미지', upload_to='party/%Y/%m')
    join_dt = models.DateTimeField('참석 날짜', auto_now_add=True)
    owner = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, verbose_name='등록자', blank=True, null=True)

    class Meta:
        ordering = ('nickname',)

    def __str__(self):
        return self.nickname

    def get_absolute_url(self):
        return reverse("party:participant_detail", args=(self.id,))
