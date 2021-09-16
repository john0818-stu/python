#import email.message
import os
import smtplib

msg = email.message.EmailMessage()
msg["From"] = "john081808180818@gmail.com"
msg["To"] = "john08180818@yahoo.com.tw"
msg["Subject"] = "Hi 你好"

"""
#print( os.listdir("../Dropbox/python/7"))
infile = open("../Dropbox/python/7/12.html")
xxx = [ x for x in infile ]
infile.close()
"""

msg.add_alternative( "<h>ff</h>" ,subtype="html" )


#gmail
server = smtplib.SMTP_SSL( "smtp.gmail.com" , 465 )
    

server.send_message( msg )
server.close()
