import tkinter as tk
from tkinter.constants import ANCHOR, CENTER, X
from tkinter import messagebox

class App():

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("To-Do-List")
        self.window.geometry("700x700")

        self.x_but, self.y_but = 0.05, 0.2 
        self.x_ent, self.y_ent = 0.05, 0.2
        self.x_but2 = 0.3
        self.info = {}

        self.start_frame()
        self.grid1()
        self.window.mainloop()
        
    def start_frame(self):
        self.label1 = tk.Label(text="To Do List", font=("", 30))
        self.label1.place(relx=0.5, rely=0.05, anchor=CENTER)

    def grid1(self):
        self.button1 = tk.Button(text="Create", command= self.create_field)
        self.button1.place(relx = self.x_but, rely= self.y_but)

    def create_field(self):

        self.y_but += 0.05
        self.button1.place(relx= self.x_but, rely= self.y_but)

        self.entry1 = tk.Entry()
        self.entry1.place(relx= self.x_ent, rely= self.y_ent)
        x = self.entry1
            

        self.button_check = tk.Button(text="✅", height= 1,command=lambda x=self.entry1: self.check(x))
        self.button_check.place(relx= self.x_but2, rely=self.y_ent)
        

        self.info[self.entry1] = False

        self.y_ent += 0.05

        

    
    def check(self,ent):
        check_var = self.info[ent]

        if not check_var:
            ent.configure(bg="Green")
            self.info[ent] = True

        else:
            ent.configure(bg="White")
            self.info[ent] = False

    
    


app = App()

