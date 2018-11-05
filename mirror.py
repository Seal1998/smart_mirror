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
        if int(datetime.datetime.now().strftime('%H')) in range(7, 24) and status == 'Clear':
            StatusImg = Image.open(self.weather['day-clear'])
            StatusImg.thumbnail((100, 100))
            StatusImg = ImageTk.PhotoImage(StatusImg)
            self.wiLabel.config(image = StatusImg)
            self.wiLabel.image = StatusImg

        elif int(datetime.datetime.now().strftime('%H')) in range(7, 24) and status == 'Thunderstorm':
            pass
        elif int(datetime.datetime.now().strftime('%H')) in range(7, 24) and status == 'Drizzle':
            pass
        elif int(datetime.datetime.now().strftime('%H')) in range(7, 24) and status == 'Rain':
            pass
        elif int(datetime.datetime.now().strftime('%H')) in range(7, 24) and status == 'Snow':
            pass
        elif int(datetime.datetime.now().strftime('%H')) in range(7, 24) and status == 'Atmosphere':
            pass
        elif int(datetime.datetime.now().strftime('%H')) in range(7, 24) and status == 'Clouds':
            pass


root = Tk()
frame = Frame(bg='black')
clock = Clock(frame)
weather = Weather(frame)
frame.pack()
clock.pack()
weather.pack()
root.mainloop()