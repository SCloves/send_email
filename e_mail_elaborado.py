import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import os

SENHA_EMAIL = os.environ["SENHA_EMAIL"]
  
MY_EMAIL = os.environ["MY_EMAIL"] #YOUR EMAIL
toaddr = ["evandrodalbem@prognoos.com", "cloves.sousa@prognoos.com"] # EMAIL's YOU WANT TO SEND TO
msg = MIMEMultipart()
msg['From'] = MY_EMAIL
msg['To'] = ", ".join(toaddr)
msg['Subject'] = "Testando smtplib"   #"SUBJECT OF THE MAIL"
   
body = "Testando a biblioteca smtplib."    #"YOUR MESSAGE HERE"
msg.attach(MIMEText(body, 'plain'))
    
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(MY_EMAIL, "c1l2o3v4")
text = msg.as_string()
server.sendmail(MY_EMAIL, toaddr, text)
server.quit()

