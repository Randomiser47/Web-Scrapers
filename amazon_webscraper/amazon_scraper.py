###################### IMPORTS ######################
import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv
########################## loading dotenv #############
load_dotenv()
###################### CONSTS #######################
MY_EMAIL = os.environ.get('EMAIL_ADDRESS')
MY_PASSWORD = os.environ.get('EMAIL_PASSWORD')
SMTP_ADDR = os.environ.get("SMTP_ADDRESS")
######################## SCRAPING ########################
response = requests.get("https://appbrewery.github.io/instant_pot/")

html = (response.text)
soup = BeautifulSoup(html,'html.parser')
span = (soup.find_all(name ='span',class_='a-price aok-align-center reinventPricePriceToPayMargin priceToPay'))
for spans in span:
    price = spans.find("span",class_='a-price-whole')
    dec_price = spans.find("span",class_='a-price-fraction')
######################### Printing Price ###########################
full_price = float((f"{price.text}{dec_price.text}"))
########################## SMTP ###################################
if full_price <= 99.99:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password = MY_PASSWORD)
        connection.sendmail(from_addr =MY_EMAIL, to_addrs= MY_EMAIL,msg=f"The price of the pot has fallen down to {full_price}, BUY NOW!!!!!")
else:
    print(f"Price is still high at {full_price}, not sending email.")

