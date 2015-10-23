from django.contrib import admin
from communicator.models import device
# Register your models here.

class devicesAdmin(admin.ModelAdmin):
	list_display = ("__unicode__","id","devicePin","deviceStatus")
	class Meta :
		model = device

admin.site.register(device,devicesAdmin)