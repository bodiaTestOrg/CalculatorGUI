from Calc import Calc
from tkinter import *

calc = Calc()

root = Tk()
root.geometry("400x400")
root.title("Calculator")


display_frame = Frame(root)
display_frame.pack()
display_label = Label(display_frame, text = "")
display_label.pack()

BUTTON_WIDTH = 10
BUTTON_HEIGHT = 2

buttons_frame = Frame(root)
buttons_frame.pack()

def input_to_display_label(char: str):
    current_input = str(display_label.cget("text"))

    if "ERROR" in current_input:
        current_input = ""

    if char in "+-*/.":
        if current_input == "": return
        if current_input[-1] in "+-*/.": return

    display_label.config(text = current_input + char)

digit_buttons = [Button(buttons_frame, text=i, command=lambda i=i: input_to_display_label(str(i)), width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
                 for i in range(10)]

for i, button in enumerate(digit_buttons[1:]):
    button.grid(row=i//3, column=i%3)
digit_buttons[0].grid(row=3, column=1)

sign_buttons = [Button(buttons_frame, text="+", command=lambda: input_to_display_label("+"), width=BUTTON_WIDTH, height=BUTTON_HEIGHT),
                Button(buttons_frame, text="-", command=lambda: input_to_display_label("-"), width=BUTTON_WIDTH, height=BUTTON_HEIGHT),
                Button(buttons_frame, text="*", command=lambda: input_to_display_label("*"), width=BUTTON_WIDTH, height=BUTTON_HEIGHT),
                Button(buttons_frame, text="/", command=lambda: input_to_display_label("/"), width=BUTTON_WIDTH, height=BUTTON_HEIGHT)]
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


special_buttons = [Button(buttons_frame, text="Clear",  command=clear_all_display_label,             width=BUTTON_WIDTH, height=BUTTON_HEIGHT),
                   Button(buttons_frame, text="<-",     command=clear_last_display_label,            width=BUTTON_WIDTH, height=BUTTON_HEIGHT),
                   Button(buttons_frame, text=".",      command=lambda: input_to_display_label("."), width=BUTTON_WIDTH, height=BUTTON_HEIGHT),
                   Button(buttons_frame, text="=",      command=show_result,                         width=BUTTON_WIDTH, height=BUTTON_HEIGHT)]
for i, button in enumerate(special_buttons):
    button.grid(row=4, column=i)

root.mainloop()
