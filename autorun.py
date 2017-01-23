

from main import startMain
from menu import loading_bar


try :
	import time 
	while True :
		Time = time.strftime("%H:%M:%S")
		print '\nAt time : ', Time
		startMain(True)
		print 'delay of 60 seconds'
		loading_bar(60)
except KeyboardInterrupt :
	exit()
