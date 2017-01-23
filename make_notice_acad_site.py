import requests
from bs4 import BeautifulSoup
from time import time
from Data import data
import pickle 

#url = "http://www.dtu.ac.in/Web/Archive/archive-latest-news.php"
url = "http://dtu.ac.in/Web/Academics/notice.php"
append_url = "http://dtu.ac.in/Web/Academics"
f = 'notice_acad_earlier_file.pkl'




def create_notice_acad_earlier_file () :
	r = requests.get(url)
	soup = BeautifulSoup(r.content , "html.parser")
	soup.encode("latin-1")

	finals = soup.find("table").find_all("tr")

	with open(f , 'wb') as out :

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
				send_link.append( append_url + str(th[3].find("a").get("href").replace("./",'')))
			except :
				pass

			send_refer =  str(send_refer).replace("[u'",'').replace("']" , '').replace('[u"','').replace('"]','')
		 	send_refer_final = send_refer.replace('\\xa0','')
		 	send_link_final = str(send_link).replace("['",'').replace("']" , '')
			data_obtained = data(send_refer_final , send_link_final , send_date)
			
			if (send_refer and send_link and send_date) :
				pickle.dump (data_obtained, out , pickle.HIGHEST_PROTOCOL)



if __name__ == "__main__" :

	create_notice_acad_earlier_file()
