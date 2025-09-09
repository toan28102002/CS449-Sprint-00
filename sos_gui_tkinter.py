"tkinter test"
import tkinter as tk
from tkinter import messagebox

def show_choice():
    choice = var.get()
    msg = f"You selected: {choice}"
    messagebox.showinfo("Radio Button Choice", msg)

def show_checkbox():
    if check_var.get():
        messagebox.showinfo("Checkbox", "Checkbox is checked!")
    else:
        messagebox.showinfo("Checkbox", "Checkbox is unchecked!")

# Main window
root = tk.Tk()
root.title("Simple GUI Example")
root.geometry("400x300")

# Add a label (text)
label = tk.Label(root, text="This is a simple GUI program", font=("Arial", 14))
label.pack(pady=10)

# Draw a line (using Canvas)
canvas = tk.Canvas(root, width=300, height=50)
canvas.pack()
canvas.create_line(20, 25, 280, 25, fill="blue", width=3)
canvas.create_line(20, 50, 280, 50, fill="red", width=3)

# Checkbox
check_var = tk.BooleanVar()
checkbox = tk.Checkbutton(root, text="Check me!", variable=check_var, command=show_checkbox)
checkbox.pack(pady=10)

# Radio buttons
var = tk.StringVar(value="Option 1")
radio1 = tk.Radiobutton(root, text="Option 1", variable=var, value="Option 1", command=show_choice)
radio2 = tk.Radiobutton(root, text="Option 2", variable=var, value="Option 2", command=show_choice)
radio1.pack()
radio2.pack()

# Run the main loop
root.mainloop()
