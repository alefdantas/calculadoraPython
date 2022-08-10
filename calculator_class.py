import tkinter as tk
from turtle import clear
from typing import List
class Calculator:
    def __init__(self,root:tk.Tk,label:tk.Label,display:tk.Entry,buttons:List[List[tk.Button]]):
        self.root= root
        self.label = label
        self.display=display
        self.buttons=buttons
    def start(self):
        self.config_buttons()
        self.config_display()
        self.root.mainloop()
    def config_buttons(self):
        buttons = self.buttons
        for  row_values in buttons:
            for button in row_values:
                button_text = button['text']
                if button_text=='C':
                    button.bind('<Button-1>',self.clear)
                if button_text in '0123456789.+-/*()':
                    button.bind('<Button-1>',self.add_text_to_display)
                if button_text == '=':
                    button.bind('<Button-1>',self.calculate)
    def config_display(self):
        ...
    def clear(self,event=None):
        self.display.delete(0,'end')
    def add_text_to_display(self,event=None):
        self.display.insert('end',event.widget['text'])
    def calculate(self,event=None):
        print('')