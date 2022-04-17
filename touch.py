from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import Rectangle, Color, Line


class Touch(Widget):
    btn = ObjectProperty()

    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        with self.canvas:
            Color(255, 255, 255, 1, mode='rgba')
            Line(points=(20, 30, 40, 50, 100, 100, 500, 700))

            Color(0, 250, 0, 0.3, mode='rgba')
            self.rect = Rectangle(pos=(190, 300), size=(150, 150))


    def on_touch_down(self, touch):
        self.rect.pos = touch.pos

        print('Mouse down', touch)

    def on_touch_up(self, touch):
        print('Mouse up', touch)

    def on_touch_move(self, touch):
        self.rect.pos = touch.pos
        print('Mouse move', touch)



class Parser(App):
    def build(self):
        return Touch()


if __name__ == '__main__':
    Parser().run()
