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

<h2>Example:</h2>
The API needs to be called with JSON in a POST.<br/>
<br/>Curl example:<br/>
<br/>
`curl -i -H "Accept: application/json" -X POST -d '{"door" : "single", "auth_key" : "xxx123", "is_test" : "True", "user": "user1", "get_image": "True"}' http://127.0.0.1:8080/garage_door`
<br/>
<br/>Web Interface:<br/>
<br/>![Alt text](/web_ui_screenshot.png?raw=true)
