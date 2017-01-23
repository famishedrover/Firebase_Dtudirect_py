from firebase import firebase

#url = 'https://tests-4f384.firebaseio.com/'
url = 'https://dtudirect-879f8.firebaseio.com/'

firebase = firebase.FirebaseApplication(url,None)

#results = firebase.get('syllabus',None)

#print results

from generate_string import key_name

keyname = key_name()

destination = '/notice/' + keyname

date = raw_input('>Date : ')
link = raw_input('>Link : ')
refer = raw_input('>Refer : ')

try :
	result = firebase.put(destination, 'date' , date  )
	result = firebase.put(destination, 'link' , link  )
	result = firebase.put(destination, 'refer', refer )
	print 'Finished.'
except :
	print 'ERROR'
	key_name_rollback(keyname)

# for key in results:
# 	print key , '\t corresponds to ' , results[key] , '\n'

#second way
# with open('workfile.txt','w') as f:
# 	for key , values in results.iteritems() :
# 		print key , ' \t ' , values
# 		f.write(str(key) + '\t' + str(values))
# 		f.write('\n\n')