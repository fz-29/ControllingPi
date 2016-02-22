from django.db import models
# Create your models here.

class device(models.Model):
	deviceName =  models.CharField(max_length=50)
	#deviceType = 
	devicePin = models.IntegerField()
	deviceStatus =  models.BooleanField()

	def __unicode__(self):
		return self.deviceName