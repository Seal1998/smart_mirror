from kivy import Config
from kivy.graphics.svg import Svg
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter

Builder.load_string('''
<BasicWidget>:
    pass: "pass"
    margin: 5
    # DEBUG
    #canvas.before:
    #    Color:
    #        rgba: 1, 1, 1, .1
    #    Rectangle:
    #        #pos: ((self.x + self.margin), (self.y + self.margin))
    #        #size: ((self.width - 2*self.margin), (self.height - 2*self.margin))
    #        pos: self.pos
    #        size: self.size

    # \DEBUG

<MonoLabel@Label>
    font_name: "./app/frames/fonts/digital-7/digital-7 (mono).ttf"
    # font_size: BIG                             # todo proper import

<MonoAdaptiveLabel@MonoLabel>


    # _scale: 1. if self.texture_size[0] < self.width else float(self.width) / self.texture_size[0]
    #margin: 2

	#canvas.before:
    # DEBUG
    #    Color:
    #        rgba: 1, 1, 0, .1
    #    Rectangle:
    #        pos: (self.x + self.margin, self.y + self.margin)
    #        size: (self.width - self.margin*2, self.height - self.margin*2)
    # \DEBUG

	#	PushMatrix
	#	Scale:
	#		origin: self.center
	#		x: self._scale or 1.
	#		y: self._scale or 1.

	#canvas.after:
	#	PopMatrix
''')

class SvgImage(Scatter):
    '''
    def __init__(self, **kwargs):
        self.source = None
        super(SvgImage, self).__init__(**kwargs)
        with self.canvas:
            svg = Svg(self.source)
        self.size = svg.width, svg.height
    '''

    source = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_source(self, instance, value):
        self.canvas.clear()
        with self.canvas:
            svg = Svg(value)

        self.size = svg.width, svg.height


class MonoLabel(Label):
    pass


class Currency(BoxLayout):
    pass


class MonoAdaptiveLabel(MonoLabel):
    pass


class TimeConstant:
    ONE_HOUR = 36 * (pow(10, 5))
    DAY = 24 * ONE_HOUR
    WEEK = 7 * DAY
    MONTH = WEEK * 4


class FontSize:
    HUGE    = int(Config.get('graphics', 'height')) / 10
    BIG     = int(Config.get('graphics', 'height')) / 12
    MEDIUM  = int(Config.get('graphics', 'height')) / 14
    SMALL   = int(Config.get('graphics', 'height')) / 16
    TINY    = int(Config.get('graphics', 'height')) / 18



