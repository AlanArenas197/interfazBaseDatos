import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import psycopg2

#WARN: https://github.com/AlanArenas197/interfazBaseDatos

class Connection:   #? Se modificó el nombre de la clase 'Connection'.
    def __init__(self):
        self.user = "postgres"          #? Se modificó el nombre de 'root' a 'postgres'.
        self.password = "dev"           #? Password del alumno 'Arenas Venegas Alan Marcel'. (CAMBIAR SI ES NECESARIO)
        self.database = "dbDiagnostico" #? Nombre de la base de datos.
        self.host = "localhost"         #? Hosting del servidor PostgreSQL.
        self.conn = None
    
    def open(self):
        try:
            self.conn = psycopg2.connect(   #? Función para conectarse desde el código Python, hacia el servidor PostgreSQL.
                database = self.database,
                host = self.host,
                user = self.user,
                password =self.password
            )
            return self.conn
        except:
            messagebox.showerror("Error de la conexión", "No se pudo conectar a la base de datos")  #? Mensaje de error si no se encuentra/conecta a la base de datos
            return None
    
    def close(self):
        if self.conn:
            self.conn.close()

    #? Se agregó las funciones CRUD.
    #!---------------------EMPLEADOS---------------------#

    def saveEmpleado(self, codigo, nombre, direccion, telefono, fecha_nac, sexo, sueldo, turno, contrasenia):
        try:
            conn = self.open()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO empleados (codigo, nombre, direccion, telefono, fecha_nac, sexo, sueldo, turno, contrasenia)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (codigo, nombre, direccion, telefono, fecha_nac, sexo, sueldo, turno, contrasenia))
            conn.commit()
            cur.close()
            messagebox.showinfo("Éxito", "Empleado insertado correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo insertar el empleado: {e}")
        finally:
            self.close()

    def updateEmplado(self, codigo, nombre, direccion, telefono, fecha_nac, sexo, sueldo, turno, contrasenia):
        try:
            conn = self.open()
            cur = conn.cursor()
            cur.execute("""
                UPDATE empleados SET nombre=%s, direccion=%s, telefono=%s, fecha_nac=%s, sexo=%s, sueldo=%s, turno=%s, contrasenia=%s
                WHERE codigo=%s
            """, (nombre, direccion, telefono, fecha_nac, sexo, sueldo, turno, contrasenia, codigo))
            conn.commit()
            cur.close()
            messagebox.showinfo("Éxito", "Empleado actualizado correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo actualizar el empleado: {e}")
        finally:
            self.close()

    def searchEmpleado(self, codigo):
        try:
            conn = self.open()
            cur = conn.cursor()
            cur.execute("SELECT * FROM empleados WHERE codigo = %s", (codigo,))
            empleado = cur.fetchone()
            cur.close()
            return empleado
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo buscar el empleado: {e}")
        finally:
            self.close()
    
    def deleteEmpleado(self, codigo):
        try:
            conn = self.open()
            cur = conn.cursor()
            cur.execute("DELETE FROM empleados WHERE codigo = %s", (codigo,))
            conn.commit()
            cur.close()
            messagebox.showinfo("Éxito", "Empleado eliminado correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar el empleado: {e}")
        finally:
            self.close()

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
        
        mainWin.geometry("1500x700")    #? Se modificó las dimensiones de la ventana principal
        self.notebook = ttk.Notebook(self)

        #-----------------------EMPLEADOS-----------------------#

        pestanaEmpleado = ttk.Frame(self.notebook)
        pestanaEmpleado.grid_columnconfigure(0, weight=1)
        pestanaEmpleado.grid_columnconfigure(1, weight=1)

        ttk.Label(pestanaEmpleado, text="Ingrese ID a buscar:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.txIdBuscar = ttk.Entry(pestanaEmpleado, width=30)
        self.txIdBuscar.grid(row=0, column=1, padx=10, pady=10)

        self.btnBuscar = ttk.Button(pestanaEmpleado, text="Buscar", command=self.buscarEmpleado)
        self.btnBuscar.grid(row=0, column=2, padx=10, pady=10)

        ttk.Label(pestanaEmpleado, text="ID:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.txID = ttk.Entry(pestanaEmpleado, width=15)
        self.txID.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(pestanaEmpleado, text="Nombre:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.txNombre = ttk.Entry(pestanaEmpleado, width=30)
        self.txNombre.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(pestanaEmpleado, text="Dirección:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.txDireccion = ttk.Entry(pestanaEmpleado, width=30)
        self.txDireccion.grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(pestanaEmpleado, text="Teléfono:").grid(row=3, column=2, padx=10, pady=5, sticky="e")
        self.txTelefono = ttk.Entry(pestanaEmpleado, width=30)
        self.txTelefono.grid(row=3, column=3, padx=10, pady=5)

        ttk.Label(pestanaEmpleado, text="Fecha de Nac.:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.txFechaNac = ttk.Entry(pestanaEmpleado, width=30)
        self.txFechaNac.grid(row=4, column=1, padx=10, pady=5)

        ttk.Label(pestanaEmpleado, text="Sexo:").grid(row=4, column=2, padx=10, pady=5, sticky="e")
        self.txSexo = ttk.Entry(pestanaEmpleado, width=30)
        self.txSexo.grid(row=4, column=3, padx=10, pady=5)

        ttk.Label(pestanaEmpleado, text="Sueldo:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.txSueldo = ttk.Entry(pestanaEmpleado, width=30)
        self.txSueldo.grid(row=5, column=1, padx=10, pady=5)

        ttk.Label(pestanaEmpleado, text="Turno:").grid(row=5, column=2, padx=10, pady=5, sticky="e")
        self.txTurno = ttk.Entry(pestanaEmpleado, width=30)
        self.txTurno.grid(row=5, column=3, padx=10, pady=5)

        ttk.Label(pestanaEmpleado, text="Contraseña:").grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.txPassword = ttk.Entry(pestanaEmpleado, width=30)
        self.txPassword.grid(row=6, column=1, padx=10, pady=5)

        self.btnNuevoUsuario = ttk.Button(pestanaEmpleado, text="Nuevo", command=self.limpiarDatos)
        self.btnNuevoUsuario.grid(row=8, column=0, padx=10, pady=10, sticky="e")

        self.btnGuardarUsuario = ttk.Button(pestanaEmpleado, text="Guardar", command=self.guardarEmpleado)
        self.btnGuardarUsuario.grid(row=8, column=1, padx=10, pady=10, sticky="w")

        self.btnCancelarUsuario = ttk.Button(pestanaEmpleado, text="Cancelar", command=self.limpiarDatos)
        self.btnCancelarUsuario.grid(row=8, column=2, padx=10, pady=10, sticky="w")

        self.btnEditarUsuario = ttk.Button(pestanaEmpleado, text="Editar", command=self.actualizarEmpleado)
        self.btnEditarUsuario.grid(row=8, column=3, padx=10, pady=10, sticky="w")

        self.btnEliminarUsuario = ttk.Button(pestanaEmpleado, text="Eliminar", command=self.eliminarEmpleado)
        self.btnEliminarUsuario.grid(row=8, column=4, padx=10, pady=10, sticky="w")

        ttk.Label(pestanaEmpleado, text="EMPLADOS:").grid(row=10, column=0, padx=10, pady=10, sticky="e")
        self.btnMostrarEmpleados = ttk.Button(pestanaEmpleado, text="Mostrar")
        self.btnMostrarEmpleados.grid(row=10, column=1, padx=10, pady=10)

        self.treeEmpleados = ttk.Treeview(self, columns=("codigo", "nombre", "direccion", "telefono", "fecha_nac", "sexo", "sueldo", "turno", "contrasenia"), show="headings", height=3)
        self.treeEmpleados.grid(row=11, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        self.treeEmpleados.column("codigo", width=50)
        self.treeEmpleados.heading("codigo", text="Codigo")

        self.treeEmpleados.column("nombre", width=100)
        self.treeEmpleados.heading("nombre", text="Nombre")

        self.treeEmpleados.column("direccion", width=150)
        self.treeEmpleados.heading("direccion", text="Direccion")

        self.treeEmpleados.column("telefono", width=80)
        self.treeEmpleados.heading("telefono", text="Tel")

        self.treeEmpleados.column("fecha_nac", width=90)
        self.treeEmpleados.heading("fecha_nac", text="Fech. Nac")

        self.treeEmpleados.column("sexo", width=50)
        self.treeEmpleados.heading("sexo", text="Sexo")

        self.treeEmpleados.column("sueldo", width=80)
        self.treeEmpleados.heading("sueldo", text="Sueldo")

        self.treeEmpleados.column("turno", width=60)
        self.treeEmpleados.heading("turno", text="Turno")

        self.treeEmpleados.column("contrasenia", width=100)
        self.treeEmpleados.heading("contrasenia", text="Contra")

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

        self.notebook.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
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
    
    #-----------------------CONFG DEL CRUD-----------------------#

    def limpiarDatos(self):
        self.txID.delete(0, 'end')
        self.txNombre.delete(0, 'end')
        self.txDireccion.delete(0, 'end')
        self.txTelefono.delete(0, 'end')
        self.txFechaNac.delete(0, 'end')
        self.txSexo.delete(0, 'end')
        self.txSueldo.delete(0, 'end')
        self.txTurno.delete(0, 'end')
        self.txPassword.delete(0, 'end')
    
    def guardarEmpleado(self):
        conexion = Connection()
        conexion.saveEmpleado(
            self.txID.get(),
            self.txNombre.get(),
            self.txDireccion.get(),
            self.txTelefono.get(),
            self.txFechaNac.get(),
            self.txSexo.get(),
            self.txSueldo.get(),
            self.txTurno.get(),
            self.txPassword.get()
        )
    
    def actualizarEmpleado(self):
        conexion = Connection()
        conexion.updateEmplado(
            self.txID.get(),
            self.txNombre.get(),
            self.txDireccion.get(),
            self.txTelefono.get(),
            self.txFechaNac.get(),
            self.txSexo.get(),
            self.txSueldo.get(),
            self.txTurno.get(),
            self.txPassword.get()
        )
    
    def eliminarEmpleado(self):
        conexion = Connection()
        conexion.deleteEmpleado(self.txIdBuscar.get())
    
    def buscarEmpleado(self):
        conexion = Connection()
        empleado = conexion.searchEmpleado(self.txIdBuscar.get())
        if empleado:
            self.txID.insert(0, empleado[0])
            self.txNombre.insert(0, empleado[1])
            self.txDireccion.insert(0, empleado[2])
            self.txTelefono.insert(0, empleado[3])
            self.txFechaNac.insert(0, empleado[4])
            self.txSexo.insert(0, empleado[5])
            self.txSueldo.insert(0, empleado[6])
            self.txTurno.insert(0, empleado[7])
            self.txPassword.insert(0, empleado[8])
        else:
            messagebox.showerror("Error", "¡Empleado no encontrado!")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    login = LoginWindow(root)
    root.mainloop()