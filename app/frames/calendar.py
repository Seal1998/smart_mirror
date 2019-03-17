import datetime
import calendar


from kivy.clock import Clock
from kivy.uix.anchorlayout import AnchorLayout


class Calendar(AnchorLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.formattedDate = ''
        self.weekday = ''

        Clock.schedule_once(self.update)
        Clock.schedule_interval(self.update, 0.25)

    def update(self, *args):
        #                                      например, "08 Nov"
        formattedDate = datetime.datetime.now().strftime("%d %B, %Y")[0:6]
        weekday = calendar.day_name[datetime.date.today().weekday()]

        # обновляем содержимое лейбла даты
        if formattedDate != self.formattedDate:
            self.formattedDate = formattedDate
            self.ids["date"].text = formattedDate

        # обновляем содержимое лейбла дня недели
        if weekday != self.weekday:
            self.weekday = weekday
            self.ids["weekday"].text = weekday




