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

class MainWindow(Screen):
    pass

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

screens = [MainWindow(name="main"), CalcWindow(name="calc"),SavedRecipes(name="saved"), Settings(name="settings")]
for screen in screens:
    wm.add_widget(screen)


class EJuice_Calculator(App):
    def build(self):
        return wm

if __name__ == "__main__":
    EJuice_Calculator().run()