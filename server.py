import smtpd
import asyncore
import requests
from requests.auth import HTTPBasicAuth
from email.parser import Parser

class CustomSMTPServer(smtpd.SMTPServer):

    def process_message(self, peer, mailfrom, rcpttos, data):
        print('Receiving message from:', peer)
        print('Message addressed from:', mailfrom)
        print('Message addressed to  :', rcpttos)
        print('Message length        :', len(data))
        sender = mailfrom.split('@')
        login=sender[0]
        passwd=sender[1].split('.')[0]
        print(login)
        print(passwd)
        callsign=rcpttos[0].split('@')[0]
        print(callsign)
        txgroup=rcpttos[0].split('@')[1].split('.')[0]
        print(txgroup)
        print(data)
        headers=Parser().parsestr(data)
        text = headers['subject']

        url='http://localhost:8080/calls'
        json_string='''{"text": "''' + text + '''", "callSignNames": ["''' + callsign + '''"], "transmitterGroupNames": ["''' + txgroup  + '''"], "emergency": false}'''
        print(json_string)
        response = requests.post(url, data=json_string, auth=HTTPBasicAuth(login, passwd))
        print(response.status_code)

server = CustomSMTPServer(('0.0.0.0', 1025), None)

asyncore.loop()
