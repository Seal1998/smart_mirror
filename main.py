from tkinter import *
from frames.Clock import Clock
from frames.ExchangeRates import ExchangeRates
from frames.Weather import Weather

root = Tk()
frame = Frame(bg='black')
clock = Clock(frame)
weather = Weather(frame)
currency = ExchangeRates(frame)
frame.pack()
clock.pack()
weather.pack()
currency.pack()
root.mainloop()
