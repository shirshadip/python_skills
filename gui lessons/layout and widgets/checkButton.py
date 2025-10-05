import tkinter as tk  
window = tk.Tk()
window.geometry("1920x1080")  # Set the window size to 1920x1080
window.title("Check Button Example")
check = tk.Checkbutton(window,text= "i agree")
check.config(width=100, height=50)  # Set the size of the check button
check.pack()
window.mainloop()