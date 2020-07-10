from django.db import models
from django.db.models import DateTimeField
from registration.models import MyUser
# Create your models here.

class FreeTime(models.Model):
	user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	appointed = models.BooleanField(default = False)


class Appointments(models.Model):
	client = models.ForeignKey(MyUser, on_delete=models.CASCADE)
	details =  models.ForeignKey(FreeTime, on_delete=models.CASCADE)
	added_to_google_calendar = models.BooleanField(default=False)

class Meetings(models.Model):
	provider = models.ForeignKey(MyUser,on_delete=models.CASCADE)
	details = models.ForeignKey(Appointments,on_delete=models.CASCADE)
	added_to_google_calendar = models.BooleanField(default=False)

