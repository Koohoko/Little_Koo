# coding=utf-8
import LED, Climate_sensor, Body_sensor

class Monitor_main(object):
	def __init__(self):
		self.LED = LED.LED()
		self.Climate_sensor = Climate_sensor.Climate_sensor()
		self.Body_sensor = Body_sensor.Body_sensor()
		
	def start(self):
		self.LED.fast()
		try:
			temp, humid = self.Climate_sensor.get_data()
			print 'halo地球人~ 现在的温度是{}摄氏度，相对湿度为{}~'.format(temp, humid)
		except:
			print 'Eweew... please wait.. TT'
		
		
		
if __name__ == "__main__":
	obj_monitor = Monitor_main()
	obj_monitor.start()
