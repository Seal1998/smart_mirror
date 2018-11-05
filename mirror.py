import tkinter
from tkinter import *
from PIL import Image, ImageTk
import datetime, requests

class Clock(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        #время
        self.time = ''
        self.tLabel = Label(self, font=('Helvetica', 64), fg="white", bg="black")
        self.tLabel.pack()

        #дата
        self.date = ''
        self.dLabel = Label(self, font=('Helvetica', 48), fg="white", bg="black")
        self.dLabel.pack()

        self.update()

    def update(self):
        time = datetime.datetime.now().strftime("%H:%M")
        date = datetime.datetime.now().strftime("%d %B, %Y")
        if self.time != time:
            self.time = time
            self.tLabel.config(text=time)
        if self.date != date:
            self.date = date
            self.dLabel.config(text=date)
        self.tLabel.after(200, self.update)

class Weather(Frame):
    weather = {
        'city': 'Kharkiv',
        'APPID': 'dbdaef6ff380721afe343cf0543f9e82',
        'day-clear': "weather/Sun.png",
        'evening-clear': "weather/Sunrise.png",
        'night-clear': "weather/Moon.png",
        'thundersorm': "weather/Storm.png",
        'drizzle': "weather/Snow.png",
        'rain': "weather/Rain.png",
        'snow': "weather/Snow.png",
        'atmosphere': "weather/Wind.png",
        'clouds-day': "weather/PartlySunny.png",
        'clouds-night': "weather/PartlyMoon.png",
    }
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='black')
        self.wLabel = Label(self, font=('Helvetica', 48), fg="white", bg="black")
        self.wiLabel = Label(self, bg="black")
        self.wsLabel = Label(self, font=('Helvetica', 48), fg="white", bg="black")
        self.wiLabel.pack(side=LEFT)
        self.wLabel.pack()
        self.wsLabel.pack()
        self.get_weather()

    def get_weather(self):

        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                            params={'q': self.weather['city'], 'type': 'like', 'units': 'metric', 'APPID': self.weather['APPID']})
        data = res.json()
        weather = ' {:+.0f} {}'.format(data['list'][0]['main']['temp'], "°C")
        weather_description = ' {}'.format(data['list'][0]['weather'][0]['description'])
        self.wLabel.config(text = weather)
        self.wsLabel.config(text = weather_description)
        status = data['list'][0]['weather'][0]['main']
        hour = int(datetime.datetime.now().strftime('%H'))
        if hour in range(7, 18) and status == 'Clear':
            StatusImg = Image.open(self.weather['day-clear'])
            StatusImg.thumbnail((100, 100))
            StatusImg = ImageTk.PhotoImage(StatusImg)
            self.wiLabel.config(image = StatusImg)
            self.wiLabel.image = StatusImg

        elif hour in range(18, 24) and status == 'Clear':
            StatusImg = Image.open(self.weather['evening-clear'])
            StatusImg.thumbnail((100, 100))
            StatusImg = ImageTk.PhotoImage(StatusImg)
            self.wiLabel.config(image = StatusImg)
            self.wiLabel.image = StatusImg

        elif hour in range(0, 7) and status == 'Clear':
            StatusImg = Image.open(self.weather['night-clear'])
            StatusImg.thumbnail((100, 100))
            StatusImg = ImageTk.PhotoImage(StatusImg)
            self.wiLabel.config(image=StatusImg)
            self.wiLabel.image = StatusImg

        elif status == 'Thunderstorm':
            StatusImg = Image.open(self.weather['thundersorm'])
            StatusImg.thumbnail((100, 100))
            StatusImg = ImageTk.PhotoImage(StatusImg)
            self.wiLabel.config(image=StatusImg)
            self.wiLabel.image = StatusImg

        elif status == 'Drizzle':
            StatusImg = Image.open(self.weather['drizzle'])
            StatusImg.thumbnail((100, 100))
            StatusImg = ImageTk.PhotoImage(StatusImg)
            self.wiLabel.config(image=StatusImg)
            self.wiLabel.image = StatusImg

        elif status == 'Rain':
            StatusImg = Image.open(self.weather['rain'])
            StatusImg.thumbnail((100, 100))
            StatusImg = ImageTk.PhotoImage(StatusImg)
            self.wiLabel.config(image=StatusImg)
            self.wiLabel.image = StatusImg

        elif status == 'Snow':
            StatusImg = Image.open(self.weather['snow'])
            StatusImg.thumbnail((100, 100))
            StatusImg = ImageTk.PhotoImage(StatusImg)
            self.wiLabel.config(image=StatusImg)
            self.wiLabel.image = StatusImg

        elif status == 'Atmosphere':
            StatusImg = Image.open(self.weather['atmosphere'])
            StatusImg.thumbnail((100, 100))
            StatusImg = ImageTk.PhotoImage(StatusImg)
            self.wiLabel.config(image=StatusImg)
            self.wiLabel.image = StatusImg

        elif hour in range(7, 19) and status == 'Clouds':
            StatusImg = Image.open(self.weather['clouds-day'])
            StatusImg.thumbnail((100, 100))
            StatusImg = ImageTk.PhotoImage(StatusImg)
            self.wiLabel.config(image=StatusImg)
            self.wiLabel.image = StatusImg

        elif hour in range(19, 24) and status == 'Clouds':
            StatusImg = Image.open(self.weather['clouds-night'])
            StatusImg.thumbnail((100, 100))
            StatusImg = ImageTk.PhotoImage(StatusImg)
            self.wiLabel.config(image=StatusImg)
            self.wiLabel.image = StatusImg

        elif hour in range(0, 7) and status == 'Clouds':
            StatusImg = Image.open(self.weather['clouds-night'])
            StatusImg.thumbnail((100, 100))
            StatusImg = ImageTk.PhotoImage(StatusImg)
            self.wiLabel.config(image=StatusImg)
            self.wiLabel.image = StatusImg


root = Tk()
frame = Frame(bg='black')
clock = Clock(frame)
weather = Weather(frame)
frame.pack()
clock.pack()
weather.pack()
root.mainloop()