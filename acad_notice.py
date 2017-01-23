import requests
from bs4 import BeautifulSoup
from time import time
from Data import data
import pickle 
from make_notice_acad_site import url as u ,  f as fold , append_url
import os

url = u
f_new = 'notice_acad_new.pkl'
f_old = fold



def output_acad_notice () :

	supply_refer = []
	supply_link = []
	supply_date = []

	if not os.path.exists(f_old) :
		create_notice_acad_earlier_file
		print f_old +' created.'
		return "created"

	r = requests.get(url)
	soup = BeautifulSoup(r.content , "html.parser")
	soup.encode("latin-1")

	finals = soup.find("table").find_all("tr")

	with open(f_new , 'wb') as out :

		count = 0
		for final in finals :
			send_refer = []
			send_link = []
			send_date = ''
			count+= 1

			if count < 5 :
				continue
			th = final.find_all("th")
			try :
				send_refer.append( th[1].text.strip() )
				send_date =  th[2].text.strip() 
				send_link.append( append_url + '/' + str(th[3].find("a").get("href").replace("./",'')))
			except :
				pass

			send_refer =  str(send_refer).replace("[u'",'').replace("']" , '').replace('[u"','').replace('"]','')
		 	send_refer_final = send_refer.replace('\\xa0','')
		 	send_link_final = str(send_link).replace("['",'').replace("']" , '')
			data_obtained = data(send_refer_final , send_link_final , send_date)
			
			if (send_refer and send_link and send_date) :
				pickle.dump (data_obtained, out , pickle.HIGHEST_PROTOCOL)


	latest = False 

	with open(f_new , 'rb' ) as n , open(f_old , 'rb') as o :
		try :
			data_new = pickle.load (n)
			data_old = pickle.load (o)

			if data_new.link == data_old.link  :
				# print data_new 
				print 'Database already to the latest version.'
				latest = True
				return "already"

		except :
			print "ERROR - Can't Load pickle - Handled"

		else :
			pass




	if not latest :
		with open (f_new , 'rb') as n , open (f_old , 'rb') as o  :
			data_old = pickle.load(o)
			while True :
				try : 
					data_new = pickle.load(n) 
					if (data_new.link == data_old.link) :
						break
					else :

						supply_date.append(data_new.date)
						supply_link.append(data_new.link)
						supply_refer.append(data_new.refer)	

				except  :
					break

		os.remove(f_old)
		os.rename(f_new , f_old)

	return (supply_refer , supply_link , supply_date)

