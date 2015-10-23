from django.db import models
# Create your models here.
class device(models.Model):
	deviceId = model.autoField(primary_key=True)
	deviceName =  models.CharField(max_length=30)
	devicePin = models.IntegerField()
	deviceStatus =  models.BooleanField()

	def __unicode__(self):
		return self.deviceName

class raspself(model.Model):
	myRaspId = model.IntegerField()
	def __unicode__(self):
		return self.myRaspId
