

from generate_string import *

def update_node (parent , url , code = 1 , given_refer = "NA", given_link = "NA", given_date = "NA" , given_desc = "NA" , given_heading = "NA" , given_imageurl = "NA") :
	#code 1 for date / link and refer eg . for notice , results
	#code 0 for link and refer , eg. syllabus
	#code 2 for events ... 
	#... desc / heading / imageurl / link
	from firebase import firebase
	firebase = firebase.FirebaseApplication(url,None)

	#results = firebase.get(parent,None)

	#print results

	

	keyname = key_name()

	destination = '/' + parent +'/' + keyname


	given = False 

	if (given_refer != "NA" or given_link != "NA" or given_date != "NA" or given_desc != "NA" or given_heading != "NA" or given_imageurl != "NA") :
		given = True

	if not given :
		if (code == 1 ) :
			date = raw_input('>Date : ')

		if (code == 1 or code == 0) :
			refer = raw_input('>Refer : ')

		if (code == 2) :
			desc = raw_input('>Desc : ')
			heading = raw_input('>Heading : ')
			imageurl = raw_input('ImageUrl : ')

		link = raw_input('>Link : ')

	else :
		if (code == 1 ) :
			date = given_date

		if (code == 1 or code == 0) :
			refer = given_refer

		if (code == 2) :
			desc = given_desc
			heading = given_heading
			imageurl = given_imageurl

		link = given_link
		





	try :
		if (code == 1) :
			result = firebase.put(destination, 'date' , date  )
		#for code 0 , link and refer are asked .
		if (code == 1 or code == 0) :
			result = firebase.put(destination, 'refer', refer )
		
		if (code == 2) :
			result = firebase.put(destination, 'desc', desc )
			result = firebase.put(destination, 'heading', heading )
			result = firebase.put(destination, 'imageurl', imageurl )

		
		result = firebase.put(destination, 'link' , link  )

		print 'Finished.'
	except :
		print 'ERROR - key_name_rollback - handled'
		key_name_rollback(keyname)




if __name__ == '__main__' :
	update_node ( 'notice' , "https://tests-4f384.firebaseio.com/" , 1 )

# for key in results:
# 	print key , '\t corresponds to ' , results[key] , '\n'

#second way
# with open('workfile.txt','w') as f:
# 	for key , values in results.iteritems() :
# 		print key , ' \t ' , values
# 		f.write(str(key) + '\t' + str(values))
# 		f.write('\n\n')