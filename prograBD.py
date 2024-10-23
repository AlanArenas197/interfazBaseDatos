import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import psycopg2

#WARN: https://github.com/AlanArenas197/interfazBaseDatos

class Connexion:
    def __init__(self):
        self.user = "root"
        self.password = ""
        self.database = "dbDiagnostico"
        self.host = "localhost"
        self.conn = None
    
    def open(self):
        try:
            self.conn = psycopg2.connect(
                database = self.database,
                host = self.host,
                user = self.user,
                passwd=self.password
            )
            return self.conn
        except:
            messagebox.showerror("Error de la conexión", "No se pudo conectar a la base de datos")
            return None
    
    def close(self):
        if self.conn:
            self.conn.close()

class LoginWindow(tk.Toplevel):
    def __init__(self, mainWin):
        super().__init__(mainWin)
        self.title("Inicio de sesión")
        self.geometry("400x250")

        ttk.Label(self, text = "Usuario").pack(pady=10)
        self.userEntry = ttk.Entry(self)
        self.userEntry.pack(pady=1)

        ttk.Label(self, text="Password:").pack(pady=10)
        self.passEntry = ttk.Entry(self, show="*")
        self.passEntry.pack(pady=1)

        self.logBtn = ttk.Button(self, text="Aceptar", command=self.veriLogin)
        self.logBtn.pack(pady=20)

        self.canBtn = ttk.Button(self, text="Cancelar", command=self.cancelLog)
        self.canBtn.pack(pady=1)

    def veriLogin(self):
        user = self.userEntry.get()
        passw = self.passEntry.get()

        if (user == 'admin' and passw == '1234') or (user == 'dev' and passw == '1'):
            self.destroy()
            root.deiconify()
            app = Application(root, user)
        else:
            messagebox.showerror("Error", "Usuario y/o Contraseña incorrecto(s)")

    def cancelLog(self):
        self.userEntry.delete(0, 'end')
        self.passEntry.delete(0, 'end')

class Application(ttk.Frame):
    def __init__(self, mainWin, user):
        super().__init__(mainWin)
        
        mainWin.title("Sistema MediSys")
        
        mainWin.geometry("750x450")
        self.notebook = ttk.Notebook(self)

        #-----------------------EMPLEADOS-----------------------#

        pestanaEmpleado = ttk.Frame(self.notebook)
        pestanaEmpleado.grid_columnconfigure(0, weight=1)
        pestanaEmpleado.grid_columnconfigure(1, weight=1)

        ttk.Label(pestanaEmpleado, text="Ingrese ID a buscar:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        txIdBuscar = ttk.Entry(pestanaEmpleado, width=30)
        txIdBuscar.grid(row=0, column=1, padx=10, pady=10)

        btnBuscar = ttk.Button(pestanaEmpleado, text="Buscar")
        btnBuscar.grid(row=0, column=2, padx=10, pady=10)

        ttk.Label(pestanaEmpleado, text="Nombre:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        txNombre = ttk.Entry(pestanaEmpleado, width=30)
        txNombre.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(pestanaEmpleado, text="Dirección:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        txCorreo = ttk.Entry(pestanaEmpleado, width=30)
        txCorreo.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(pestanaEmpleado, text="Teléfono:").grid(row=2, column=2, padx=10, pady=5, sticky="e")
        txTelefono = ttk.Entry(pestanaEmpleado, width=30)
        txTelefono.grid(row=2, column=3, padx=10, pady=5)

        ttk.Label(pestanaEmpleado, text="Fecha de Nac.:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        txFechaNac = ttk.Entry(pestanaEmpleado, width=30)
        txFechaNac.grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(pestanaEmpleado, text="Sexo:").grid(row=3, column=2, padx=10, pady=5, sticky="e")
        txSexo = ttk.Entry(pestanaEmpleado, width=30)
        txSexo.grid(row=3, column=3, padx=10, pady=5)

        ttk.Label(pestanaEmpleado, text="Sueldo:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        txSueldo = ttk.Entry(pestanaEmpleado, width=30)
        txSueldo.grid(row=4, column=1, padx=10, pady=5)

        ttk.Label(pestanaEmpleado, text="Turno:").grid(row=4, column=2, padx=10, pady=5, sticky="e")
        txTurno = ttk.Entry(pestanaEmpleado, width=30)
        txTurno.grid(row=4, column=3, padx=10, pady=5)

        ttk.Label(pestanaEmpleado, text="Contraseña:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
        txPassword = ttk.Entry(pestanaEmpleado, width=30)
        txPassword.grid(row=5, column=1, padx=10, pady=5)

        btnNuevoUsuario = ttk.Button(pestanaEmpleado, text="Nuevo")
        btnNuevoUsuario.grid(row=7, column=0, padx=10, pady=10, sticky="e")

        btnGuardarUsuario = ttk.Button(pestanaEmpleado, text="Guardar")
        btnGuardarUsuario.grid(row=7, column=1, padx=10, pady=10, sticky="w")

        btnCancelarUsuario = ttk.Button(pestanaEmpleado, text="Cancelar")
        btnCancelarUsuario.grid(row=7, column=2, padx=10, pady=10, sticky="w")

        btnEditarUsuario = ttk.Button(pestanaEmpleado, text="Editar")
        btnEditarUsuario.grid(row=7, column=3, padx=10, pady=10, sticky="w")

        btnEliminarUsuario = ttk.Button(pestanaEmpleado, text="Eliminar")
        btnEliminarUsuario.grid(row=7, column=4, padx=10, pady=10, sticky="w")

        self.notebook.add(pestanaEmpleado, text="Emplados")

        #-----------------------DOCTORES-----------------------#

        pestanaDoctores = ttk.Frame(self.notebook)
        pestanaDoctores.grid_columnconfigure(0, weight=1)
        pestanaDoctores.grid_columnconfigure(1, weight=1)

        ttk.Label(pestanaDoctores, text="PESTAÑA DE DOCTORES").grid(row=0, column=0, padx=10, pady=10, sticky="e")


        self.notebook.add(pestanaDoctores, text="Doctores")

        #-----------------------PACIENTES-----------------------#

        pestanaPacientes = ttk.Frame(self.notebook)
        pestanaPacientes.grid_columnconfigure(0, weight=1)
        pestanaPacientes.grid_columnconfigure(1, weight=1)

        ttk.Label(pestanaPacientes, text="PESTAÑA DE PACIENTES").grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.notebook.add(pestanaPacientes, text="Pacientes")

        #-----------------------CITAS-----------------------#

        pestanaCitas = ttk.Frame(self.notebook)
        pestanaCitas.grid_columnconfigure(0, weight=1)
        pestanaCitas.grid_columnconfigure(1, weight=1)

        ttk.Label(pestanaCitas, text="PESTAÑA DE CITAS").grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.notebook.add(pestanaCitas, text="Citas")

        #-----------------------CONFG DEL NOTEBOOK-----------------------#

        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)
        self.pack()

        #-----------------------IMAGEN-----------------------#

        self.addLogo(mainWin)

        #-----------------------CONFG DE LA IMAGEN-----------------------#
        
    def addLogo(self, mainWin):
        currentDir = os.path.dirname(os.path.abspath(__file__))
        logoDireccion = os.path.join(currentDir, 'imagenes', 'logo.png')

        image = Image.open(logoDireccion)
        image = image.resize((120, 50))

        self.logo = ImageTk.PhotoImage(image)

        logoLabel = tk.Label(mainWin, image=self.logo)
        logoLabel.pack(side="bottom", pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    login = LoginWindow(root)
    root.mainloop()