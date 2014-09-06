import urllib2
import urllib
from xml.dom import minidom
import RPi.GPIO as GPIO
import time

def setuppwm(pin,freq):
	GPIO.setmode(GPIO.BOARD)

	GPIO.setup(pin,GPIO.OUT)
	p = GPIO.PWM(pin,freq)
	p.start(0)
	return p

def cleanpwm(pwm):
	pwm.stop()
	GPIO.cleanup()

def setpos(pwm,angle):
	val = ((angle/90)+0.5)/20*100
	print "Moving to ",val,angle
	pwm.ChangeDutyCycle(val)
	#pwm.start(val)
	time.sleep(2)
	pwm.ChangeDutyCycle(0)

def issunny():
	url = "http://weather.yahooapis.com/forecastrss?w=3534"
	dom = minidom.parse(urllib.urlopen(url))
	cond = dom.getElementsByTagName('yweather:condition')[0]
	code = int(cond.attributes['code'].value)
	if ((code >= 19 and code <=34) or code == 36 or code == 44):
		return True
	else:
		return False

def setsunny(pwm):
	setpos(pwm,40.0)

def setrainy(pwm):
	setpos(pwm,150.0)

def setinitial(pwm):
	setpos(pwm,100.0)

def setmeteo(sunny,pwm):
	if (sunny):
		setsunny(pwm)
	else:
		setrainy(pwm)

if __name__ == "__main__":
	try:
		pwm = setuppwm(7,50)
		setinitial(pwm)

		sunny = issunny()
		oldsunny = not sunny
		while True:
			if (sunny != oldsunny):
				setmeteo(sunny,pwm)

			time.sleep(900)
			oldsunny = sunny
			sunny = issunny()			

	except KeyboardInterrupt:
		cleanpwm(pwm)
	except:
    		print "Unexpected error:", sys.exc_info()[0]
		cleanpwm(pwm)
