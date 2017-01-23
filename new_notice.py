from connect_url import open_url
from bs4 import BeautifulSoup
import pickle
from Data import data

url = "http://dtu.ac.in/Web/Academics/notice.php"
#f = 'earlier_file.pkl'
append_url = "http://dtu.ac.in/Web/Academics"

r = open_url(url)

soup = BeautifulSoup(r.content , "html.parser")

finals = soup.find("table").find_all("tr")


count = 0
for final in finals :
	count+= 1

	if count < 5 :
		continue

	th = final.find_all("th")
	
	
	try :
		print '\n',count 
		print th[1].text.strip()
		print th[2].text.strip()
		print append_url + str(th[3].find("a").get("href").replace("./",''))
	except :
		pass