import datetime

from kivy_frames.utils import BasicWidget
from kivy.clock import Clock


class Calendar(BasicWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.formattedDate = ''

        Clock.schedule_once(self.update)
        Clock.schedule_interval(self.update, 0.25)


    def update(self, *args):
        #                                      например, "08 Nov"
        formattedDate = datetime.datetime.now().strftime("%d %B, %Y")[0:6]

        # обновляем содержимое лейбла даты
        if formattedDate != self.formattedDate:
            self.formattedDate = formattedDate
            self.ids["date"].text = formattedDate
