from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class BasicWidget(BoxLayout):
    pass


class MonoLabel(Label):
    pass


class Currency(BoxLayout):
    pass


class MonoAdaptiveLabel(MonoLabel):
    pass


class TimeConstant:
    ONE_HOUR = 36*(pow(10, 5))
    DAY = 24 * ONE_HOUR
    WEEK = 7 * DAY
    MONTH = WEEK * 4
