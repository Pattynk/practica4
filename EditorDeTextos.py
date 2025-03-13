import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox

#Funciones para las acciones de los botones
def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filepath:
        with open(filepath, "r", encoding="utf-8") as file:
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, file.read())

def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filepath:
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(text_area.get("1.0", tk.END))

def clear_text():
    text_area.delete("1.0", tk.END)

def change_text_color():
    color = colorchooser.askcolor()[1]
    if color:
        text_area.config(fg=color)

def find_and_replace():
    find_str = find_entry.get()
    replace_str = replace_entry.get()
    content = text_area.get("1.0", tk.END)
    new_content = content.replace(find_str, replace_str)
    text_area.delete("1.0", tk.END)
    text_area.insert("1.0", new_content)
    messagebox.showinfo("Buscar y Reemplazar", "Reemplazo completado.")

# Crear la ventana principal de la interfaz
root = tk.Tk()
root.title("Editor de Texto")
root.geometry("600x600")

# Crear un menú superior y desplegable
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Abrir", command=lambda: None, accelerator="Ctrl+A")
file_menu.add_command(label="Guardar", command=lambda: None, accelerator="Ctrl+G")
file_menu.add_separator()
file_menu.add_command(label="Borrar", command=lambda: None, accelerator="Ctrl+B")
menu_bar.add_cascade(label="Archivo", menu=file_menu)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cambiar color de texto", command=lambda: None,)
menu_bar.add_cascade(label="Editar", menu=edit_menu)

# Área de texto
text_area = tk.Text(root, wrap="word", font=("Arial", 12))
text_area.pack(expand=True, fill="both")

# Frame para Buscar y Reemplazar
frame = tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame, text="Buscar:").grid(row=0, column=0)
find_entry = tk.Entry(frame)
find_entry.grid(row=0, column=1)

tk.Label(frame, text="Reemplazar con:").grid(row=0, column=2)
replace_entry = tk.Entry(frame)
replace_entry.grid(row=0, column=3)

tk.Button(frame, text="Reemplazar", command=lambda: None,).grid(row=0, column=4)

# Atajos de teclado
root.bind("<Control-a>", lambda event: None())
root.bind("<Control-g>", lambda event: None())
root.bind("<Control-b>", lambda event: None())

# Ejecutar
root.mainloop()
