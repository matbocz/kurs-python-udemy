import tkinter as tk


def convert_from_kg():
    grams = float(e1_value.get()) * 1000
    pounds = float(e1_value.get()) * 2.20462
    ounces = float(e1_value.get()) * 35.274

    t2.delete("1.0", tk.END)
    t2.insert(tk.END, grams)

    t3.delete("1.0", tk.END)
    t3.insert(tk.END, pounds)

    t4.delete("1.0", tk.END)
    t4.insert(tk.END, ounces)


window = tk.Tk()

l1 = tk.Label(window, text="kg")
l1.grid(row=0, column=2)
e1_value = tk.StringVar()
e1 = tk.Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

b1 = tk.Button(window, text="Convert", command=convert_from_kg)
b1.grid(row=3, column=2)

l2 = tk.Label(window, text="grams = ")
l2.grid(row=1, column=0)
t2 = tk.Text(window, height=1, width=15)
t2.grid(row=1, column=1)

l3 = tk.Label(window, text="pounds = ")
l3.grid(row=2, column=0)
t3 = tk.Text(window, height=1, width=15)
t3.grid(row=2, column=1)

l4 = tk.Label(window, text="ounces = ")
l4.grid(row=3, column=0)
t4 = tk.Text(window, height=1, width=15)
t4.grid(row=3, column=1)

window.mainloop()
