from bs4 import BeautifulSoup
import urllib.request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Scraper
main_page = urllib.request.urlopen("https://www.lapalabraisraelita.cl/")
soup = BeautifulSoup(main_page, "html.parser")

article = soup.find("a", attrs={"class":"article-0-1"})["href"]

article_code = ""
slash = False
for letter in article:
    if slash:
        article_code += letter
    if letter == "/":
        slash = True
    else:
        continue
donwload = "https://www.lapalabraisraelita.cl/backend/views/pdf/ediciones/" + article_code + ".pdf"

# Mail
from_m = "satelerd@gmail.com"   # MAIL DE DONDE SERA ENVIADO
pwd_m = "5Ata5k00"              # CLAVE DEL MAIL
to_m = "satelerd@gmail.com"     # MAIL HACIA DONDE SERA ENVIADO
message = f"""Hola Denisse! Soy NanaBot y te traigo la nueva revista de La Palabra Israelita.

Solo debes apretar el siguiente link: {donwload}"""

s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
s.login(from_m, pwd_m)

msg = MIMEMultipart()       # create a message
msg['From']= from_m
msg['To']= to_m
msg['Subject']= "Nueva edición de la Palabra Israelita"
msg.attach(MIMEText(message, 'plain'))

s.send_message(msg)
print("Enviado")
