#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from __future__ import unicode_literals

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

# Boxlayout is the App class


class BoxLayoutDemo(App):
    def build(self):
        superBox = BoxLayout(orientation='vertical')

        UIBoxTop = BoxLayout(orientation='vertical')
        buttonRoll = Button(text="Roll")
        buttonRoll.bind(on_press=RollCallback)
        UIBoxTop.add_widget(buttonRoll)
        buttonLost = Button(text="Lost")
        buttonLost.bind(on_press=LostCallback)
        UIBoxTop.add_widget(buttonLost)
        buttonShow = Button(text="Show")
        buttonShow.bind(on_press=ShowCallback)
        UIBoxTop.add_widget(buttonShow)
        superBox.add_widget(UIBoxTop)

        DiceBox = BoxLayout(orientation='horizontal')
        button1 = Button(text="1")
        button1.bind(on_press=ButtonCallback)
        button2 = Button(text="2")
        button2.bind(on_press=ButtonCallback)
        button3 = Button(text="3")
        button3.bind(on_press=ButtonCallback)
        button4 = Button(text="4")
        button4.bind(on_press=ButtonCallback)
        button5 = Button(text="X")
        button5.bind(on_press=ButtonCallback)
        DiceBox.add_widget(button1)
        DiceBox.add_widget(button2)
        DiceBox.add_widget(button3)
        DiceBox.add_widget(button4)
        DiceBox.add_widget(button5)

        verticalBox = BoxLayout(orientation='vertical')
        button4 = Button(text="Peek")
        verticalBox.add_widget(button4)
        superBox.add_widget(DiceBox)
        superBox.add_widget(verticalBox)
        return superBox

# def ButtonCallback(instance, value):
def ButtonCallback(instance):
    print('My callback <%s> state is ' % (instance))
    # instance.background_color

def LostCallback(instance):
    print('My lost <%s> state is ' % (instance))

def RollCallback(instance):
    print('My roll <%s> state is ' % (instance))
    
def ShowCallback(instance):
    print('My show <%s> state is ' % (instance))

# Instantiate and run the kivy app
if __name__ == '__main__':
    BoxLayoutDemo().run()
