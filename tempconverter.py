# Taylor Abbott
from functools import partial
import tkinter as tk


class Example(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        f2 = GradientFrame(self, "green", "blue", borderwidth=1, relief="sunken")
        f2.pack(side="bottom", fill="both", expand=True)


class GradientFrame(tk.Canvas):

    def __init__(self, parent, color1, color2, **kwargs):
        tk.Canvas.__init__(self, parent, **kwargs)

        self._color1 = color1
        self._color2 = color2
        self.bind("<Configure>", self._draw_gradient)

    def _draw_gradient(self):
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = width
        (r1, g1, b1) = self.winfo_rgb(self._color1)
        (r2, g2, b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2 - r1) / limit
        g_ratio = float(g2 - g1) / limit
        b_ratio = float(b2 - b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr, ng, nb)
            self.create_line(i, 0, i, height, tags=("gradient",), fill=color)
        self.lower("gradient")


# these classes to make color gradient taken from stack overflow^^
window = tk.Tk()
Example(window).pack(fill="both", expand=True)

# global variable

tempVal = "Celsius"
tempVal1 = "Celsius"
# grab drop down value


def store_temp(sel_temp):
    global tempVal
    tempVal = sel_temp


def store_temp1(sel_temp1):
    global tempVal1
    tempVal1 = sel_temp1


# temp conversion

def call_convert(rlabel1, inputn):
    tem = inputn.get()

    if tem == "":
        rlabel1.config(text="Error" + " " * 20)

    if tempVal == 'Celsius':
        f = round(float((float(tem) * 9 / 5) + 32), 3)
        k = round(float((float(tem) + 273.15)))
        if tempVal1 == "Kelvin":
            if k < 0:
                rlabel1.config(text="Error" + " " * 20)
            else:
                rlabel1.config(text=str(k) + " " * 21)

        elif tempVal1 == "Fahrenheit":
            if f < -459:
                rlabel1.config(text="Error" + " " * 20)
            else:
                rlabel1.config(text=str(f) + " " * 21)
        elif tempVal1 == "Celsius":
            if int(tem) < -273:
                rlabel1.config(text="Error" + " " * 20)
            else:
                rlabel1.config(text=str(input_entry.get()) + " " * 21)

    if tempVal == 'Fahrenheit':
        c = round(float((float(tem) - 32) * 5 / 9))
        k = round(c + 273)
        if tempVal1 == "Celsius":
            if c < -273:
                rlabel1.config(text="Error" + " " * 20)
            else:
                rlabel1.config(text=str(c) + " " * 21)
        elif tempVal1 == "Kelvin":
            if k < 0:
                rlabel1.config(text="Error" + " " * 20)
            else:
                rlabel1.config(text=str(k) + " " * 21)
        elif tempVal1 == "Fahrenheit":
            if int(tem) < -459:
                rlabel1.config(text="Error" + " " * 20)
            else:
                rlabel1.config(text=str(input_entry.get()) + " " * 21)

    if tempVal == 'Kelvin':
        c = round(float((float(tem) - 273.15)))
        f = round(float((float(tem) - 273.15) * 1.8000 + 32.00))
        if tempVal1 == "Celsius":
            if c < -273:
                rlabel1.config(text="Error" + " " * 20)
            else:
                rlabel1.config(text=str(c) + " " * 21)
        elif tempVal1 == "Fahrenheit":
            if c < -459:
                rlabel1.config(text="Error" + " " * 20)
            else:
                rlabel1.config(text=str(f) + " " * 21)
        elif tempVal1 == "Kelvin":
            if int(tem) < 0:
                rlabel1.config(text="Error" + " " * 20)
            else:
                rlabel1.config(text=str(input_entry.get()) + " " * 21)
    return


window.geometry('600x450+100+200')
window.title('Temperature Converter')
window.resizable(width=True, height=True)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)
numberInput = tk.StringVar()
var = tk.StringVar()
var1 = tk.StringVar()

# label and entry field

input_entry = tk.Entry(window, textvariable=numberInput)
input_entry.place(x=60, y=150)
result_label1 = tk.Label(window, background='white', foreground="black", text=" " * 25)
label = tk.Label(window, background='white', foreground="black", text="Enter Temperature:  ")
label.place(x=65, y=110)
result_label1.place(x=350, y=150)
result_label2 = tk.Label(window, background='white', foreground="black")
dropDownList = ["Celsius", "Fahrenheit", "Kelvin"]
dropDownList1 = ["Celsius", "Fahrenheit", "Kelvin"]
dropdown = tk.OptionMenu(window, var, *dropDownList, command=store_temp)
dropdown1 = tk.OptionMenu(window, var1, *dropDownList, command=store_temp1)
var.set(dropDownList[0])
var1.set(dropDownList1[0])
dropdown1.place(x=450, y=145)
dropdown.place(x=190, y=145)
# button click

call_convert = partial(call_convert, result_label1, numberInput)
result_button = tk.Button(window, text="Convert", command=call_convert, background='white', foreground="black")
result_button.place(x=280, y=200)
window.mainloop()
