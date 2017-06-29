import smtplib
import email.utils
from email.mime.text import MIMEText

# Create the message
msg = MIMEText('This is the body of the message.')
msg['To'] = email.utils.formataddr(('Recipient',
                                    'dh3wr@all.hampager.de'))
msg['From'] = email.utils.formataddr(('dh3wr',
                                      'dh3wr@MYPASSWORD.hampager.de'))
msg['Subject'] = 'Simple tmessage'

server = smtplib.SMTP('dapnet.db0sda.ampr.org', 1025)
server.set_debuglevel(True)  # show communication with the server
try:
    server.sendmail('dh3wr@MYPASSWORD.hampager.de',
                    ['dh3wr@all.hampager.de'],
                    msg.as_string())
finally:
    server.quit()
