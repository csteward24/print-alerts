import smtplib


def send(server, sender, recipient, subject, body):
    message = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (sender, recipient, subject, body)
    server.sendmail(sender, recipient, message)


gmail = smtplib.SMTP("smtp.gmail.com", 587)
gmail.ehlo()
gmail.starttls()
gmail.login("printalerts23", "printer95")
print "sending email"
#Send to Christian's Phone
send(gmail, "printalerts95", "8565357733@vtext.com", "printer 1", "paper is low")
#Send to Sean's Phone
send(gmail, "printalerts95", "9739609245@tmomail.net", "printer 1", "paper is low")
