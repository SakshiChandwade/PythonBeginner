import tkinter as tk

# Step 1: Create window
window = tk.Tk()
window.title("Simple Calculator( Sakshi Chandwade)")
window.geometry("300x400")

# Step 2: Create input field
entry = tk.Entry(window, width=16, font=("Arial", 24), bd=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Step 3: Define button click function
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Step 4: Create buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Step 5: Add buttons to window
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(window, text=text, width=5, height=2, command=calculate).grid(row=row, column=col)
    elif text == 'C':
        tk.Button(window, text=text, width=23, height=2, command=clear).grid(row=row, column=col, columnspan=4)
    else:
        tk.Button(window, text=text, width=5, height=2, command=lambda t=text: button_click(t)).grid(row=row, column=col)

# Step 6: Run the app
window.mainloop()
