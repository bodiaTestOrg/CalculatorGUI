from Calc import Calc
from tkinter import *

calc = Calc()

root = Tk()
root.geometry("400x400")
root.title("Calculator")

BUTTON_WIDTH = 10
BUTTON_HEIGHT = 2
BUTTON_FONT = ("Arial", 10)
RESULT_FONT = ("Arial", 12)

display_frame = Frame(root)
display_frame.pack()
display_label = Label(display_frame, text = "", font=RESULT_FONT)
display_label.pack()

buttons_frame = Frame(root)
buttons_frame.pack()

def input_to_display_label(char: str):
    current_input = str(display_label.cget("text"))

    if char == ".":
        str_without_numbers = ""
        for c in current_input:
            if c in "+-*/.":
                str_without_numbers += c
        try: 
            if str_without_numbers[-1] == ".": return
        except:
            ...

    if "ERROR" in current_input:
        current_input = ""

    if char in "+-*/":
        if current_input == "": return
        if current_input[-1] in "+-*/": return

    display_label.config(text = current_input + char)

digit_buttons = [Button(buttons_frame, text=i, command=lambda i=i: input_to_display_label(str(i)))
                 for i in range(10)]

for i, button in enumerate(digit_buttons[1:]):
    button.grid(row=i//3, column=i%3)
digit_buttons[0].grid(row=3, column=1)

sign_buttons = [Button(buttons_frame, text="+", command=lambda: input_to_display_label("+")),
                Button(buttons_frame, text="-", command=lambda: input_to_display_label("-")),
                Button(buttons_frame, text="*", command=lambda: input_to_display_label("*")),
                Button(buttons_frame, text="/", command=lambda: input_to_display_label("/"))]
for i, button in enumerate(sign_buttons):
    button.grid(row=i, column=3)

def clear_all_display_label():
    display_label.config(text = "")

def clear_last_display_label():
    try:
        display_label.config(text = display_label.cget("text")[:-1])
    except:
        display_label.config(text = "")

def show_result():
    operation = str(display_label.cget("text"))
    try:
        display_label.config(text = calc.calculate(operation))
    except:
        if "/0" in operation:
            display_label.config(text = "ERROR: division by zero")
        else:
            display_label.config(text = "ERROR: invalid input")

special_buttons = [Button(buttons_frame, text="Clear",  command=clear_all_display_label),
                   Button(buttons_frame, text="<-",     command=clear_last_display_label),
                   Button(buttons_frame, text=".",      command=lambda: input_to_display_label(".")),
                   Button(buttons_frame, text="=",      command=show_result)]
for i, button in enumerate(special_buttons):
    button.grid(row=4, column=i)

all_buttons = digit_buttons + sign_buttons + special_buttons
for button in all_buttons:
    button.config(width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=BUTTON_FONT)

root.mainloop()
