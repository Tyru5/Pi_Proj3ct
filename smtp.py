# Tyrus Malmstrom
# May 16th,2016
# Rasberry Pi Project

import smtplib #The smtplib module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.
# Import the email modules we'll need
import time
from datetime import datetime
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# method that will allow the user to enter in details on the command line:
def info(prompt):
    return raw_input(prompt).strip()

email       = info("Email: ")
recipient   = info("To: ")
passW       =  info("Password: ")
print "Now enter your message that you want to send to the person:"

# Add the From: and To: headers at the start!
current_msg = info("Message: ")

print "The length of your message is: ",len(current_msg)

#now using the smptlib moduel to acutally send the email:
smtpObj = smtplib.SMTP('smtp.gmail.com:587') # using gmail server to send the email.
#testing the connection:
smtpObj.ehlo()
#secure connection:
smtpObj.starttls()
smtpObj.login( email, passW )
smtpObj.set_debuglevel(1)
smtpObj.sendmail( email, recipient, 'Subject: Info.\n' + current_msg )
#disconnecting from smtp server:
smtpObj.quit()

