# github.com/RohitKaushal7
import requests
from bs4 import BeautifulSoup
url = "https://codeforces.com/profile/"
handle = input("Enetr your handle:  ")
url += handle
try:
    page = requests.get(url)
    
    soup = BeautifulSoup(page.text,'html5lib')
    path = soup.find("div",{"class":"user-rank"})
    rat = soup.select("div.info li span")
    
    print(path.text.strip()," >> ",rat[0].text.strip(),rat[1].text.strip())
except:
    print("Error : pls check internet or User-handle")
    