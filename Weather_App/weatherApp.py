from doctest import master
import imghdr
from webbrowser import get
import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image

url = "https://weather.com/weather/today/l/23.72,90.41"


master = Tk()
master.title("Weather Application")
master.config(bg="white")

img = Image.open("C:/Users/User/Desktop/weather_App/weather.png")
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)


def getWeather():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    location = soup.find('h1',class_="CurrentConditions--location--kyTeL").text
    temparature = soup.find('span',class_="CurrentConditions--tempValue--3a50n").text
    weatherPrediction = soup.find('div',class_="CurrentConditions--phraseValue--2Z18W").text
    
    locationLabel.config(text=location)
    temparatureLabel.config(text=temparature)
    weatherPredictionLabel.config(text=weatherPrediction)

    temparatureLabel.after(60000,getWeather)
    master.update()

locationLabel = Label(master,font=("Calibri bold",20),bg="white")
locationLabel.grid(row=0,sticky="N" ,padx=100)
temparatureLabel = Label(master,font=("Calibri bold",20),bg="white")
temparatureLabel.grid(row=1,sticky="W" ,padx=40)
Label(master, image=img,bg="white").grid(row=1,sticky="E")
weatherPredictionLabel= Label(master,font=("Calibri bold",15),bg="white")
weatherPredictionLabel.grid(row=2,sticky="W",padx=40)
getWeather()
master.mainloop()

