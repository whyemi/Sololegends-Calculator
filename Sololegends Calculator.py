import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import pytz

sanciones = {
    "primera": 6,
    "segunda": 12,
    "tercera": 24
}

def calcular():
    try:
        fecha = entry_fecha.get()
        hora = entry_hora.get()
        tipo = combo_sancion.get().lower()
        zona = combo_zona.get()

        if not fecha or not hora or not tipo or not zona:
            messagebox.showwarning("Error", "Completa todos los campos.")
            return

        
        tz = pytz.timezone(zona)
        fecha_hora = datetime.strptime(f"{fecha} {hora}", "%d/%m/%Y %H:%M")
        fecha_hora = tz.localize(fecha_hora)

        
        horas_sancion = sanciones.get(tipo, 0)
        fin_sancion = fecha_hora + timedelta(hours=horas_sancion)

        
        siguiente_ban = fin_sancion + timedelta(hours=24)

        messagebox.showinfo(
            "Resultado",
            f"📌 Fin de sanción: {fin_sancion.strftime('%d/%m/%Y %H:%M %Z')}\n"
            f"⏳ Puedes volver a banear desde: {siguiente_ban.strftime('%d/%m/%Y %H:%M %Z')}"
        )

    except Exception as e:
        messagebox.showerror("Error", f"Hubo un problema: {e}")

# Ventana principal
root = tk.Tk()
root.title("Sololegends Calculator")
root.geometry("400x300")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Fecha (dd/mm/aaaa):").pack(pady=5)
entry_fecha = tk.Entry(root)
entry_fecha.pack()

tk.Label(root, text="Hora (HH:MM 24h):").pack(pady=5)
entry_hora = tk.Entry(root)
entry_hora.pack()

tk.Label(root, text="Tipo de sanción:").pack(pady=5)
combo_sancion = ttk.Combobox(root, values=["Primera", "Segunda", "Tercera"])
combo_sancion.pack()

tk.Label(root, text="Zona horaria:").pack(pady=5)
combo_zona = ttk.Combobox(root, values=pytz.all_timezones, width=40)
combo_zona.set("America/Bogota")  # Por defecto Colombia
combo_zona.pack()

tk.Button(root, text="Calcular", command=calcular).pack(pady=20)

root.mainloop()
