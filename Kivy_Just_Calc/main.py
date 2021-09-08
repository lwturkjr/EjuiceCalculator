#! /usr/bin/env python3
from re import MULTILINE
import kivy
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call grid constructor
        super(MyGrid, self).__init__(**kwargs)

        # Set Columns
        self.cols = 1
        self.how_many_flavors = GridLayout()   
        self.how_many_flavors.cols = 3
        self.flavors = GridLayout()
        self.flavors.cols = 4

        #self.add_widget(Label(text="Name: "))
        #self.name = TextInput(multiline=False)
        #self.add_widget(self.name)

        # Add widgets
        self.how_many_flavors.add_widget(Label(text="Number of flavorings: "))
        # Add Input Box
        self.num_flavs = TextInput(multiline=False, input_filter="int")
        self.how_many_flavors.add_widget(self.num_flavs)
        
        # Add button to populate other flavor input boxes
        self.button00 = Button(text="Submit")
        self.button00.bind(on_press=self.populate)
        self.how_many_flavors.add_widget(self.button00)
        
        self.add_widget(self.how_many_flavors)
    
        #self.submit = Button(text="Submit", font_size=40)
        #self.submit.bind(on_press=self.pressed)
        #self.add_widget(self.submit)

    def populate(self, instance):
        number_of_flavorings = self.num_flavs.text
        flavor_dictionary = dict()
        count = 0
        while count < int(number_of_flavorings):
            count += 1
            self.flavors.add_widget(Label(text="Input Flavor Name: "))
            self.flav_name = TextInput(multiline=False)
            self.flavors.add_widget(self.flav_name)
            self.flavors.add_widget(Label(text="Flavor Percentage: "))
            self.flav_perc = TextInput(multiline=False, input_filter="float")
            self.flavors.add_widget(self.flav_perc)
        self.add_widget(self.flavors)
            




class EJuiceCalc(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    EJuiceCalc().run()