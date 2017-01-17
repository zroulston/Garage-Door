# Garage-Door
Raspberry Pi based garage door opener. This project consists of two parts, an API and a mobile web client.

Hardware:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Raspberry Pi P1<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SunFounder 2 Channel DC 5V Relay Module<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Genie Intellicode Gitr-3 Remote<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Foscam FI8910W<br/>

Software:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Raspbian GNU/Linux<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nginx/1.6<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Python 2.7<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Amazon SNS<br/>

<h1>API</h1>
<h2>Required Input</h2>
	"auth_key": Key required to call the API
	"doors": 'single' or 'double'
	"is_test": 'True' or 'False' If false, the relays will not fire and SNS will not send alert
	"user": Must be in garage_door.json
	"get_image": 'True' or 'False' If true, a base64 encoded JPEG retrieved from security camera URL
<h2>Configuration File</h2>
	**See garage_door.json for example**
	"authorized_users": Users that are permitted to call API
	"button_press_in_seconds": How long relays should be engaged
	"doors": Labeling for doors
	"double_door_pin": GPIO pin mapped to double door
	"single_door_pin": GPIO pin mapped to single door
	"alert_phone_number": 12 digit phone number to receive alert from SNS. See doto3 config
	"security_camera_url": URL to provide jpeg output
<h2>Example:</h2>
The API can be called with JSON in a POST.<br/>
<br/>Curl:<br/>
<br/>
`curl -i -H "Accept: application/json" -X POST -d '{"door" : "single", "auth_key" : "xxx123", "is_test" : "True", "user": "user1", "get_image": "True"}' http://127.0.0.1:8080/garage_door`
<br/>
<br/>Web Interface:<br/>
<br/>![Alt text](/web_ui_screenshot.png?raw=true)
