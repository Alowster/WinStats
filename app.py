import tkinter as tk
import psutil

def actualizar_cpu():
    cpu = psutil.cpu_percent(interval=1)
    label.config(text=f'C:{cpu}%')
    root.after(200 , actualizar_cpu)

# Crear la ventana
root = tk.Tk()
root.title("Ventana Transparente con Texto")
root.geometry("80x50+1080+0")
root.config(bg='black')
root.overrideredirect(True)
root.attributes("-transparentcolor", "black")
root.attributes("-topmost", True)

label = tk.Label(root, text='C:0%', font=("Arial", 11), fg="white", bg="black")
label.pack(side="left")

button = tk.Button(root, text="X", command=root.destroy, bg="black", fg="white", bd=0 )
button.pack(side="right")

actualizar_cpu()

root.mainloop()