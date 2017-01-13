#!/usr/bin/env python
import web
import RPi.GPIO as GPIO
import time
import boto3
import json
import base64
import requests

#Read in app config
try:
	with open('/root/garage_door.json') as json_data:
		config = json.load(json_data)

	auth_key = config['config'][0]['auth_key']
	authorized_clients = config['config'][0]['authorized_clients']
	authorized_users = config['config'][0]['authorized_users']
	button_press_in_seconds = config['config'][0]['button_press_in_seconds']
	doors = config['config'][0]['doors']
	double_door_pin = config['config'][0]['double_door_pin']
	single_door_pin = config['config'][0]['single_door_pin']
	alert_phone_number = config['config'][0]['alert_phone_number']
	security_camera_url = config['config'][0]['security_camera_url']
except:
	print "Error loading conifg file"

urls = (
	'/', 'index',
	'/garage_door', 'garage_door',
	'/.*', 'catch_all'
)

app = web.application(urls, globals())

class index:        
    def GET(self):
        return return405()

    def POST(self):
	return return403()

class catch_all:
    def GET(self):
        return return405()

    def POST(self):
        return return404("URI not found")

class garage_door(object):
    def GET(self):
	return return405()

    def POST(self):
	try:
		data = json.loads(web.data())
	except:
		return return500("Invalid JSON input")
	try:
	        door = data["door"]
		client_key = data["auth_key"]
		is_test = data["is_test"]
		client_ip = web.ctx["ip"]
		user = data["user"]
		get_image = data["get_image"]
		alert_fired = False
	except:
		return return500("Invalid or missing input parameter")

	#Check client authentication
	if client_key.upper() != auth_key.upper():
		return return403() 

	#Check user in list
	if user.lower() not in authorized_users:
		return return403()

	#Check if door paramater is valid
	if door.lower() not in doors:
		return return404()

	#get image from securit camera
	if get_image == "True":
		security_camera_image = get_security_camera_image(security_camera_url)
	else:
		security_camera_image = "Not requested"

        if door.lower() == 'double' and is_test.lower() == "false":
		openDoor(double_door_pin)
		sendSnsAlert("Double")
		alert_fired = True
        if door.lower() == 'single' and is_test.lower() == "false":
		openDoor(single_door_pin)
		sendSnsAlert("Single")
		alert_fired = True
        return return200(door,alert_fired,is_test,client_ip,security_camera_image) 



def return200(door,alert_fired,is_test,client_ip,security_camera_image):
        web.header('Content-Type', 'application/json')
        web.header('Access-Control-Allow-Origin', '*')
        return "{ \"response\": { \"door\": \"%s\", \"alert_fired\": \"%s\", \"is_test\": \"%s\", \"client_ip\": \"%s\", \"security_camera_image\": \"%s\"} }\n"%(door,alert_fired,is_test,client_ip,security_camera_image)

def return403():
	web.ctx.status = '403 Forbidden'
	web.header('Content-Type', 'application/json')
	return "{ \"error\": { \"code\": 403, \"message\": \"Forbidden\" } }\n"

def return404(*reason):
	if not reason:
		reason ="Not specified"
	web.header('Content-Type', 'application/json')
	web.ctx.status = '404 Not Found'
	return "{ \"error\": { \"code\": 404, \"message\": \"Not found\", \"detail\": \"%s\" } }\n"%(reason)

def return405():
        web.header('Content-Type', 'application/json')
	web.ctx.status = '405 Method Not Allowed'
        return "{ \"error\": { \"code\": 405, \"message\": \"Method Not Allowed\" } }\n"

def return500(*reason):
	if not reason:
		reason ="Not specified"
	web.header('Content-Type', 'application/json')
	web.ctx.status = "500 Internal Server Error"
	return "{ \"error\": { \"code\": 500, \"message\": \"Internal Server Error\", \"detail\": \"%s\" } }\n"%(reason)

#This is where we open the door
def openDoor(garage_door):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(garage_door, GPIO.OUT)
	GPIO.output(garage_door, False)
	time.sleep(button_press_in_seconds)
	GPIO.output(garage_door, True)

#Use Amazon SNS to send SMS alert
def sendSnsAlert(garage_door):
    sns = boto3.client('sns')
    sns.publish(PhoneNumber = alert_phone_number, Message = garage_door + " door relay actuated via API.")

def get_security_camera_image(url):
	return base64.b64encode(requests.get(url).content)

if __name__ == "__main__":
    app.run()
