import tkinter as tk
import psutil

W, H = 200, 50  # Tamaño de ventana
DELAY, INTERVAL = 300, 0.4

def act():
    c = psutil.cpu_percent(interval=INTERVAL)
    o = v.get()
    if o == "1":
        t = f'C:{c:02.0f}%'
    elif o == "2":
        r = psutil.virtual_memory().percent
        t = f'C:{c:02.0f}% | R:{r:02.0f}%'
    elif o == "X":
        win.destroy()
        return
    else:
        t = "Modo inválido"
    lbl.config(text=t)
    win.after(DELAY, act)

win = tk.Tk()
win.withdraw()
win.update_idletasks()

sw, sh = win.winfo_screenwidth(), win.winfo_screenheight()
x = max(sw - W, 0)

win.geometry(f'{W}x{H}+{x}+0')
win.config(bg='black')
win.overrideredirect(True)
win.attributes('-transparentcolor', 'black')
win.attributes('-topmost', True)
win.deiconify()

lbl = tk.Label(win, text='C:00%', font=("Arial", 11), fg='white', bg='black')
lbl.place(x=45, y=0)

v = tk.StringVar(value="1")
m = tk.OptionMenu(win, v, "1", "2", "X")
m.config(bg='black', fg='black', highlightthickness=0, bd=0, activebackground='gray')
m["menu"].config(bg='black', fg='white')
m.place(x=0, y=0)

act()
win.mainloop()