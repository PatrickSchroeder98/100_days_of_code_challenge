import tkinter as tk

gui = tk.Tk()
gui.title("Mile to Kilometers Converter")
gui.minsize(width=150, height=100)

input_value = tk.Entry()
input_value.grid(row=0, column=1)

miles = tk.Label(text=" Miles")
miles.grid(row=0, column=2)

is_equal = tk.Label(text="Is equal to: ")
is_equal.grid(row=1, column=0)

value = tk.Label(text="0")
value.grid(row=1, column=1)

km = tk.Label(text=" Km")
km.grid(row=1, column=2)


def calculate():
    new_val = float(input_value.get()) * 1.6
    value.config(text=new_val)


btn = tk.Button(text="Calculate", command=calculate)
btn.grid(row=2, column=1)

gui.mainloop()
