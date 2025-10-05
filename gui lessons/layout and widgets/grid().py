
import tkinter as tk

window = tk.Tk()
window.title("Grid Layout Example")

label = tk.Label(window , text="shirshadip")
label.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(window)
entry.grid(row=1, column=0, padx=10, pady=10)
window = tk.Tk()
window.title("Grid Layout Example")

window.mainloop()