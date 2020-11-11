from django.contrib import admin

# Register your models here.
from .models import Namecard_TBL
# Register your models here.

@admin.register(Namecard_TBL)
class BookmarkAdmin(admin.ModelAdmin):
    list_display=('name','tel','company','email')
