import customtkinter as ctk
from settings import *

# Vars
class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color= MAIN)
        self.geometry('500x500+720+200')
        self.title('BMI calculator')
        self.resizable(False, False)

        # vars
        self.weight_var = ctk.DoubleVar(value= 60)
        self.height_var = ctk.IntVar(value= 160)
        self.bmistring = ctk.StringVar(value='string')
        self.weightstring = ctk.StringVar(value = f"{self.weight_var.get()}Kg")
        self.heihgtstring = ctk.StringVar(value = f"{self.height_var.get()/100}m")
        self.updatebmi()

        # tracing
        self.weight_var.trace('w', self.updatebmi)
        self.height_var.trace('w', self.updatebmi)


        # layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=2, uniform='a')
        self.rowconfigure(1, weight=1, uniform='a')
        self.rowconfigure(2, weight=1, uniform='a')
        Output(self, self.bmistring)
        WeightInput(self, self.weight_var, self.weightstring)
        HeightInput(self, self.height_var, self.heihgtstring)
        self.mainloop()
    def updatebmi(self, *args):
        self.bmistring.set(round(self.weight_var.get() / (self.height_var.get()/100) ** 2, 2))
        self.weightstring.set(f"{round(self.weight_var.get(), 2)}Kg")
        self.heihgtstring.set(f"{round(self.height_var.get()/100, 2):.2f}m")
class Output(ctk.CTkLabel):
    def __init__(self, parent, output):
        super().__init__(master=parent,font = ctk.CTkFont(FONT, size=100, weight='bold'),text_color=SIDE, textvariable=output)
        self.grid(row = 0, column = 0, sticky="nsew")

class WeightInput(ctk.CTkFrame):
    def __init__(self, parent, weight, weightstring):
        super().__init__(master=parent, fg_color=SIDE)
        self.weight = weight
        self.grid(row = 1, column = 0, sticky = 'nsew', pady = 20, padx = 10)
        font = ctk.CTkFont(FONT, size=20, weight='bold')

        # layout
        self.rowconfigure(0, weight=1, uniform='b')
        self.columnconfigure((0, 4),weight= 2, uniform='b')
        self.columnconfigure((1, 3),weight= 1, uniform='b')
        self.columnconfigure(2,weight= 3, uniform='b')


        # widgets
        bigPlus = ctk.CTkButton(self, font = font,text_color=BLACK,  text = '+', fg_color=BUTTON, hover_color=BUTTON_HOVER, corner_radius = 6, command = lambda: self.weightupdate('+', 1))
        smallPLus = ctk.CTkButton(self, font = font,text_color=BLACK,  text = '+', fg_color=BUTTON, hover_color=BUTTON_HOVER, height = 50,corner_radius = 6, command = lambda: self.weightupdate('+', 0.1))
        bigMinus = ctk.CTkButton(self, font = font,text_color=BLACK,  text = '-', fg_color=BUTTON, hover_color=BUTTON_HOVER, corner_radius = 6, command = lambda: self.weightupdate('-', 1))
        smallMinus = ctk.CTkButton(self, font = font,text_color=BLACK,  text = '-', fg_color=BUTTON, hover_color=BUTTON_HOVER, height = 50, corner_radius = 6, command = lambda: self.weightupdate('-', 0.1))
        outputWeight = ctk.CTkLabel(self, textvariable = weightstring,text_color=BLACK, font=(FONT, 22))



        # button layout
        bigMinus.grid(row = 0, column = 0, sticky = 'nsew', padx = 8, pady = 8)
        smallMinus.grid(row = 0, column = 1, sticky = 'ew', padx = 4, pady = 8)
        outputWeight.grid(row = 0, column = 2, sticky = 'nsew', padx = 8, pady = 8)
        smallPLus.grid(row = 0, column = 3, sticky = 'ew', padx = 4, pady = 8)
        bigPlus.grid(row = 0, column = 4, sticky = 'nsew', padx = 8, pady = 8)
    def weightupdate(self, operatot, amount):
        if operatot == '+':
            if self.weight.get() + amount <= 150  : self.weight.set(self.weight.get() + amount)
        else:
            if self.weight.get() - amount >= 40  : self.weight.set(self.weight.get() - amount)
        
class HeightInput(ctk.CTkFrame):
    def __init__(self, parent, height, heightstring):
        super().__init__(master = parent, fg_color=SIDE)
        self.grid(row = 2, column = 0, padx = 8, pady = 8, sticky = 'nsew')
        bar = ctk.CTkSlider(self, 
                            height= 20, 
                            progress_color=MAIN, 
                            fg_color=BUTTON, 
                            button_color=MAIN, 
                            button_hover_color=BUTTON_HOVER,
                            from_ = 100,
                            to = 250,
                            variable = height
                            )
        label = ctk.CTkLabel(self, textvariable = heightstring, font = (FONT, 20), text_color=BLACK)
        bar.pack(expand = True, fill = 'x', padx = 10,side = 'left')
        label.pack(fill = 'x', padx = 15,side = 'left')
if __name__ == "__main__":
    App()