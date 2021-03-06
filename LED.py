import RPi.GPIO as GPIO
import time

class LED(object):
	LED_PIN = 7
	def blink(self):
		io = LED.LED_PIN
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(io, GPIO.OUT)
		GPIO.output(io, 1)
		time.sleep(1)
		GPIO.output(io, 0)
		time.sleep(1)
		GPIO.cleanup()
	def fast(self):
		io = LED.LED_PIN
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(io, GPIO.OUT)
		GPIO.output(io, 1)
		time.sleep(0.2)
		GPIO.output(io, 0)
		time.sleep(0.2)
		GPIO.output(io, 1)
		time.sleep(0.2)
		GPIO.output(io, 0)
		time.sleep(0.2)
		GPIO.output(io, 1)
		time.sleep(0.2)
		GPIO.output(io, 0)
		GPIO.cleanup()
