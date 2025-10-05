import tkinter  as tk
window = tk.Tk()
window.geometry("1920x1080")  # Set the window size to 1920x1080
window.title("Entry Text Box")
entry = tk.Entry(window)
entry.pack(pady=20)
window.mainloop()
