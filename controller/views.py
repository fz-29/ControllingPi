from django.shortcuts import render

import RPi.GPIO as GPIO
# Create your views here.

def switch_on(pin):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,True)
	return True

def switch_off(pin):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,False)
	return True