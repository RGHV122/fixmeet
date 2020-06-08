from django.contrib import admin
from .models import FreeTime, Appointments,Meetings

# Register your models here.

admin.site.register(FreeTime)
admin.site.register(Appointments)
admin.site.register(Meetings)
