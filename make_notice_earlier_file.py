import requests
from bs4 import BeautifulSoup
from time import time
from Data import data
import pickle 

url = "http://www.dtu.ac.in/Web/Archive/archive-latest-news.php"
#url = "http://dtu.ac.in/Web/Academics/notice.php"

f = 'notice_earlier_file.pkl'


def create_notice_earlier_file () :
	r = requests.get(url)
	soup = BeautifulSoup(r.content , "html.parser")
	soup.encode("latin-1")

	finals = soup.find_all("li")

	with open(f , 'wb') as out :

		i = 0
		for final in finals :
			i+=1


			send_refer = []
			send_link = []
			send_link_final =''
			send_refer_final =''
			dates = final.find_all("small")
			links = final.find_all("a" , {"class":"colr"} )

			send_date = ''
			for pdate in dates :
				# if ( i < 100):
				# 	print 'Cont'
				# 	continue 
				send_date =  pdate.text.strip().replace('Date:','') 

			for link in links :
				send_refer.append(link.text.strip())
				send_link.append(link.get("href"))

				send_refer_final =  str(send_refer).replace("[u'",'').replace("']" , '')
				send_link_final = str(send_link).replace("[u'",'').replace("']" , '')

			data_obtained = data(send_refer_final , send_link_final , send_date)
			if (send_refer and send_link and send_date) :
				pickle.dump (data_obtained, out , pickle.HIGHEST_PROTOCOL)



if __name__ == "__main__" :
	create_notice_earlier_file()
