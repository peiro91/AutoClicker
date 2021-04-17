import tkinter as tk

ro = tk.Tk()
w = tk.Label(ro, text="Hello world")
ro.geometry("600x600")
butt=tk.Button(text="OK")
butt.config(height = 1, width = 10)
butt.grid(row=1)
w.grid(row=0)
ro.mainloop()