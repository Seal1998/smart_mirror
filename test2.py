#import requests

#timezone = 2
#json_response = requests.get('http://worldclockapi.com/api/json/utc/now', ).json()
#print(json_response['currentDateTime'])

import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.label import Label

class Main(App):

    def build(self):
        return Label(text='hello, govnokod')

if __name__ == '__main__':
    Main().run()
