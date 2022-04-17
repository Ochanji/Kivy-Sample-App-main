from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class HomeWindow(Screen):
    pass

class DonationWindow(Screen):
    pass

class ActionWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('main.kv')

class Main(App):
    def build(self):
        return kv


if __name__ == '__main__':
    print(dir(kv))
    Main().run()
