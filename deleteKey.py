
# url = 'https://tests-4f384.firebaseio.com/'
def delete_key ( node , url ) :
	from firebase import firebase
	firebase = firebase.FirebaseApplication(url , None)
	results = firebase.get(node,None)
	key_name = []
	for result in results :
		key_name.append(str(result))
	key_name = sorted(key_name)
	top = key_name[0]
	try :
		firebase.delete(node ,top)
	except :
		print 'ERROR Deleting'

		
if __name__ == '__main__' :
	print 'main'
	delete_key('results','https://tests-4f384.firebaseio.com/')