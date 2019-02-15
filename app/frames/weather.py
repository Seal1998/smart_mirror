import datetime

import requests
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty, ReferenceListProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

from .utilities import TimeConstant, MonoAdaptiveLabel

Builder.load_string(
'''
<Weather>:
    orientation: "vertical"

    BoxLayout:
        #size_hint: (1, None)
        orientation: "horizontal"

        BoxLayout:
            id: weatherImage
            #:import SvgImage app.frames.utilities.SvgImage
            SvgImage:
                size_hint: (1, .9)
                id: 'image'
                source: ''

        MonoAdaptiveLabel:
            size_hint: (1, 1)
            id: weatherTemperature
            font_size: self.height/2
            text: '+666°C'

    MonoAdaptiveLabel:

        size_hint: (1, 0.5)
        id: weatherStatus
        text: 'debug'
'''
)

class Weather(BoxLayout):

    weather_config = {
        'city': 'Kharkiv',
        'APPID': 'dbdaef6ff380721afe343cf0543f9e82',
    }

    # словарь дневных изображений
    weather_day_images = {
        'thunderstorm': 'source/weather_icons/Storm.svg',
        'drizzle': 'source/weather_icons/Snow.svg',
        'rain': 'source/weather_icons/Rain.svg',
        'snow': 'source/weather_icons/Snow.svg',
        'atmosphere': 'source/weather_icons/Haze.svg',
        'clear': 'source/weather_icons/Sun.svg',
        'clouds': 'source/weather_icons/PartlySunny.svg',
    }

    # словарь ночных изображений
    weather_night_images = {
        'thunderstorm': 'source/weather_icons/Storm.svg',
        'drizzle': 'source/weather_icons/Snow.svg',
        'rain': 'source/weather_icons/Rain.svg',
        'snow': 'source/weather_icons/Snow.svg',
        'atmosphere': 'source/weather_icons/Haze.svg',
        'clear': 'source/weather_icons/Moon.svg',
        'clouds': 'source/weather_icons/PartlyMoon.svg',
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

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self._post_init)

    def _post_init(self, *args):
        '''
        image = Image(
                                size_hint = (1, .9),
                                id        = 'image',
                                source    = '')
        temperature = MonoAdaptiveLabel(
                                size_hint = (1, 1),
                                id        = 'weatherTemperature',
                                font_size = self.height/2,
                                text      = '+666°C')
        statusLabel = MonoAdaptiveLabel(
                                size_hint = (1, 0.5),
                                id        = 'weatherStatus',
                                text      = 'debug')


        imageBox = BoxLayout()
        imageBox.add_widget(image)

        iconAndTemp = BoxLayout(
                                orientation = "horizontal")

        iconAndTemp.add_widget(imageBox)
        iconAndTemp.add_widget(temperature)

        self.orientation = "vertical"
        self.add_widget(iconAndTemp)
        self.add_widget(statusLabel)
        '''

        '''
        self.ids.weatherImage.add_widget(Image(
                                size_hint = (1, .9),
                                id        = 'image',
                                source    = ''))
        '''

        # todo добавить динамический выбор виджета для иконки в зависимости от формата изображения


        # обновляем погоду на лейблах
        Clock.schedule_once(self.update)
        Clock.schedule_interval(self.update, TimeConstant.ONE_HOUR)

    def pick_image_name_from_id(self, hour, weather_id):
        for weather_type in self.weather_id:                  # Перебираем погодные типы из словаря типов
            for w_id in self.weather_id[weather_type]:        # Перебираем идентификаторы (id) из погодного типа
                if w_id == weather_id:                        # Если нашлось совпадение по id, то
                    if hour in range(6, 18):                  # Устанивливаем картику, соответствующую времени суток
                        return self.weather_day_images[weather_type]
                    else:
                        return self.weather_night_images[weather_type]
        # return                                              # todo иначе возвращаем картинку ошибки

    def update(self, *args):
        # получаем погоду с api.openweathermap.org
        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/find",
                               params={
                                   'q': self.weather_config['city'],
                                   'type': 'like',
                                   'units': 'metric',
                                   'APPID': self.weather_config['APPID']})
        except:
            self.ids['weatherImage'].source = self.weather_day_images['clear']
            self.ids['weatherTemperature'].text = 'No connection'
            self.ids['weatherStatus'].text = 'No connection'

            return

        json_response = res.json()

        # пример  '+3°C'
        weather = '{:+.0f}{}'.format(json_response['list'][0]['main']['temp'], "°C")

        weather_description = ' {}'.format(json_response['list'][0]['weather'][0]['description'])

        weather_id = json_response['list'][0]['weather'][0]['id']

        hour = int(datetime.datetime.now().strftime('%H'))

        #self.ids['image'].source = self.pick_image_name_from_id(hour, weather_id)
        self.ids['weatherTemperature'].text = weather
        self.ids['weatherStatus'].text = weather_description

