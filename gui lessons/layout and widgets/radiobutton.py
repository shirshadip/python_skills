import tkinter as tk
window = tk.Tk()
window.geometry("1920x1080")  # Set the window size to 1920x1080
window.title("Radio Button Example")
choice = tk.StringVar()

radio1 = tk.Radiobutton(window, text = "option A", variable = choice,value = "A")
radio2= tk.Radiobutton(window , text = "option B", variable = choice , value = "B")
radio1.pack()
radio2.pack()
window.mainloop()