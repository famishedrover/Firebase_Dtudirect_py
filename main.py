from Resultmain import output_result , CREATED , ALREADY_EXISTS
#from parsedtu import output_notice
from acad_notice import output_acad_notice


#url = "https://tests-4f384.firebaseio.com/"
url = 'https://dtudirect-879f8.firebaseio.com/'

#-----------------------------------------------------------

menu = "\n --------------------- DTU DIRECT DATABASE ALTER --------------------- \n"
menu += " 1.Notice\t2.Result\t3.Events\t4.Syllabus\t5.Auto"
menu += '\n'



def startMain (auto_t) :

	if not auto_t :
		print menu
		x = raw_input('>Option : ')
		try :
			x = int (x)
		except :
			print 'Invalid Response'
			exit()	
	else :
		x = 5

	from input_data import update_node
	auto = False 
	if (x == 5) :
		auto  = True
		x = 1

	if ( x == 1 ) :
		print '\nSelected Notice'
		#update_node ( 'notice' , url , 1 )
		if not auto :
			update_node ( 'notice' , url , 1 )

		else :
			#print 'Handled Automatically'
			# a = output_notice ()
			a = output_acad_notice()
			if (a[0] == 'c') : #first letter of created 
				print 'No Changes , created notice_acad_earlier_file.pkl'
			elif ( a[0] == 'a') : #first letter of already
				print 'No Changes In the Databse Found'
			else :
				mlen = len (a[0])
				m = reversed (a[0])
				n = reversed (a[1])
				o = reversed (a[2])
				
				print '\nTotal ' + str(mlen) + ' uploads'

				count = 1

				for  r, l , d in zip(m, n , o) :
					print count , ' '
					update_node('notice' , url , 1 , given_refer = r , given_link = l , given_date = d)
					count += 1
			x = 2
		
		
	if ( x ==2 ) :
		print '\nSelected Results'


		if not auto :
			update_node ( 'results' , url , 1 )

		else :
			a = output_result ()
			if (a[0] == 'c') : #first letter of created 
				print 'No Changes , created earlier_file.pkl'
			elif ( a[0] == 'a') : #first letter of already
				print 'No Changes In the Databse Found'
			else :
				mlen = len (a[0])
				m = reversed (a[0])
				n = reversed (a[1])
				o = reversed (a[2])
				
				print '\nTotal ' + str(mlen) + ' uploads'

				count = 1

				for  r, l , d in zip(m, n , o) :
					print count , ' '
					update_node('results' , url , 1 , given_refer = r , given_link = l , given_date = d)
					count += 1
			#x = 3 when scraping of Events or Syllabus is done
		


	if ( x==3 ) :
		print '\nSelected Events'
		update_node ( 'events' , url , 2 )
		


	if ( x==4 ) :
		print '\nSelected Syllabus'
		update_node ( 'syllabus' , url , 0 )
		


	if (x not in [1,2,3,4,5] ) :
		print 'Invalid Response'


if __name__ == "__main__" :
	t = False
	startMain(t)


