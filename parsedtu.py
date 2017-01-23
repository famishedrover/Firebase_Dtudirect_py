import requests
from bs4 import BeautifulSoup
from time import time
from Data import data
import pickle 
from make_notice_earlier_file import url as u ,  f as fold
import os

url = u
f_new = 'notice_new.pkl'
f_old = fold



def output_notice () :

	supply_refer = []
	supply_link = []
	supply_date = []

	if not os.path.exists(f_old) :
		create_earlier_file()
		print f_old +' created.'
		return "created"


	from connect_url import open_url
	r = open_url(url)
	soup = BeautifulSoup(r.content , "html.parser")
	soup.encode("latin-1")

	finals = soup.find_all("li")

	with open(f_new , 'wb') as out :
		for final in finals :
			send_refer = []
			send_link = []
			send_link_final =''
			send_refer_final =''
			dates = final.find_all("small")
			links = final.find_all("a" , {"class":"colr"} )

			send_date = ''
			for pdate in dates :
				send_date =  pdate.text.strip().replace('Date:','') 

			for link in links :
				send_refer.append(link.text.strip())
				send_link.append(link.get("href"))


				send_refer_final =  str(send_refer).replace("[u'",'').replace("']" , '')
				send_link_final = str(send_link).replace("[u'",'').replace("']" , '')

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
			print 'ERR'

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








# from print_pkl_file import print_file
# print_file(f)
