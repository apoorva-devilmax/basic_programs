import smtplib
from email.mime.text import MIMEText

body = "This is a test email.How are you"

msg = MIMEText(body)
msg['From'] = "springxyzabc@nomail.com"
msg['To'] = "springxyzabc@nomail.com"
msg['Subject'] = "Hello"

server = smtplib.SMTP('smtp.nomail.com',25)

server.starttls()

server.login("springxyzabc@nomail.com","xyzabc")

server.send_message(msg)

print("Mail sent")

server.quit()

