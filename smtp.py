# Tyrus Malmstrom
# May 16th,2016
# Rasberry Pi Project

import sys
import smtplib #The smtplib module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.
# Import the email modules we'll need
import time
from datetime import datetime
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# method that will allow the user to enter in details on the command line:
def info(prompt):
    return raw_input(prompt).strip()

fromAddr = info("From: ")
toAddr   = info("To: ").split()

print "Now enter your message that you want to send to the person:"

# Add the From: and To: headers at the start!
current_msg = ("From: %s\r\nTo: %s\r\n\r\n" % (fromAddr, ", ".join(toAddr))) # string formatting.

while True:
    try:
        line = raw_input()
    except EOFError:
        break
    if not line:
        break
    current_msg = current_msg + line

print "The length of your message is: ",len(current_msg),

#now using the smptlib moduel to acutally send the email:
smtpObj = smtplib.SMTP('localhost')
smtpObj.set_debuglevel(1)
smtpObj.sendmail(fromaddr, toaddrs, msg)
smtpObj.quit()

