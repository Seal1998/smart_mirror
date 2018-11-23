import datetime
from tkinter import *

import requests
from PIL import Image, ImageTk

from .utils import TimeConstant


class Weather(Frame):
    weather_config = {
        'city': 'Kharkiv',
        'APPID': 'dbdaef6ff380721afe343cf0543f9e82',
    }

    # словарь дневных изображений
    weather_day_images = {
        'thunderstorm': 'source/weather_icons/Storm.png',
        'drizzle': 'source/weather_icons/Snow.png',
        'rain': 'source/weather_icons/Rain.png',
        'snow': 'source/weather_icons/Snow.png',
        'atmosphere': 'source/weather_icons/Haze.png',
        'clear': 'source/weather_icons/Sun.png',
        'clouds': 'source/weather_icons/PartlySunny.png',
    }

    # словарь ночных изображений
    weather_night_images = {
        'thunderstorm': 'source/weather_icons/Storm.png',
        'drizzle': 'source/weather_icons/Snow.png',
        'rain': 'source/weather_icons/Rain.png',
        'snow': 'source/weather_icons/Snow.png',
        'atmosphere': 'source/weather_icons/Haze.png',
        'clear': 'source/weather_icons/Moon.png',
        'clouds': 'source/weather_icons/PartlyMoon.png',
    }

    # словарь соответствия идентификаторов погоды соответствующим картинкам
    weather_id = {
        'thunderstorm': {200, 201, 202, 210, 211, 212, 221, 230, 231, 232},
        'drizzle': {300, 301, 302, 310, 311, 312, 313, 314, 321},
        'rain': {500, 501, 502, 503, 504, 511, 520, 521, 522, 531},
        'snow': {600, 601, 602, 611, 612, 615, 616, 620, 621, 622},
        'atmosphere': {701, 711, 721, 731, 741, 751, 761, 762, 771, 781},
        'clear': {800},
        'clouds': {801, 802, 803, 804},
                }

    def __init__(self, parent):
        # инициализация фрейма с погодой
        Frame.__init__(self, parent, bg='black')

        # настраиваем лейблы с погодой
        self.weatherLabel = Label(self, font=('Helvetica', 48), fg="white", bg="black")
        self.weatherImageLabel = Label(self, bg="black")
        self.weatherDescriptionLabel = Label(self, font=('Helvetica', 48), fg="white", bg="black")

        # распологаем лейблы с погодой на экране
        self.weatherImageLabel.pack(side=LEFT)
        self.weatherLabel.pack()
        self.weatherDescriptionLabel.pack()

        # обновляем погоду на лейблах
        self.get_weather()

    def pick_image_name_from_id(self, weather_id):
        hour = int(datetime.datetime.now().strftime('%H'))

        for weather_type in self.weather_id:                  # Перебираем погодные типы из словаря типов
            for w_id in self.weather_id[weather_type]:        # Перебираем идентификаторы (id) из погодного типа
                if w_id == weather_id:                        # Если нашлось совпадение по id, то
                    if hour in range(6, 18):                  # Устанивливаем картику, соответствующую времени суток
                        return self.weather_day_images[weather_type]
                    else:
                        return self.weather_night_images[weather_type]

    def get_weather(self):

        # получаем погоду с api.openweathermap.org
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={
                               'q': self.weather_config['city'],
                               'type': 'like',
                               'units': 'metric',
                               'APPID': self.weather_config['APPID']})
        json_response = res.json()

        # todo:    привести пример
        weather = ' {:+.0f} {}'.format(json_response['list'][0]['main']['temp'], "°C")

        # weather_status = data['list'][0]['weather_icons'][0]['main']

        weather_description = ' {}'.format(json_response['list'][0]['weather'][0]['description'])

        weather_id = json_response['list'][0]['weather'][0]['id']

        self.weatherLabel.config(text=weather)
        self.weatherDescriptionLabel.config(text=weather_description)

        # устанавливаем иконку соотвествующей погоды
        statusImg = Image.open(self.pick_image_name_from_id(weather_id))
        statusImg.thumbnail((100, 100))
        statusImg = ImageTk.PhotoImage(statusImg)

        self.weatherImageLabel.config(image=statusImg)
        self.weatherImageLabel.image = statusImg

        self.weatherImageLabel.after(TimeConstant.ONE_HOUR, self.get_weather)
