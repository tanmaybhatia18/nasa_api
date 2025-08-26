import tkinter as tk

win = tk.Tk()
win.geometry("200x150")

def show_state():
    print("Checked!" if var.get() else "Unchecked!")

var = tk.IntVar()  # 1 = checked, 0 = unchecked
cb = tk.Checkbutton(win, text="I agree", variable=var, command=show_state)
cb.pack(pady=10)

tk.Button(win, text="Select", command=cb.select).pack()
tk.Button(win, text="Deselect", command=cb.deselect).pack()
tk.Button(win, text="Toggle", command=cb.toggle).pack()
tk.Button(win, text="Flash", command=cb.flash).pack()

win.mainloop()
