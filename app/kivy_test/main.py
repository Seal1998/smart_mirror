#import requests

#timezone = 2
#json_response = requests.get('http://worldclockapi.com/api/json/utc/now', ).json()
#print(json_response['currentDateTime'])

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout

from kivy_frames.basicWidget import BasicWidget
from kivy_frames.calendar import Calendar
from kivy_frames.clock import Clock
from kivy_frames.events import Events
from kivy_frames.exchangeRates import ExchangeRates
from kivy_frames.mail import Mail
from kivy_frames.news import News
from kivy_frames.weather import Weather

class Root(GridLayout):
    display = ObjectProperty()


class MainApp(App):
    def build(self):
        self.title = 'SmartMirror'
        return Root()


if __name__ == "__main__":
    from os import listdir

    kv_path = './kv/'
    for kv in listdir(kv_path):
        if(kv == "__pycache__"):
            continue
        Builder.load_file(kv_path + kv)

    app = MainApp()
    app.run()