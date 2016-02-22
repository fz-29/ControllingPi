from communicator.models import device
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
		obj = device.objects.get(id=id)
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
		return JsonResponse({'success':'1','status':str(obj.deviceStatus)})

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
		obj = device.objects.get(id=id)
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

@csrf_exempt
def off(request):
	return JsonResponse({'success':'1'})