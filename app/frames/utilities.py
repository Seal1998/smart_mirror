from kivy import Config
from kivy.graphics.svg import Svg
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter

from kivy import Config
scrH = (int(int(Config.get('graphics', 'width')) / 16 * 9))

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
    #size_hint: (None, None)
    size: self.texture_size
    font_name: "./app/frames/fonts/secrcode.ttf"

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

    HUGE    = scrH / 5
    BIG     = HUGE / 2
    MEDIUM  = BIG / 2
    SMALL   = MEDIUM / 2
    TINY    = SMALL / 2






