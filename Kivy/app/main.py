#! /usr/bin/env python3
import os
import sys
import json
import pathlib


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.config import Config

Config.set("kivy","window_icon","icon.ico")

path = os.path.join(sys.path[0])

class MainMenu(Screen):
    mainmenu = ObjectProperty(None)
    settings = ObjectProperty(None)
    calculator = ObjectProperty(None)
    savedrecipes = ObjectProperty(None)
    current = ""



class CalcWindow(Screen):
    pass

class SavedRecipes(Screen):
    pass

class Settings(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")
wm = WindowManager()
saved_recipes_dir = f"{path}/saved_recipes/"

screens = [MainMenu(name="main"), CalcWindow(name="calc"),SavedRecipes(name="saved"), Settings(name="settings")]
for screen in screens:
    wm.add_widget(screen)


class EJuiceWorkshop(App):
    def build(self):
        return wm

if __name__ == "__main__":
    EJuiceWorkshop().run()
