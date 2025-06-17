import tkinter as tk
import math

# Create main window
window = tk.Tk()
window.title("Scientific Calculator")
window.geometry("400x600")
window.configure(bg="#f2f2f2")
window.resizable(False, False)

expression = ""

def press(symbol):
    global expression
    expression += str(symbol)
    input_text.set(expression)

def clear():
    global expression
    expression = ""
    input_text.set("")

def backspace():
    global expression
    expression = expression[:-1]
    input_text.set(expression)

def equal():
    global expression
    try:
        result = str(eval(expression, {"__builtins__": None}, math.__dict__))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

def key_press(event):
    key = event.keysym
    numpad_map = {
        'KP_0': '0', 'KP_1': '1', 'KP_2': '2', 'KP_3': '3',
        'KP_4': '4', 'KP_5': '5', 'KP_6': '6', 'KP_7': '7',
        'KP_8': '8', 'KP_9': '9', 'KP_Decimal': '.', 'KP_Add': '+',
        'KP_Subtract': '-', 'KP_Multiply': '*', 'KP_Divide': '/',
        'Return': '=', 'BackSpace': '⌫', 'Escape': 'C'
    }

    if key in numpad_map:
        key = numpad_map[key]

    if key.isdigit() or key in "+-*/().":
        press(key)
    elif key == "=" or key == "Return":
        equal()
    elif key == "C" or key == "Escape":
        clear()
    elif key == "⌫" or key == "BackSpace":
        backspace()

# Input text variable
input_text = tk.StringVar()

# Display panel
input_frame = tk.Frame(window, bg="#f2f2f2")
input_frame.pack(pady=10)

input_field = tk.Entry(input_frame, textvariable=input_text, font=('Segoe UI', 24),
                       justify='right', bd=0, bg="white", relief="flat", width=20)
input_field.grid(row=0, column=0, ipadx=8, ipady=20)

# Bind keyboard keys
window.bind('<Key>', key_press)

# Button layout
buttons_frame = tk.Frame(window, bg="#f2f2f2")
buttons_frame.pack()

buttons = [
    ['C', '⌫', '(', ')', '/'],
    ['7', '8', '9', '*', 'sqrt'],
    ['4', '5', '6', '-', 'pow'],
    ['1', '2', '3', '+', 'log'],
    ['0', '.', '=', 'pi', 'e'],
    ['sin', 'cos', 'tan']
]

# Button generation
def create_button(text, row, col, colspan=1):
    font_style = ('Segoe UI', 16, 'bold')
    btn = tk.Button(buttons_frame, text=text, width=6 * colspan, height=2,
                    bg="#ffffff", fg="#000000", font=font_style,
                    bd=0, relief="ridge", highlightthickness=1,
                    highlightbackground="#cccccc", highlightcolor="#cccccc")

    if text == '=':
        btn.config(bg="#4CAF50", fg="white", command=equal)
    elif text == 'C':
        btn.config(command=clear)
    elif text == '⌫':
        btn.config(command=backspace)
    elif text == 'sqrt':
        btn.config(command=lambda: press('math.sqrt('))
    elif text == 'pow':
        btn.config(command=lambda: press('math.pow('))
    elif text == 'log':
        btn.config(command=lambda: press('math.log10('))
    elif text == 'sin':
        btn.config(command=lambda: press('math.sin(math.radians('))
    elif text == 'cos':
        btn.config(command=lambda: press('math.cos(math.radians('))
    elif text == 'tan':
        btn.config(command=lambda: press('math.tan(math.radians('))
    elif text == 'pi':
        btn.config(command=lambda: press('math.pi'))
    elif text == 'e':
        btn.config(command=lambda: press('math.e'))
    else:
        btn.config(command=lambda x=text: press(x))

    btn.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5, sticky="nsew")

# Create buttons in grid
for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        create_button(btn_text, i, j)

# Grid resizing config
for i in range(6):
    buttons_frame.rowconfigure(i, weight=1)
    buttons_frame.columnconfigure(i, weight=1)

# Start GUI
window.mainloop()

