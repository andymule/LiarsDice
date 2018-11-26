# Sample Kivy app demonstrating the working of Box layout
# imports
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

# Boxlayout is the App class

class BoxLayoutDemo(App):
    def build(self):
        superBox = BoxLayout(orientation='vertical')
        horizontalBox = BoxLayout(orientation='horizontal')
        button1 = Button(text="One")
        button2 = Button(text="Two")
        button3 = Button(text="Two")
        button4 = Button(text="Two")
        button5 = Button(text="Two")
        horizontalBox.add_widget(button1)
        horizontalBox.add_widget(button2)
        horizontalBox.add_widget(button3)
        horizontalBox.add_widget(button4)
        horizontalBox.add_widget(button5)
        verticalBox = BoxLayout(orientation='vertical')
        # button3 = Button(text="Three")
        button4 = Button(text="Peek")
        # verticalBox.add_widget(button3)
        verticalBox.add_widget(button4)
        superBox.add_widget(horizontalBox)
        superBox.add_widget(verticalBox)
        return superBox

# Instantiate and run the kivy app
if __name__ == '__main__':
    BoxLayoutDemo().run()
