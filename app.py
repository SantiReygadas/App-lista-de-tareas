import tkinter as tk
from tkinter import messagebox

class ListaDeTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("600x500")
        self.root.minsize(400, 300)
        self.root.config(bg="#2c3e50")
        self.tareas = []
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

        self.entry_tarea = tk.Entry(root, width=30, font=('Roboto', 14), bg="#34495e", fg="#ecf0f1", insertbackground="#ecf0f1", relief="flat")
        self.entry_tarea.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")

        

        self.lista_tareas = tk.Listbox(root, width=40, height=10, font=('Roboto', 17), bg="#ecf0f1", fg="#2c3e50", selectbackground="#2980b9", relief="flat")
        self.lista_tareas.grid(row=1, column=0, columnspan=2, padx=15, pady=15, sticky="nsew")

        boton_quitar = tk.Button(root, text="Quitar Tarea", command=self.quitar_tarea, font=('Roboto', 12), bg="#e74c3c", fg="#ecf0f1", activebackground="#c0392b", relief="flat")
        boton_quitar.grid(row=2, column=0, padx=15, pady=15, sticky="ew")
        boton_añadir = tk.Button(root, text="Añadir Tarea", command=self.añadir_tarea, font=('Roboto', 12), bg="#1abc9c", fg="#ecf0f1", activebackground="#16a085", relief="flat")
        boton_añadir.grid(row=0, column=1, padx=15, pady=15, sticky="nsew")
        boton_completar = tk.Button(root, text="Tarea Completada", command=self.completar_tarea, font=('Roboto', 12), bg="#f39c12", fg="#ecf0f1", activebackground="#e67e22", relief="flat")
        boton_completar.grid(row=2, column=1, padx=15, pady=15, sticky="ew")

        self.lista_tareas.bind('<Double-Button-1>', lambda event: self.completar_tarea())
        self.lista_tareas.bind('<space>', lambda event: self.quitar_tarea())
        self.entry_tarea.bind('<Return>', lambda event: self.añadir_tarea())
        
        

    def añadir_tarea(self):
        tarea = self.entry_tarea.get()
        if tarea:
            self.tareas.append(tarea)
            self.actualizar_lista_de_tareas()
            self.entry_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Escribe una tarea")

    def quitar_tarea(self):
        indice_tarea_seleccionada = self.lista_tareas.curselection()
        if indice_tarea_seleccionada:
            if messagebox.askyesno("Confirmación", "¿Estás seguro de que quieres eliminar esta tarea?"):
                self.tareas.pop(indice_tarea_seleccionada[0])
                self.actualizar_lista_de_tareas()

    def completar_tarea(self):
        indice_tarea_seleccionada = self.lista_tareas.curselection()
        if indice_tarea_seleccionada:
            indice_tarea = indice_tarea_seleccionada[0]
            tarea = self.tareas[indice_tarea]
            if not tarea.startswith("[Completada]"):
                self.tareas[indice_tarea] = f"[Completada] {tarea}"
                self.actualizar_lista_de_tareas()

    def actualizar_lista_de_tareas(self):
        self.lista_tareas.delete(0, tk.END)
        for tarea in self.tareas:
            if tarea.startswith("[Completada]"):
                self.lista_tareas.insert(tk.END, tarea)
                self.lista_tareas.itemconfig(tk.END, {'bg':'#d5dbdb'})
            else:
                self.lista_tareas.insert(tk.END, tarea)

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaDeTareas(root)
    root.mainloop()
