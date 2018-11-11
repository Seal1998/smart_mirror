import datetime
from tkinter import *


class Clock(Frame):
    def __init__(self, parent, *args, **kwargs):
        # инициализация фрейма с датой и временем
        Frame.__init__(self, parent, bg='black')

        # инициализация лейбла со временем
        self.formattedTime = ''
        self.timeLabel = Label(self, font=('Helvetica', 64), fg="white", bg="black")
        self.timeLabel.pack()

        # инициализация лейбла с датой
        self.formattedDate = ''
        self.dateLabel = Label(self, font=('Helvetica', 48), fg="white", bg="black")
        self.dateLabel.pack()

        self.update()

    def update(self):
        #                                      например, "22:30"
        formattedTime = datetime.datetime.now().strftime("%H:%M")
        #                                      например, "08 November, 2018"
        formattedDate = datetime.datetime.now().strftime("%d %B, %Y")

        # обновляем содержимое лейблов даты и времени
        if formattedTime != self.formattedTime:
            self.formattedTime = formattedTime
            self.timeLabel.config(text=formattedTime)

        if formattedDate != self.formattedDate:
            self.formattedDate = formattedDate
            self.dateLabel.config(text=formattedDate)

        # выполняем апдейт 10 раз/секунду
        self.timeLabel.after(100, self.update)
