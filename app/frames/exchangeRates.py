from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout

from kivy_frames.utils import BasicWidget, Currency
import requests
from utils import TimeConstant


class ExchangeRates(BasicWidget):
    ex_config = {
        'url': 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json',
        'currency': ['USD', 'RUB']
    }

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

        Clock.schedule_once(self._post_init)
        Clock.schedule_once(self.update)
        Clock.schedule_interval(self.update, TimeConstant.ONE_HOUR)

    def _post_init(self, *args):
        for i in range(0, self.ex_config['currency'].__len__()):
            self.ids['currencies'].add_widget(Currency(
                id='currency' + i.__str__(),
                name=self.ex_config['currency'][i]
            ))

    def update(self, *args):

        try:
            for element in requests.get(self.ex_config['url'], ).json():
                if element['cc'] in self.ex_config['currency']:
                    pass
                    #rates_string = ('{}: {:.2f}{}'.format(element['cc'], element['rate'], ' UAH'))

                    for child in self.ids['currencies'].children:
                        if child.name == element['cc']:
                            child.children[1].text = ('{}:'.format(element['cc']))
                            child.children[0].text = ('{:.2f}{}'.format(element['rate'], ' UAH'))
        except:
            for i in range(0, self.ids['currencies'].children.__len__()):
                self.ids['currencies'].children[i].children[1].text = ('{}:'.format(self.ex_config['currency'][i]))
                self.ids['currencies'].children[i].children[0].text = 'no connection'
