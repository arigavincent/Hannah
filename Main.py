from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel


KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: 10
    spacing: 10

    MDTextField:
        id: input_number
        hint_text: "Enter number"
        input_filter: 'int'

    MDTextField:
        id: input_base
        hint_text: "Enter base (2-16)"
        input_filter: 'int'

    MDRaisedButton:
        text: "Convert"
        on_press: app.convert_number()

    MDLabel:
        id: result_label
        text: "Result will appear here"
        halign: 'center'
'''

class NumberConverterApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def convert_number(self):
        input_number = self.root.ids.input_number.text
        input_base = self.root.ids.input_base.text

        if input_number.isdigit() and input_base.isdigit():
            number = int(input_number)
            base = int(input_base)

            if 2 <= base <= 16:
                result = self.convert_to_base(number, base)
                self.root.ids.result_label.text = f"Converted: {result}"
            else:
                self.root.ids.result_label.text = "Base must be between 2 and 16"
        else:
            self.root.ids.result_label.text = "Invalid input"

    def convert_to_base(self, number, base):
        digits = "0123456789ABCDEF"
        res = ""
        while number > 0:
            res = digits[number % base] + res
            number //= base
        return res if res else "0"

NumberConverterApp().run()
