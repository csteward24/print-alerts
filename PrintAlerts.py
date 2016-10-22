from bs4 import BeautifulSoup #for the parser
import re #for finding texr
import smtplib #for emails

#function for sending emails
def send(server, sender, recipient, subject, body):
    message = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (sender, recipient, subject, body)
    server.sendmail(sender, recipient, message)


def login():
    #login to email server
    gmail.ehlo()
    gmail.starttls()
    password=raw_input("Please enter password: ")
    gmail.login("printalerts23", password)

def trayCheck(trayNumber):
    # Find the right codeblock
    tray = soup.find(string=re.compile("Tray " + str(trayNumber)))
    tr = tray.parent.parent.parent
    # Find the empty string
    result = tr.find(string=re.compile("Empty"))
    print result
    # send the email if paper is empty
    if result is None:
        print "Paper is not empty"
    else:
        print "Paper is empty"
        print "sending email"
        send(gmail, "printalerts23", "8565357733@vtext.com", "printer 1", "paper is empty")
        #send(gmail, "printalerts23", "9739609245@tmomail.net", "printer 1", "paper is empty")


gmail = smtplib.SMTP("smtp.gmail.com", 587)
login()
doc = open("hp.html","r") #local files
#doc = urllib.urlopen('http://flourite.co/index.html').read()  #webpages
soup = BeautifulSoup(doc,'html.parser')
trayCheck(1)
trayCheck(2)

