import tkinter as tk
from tkinter import filedialog
import pandas as pd

def convertir_a_excel():
    archivo_json = filedialog.askopenfilename(filetypes=[('Archivos JSON', '*.json')])
    if archivo_json:
        data = pd.read_json(archivo_json)
        archivo_excel = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[('Archivos Excel', '*.xlsx')])
        if archivo_excel:
            data.to_excel(archivo_excel, index=False)
            mensaje.config(text=f'Se ha convertido {archivo_json} a {archivo_excel}')

app = tk.Tk()
app.title("Conversor JSON a Excel")

boton = tk.Button(app, text="Convertir a XLS", command=convertir_a_excel)
boton.pack(pady=20)

mensaje = tk.Label(app, text="")
mensaje.pack()

app.mainloop()