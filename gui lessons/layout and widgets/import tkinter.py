import tkinter as tk 

window = tk.Tk()
window.title("my first gui")
window.geometry("720x480")

label = tk.Label (window, text ="hello")
label.pack(pady=10)

def on_button_click():
    label.config(text="Button clicked!")

button = tk.Button(window , text="click here", command = on_button_click)
button.pack(pady=70)

window.mainloop()
# This code creates a simple GUI application with a label and a button.