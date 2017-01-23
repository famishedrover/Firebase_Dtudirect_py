from connect_url import open_url
from bs4 import BeautifulSoup

url = "http://dtu.ac.in/"
r = open_url(url)



soup = BeautifulSoup(r.content , "html.parser")


finals = soup.find("div" , {"class" : "latest_tab"}).find_all("li")


count = 1
for final in finals :
	dates = final.find_all("small")
	links = final.find_all("a" , {"class":"colr"})
	print '\n\n'
	for date in dates :
		print date.text.strip().replace("Date:" , '')
	for link in links :
		print  'Link Text ' ,link.text
		link_final = link.get("href")
		link_final = str (link.get("href"))

		if "/" not in link_final[1:]:
			pass
		elif "dtu.ac.in" not in link_final :
			print "http://dtu.ac.in" + link_final[1:]
		else :
			print link.get("href")






