
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp


class MortgageCalculatorApp(MDApp):
    def build(self):
        return MDLabel(text='Hello, Mortgage Calculator',halign='center')


MortgageCalculatorApp().run()