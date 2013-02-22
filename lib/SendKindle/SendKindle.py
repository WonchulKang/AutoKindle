#!/usr/bin/env python
# -*-coding:utf-8-*-


import os, smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders

class SendKindle :
	def __init__ (self, gmail_id, gmail_pass, kindle_id) :
		self.gmailID = gmail_id
		self.gmailPass = gmail_pass
		self.kindleID = kindle_id

	def printInfo (self) :
		print "Gmail ID : %s" % self.gmailID
		print "Gmail Pass : %s" % self.gmailPass
		print "Kindle ID : %s" % self.kindleID

	def send(self, subject, text, attach) :
		msg=MIMEMultipart()
		msg['From']=self.gmailID
		msg['To']=self.kindleID
		msg['Subject']=subject
		msg.attach(MIMEText(text))
		part=MIMEBase('application','octet-stream')
		part.set_payload(open(attach, 'rb').read())
		Encoders.encode_base64(part)
		part.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(attach))

		msg.attach(part)
		mailServer=smtplib.SMTP("smtp.gmail.com",587)
		mailServer.ehlo()
		mailServer.starttls()
		mailServer.ehlo()
		mailServer.login(self.gmailID,self.gmailPass)
		mailServer.sendmail(self.gmailID, self.kindleID, msg.as_string())
		mailServer.close()
