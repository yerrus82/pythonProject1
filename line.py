from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class MainApp(App):
    def build(self):
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        self.solution = TextInput(multiline=False, readonly=False, halign="right", font_size=55)
        main_layout.add_widget(self.solution)

        self.solution2 = TextInput(multiline=False, readonly=False, halign="right", font_size=55)
        main_layout.add_widget(self.solution2)

        equals_button = Button(text="вывести длину", pos_hint={"center_x": 0.5, "center_y": 0.5})
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_solution(self, instance):

        if self.solution.text:
            try:
                kol = int(self.solution.text)

                s = 0
                a = int(self.solution2.text) / 1000
                b = 38 / 100
                for i in range(kol):
                    b = b + a
                    s = s + b
                self.solution.text = str(s)
            except:
                self.solution.text = "Error"


if __name__ == '__main__':
    MainApp().run()
