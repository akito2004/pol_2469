import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
from ttkthemes import ThemedTk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def runge_kutta(f, x0, y0, xf, h):
    x = np.arange(x0, xf + h, h)
    y = np.zeros(len(x))
    y[0] = y0
    for i in range(1, len(x)):
        k1 = h * f(x[i - 1], y[i - 1])
        k2 = h * f(x[i - 1] + h / 2, y[i - 1] + k1 / 2)
        k3 = h * f(x[i - 1] + h / 2, y[i - 1] + k2 / 2)
        k4 = h * f(x[i - 1] + h, y[i - 1] + k3)
        y[i] = y[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return x, y


def mostrar_grafico(x, y):
    # Crear una nueva ventana para la gráfica
    ventana_grafico = tk.Toplevel(root)
    ventana_grafico.title("Gráfico del Método de Runge-Kutta")
    # Fondo oscuro de la ventana emergente (opcional)
    ventana_grafico.configure(bg="#2B2B2B")

    # Crear la figura de Matplotlib
    fig = plt.Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)

    # Fondo oscuro para la figura y los ejes
    fig.patch.set_facecolor('#2B2B2B')  # Fondo de la figura
    ax.set_facecolor('#2B2B2B')  # Fondo del área de la gráfica

    # Graficar los datos
    ax.plot(x, y, label='Aproximación', color='blue', linewidth=2)

    # Colores y tamaños de texto
    ax.set_xlabel("x", fontsize=12, color="white")
    ax.set_ylabel("y", fontsize=12, color="white")
    ax.set_title("Método de Runge-Kutta", fontsize=14, color="white")

    # Cambiar color de las líneas de los ejes (spines) a blanco
    for spine in ax.spines.values():
        spine.set_color('white')
    # Cambiar color de los valores en los ejes
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    # Rejilla gris
    ax.grid(True, color="gray", linestyle='--', linewidth=0.5)

    # Leyenda con fondo oscuro
    legend = ax.legend()
    frame = legend.get_frame()
    frame.set_facecolor('#3A3A3A')  # Fondo de la leyenda
    frame.set_edgecolor('white')  # Borde de la leyenda
    # Cambiar color del texto de la leyenda
    for text in legend.get_texts():
        text.set_color('white')

    # Integrar la figura en la ventana usando FigureCanvasTkAgg
    canvas = FigureCanvasTkAgg(fig, master=ventana_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Función para guardar el gráfico como imagen
    def guardar_imagen():
        ruta = filedialog.asksaveasfilename(defaultextension=".png",
                                            filetypes=[("PNG files", "*.png"), ("Todos los archivos", "*.*")])
        if ruta:
            fig.savefig(ruta)

    # Frame para los botones
    frame_botones = ttk.Frame(ventana_grafico)
    frame_botones.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

    ttk.Button(frame_botones, text="Guardar imagen", command=guardar_imagen).pack(side=tk.LEFT, padx=10)
    ttk.Button(frame_botones, text="Cerrar", command=ventana_grafico.destroy).pack(side=tk.LEFT, padx=10)


def resolver_ecuacion():
    try:
        eq = entrada_ecuacion.get()
        f = lambda x_val, y_val: eval(eq, {"x": x_val, "y": y_val, "np": np})
        x0 = float(entrada_x0.get())
        y0 = float(entrada_y0.get())
        xf = float(entrada_xf.get())
        h = float(entrada_h.get())
        x, y = runge_kutta(f, x0, y0, xf, h)
        mostrar_grafico(x, y)
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")


# Ventana principal con tema oscuro
root = ThemedTk(theme="equilux")
root.title("Solucionador de Runge-Kutta")
root.geometry("500x400")

# Fondo oscuro de la ventana principal
root.configure(bg="#2B2B2B")

# Configurar estilos para TTK
style = ttk.Style(root)
style.configure("TFrame", background="#2B2B2B")
style.configure("TLabel", background="#2B2B2B", foreground="white", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))
style.configure("TEntry", fieldbackground="#3A3A3A", foreground="white")

# --- Encabezado ---
header_frame = ttk.Frame(root)
header_frame.pack(pady=20)
ttk.Label(header_frame, text="Solucionador de Runge-Kutta", font=("Helvetica", 18, "bold")).pack()

# --- Frame principal ---
main_frame = ttk.Frame(root)
main_frame.pack(pady=10, padx=20, fill=tk.X)

# dy/dx
ttk.Label(main_frame, text="dy/dx =").grid(row=0, column=0, sticky=tk.W, pady=5)
entrada_ecuacion = ttk.Entry(main_frame, width=40)
entrada_ecuacion.grid(row=0, column=1, pady=5)

# x0
ttk.Label(main_frame, text="x0:").grid(row=1, column=0, sticky=tk.W, pady=5)
entrada_x0 = ttk.Entry(main_frame, width=20)
entrada_x0.grid(row=1, column=1, sticky=tk.W, pady=5)

# y0
ttk.Label(main_frame, text="y0:").grid(row=2, column=0, sticky=tk.W, pady=5)
entrada_y0 = ttk.Entry(main_frame, width=20)
entrada_y0.grid(row=2, column=1, sticky=tk.W, pady=5)

# xf
ttk.Label(main_frame, text="xf:").grid(row=3, column=0, sticky=tk.W, pady=5)
entrada_xf = ttk.Entry(main_frame, width=20)
entrada_xf.grid(row=3, column=1, sticky=tk.W, pady=5)

# h
ttk.Label(main_frame, text="h:").grid(row=4, column=0, sticky=tk.W, pady=5)
entrada_h = ttk.Entry(main_frame, width=20)
entrada_h.grid(row=4, column=1, sticky=tk.W, pady=5)

# --- Frame inferior (botón Resolver) ---
footer_frame = ttk.Frame(root)
footer_frame.pack(pady=20)
ttk.Button(footer_frame, text="Resolver", command=resolver_ecuacion).pack()

root.mainloop()
