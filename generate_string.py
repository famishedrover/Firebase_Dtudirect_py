def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()
def key_name () :
	with open('last_index_name.txt','r') as f :
		x = f.read()
		z = list(x)
		name = list(x)

	import string
	alpha = list(string.ascii_uppercase)


	#ord() gives ascii value  and chr(some_integer) gives char back
	num = len(z)
	for k in range (len(z)) :
		i =  num - k - 1
		if z[i] == alpha[0]:
			z[i] = alpha[25]
			z[i-1] = alpha[ alpha.index(z[i-1]) - 1 ]
			break
		else :
			z[i] = alpha[ alpha.index(z[i]) - 1 ]
			break

	newstr = "".join(z)
	name = "".join(name)

	with open('last_index_name.txt','w') as f :
		deleteContent(f)
		f.write(newstr)

	return name 

def key_name_rollback( content ) :
	with open('last_index_name.txt','w') as f :
		deleteContent(f)
		f.write(content)


if __name__ == '__main__' :
	print 'This is main'

	x  = key_name()

	print x



	
