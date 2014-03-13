import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = 'n00bsaiboth@gmail.com'
toaddr = 'jussi.jokinen@students.turkuamk.fi'
text = 'this is a test message sent from python'
username = 'n00bsaiboth'
password = 'g00gl3-synt1984'
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'test message from python'
msg.attach(MIMEText(text))

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.sendmail(fromaddr, toaddr, msg.as_string())
server.quit()

print('success')