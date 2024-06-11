from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter

class myApp(App):
    def build(self):
        s = Scatter()
        fl = FloatLayout(size=(1000, 400))
        s.add_widget(fl)

        self.text_input = TextInput(size_hint=(0.5, 0.1), pos_hint={'x': 0.25, 'y': 1.5})
        fl.add_widget(self.text_input)

        self.label = Label(size_hint=(0.5, 0.1), pos_hint={'x': 0.25, 'y': 1.6})
        fl.add_widget(self.label)

        self.colors = [
            {"code": "#ff0000", "name": "красный", "color": [1, 0, 0, 1]},
            {"code": "#ff8800", "name": "оранжевый", "color": [1, 0.529, 0, 1]},
            {"code": "#ffff00", "name": "желтый", "color": [1, 1, 0, 1]},
            {"code": "#00ff00", "name": "зеленый", "color": [0, 1, 0, 1]},
            {"code": "#00ffff", "name": "голубой", "color": [0, 1, 1, 1]},
            {"code": "#0000ff", "name": "синий", "color": [0, 0, 1, 1]},
            {"code": "#ff00ff", "name": "фиолетовый", "color": [1, 0, 1, 1]}
        ]

        y = 500
        for color in self.colors:
            button = Button(
                on_press=self.btn_press,
                background_color=color["color"],
                background_normal='',
                size_hint=(0.1, 0.1),
                pos_hint={'x': 0.45, 'y': y / 400}
            )
            fl.add_widget(button)
            y -= 40

        return s

    def btn_press(self, instance):
        for color in self.colors:    # обращение к списку colors с помощью self.colors
            if instance.background_color == color["color"]:
                self.text_input.text = color["code"]
                self.label.text = color["name"]

if __name__ == "__main__":
    myApp().run()
