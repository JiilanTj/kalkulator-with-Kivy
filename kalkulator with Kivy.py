from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorApp(App):

    def build(self):
        self.title = 'Kalkulator'
        self.grid = GridLayout(cols=4)
        self.last_was_operator = None
        self.result = TextInput(font_size=32, readonly=True, halign='right', multiline=False)
        self.grid.add_widget(self.result)
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        for button in buttons:
            button_instance = Button(text=button, pos_hint={'center_x': 0.5, 'center_y': 0.5})
            button_instance.bind(on_press=self.on_button_press)
            self.grid.add_widget(button_instance)
        equals_button = Button(text="=")
        equals_button.bind(on_press=self.on_solution)
        self.grid.add_widget(equals_button)
        clear_button = Button(text="C")
        clear_button.bind(on_press=self.on_clear)
        self.grid.add_widget(clear_button)
        return self.grid

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if button_text == 'C':
            self.result.text = ''
        else:
            new_text = current + button_text
            self.result.text = new_text

    def on_clear(self, instance):
        self.result.text = ''

    def on_solution(self, instance):
        text = self.result.text
        try:
            answer = str(eval(self.result.text))
            self.result.text = answer
        except Exception:
            self.result.text = 'Error'


if __name__ == '__main__':
    app = CalculatorApp()
    app.run()
