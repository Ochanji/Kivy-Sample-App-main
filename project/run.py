from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label

from url_parser import get_characters_count, url_validated


class ParseURL(Screen):
    url = ObjectProperty(None)

    def parse(self):
        url = self.url.text
        if url_validated(url):        
            self.url.text = get_characters_count(url)
            print(f'!!!Word count: {self.url.text}')

        else:        
            invalidURL()


class DonationsWindow(Screen):
    amount = ObjectProperty(0)

    def donateBtn(self):
        amount = self.amount.text
        if amount.isdigit():
            print(f'!!!Donations: {amount}')
            successfulTransaction()
        else:
            invalidAmount()
            print(f'!!!Idiot inserted a non-integer value: {amount}')
            self.amount.text = ''

    def goHome(self):
        sm.current = 'home'



class MainWindow(Screen):
    def goHome(self):
        sm.current = 'home'


class WindowManager(ScreenManager):
    pass


def invalidURL():
    pop = Popup(title='Invalid URL',
                  content=Label(text='Please fill correct URL, which should start with "http" or "https"'),
                  size_hint=(None, None), size=(600, 100))

    pop.open()


def invalidAmount():
    pop = Popup(title='Invalid Amount',
                  content=Label(text='Please enter a valid amount of money (e.g, 10000)'),
                  size_hint=(None, None), size=(600, 100))

    pop.open()


def successfulTransaction():
    pop = Popup(title='Successful Transaction!',
                  content=Label(text='Thanks for sending me money. God bless you!'),
                  size_hint=(None, None), size=(600, 100))

    pop.open()
    
    

kv = Builder.load_file('project.kv')

sm = WindowManager()
screens = (DonationsWindow(name='donations'), ParseURL(name='parse'), MainWindow(name='home'))

for screen in screens:
    sm.add_widget(screen)

sm.current = 'home'


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()