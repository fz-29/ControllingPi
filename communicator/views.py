from communicator.models import device,raspself
from controller.views import switch_on, switch_off

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt                                          
# Create your views here.

@csrf_exempt
def toggle(request):
	response={}
	error=""
	if request.method == 'GET':
		response['success']='0'
		error='GET not allowed'
		response['error']=error
		return JsonResponse(response)
	if request.method == 'POST':
		if not request.POST.get('deviceid', ''):
			error='no device id'
			response['success']='0'
			response['error']=error
			return JsonResponse(response)

		if error=="":
			id=request.POST['deviceid']
	try :
		obj = device.objects.get(deviceId=id)
	except device.DoesNotExist:
		response['success']='0'
		error='wrong device id'
		response['error']=error
		return JsonResponse(response)
	else:
		state = obj.deviceStatus
		pin = obj.devicePin
		if state == False:
		
			#call On from controller
			switch_on(pin)
			obj.deviceStatus = 1	
		else:
		
			#call Off
			switch_off(pin)
			obj.deviceStatus = 0

		obj.save()
		return JsonResponse({'success':'1'})

@csrf_exempt
def on(request):
	response={}
	error=""
	if request.method == 'GET':
		response['success']='0'
		error='GET not allowed'
		response['error']=error
		return JsonResponse(response)
	if request.method == 'POST':
		if not request.POST.get('deviceid', ''):
			error='no device id'
			response['success']='0'
			response['error']=error
			return JsonResponse(response)

		if error=="":
			id=request.POST['deviceid']
	try :
		obj = device.objects.get(deviceId=id)
	except device.DoesNotExist:
		response['success']='0'
		error='wrong device id'
		response['error']=error
		return JsonResponse(response)
	else:
		state = obj.deviceStatus
		pin = obj.devicePin	
		#call On from controller
		switch_on(pin)
		obj.deviceStatus = 1	
		obj.save()
		return JsonResponse({'success':'1'})
@csrf_exempt
def off(request):
	response={}
	error=""
	if request.method == 'GET':
		response['success']='0'
		error='GET not allowed'
		response['error']=error
		return JsonResponse(response)
	if request.method == 'POST':
		if not request.POST.get('deviceid', ''):
			error='no device id'
			response['success']='0'
			response['error']=error
			return JsonResponse(response)

		if error=="":
			id=request.POST['deviceid']
	try :
		obj = device.objects.get(deviceId=id)
	except device.DoesNotExist:
		response['success']='0'
		error='wrong device id'
		response['error']=error
		return JsonResponse(response)
	else:		
		pin = obj.devicePin
		#call Off
		switch_off(pin)
		obj.deviceStatus = 0
		obj.save()
		return JsonResponse({'success':'1'})
@csrf_exempt
def addDevice(request):
	response={}
	error=""
	if request.method == 'GET':
		response['success']='0'
		error='GET not allowed'
		response['error']=error
		return JsonResponse(response)
	if request.method == 'POST':
		if (not request.POST.get('rasp_id', '')) or (not request.POST.get('device_name', '') or (not request.POST.get('device_pin', '')) :
			error='attribute(s) missing'
			response['success']='0'
			response['error']=error
			return JsonResponse(response)
		if raspself.objects.filter(id=1).myRaspId != request.POST['rasp_id']
			error='rasp_id mismatch'
			response['success']='0'
			response['error']=error
			return JsonResponse(response)
		if error=="":
			pin=request.POST['device_pin']
	try :
		oldobj = device.objects.get(devicePin=pin)
	except device.DoesNotExist:	#means pin is empty
		newobj = device.objects.create(deviceName=request.POST['device_name'],devicePin=request.POST['device_pin'], deviceStatus=False)
		newobj.save();
		response['success']='1'
		response['device_id']=id
		return JsonResponse(response)
	else:
		response['success']='0'
		error='pin is not free'
		response['error']=error
		return JsonResponse(response)
@csrf_exempt
def statusAll(request):
	response={}
	error=""
	if request.method == 'GET':
		response['success']='0'
		error='GET not allowed'
		response['error']=error
		return JsonResponse(response)
	if request.method == 'POST':
		if not request.POST.get('rasp_id', '') #check for presence of valid key
			error='no rasp_id'
			response['success']='0'
			response['error']=error
			return JsonResponse(response)
		if raspself.objects.filter(id=1).myRaspId != request.POST['rasp_id']	#check for rasp_id
			error='rasp_id mismatch'
			response['success']='0'
			response['error']=error
			return JsonResponse(response)
	try :
		alldeviceobjs = device.objects.all()
	except device.DoesNotExist:
		response['success']='0'
		error='no devices'
		response['error']=erroralldeviceobjs[i]
		return JsonResponse(response)
	else:	
		response['success'=1]	
		for dev in alldeviceobjs:
			temp=[]
			temp.append(dev.deviceName)
			temp.append(dev.deviceStatus)
			response[dev.deviceId]=temp
		return JsonResponse(response)

		
@csrf_exempt
def statusDevice(request):
response={}
	error=""
	if request.method == 'GET':
		response['success']='0'
		error='GET not allowed'
		response['error']=error
		return JsonResponse(response)
	if request.method == 'POST':
		if (not request.POST.get('rasp_id', '')) or (not request.POST.get('device_name', '') or (not request.POST.get('device_pin', '')) :
			error='attribute(s) missing'
			response['success']='0'
			response['error']=error
			return JsonResponse(response)
		if raspself.objects.filter(id=1).myRaspId != request.POST['rasp_id']
			error='rasp_id mismatch'
			response['success']='0'
			response['error']=error
			return JsonResponse(response)
		if error=="":
			pin=request.POST['device_pin']
	try :
		obj = device.objects.get(id=id)
	except device.DoesNotExist:
		response['success']='0'
		error='wrong device id'
		response['error']=error
		return JsonResponse(response)
	else:		
		pin = obj.devicePin
		#call Off
		switch_off(pin)
		obj.deviceStatus = 0
		obj.save()
		return JsonResponse({'success':'1'})
