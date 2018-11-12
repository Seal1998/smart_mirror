from tkinter import *
import requests

from frames.utils import ONE_HOUR_MS


class ExchangeRates(Frame):
    ex_config = {
        'url': 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json',
        'currency': {'USD', 'RUB'}
    }

    def __init__(self, parent):
        # инициализация фрейма с курсами валют
        Frame.__init__(self, parent, bg='black')

        # инициализация лейбла с курсами валют во фрейме
        self.currencyLabel = Label(self, font=('Helvetica', 48), fg="white", bg="black")
        self.currencyLabel.pack()

        # получение и вывод курса валют
        self.update_rates()

    def update_rates(self):
        json_response = requests.get(self.ex_config['url'], ).json()

        self.currencyLabel.config(text=self.extract_currency_rates(json_response))

        self.after(ONE_HOUR_MS, self.update_rates)

    def extract_currency_rates(self, json_data):
        rates_string = ''

        for element in json_data:
            if element['cc'] in self.ex_config['currency']:

                # например      'USD: 27.87 UAH
                #               'RUB: 0.42 UAH
                rates_string += ('{}: {:.2f}{}'.format(element['cc'], element['rate'], ' UAH\n'))

        # убираем лишний перенос строки
        rates_string = rates_string[:-1]

        return rates_string
