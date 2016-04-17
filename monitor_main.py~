import LED, Climate_sensor, Body_sensor

class Monitor_main(object):
	def __init__(self):
		self.LED = LED.LED()
		self.Climate_sensor = Climate_sensor.Climate_sensor()
		self.Body_sensor = Body_sensor.Body_sensor()
		
	def start(self):
		self.LED.blink()
		self.LED.fast()
		
		
if __name__ == "__main__":
	obj_monitor = Monitor_main()
	obj_monitor.start()
