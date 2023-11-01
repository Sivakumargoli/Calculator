import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
class Calculator(App):
    def build(self):
        self.icon = "calcu.png"
        self.operators = ["+","-","*","/"]
        self.last_was_operator = None
        self.last_button = None
        main_layout = BoxLayout(orientation = "vertical")
        self.sol = TextInput(background_color = "black",foreground_color = "white",font_size=40)
        main_layout.add_widget(self.sol)
        buttons = [
            ["7","8","9","+"],
            ["4","5","6","-"],
            ["1","2","3","*"],
            ["0",".","c","/"],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text = label,font_size=30,background_color="grey",
                    pos_hint={"center_x":0.5,"center_y":0.5}
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        equal_button = Button(
            text = "=",font_size=30,background_color="grey",
                    pos_hint={"center_x":0.5,"center_y":0.5})
        equal_button.bind(on_press=self.on_sol)
        main_layout.add_widget(equal_button)
        return main_layout
    def on_button_press(self,instance):
        current = self.sol.text
        button_text = instance.text
        if button_text=='c':
            self.sol.text = ""
        else:
            if current and (
                self.last_was_operator and button_text in self.operators
            ):
                return
            elif current == "" and button_text in self.operators:
                return
            else:
                new_text = current+button_text
                self.sol.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators
    def on_sol(self,instance):
        text = self.sol.text
        if text:
            solution = str(eval(self.sol.text))
            self.sol.text = solution
Calculator().run()