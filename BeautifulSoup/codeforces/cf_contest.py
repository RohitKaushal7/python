# github.com/RohitKaushal7
import requests
import sys
from bs4 import BeautifulSoup

sys.stderr.write("Enter Username : ")
usr = input();
url = "https://codeforces.com/contests/with/"+usr

page = requests.get(url);

try:
	soup = BeautifulSoup(page.text,'html5lib')
	data = soup.select(".datatable")[0]
	tab = data.select("table")[0]
	tr = tab.select("tr")

	th = tr[0].select("th")
	print("{:^4s}| {:^55s} |{:^6s}| {:^4s} | {:^5s} | {:^10s}".format(th[0].text.strip(),th[1].text.strip(),th[2].text.strip(),"Sol","Chg","New"))
	print("-------------------------------------------------------------------------------------------------------------------")

	for i in range(1,len(tr)):
		td = tr[i].select("td")
		print("{:<3s} | {:<55s} | {:^4s} | {:^4s} | {:^5s} | {:^10s} >> {:<20}".format(td[0].text.strip(),td[1].text.strip(),td[2].text.strip(),td[3].text.strip(),td[4].text.strip(),td[5].text.strip()," ".join(td[6].text.split()))) ;

except:
	print("Some Error Occured Check url "+url)