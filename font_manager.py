"""
  F27SQ - Coursework 4 - Task 1

  @author: Basil
      
  This is GUI program to display a simple interface to show the letter X and
  two buttons to increase or decrease the font size used for the display of X.
 
"""

import tkinter as tk  #Importing tkinter to build the GUI.

class FontSizeApp:  #Defining a class for the window.
    def __init__(self, master):
        self.master = master 
        self.font_size = 18 #Default font size starts from 18.

        #Creating a label with the letter "X".
        self.x_label = tk.Label(self.master, text="X", font=("Arial", self.font_size))
        self.x_label.grid(row=0, column=3, padx=10, pady=10) #Placing it above & between the 2 buttons.

        self.font_size_label = tk.Label(self.master, text=str(self.font_size)) #Displaying the current font size.
        self.font_size_label.grid(row=0, column=4) #

        #Creating an "Increase" button & connecting it to the increase_font_size function.
        self.increase_button = tk.Button(self.master, text="Increase", command=self.increase_font_size, relief="groove")
        self.increase_button.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        #Creating a "Decrease" button & connecting it to the decrease_font_size function.
        self.decrease_button = tk.Button(self.master, text="Decrease", command=self.decrease_font_size, relief="groove")
        self.decrease_button.grid(row=1, column=5, padx=10, pady=10, columnspan=2)

    def increase_font_size(self):
        if self.font_size < 120: #If it's less than 120,
            self.font_size += 1  #Increasing the font size by 1. 
            self.x_label.config(font=("Arial", self.font_size))  #Updating the font size of the "X" label.
            self.font_size_label.config(text=str(self.font_size))  #Updating the displayed font size.

    def decrease_font_size(self):
        if self.font_size > 1:   #If it's greater than 1,
            self.font_size -= 1  #Decrease the font size by 1.
            self.x_label.config(font=("Arial", self.font_size))  #Updating the font size of the "X" label.
            self.font_size_label.config(text=str(self.font_size))  #Updating the displayed font size.

root = tk.Tk()  #Creating the root window for the application
app = FontSizeApp(root)
root.mainloop()  #Starting the loop for the application.