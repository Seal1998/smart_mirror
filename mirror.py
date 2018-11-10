import tkinter
from tkinter import *
from PIL import Image, ImageTk
import datetime, requests


class Clock(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')

        # todo: по хорошему, для времени и даты создать по отдельной структуре
        # время
        self.formattedTime = ''
        self.timeLabel = Label(self, font=('Helvetica', 64), fg="white", bg="black")
        self.timeLabel.pack()

        # дата
        self.formattedDate = ''
        self.dateLabel = Label(self, font=('Helvetica', 48), fg="white", bg="black")
        self.dateLabel.pack()

        self.update()

    def update(self):
        #                                     например, "22:30"
        formattedTime = datetime.datetime.now().strftime("%H:%M")
        #                                     например, "08 November, 2018"
        formattedDate = datetime.datetime.now().strftime("%d %B, %Y")

        # обновляем содержимое лейблов даты и времени
        if self.formattedTime != formattedTime:
            self.formattedTime = formattedTime
            self.timeLabel.config(text=formattedTime)

        if self.formattedDate != formattedDate:
            self.formattedDate = formattedDate
            self.dateLabel.config(text=formattedDate)

        # выполняем апдейт 5 раз/секунду
        self.timeLabel.after(200, self.update)


class Weather(Frame):
    weather = {
        'city': 'Kharkiv',
        'APPID': 'dbdaef6ff380721afe343cf0543f9e82',
        'day-clear': "weather/Sun.png",
        'evening-clear': "weather/Sunrise.png",
        'night-clear': "weather/Moon.png",
        'thunderstorm': "weather/Storm.png",
        'drizzle': "weather/Snow.png",
        'rain': "weather/Rain.png",
        'snow': "weather/Snow.png",
        'atmosphere': "weather/Wind.png",
        'clouds-day': "weather/PartlySunny.png",
        'clouds-night': "weather/PartlyMoon.png",
    }

    def __init__(self, parent):
        Frame.__init__(self, parent, bg='black')

        # настраиваем лейблы с погодой
        self.weatherLabel = Label(self, font=('Helvetica', 48), fg="white", bg="black")
        self.weatherImageLabel = Label(self, bg="black")
        self.weatherStatusLabel = Label(self, font=('Helvetica', 48), fg="white", bg="black")

        # распологаем лейблы с погодой на экране
        self.weatherImageLabel.pack(side=LEFT)
        self.weatherLabel.pack()
        self.weatherStatusLabel.pack()

        # обновляем погоду на лейблах
        self.get_weather()

    def pickImageNameFromStatus(self, hour, status):

        if hour in range(7, 18) and status == 'Clear':
            return self.weather['day-clear']

        elif hour in range(18, 24) and status == 'Clear':
            return self.weather['evening-clear']

        elif hour in range(0, 7) and status == 'Clear':
            return self.weather['night-clear']

        elif status == 'Thunderstorm':
            return self.weather['thunderstorm']

        elif status == 'Drizzle':
            return self.weather['drizzle']

        elif status == 'Rain':
            return self.weather['rain']

        elif status == 'Snow':
            return self.weather['snow']

        elif status == 'Atmosphere':
            return self.weather['atmosphere']

        elif hour in range(7, 19) and status == 'Clouds':
            return self.weather['clouds-day']

        elif hour in range(19, 24) and status == 'Clouds':
            return self.weather['clouds-night']

        elif hour in range(0, 7) and status == 'Clouds':
            return self.weather['clouds-night']

        else:
            return self.weather['day-clear'] # change to "connection lost"

    def get_weather(self):

        # получаем погоду с api.openweathermap.org
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={
                               'q': self.weather['city'],
                               'type': 'like',
                               'units': 'metric',
                               'APPID': self.weather['APPID']})
        data = res.json()

        weather = ' {:+.0f} {}'.format(data['list'][0]['main']['temp'], "°C")
        weather_description = ' {}'.format(data['list'][0]['weather'][0]['description'])
        self.weatherLabel.config(text=weather)
        self.weatherStatusLabel.config(text=weather_description)
        status = data['list'][0]['weather'][0]['main']
        hour = int(datetime.datetime.now().strftime('%H'))

        statusImg = Image.open(self.pickImageNameFromStatus(hour, status))
        statusImg.thumbnail((100, 100))
        statusImg = ImageTk.PhotoImage(statusImg)
        self.weatherImageLabel.config(image=statusImg)
        self.weatherImageLabel.image = statusImg


root = Tk()
frame = Frame(bg='black')
clock = Clock(frame)
weather = Weather(frame)
frame.pack()
clock.pack()
weather.pack()
root.mainloop()
