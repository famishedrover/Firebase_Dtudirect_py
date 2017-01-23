from time import sleep 
import sys 




def loading_bar (t) :
	t = t /100.0
	print t
	num = 100
	print 'Wait: [%s] %d%%' % (' '*(num/2), 0),


	try:
	    colorCode = 43
	    for x in xrange(num+1):
	        if x == num: colorCode = 42
	        print '\rWait: [\033[1;%dm%s\033[1;m%s] %d%%' % (colorCode, "|"*(x/2), " "*(num/2-x/2), x), 
	        sys.stdout.flush()
	        sleep(t) # do actual stuff here instead 
	except KeyboardInterrupt:
	        print '\rWait: [\033[1;41m%s\033[1;m%s] %d%%  ' % ("|"*(x/2), " "*(num/2-x/2), x)


if __name__ == "__main__" :
	loading_bar(2)