import webbrowser
x=input("Problem No. ### (1-240) : ")
y=int(x)
if(y>0 and y<=240):
	if(y<10):
		x="00"+x;
	elif(y<100):
		x="0"+x
	url="https://www.hackerrank.com/contests/projecteuler/challenges/euler"+x+"/problem"
	print(url);
	webbrowser.open(url);
else:
	print("Only 240 problems available on Hackerrank")
