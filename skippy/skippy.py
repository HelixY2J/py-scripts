import smtplib
from bs4 import BeautifulSoup
import requests
import schedule

def rain_rescue():
    location = input("Please enter your location:\n")
    
    mail = input("And your mail :\n")
    
    password = input("Your password too :\n")

    url = ("https://www.google.com/search?q=" + "weather" + location)

    html_content = requests.get(url).content
    

    soup = BeautifulSoup(html_content,'html.parser')

    temp = soup.find('div',attrs={'class' : 'BNeawe iBp4i AP7Wnd'}).text
    weather_lst = soup.find('div',  attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text 

    weather = weather_lst.split('\n')[1]
    

    if (weather =="Sunny" or weather == "Haze" or weather == "Partly Cloudy" ):
        smtpObj = smtplib.SMTP('smtp.gmail.com',587)
        # smptObj represents a connection to an SMTP mail server
        # It has methods for sending mails
        smtpObj.ehlo()
        

        smtpObj.starttls()

        smtpObj.login(mail,password)

        subject = "Friendly Reminder to get your Umbrellas"
        

        body = (f"We are live today and the weather is looking {weather},its freaking {temp} outside !!! Get that Umbrella")
        msg  = (f"Subject:{subject}\n\n{body}\n\nUntill next time....".encode('utf-8'))

        smtpObj.sendmail(mail,mail,msg)

        smtpObj.quit()
        print("Reminder sent")

rain_rescue()





