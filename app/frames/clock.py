from kivy.animation import Animation
from kivy.clock import Clock as Cl
import datetime

from kivy.uix.anchorlayout import AnchorLayout


class Clock(AnchorLayout):
    iteration = 0

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

        Cl.schedule_once(self._post_init)
        Cl.schedule_once(self.update)
        Cl.schedule_interval(self.update, 0.1)



    def _post_init(self, *args, **kwargs):
        anim1 = Animation(duration = .1) + Animation(opacity=0., duration=.4) +\
                Animation(opacity=1., duration=.4) + Animation(duration = .1)
        #anim2 = Animation(duration = .1) + Animation(opacity=0., duration=.4) +\
        #        Animation(opacity=1., duration=.4) + Animation(duration = .1)
        tempSec = datetime.datetime.now().strftime("%S")

        while tempSec == datetime.datetime.now().strftime("%S"):
            import time
            time.sleep(0.05)
            pass    # synchronize animation with seconds update

        Cl.schedule_interval(lambda l: anim1.start(self.ids['clock0column1']), 1)
        #Cl.schedule_interval(lambda l: anim2.start(self.ids['clock0column2']), 1)







    def update(self, *args):
        #                                         например, "22"
        self.ids['clock0hours'].text = datetime.datetime.now().strftime("%H")
        #                                         например, "30"
        self.ids['clock0minutes'].text = datetime.datetime.now().strftime("%M")
        #                                         например, "30"
        #self.ids['clock0seconds'].text = datetime.datetime.now().strftime("%S")


