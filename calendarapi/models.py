from django.db import models
from django.forms import ModelForm
from django.urls import reverse

class Event(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField(blank=True, null=True)
    date = models.DateTimeField()
    uniqueTempKey = models.CharField(max_length=200, default='myNull')

    saleDocLink = models.URLField(blank=True, null=True)
    salePointsCreated = models.NullBooleanField()
    researchDone = models.NullBooleanField()
    internalMeetingCreated = models.NullBooleanField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('calenderapi:add', kwargs={'pk': self.pk})
