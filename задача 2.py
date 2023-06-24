from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical') 
        num1 = TextInput(multiline=False)
        num2 = TextInput(multiline=False)
        layout.add_widget(num1)
        layout.add_widget(num2)
        but = Button(text='сложить')
        but.bind(on_press=lambda instance: setattr(res_lbl, 'text', str(float(num1.text) + float(num2.text))))
        res_lbl = Label()
        layout.add_widget(but)
        layout.add_widget(res_lbl)
        return layout
MainApp().run()