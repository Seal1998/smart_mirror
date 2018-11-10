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
    weather_config = {
        'city': 'Kharkiv',
        'APPID': 'dbdaef6ff380721afe343cf0543f9e82',
    }
#словарь дневных изображений
    weather_day_images = {
        'thunderstorm': 'weather/Storm.png',
        'drizzle': 'weather/Snow.png',
        'rain': 'weather/Rain.png',
        'snow': 'weather/Snow.png',
        'atmosphere': 'weather/Haze.png',
        'clear': 'weather/Sun.png',
        'clouds': 'weather/PartlySunny.png',
    }
#словарь ночных изображений
    weather_night_images = {
        'thunderstorm': 'weather/Storm.png',
        'drizzle': 'weather/Snow.png',
        'rain': 'weather/Rain.png',
        'snow': 'weather/Snow.png',
        'atmosphere': 'weather/Haze.png',
        'clear': 'weather/Moon.png',
        'clouds': 'weather/PartlyMoon.png',
    }
#словарь типов погоды
    weather_id = {
        'thunderstorm': {200, 201, 202, 210, 211, 212, 221, 230, 231, 232},
        'drizzle': {300, 301, 302, 310, 311, 312, 313, 314, 321},
        'rain': {500, 501, 502, 503, 504, 511, 520, 521, 522, 531},
        'snow': {600, 601, 602, 611, 612, 615, 616, 620, 621, 622},
        'atmosphere': {701, 711, 721, 731, 741, 751, 761, 762, 771, 781},
        'clear': {800, },
        'clouds': {801, 802, 803, 804},
                }

    def __init__(self, parent):
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


    def pickImageNameFromId(self, hour, id):
        for type in self.weather_id: # выбираем погодный тип из словаря типов
            for ID in self.weather_id[type]: # выбираем идентификатор из погодного типа (id описания)
                if id == ID: # если нашлось совпадение по id, то в зависимости от времени возвращаем изобр. в основную функцию
                    if hour in range(6, 18):
                        return self.weather_day_images[type]
                    else:
                        return self.weather_night_images[type]

    def get_weather(self):

        # получаем погоду с api.openweathermap.org
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={
                               'q': self.weather_config['city'],
                               'type': 'like',
                               'units': 'metric',
                               'APPID': self.weather_config['APPID']})
        data = res.json()

        weather = ' {:+.0f} {}'.format(data['list'][0]['main']['temp'], "°C")
        #weather_status = data['list'][0]['weather'][0]['main']
        weather_description = ' {}'.format(data['list'][0]['weather'][0]['description'])
        weather_id = data['list'][0]['weather'][0]['id']
        self.weatherLabel.config(text=weather)
        self.weatherDescriptionLabel.config(text=weather_description)
        hour = int(datetime.datetime.now().strftime('%H'))

        # устанавливаем иконку соотвествующей погоды
        statusImg = Image.open(self.pickImageNameFromId(hour, weather_id))
        statusImg.thumbnail((100, 100))
        statusImg = ImageTk.PhotoImage(statusImg)
        self.weatherImageLabel.config(image=statusImg)
        self.weatherImageLabel.image = statusImg

        self.weatherImageLabel.after(36*(pow(10, 5)), self.get_weather)


root = Tk()
frame = Frame(bg='black')
clock = Clock(frame)
weather = Weather(frame)
frame.pack()
clock.pack()
weather.pack()
root.mainloop()
