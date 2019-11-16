# github.com/RohitKaushal7
import requests
from bs4 import BeautifulSoup

cn = input("enter Contest Number  ")

url = "https://codeforces.com/contest/"+cn
purl="/contest/"+cn+"/problem"

try:
    page= requests.get(url);
    soup = BeautifulSoup(page.text,'html5lib')
    prob = soup.select('a[href*="'+purl+'"]')
    ctst= soup.select('a[href="/contest/'+cn+'"]')
    print("\n"+ctst[0].text)
    for i in range(0,len(prob)-1,2):
        nam = prob[i+1].text
        print("%-1s : %-40s %-30s"%(prob[i].text.strip(),nam.strip(),"\t>>>\thttp://codeforces.com"+prob[i]['href']))

except:
    print("Contest Number May Not Be Right")

