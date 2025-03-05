from extendedCalc import extendetCalc
from tkinter import *

calc = extendetCalc()
calc.start()

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

    if char in "+-*/":
        if (current_input == "" or
            current_input[-1] in "+-*/."):
            return

    elif char == ".":
        input_without_numbers = ""
        for c in current_input:
            if c in "+-*/.":
                input_without_numbers += c
        try: 
            if input_without_numbers[-1] == ".":
                return
        except IndexError:
            ...

    if "ERROR" in current_input:
        current_input = ""

    display_label.config(text = current_input + char)

digit_buttons = [Button(buttons_frame, text=i, command=lambda i=i: input_to_display_label(str(i)))
                 for i in range(10)]

digit_buttons[0].grid(row=3, column=1)
for i, button in enumerate(digit_buttons[1:]):
    button.grid(row=i//3, column=i%3)

sign_buttons = [Button(buttons_frame, text="+", command=lambda: input_to_display_label("+")),
                Button(buttons_frame, text="-", command=lambda: input_to_display_label("-")),
                Button(buttons_frame, text="*", command=lambda: input_to_display_label("*")),
                Button(buttons_frame, text="/", command=lambda: input_to_display_label("/"))]
for i, button in enumerate(sign_buttons):
    button.grid(row=i, column=3)

def clear_all_display_label():
    display_label.config(text = "")

def clear_last_display_label():
    display_label.config(text = display_label.cget("text")[:-1])

def show_result():
    operation = str(display_label.cget("text"))

    if operation == "": return
    elif operation[-1] == ".": operation += "0"

    display_label.config(text = calc.calculate(operation))
    update_logs_list()

special_buttons = [Button(buttons_frame, text="Clear",  command=clear_all_display_label),
                   Button(buttons_frame, text="<-",     command=clear_last_display_label),
                   Button(buttons_frame, text=".",      command=lambda: input_to_display_label(".")),
                   Button(buttons_frame, text="=",      command=show_result)]
for i, button in enumerate(special_buttons):
    button.grid(row=4, column=i)

all_buttons = digit_buttons + sign_buttons + special_buttons
for button in all_buttons:
    button.config(width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=BUTTON_FONT)

logs_frame = Frame(root)
logs_frame.pack()
logs_list = Listbox(logs_frame, width=BUTTON_WIDTH * 6)
logs_list.pack()

def update_logs_list():
    rows = calc.getLogs()
    history_rows = calc.history

    lines = map(lambda i: f"{i[0]} | {i[1]}", rows)
    recent_lines = map(lambda i: f"{i[0]}0 | {i[1]}", history_rows)

    logs_list.delete(0, END)

    logs_list.insert(END, *lines)
    logs_list.insert(END, *recent_lines)

update_logs_list()

def on_window_close():
    calc.end()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_window_close)

root.mainloop()