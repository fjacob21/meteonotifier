import RPi.GPIO as GPIO
import time

def setpos(pwm,angle):
	val = ((angle/90)+0.5)/20*100
	print "Moving to ",val,angle
	pwm.ChangeDutyCycle(val)
	#pwm.start(val)
	time.sleep(2)
	pwm.ChangeDutyCycle(0)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)
p = GPIO.PWM(7,50)
p.start(0)

try:
	while True:
		setpos(p,40.0)
		time.sleep(5)
		setpos(p,150.0)
		time.sleep(5)
		#setpos(p,180.0)
		#time.sleep(5)
		#p.ChangeDutyCycle(7.5)
		#time.sleep(2)
		#p.ChangeDutyCycle(0)
		#time.sleep(1)
		#p.ChangeDutyCycle(12.5)
		#time.sleep(2)
		#p.ChangeDutyCycle(0)
		#time.sleep(1)
		#p.ChangeDutyCycle(2.5)
		#time.sleep(2)
		#p.ChangeDutyCycle(0)
		#time.sleep(1)

except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()

