#! /usr/bin/env python3
from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen

#Define screens
class MainMenu(Screen):
    pass

class CalcWindow(Screen):
    pass

class SavedRecipes(Screen):
    pass

class AvilableFlavors(Screen):
    pass

class SettingsScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")

class EJuiceWorkshop(App):
    def build(self):
        return kv

if __name__ == "__main__":
    EJuiceWorkshop().run()