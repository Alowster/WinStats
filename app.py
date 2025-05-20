import tkinter as tk
import psutil

def actualizar_metricas():
    cpu = psutil.cpu_percent(interval=0.4)
    match opcion.get():
        case "1":
            label.config(text=f'C:{cpu:02.0f}%')
        case "2":
            ram = psutil.virtual_memory().percent
            label.config(text=f'C:{cpu:02.0f}% | R:{ram:02.0f}%')
        case "X":
            exit()
    root.after(300 , actualizar_metricas)

# Crear la ventana
root = tk.Tk()
root.geometry("200x50+1080+0")
root.config(bg='black')
root.overrideredirect(True)
root.attributes("-transparentcolor", "black")
root.attributes("-topmost", True)

label = tk.Label(root, text='C:00%', font=("Arial", 11), fg="white", bg="black")
label.place(x=45, y=0)

opcion = tk.StringVar(root)
opcion.set("1")  # Valor por defecto

actualizar_metricas()
menu = tk.OptionMenu(root, opcion, "1", "2", "X")
menu.config(bg="black", fg="black", highlightthickness=0, bd=0, activebackground="gray")
menu["menu"].config(bg="black", fg="white")  # Colores del menú desplegable
menu.place(x=0, y=0)

root.mainloop()


