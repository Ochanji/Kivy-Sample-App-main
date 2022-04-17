from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyWidget(Widget):
    name = ObjectProperty()
    age = ObjectProperty()

    def btn(self):
        print(f'Name: {self.name.text}')
        print(f'Age: {self.age.text}')
        self.name.text = 'Thanks'
        self.age.text = 'For sharing'


class WidgetApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    WidgetApp().run()
