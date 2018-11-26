#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from __future__ import unicode_literals

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
import random

class BoxLayoutDemo(App):
    min = 1
    max = 6
    buttonCount = 5
    buttons = []
    DiceBox = BoxLayout()

    def build(self):
        app = App.get_running_app()
        superBox = BoxLayout(orientation='vertical')

        UIBoxTop = BoxLayout(orientation='vertical')
        buttonRoll = Button(text="Roll")
        buttonRoll.bind(on_press=RollCallback)
        UIBoxTop.add_widget(buttonRoll)
        buttonLost = Button(text="Lost")
        buttonLost.bind(on_press=LostCallback)
        UIBoxTop.add_widget(buttonLost)
        superBox.add_widget(UIBoxTop)

        DiceBox = BoxLayout(orientation='horizontal')
        AddButtons(DiceBox, app.buttonCount)

        verticalBox = BoxLayout(orientation='vertical')
        buttonPeek = Button(text="Peek-n-Hide")
        buttonPeek.bind(on_press=PeekCallback, on_release=PeekCallback)
        verticalBox.add_widget(buttonPeek)
        superBox.add_widget(DiceBox)
        superBox.add_widget(verticalBox)
        RollDice()
        return superBox

def RollDice():
    app = App.get_running_app()
    for button in app.buttons:
        button.text = str(random.randint(app.min, app.max))
        button.font_size = 15
        button.background_color = (1,1,1,1)

def AddButtons(dicebox, amount):
    app = App.get_running_app()
    for i in range(0,amount):
        b = Button(text="X")
        b.bind(on_press=ButtonCallback)
        dicebox.add_widget(b)
        app.buttons.append(b)

def ButtonCallback(instance):
    b = Button()    # lets us get autocomplete on buttons in callbacks lololol
    b = instance
    if b.font_size != 80:
        b.font_size = 80
        b.background_color = (0,1,0,1)
    else:
        b.font_size = 15
        b.background_color = (1,1,1,1)

def LostCallback(instance):
    app = App.get_running_app()
    if app.buttonCount > 0:
        app.buttonCount -= 1
        b = app.buttons.pop()
        b.text = ""
        b.disabled = True

def PeekCallback(instance):
    app = App.get_running_app()
    bb = Button()
    bb = instance
    if bb.state == "down":
        for button in app.buttons:
            aa = Button()
            aa = button
            aa.font_size = 15
    else:
        for button in app.buttons:
            aa = Button()
            aa = button
            aa.font_size = 0
            aa.background_color = (1,1,1,1)

def RollCallback(instance):
    RollDice()
    
def ShowCallback(instance):
    b = Button()    # lets us get autocomplete on buttons in callbacks lololol
    b = instance
    b.background_color = (0,1,0,1)

# Instantiate and run the kivy app
if __name__ == '__main__':
    BoxLayoutDemo().run()
