from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text='Your full name:'))
        self.full_name = TextInput(multiline=False)
        self.inside.add_widget(self.full_name)

        self.inside.add_widget(Label(text='Your bank account number:'))
        self.bank_number = TextInput(multiline=False)
        self.inside.add_widget(self.bank_number)

        self.inside.add_widget(Label(text='Your bank account password:'))
        self.bank_password = TextInput(multiline=False)
        self.inside.add_widget(self.bank_password)

        self.add_widget(self.inside)

        self.submit = Button(text='Submit!', font_size=52)
        self.submit.bind(on_press=self.submit_pressed)
        self.add_widget(self.submit)

    def submit_pressed(self, instance):
        print(f'Full name: {self.full_name.text}')
        print(f'Bank account number: {self.bank_number.text}')
        print(f'Bank account password: {self.bank_password.text}')

        # Clear inputs
        self.full_name.text = ''
        self.bank_number.text = ''
        self.bank_password.text = ''


class GridApp(App):
    def build(self):
        return MyGrid()




if __name__ == '__main__':
    GridApp().run()