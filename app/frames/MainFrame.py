from tkinter import *
from app.frames.Clock import Clock
from app.frames.ExchangeRates import ExchangeRates
from app.frames.Weather import Weather
from app.manager import manager

class MainFrame():
    def __init__(self):
        self.window = Tk()
        self.window.configure(background="black")
        self.window.config(cursor='none')
        self.window.bind("<z>", self.activate_fullscreen)
        self.window.bind("<x>", self.deactivate_fullscreen)

        self.topFrame = Frame(self.window)
        self.topLeftFrame = Frame(self.topFrame, background="black")
        self.topRightFrame = Frame(self.topFrame, background="black")

        self.bottomFrame = Frame(self.window, background="black")

        self.topFrame.pack(side=TOP, pady=(50, 0))
        self.topLeftFrame.pack(side=LEFT, padx=(0, 120))
        self.topRightFrame.pack(side=RIGHT, anchor=N, padx=(120, 0))
        self.topFrame.config(background="black")

        self.bottomFrame.pack(side=BOTTOM)

        self.status = Label(self.bottomFrame, font=('Helvetica', 48), fg="white", bg="black")
        self.status.pack()

        if manager.has_internet_connection:
            self.setup_frames()
        else:
            manager.set_up_connection()
            if manager.status == 1:
                self.status.config(text='Подключен')
            elif manager.status == 2:
                self.status.config(text='Нет записи в базе данных')

    def setup_frames(self):

        self.clockFrame = Clock(self.topLeftFrame)
        self.clockFrame.pack(pady=(0, 100))

        self.ExchangeRatesFrame = ExchangeRates(self.topLeftFrame)
        self.ExchangeRatesFrame.pack(pady=(0, 100))

        self.weatherFrame = Weather(self.topRightFrame)
        self.weatherFrame.pack()

        self.activate_fullscreen()

    def activate_fullscreen(self, event=None):
        self.window.attributes("-fullscreen", True)

    def deactivate_fullscreen(self, event=None):
        self.window.attributes("-fullscreen", False)

app = MainFrame()
app.window.mainloop()