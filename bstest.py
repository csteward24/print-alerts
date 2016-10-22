from bs4 import BeautifulSoup
import re
import urllib

doc = open("hp.html","r")
#soup = BeautifulSoup(html_doc, 'html.parser')
#doc = urllib.urlopen('http://flourite.co/index.html').read()
soup = BeautifulSoup(doc,'html.parser')


tray1 = soup.find(string=re.compile("Tray 1"))
tr = tray1.parent.parent.parent

result=tr.find(string=re.compile("Empty"))

print result
if result is None:
    print "Paper is not empty"
else:
    print "Paper is empty"