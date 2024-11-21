#Equipo #1
#ALCOCER CAMARENA CHRISTOPHER
#ALVIS BENITEZ MARIA MONICA
#ARCE ZARAGOZA LUIS GILBERTO
#ARENAS VENEGAS ALAN MARCEL
#SECCIÓN: D02
#CALENDARIO: 2024B

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from docx.shared import Pt
from fpdf import FPDF
import os
import psycopg2
import dotenv

dotenv.load_dotenv()

#WARN: https://github.com/AlanArenas197/interfazBaseDatos

class Connection:   #? Se modificó el nombre de la clase 'Connection' con el .env.
    def __init__(self):
        #? Si no se encuentran variables en el archivo '.env.example', esas variables se meten por defecto.
        self.user = os.getenv("DB_USER", "postgres")
        self.password = os.getenv("DB_PASSWORD", "dev")
        self.database = os.getenv("DB_NAME", "dbDiagnostico")
        self.host = os.getenv("DB_HOST", "localhost")
        self.conn = None
    
    def open(self):
        try:
            self.conn = psycopg2.connect(
                database = self.database,
                host = self.host,
                user = self.user,
                password =self.password
            )
            return self.conn
        except:
            messagebox.showerror("Error de la conexión", "No se pudo conectar a la base de datos")
            return None
    
    def close(self):
        if self.conn:
            self.conn.close()

    #? Se agregó la función de Login en el programa.
    #!---------------------LOG-IN---------------------#

    def verifyUsers(self, codigo, contrasenia):
        conn = self.open()
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT codigo, nombre FROM empleados WHERE codigo = %s AND contrasenia = %s", (codigo, contrasenia))
            empleado = cur.fetchone()  #? Devuelve el código y nombre del empleado si es válido
            if not empleado: 
                cur.execute("SELECT codigo, nombre FROM doctores WHERE codigo = %s AND contrasenia = %s", (codigo, contrasenia)) 
                empleado = cur.fetchone()
            cur.close()                
            self.close()
            return empleado  #? Retornará el codigo y nombre si es que existe
        return None

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

    #!---------------------DOCTORES---------------------#

    def saveDoctor(self, codigo, nombre, direccion, telefono, fecha_nac, sexo, especialidad, contrasenia):
        try:
            conn = self.open()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO doctores (codigo, nombre, direccion, telefono, fecha_nac, sexo, especialidad, contrasenia)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (codigo, nombre, direccion, telefono, fecha_nac, sexo, especialidad, contrasenia))
            conn.commit()
            cur.close()
            messagebox.showinfo("Éxito", "Doctor insertado correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo insertar el doctor: {e}")
        finally:
            self.close()

    def updateDoctor(self, codigo, nombre, direccion, telefono, fecha_nac, sexo, especialidad, contrasenia):
        try:
            conn = self.open()
            cur = conn.cursor()
            cur.execute("""
                UPDATE doctores SET nombre=%s, direccion=%s, telefono=%s, fecha_nac=%s, sexo=%s, especialidad=%s, contrasenia=%s
                WHERE codigo=%s
            """, (nombre, direccion, telefono, fecha_nac, sexo, especialidad, contrasenia, codigo))
            conn.commit()
            cur.close()
            messagebox.showinfo("Éxito", "Doctor actualizado correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo actualizar el doctor: {e}")
        finally:
            self.close()

    def searchDoctor(self, codigo):
        try:
            conn = self.open()
            cur = conn.cursor()
            cur.execute("SELECT * FROM doctores WHERE codigo = %s", (codigo,))
            doctor = cur.fetchone()
            cur.close()
            return doctor
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo buscar el doctor: {e}")
        finally:
            self.close()
    
    def deleteDoctor(self, codigo):
        try:
            conn = self.open()
            cur = conn.cursor()
            cur.execute("DELETE FROM doctores WHERE codigo = %s", (codigo,))
            conn.commit()
            cur.close()
            messagebox.showinfo("Éxito", "Doctor eliminado correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar el doctor: {e}")
        finally:
            self.close()

    #!---------------------PACIENTES---------------------#

    def savePaciente(self, codigo, nombre, direccion, telefono, fecha_nac, sexo, edad, estatura):
        try:
            conn = self.open()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO pacientes (codigo, nombre, direccion, telefono, fecha_nac, sexo, edad, estatura)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (codigo, nombre, direccion, telefono, fecha_nac, sexo, edad, estatura))
            conn.commit()
            cur.close()
            messagebox.showinfo("Éxito", "Paciente insertado correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo insertar el paciente: {e}")
        finally:
            self.close()

    def updatePaciente(self, codigo, nombre, direccion, telefono, fecha_nac, sexo, edad, estatura):
        try:
            conn = self.open()
            cur = conn.cursor()
            cur.execute("""
                UPDATE pacientes SET nombre=%s, direccion=%s, telefono=%s, fecha_nac=%s, sexo=%s, edad=%s, estatura=%s
                WHERE codigo=%s
            """, (nombre, direccion, telefono, fecha_nac, sexo, edad, estatura, codigo))
            conn.commit()
            cur.close()
            messagebox.showinfo("Éxito", "Paciente actualizado correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo actualizar el paciente: {e}")
        finally:
            self.close()

    def searchPaciente(self, codigo):
        try:
            conn = self.open()
            cur = conn.cursor()
            cur.execute("SELECT * FROM pacientes WHERE codigo = %s", (codigo,))
            doctor = cur.fetchone()
            cur.close()
            return doctor
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo buscar el paciente: {e}")
        finally:
            self.close()
    
    def deletePaciente(self, codigo):
        try:
            conn = self.open()
            cur = conn.cursor()
            cur.execute("DELETE FROM pacientes WHERE codigo = %s", (codigo,))
            conn.commit()
            cur.close()
            messagebox.showinfo("Éxito", "Paciente eliminado correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar el paciente: {e}")
        finally:
            self.close()
    
    #!---------------------CITAS---------------------#

    def saveCita(self, codigo, paciente_id, doctor_id, dia, hora):
        try:
            conn = self.open()
            cur = conn.cursor()

            #CHECAR DISPONIBILIDAD
            cur.execute("""
                SELECT * FROM citas 
                WHERE (paciente_id = %s OR doctor_id = %s) AND dia = %s AND hora = %s
            """, (paciente_id, doctor_id, dia, hora))
            if cur.fetchone():
                messagebox.showerror("Error", "Conflicto de horarios: el paciente o doctor ya tiene una cita en esta fecha y hora.")
                return

            cur.execute("""
                INSERT INTO citas (codigo, paciente_id, doctor_id, dia, hora) 
                VALUES (%s, %s, %s, %s, %s)
            """, (codigo, paciente_id, doctor_id, dia, hora))
            conn.commit()
            cur.close()
            messagebox.showinfo("Éxito", "Cita guardada correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar la cita: {e}")
        finally:
            self.close()

    def updateCita(self, codigo, paciente_id, doctor_id, dia, hora):
        try:
            conn = self.open()
            cur = conn.cursor()
            cur.execute("""
                SELECT * FROM citas 
                WHERE (paciente_id = %s OR doctor_id = %s) AND dia = %s AND hora = %s AND codigo != %s
            """, (paciente_id, doctor_id, dia, hora, codigo))
            if cur.fetchone():
                messagebox.showerror("Error", "Conflicto de horarios: el paciente o doctor ya tiene una cita en esta fecha y hora.")
                return

            cur.execute("""
                UPDATE citas SET paciente_id=%s, doctor_id=%s, dia=%s, hora=%s
                WHERE codigo=%s
            """, (paciente_id, doctor_id, dia, hora, codigo))
            conn.commit()
            cur.close()
            messagebox.showinfo("Éxito", "Cita actualizada correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo actualizar la cita: {e}")
        finally:
            self.close()
            
    def searchCita(self, codigo):
        try:
            conn = self.open()
            cur = conn.cursor()
            cur.execute("SELECT * FROM citas WHERE codigo = %s", (codigo,))
            cita = cur.fetchone()
            cur.close()
            return cita
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo buscar la cita: {e}")
        finally:
            self.close()

    def deleteCita(self, codigo):
        try:
            conn = self.open()
            cur = conn.cursor()
            
            cur.execute("DELETE FROM citas WHERE codigo = %s", (codigo,))
            conn.commit()
            
            cur.close()
            messagebox.showinfo("Éxito", "Cita eliminada correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar la cita: {e}")
        finally:
            self.close()
    
    #!---------------------MEDICAMENTOS---------------------#

    def saveMedicina(self, codigo, nombre, via_admin, presentacion, fecha_cad):
        try:
            conn = self.open()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO medicamentos (codigo, nombre, via_admin, presentacion, fecha_cad)
                VALUES (%s, %s, %s, %s, %s)
            """, (codigo, nombre, via_admin, presentacion, fecha_cad))
            conn.commit()
            cur.close()
            messagebox.showinfo("Éxito", "Medicamento insertado correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo insertar el medicamento: {e}")
        finally:
            self.close()

    def updateMedicina(self, codigo, nombre, via_admin, presentacion, fecha_cad):
        try:
            conn = self.open()
            cur = conn.cursor()
            cur.execute("""
                UPDATE medicamentos SET nombre=%s, via_admin=%s, presentacion=%s, fecha_cad=%s
                WHERE codigo=%s
            """, (nombre, via_admin, presentacion, fecha_cad, codigo))
            conn.commit()
            cur.close()
            messagebox.showinfo("Éxito", "Medicamento actualizado correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo actualizar el medicamento: {e}")
        finally:
            self.close()

    def searchMedicina(self, codigo):
        try:
            conn = self.open()
            cur = conn.cursor()
            cur.execute("SELECT * FROM medicamentos WHERE codigo = %s", (codigo,))
            doctor = cur.fetchone()
            cur.close()
            return doctor
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo buscar el medicamento: {e}")
        finally:
            self.close()
    
    def deleteMedicina(self, codigo):
        try:
            conn = self.open()
            cur = conn.cursor()
            cur.execute("DELETE FROM medicamentos WHERE codigo = %s", (codigo,))
            conn.commit()
            cur.close()
            messagebox.showinfo("Éxito", "Medicamento eliminado correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar el medicamento: {e}")
        finally:
            self.close()

    #!---------------------CONSULTAS---------------------#

    def saveConsulta(self, codigo, id_cita, diagnostico, id_medicamento):
        try:
            conn = self.open()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO consultas (codigo, id_cita, diagnostico, id_medicamento)
                VALUES (%s, %s, %s, %s)
            """, (codigo, id_cita, diagnostico, id_medicamento))
            conn.commit()
            cur.close()
            messagebox.showinfo("Éxito", "Consulta insertado correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo insertar la consulta: {e}")
        finally:
            self.close()

    def updateConsulta(self, codigo, id_cita, diagnostico, id_medicamento):
        try:
            conn = self.open()
            cur = conn.cursor()
            cur.execute("""
                UPDATE consultas SET id_cita=%s, diagnostico=%s, id_medicamento=%s
                WHERE codigo=%s
            """, (id_cita, diagnostico, id_medicamento, codigo))
            conn.commit()
            cur.close()
            messagebox.showinfo("Éxito", "Consulta actualizada correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo actualizar la consulta: {e}")
        finally:
            self.close()

    def searchConsulta(self, codigo):
        try:
            conn = self.open()
            cur = conn.cursor()
            cur.execute("SELECT * FROM consultas WHERE codigo = %s", (codigo,))
            doctor = cur.fetchone()
            cur.close()
            return doctor
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo buscar la consulta: {e}")
        finally:
            self.close()
    
    def deleteConsulta(self, codigo):
        try:
            conn = self.open()
            cur = conn.cursor()
            cur.execute("DELETE FROM consultas WHERE codigo = %s", (codigo,))
            conn.commit()
            cur.close()
            messagebox.showinfo("Éxito", "Consulta eliminada correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar la consulta: {e}")
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
        codigo = self.userEntry.get()
        contrasenia = self.passEntry.get()

        if codigo == 'admin' and contrasenia == '1234':
            self.destroy()
            root.deiconify()
            app = Application(root, codigo, "Administrador")
        else:
            conexion = Connection()
            empleado = conexion.verifyUsers(codigo, contrasenia)
            
            if empleado:
                codigo, nombre = empleado
                self.destroy()
                root.deiconify()
                app = Application(root, codigo, nombre)
            else:
                messagebox.showerror("Error", "Usuario y/o Contraseña incorrecto(s)")

    def cancelLog(self):
        self.userEntry.delete(0, 'end')
        self.passEntry.delete(0, 'end')

class Application(ttk.Frame):
    def __init__(self, mainWin, codigo, nombre):
        super().__init__(mainWin)
        
        mainWin.title(f"Sistema MediSys - Hola {nombre}")
        
        screen_width = mainWin.winfo_screenwidth()
        screen_height = mainWin.winfo_screenheight()
        
        mainWin.geometry(f"{screen_width}x{screen_height}")    #? Se modificó las dimensiones de la ventana principal a pantalla completa
        self.notebook = ttk.Notebook(self)

        #-----------------------EMPLEADOS-----------------------#

        pestanaEmpleado = ttk.Frame(self.notebook)
        pestanaEmpleado.grid_columnconfigure(0, weight=1)
        pestanaEmpleado.grid_columnconfigure(1, weight=1)

        ttk.Label(pestanaEmpleado, text="Ingrese Codigo:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.txIdBuscar = ttk.Entry(pestanaEmpleado, width=30)
        self.txIdBuscar.grid(row=0, column=1, padx=10, pady=10)

        self.btnBuscar = ttk.Button(pestanaEmpleado, text="Buscar", command=self.buscarEmpleado)
        self.btnBuscar.grid(row=0, column=2, padx=10, pady=10)

        ttk.Label(pestanaEmpleado, text="Codigo:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.txID = ttk.Entry(pestanaEmpleado, width=15)
        self.txID.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(pestanaEmpleado, text="Nombre:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.txNombre = ttk.Entry(pestanaEmpleado, width=45)
        self.txNombre.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(pestanaEmpleado, text="Dirección:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.txDireccion = ttk.Entry(pestanaEmpleado, width=45)
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

        ttk.Label(pestanaEmpleado, text="EMPLEADOS:").grid(row=10, column=0, padx=10, pady=10, sticky="e")
        self.btnMostrarEmpleados = ttk.Button(pestanaEmpleado, text="Mostrar", command=self.mostrarTodosEmpleados)
        self.btnMostrarEmpleados.grid(row=10, column=1, padx=10, pady=10)

        self.treeEmpleados = ttk.Treeview(pestanaEmpleado, columns=("codigo", "nombre", "direccion", "telefono", "fecha_nac", "sexo", "sueldo", "turno", "contrasenia"), show="headings", height=14)
        self.treeEmpleados.grid(row=11, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        self.treeEmpleados.column("codigo", width=50)
        self.treeEmpleados.heading("codigo", text="Codigo")

        self.treeEmpleados.column("nombre", width=250)
        self.treeEmpleados.heading("nombre", text="Nombre")

        self.treeEmpleados.column("direccion", width=150)
        self.treeEmpleados.heading("direccion", text="Direccion")

        self.treeEmpleados.column("telefono", width=100)
        self.treeEmpleados.heading("telefono", text="Tel")

        self.treeEmpleados.column("fecha_nac", width=100)
        self.treeEmpleados.heading("fecha_nac", text="Fech. Nac")

        self.treeEmpleados.column("sexo", width=80)
        self.treeEmpleados.heading("sexo", text="Sexo")

        self.treeEmpleados.column("sueldo", width=80)
        self.treeEmpleados.heading("sueldo", text="Sueldo")

        self.treeEmpleados.column("turno", width=80)
        self.treeEmpleados.heading("turno", text="Turno")

        self.treeEmpleados.column("contrasenia", width=100)
        self.treeEmpleados.heading("contrasenia", text="Contra")

        if nombre == "Administrador":
            self.notebook.add(pestanaEmpleado, text="Emplados")

        #-----------------------DOCTORES-----------------------#

        pestanaDoctores = ttk.Frame(self.notebook)
        pestanaDoctores.grid_columnconfigure(0, weight=1)
        pestanaDoctores.grid_columnconfigure(1, weight=1)

        ttk.Label(pestanaDoctores, text="Ingrese Codigo:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.txIdDoctorBuscar = ttk.Entry(pestanaDoctores, width=30)
        self.txIdDoctorBuscar.grid(row=0, column=1, padx=10, pady=10)

        self.btnBuscarDoctor = ttk.Button(pestanaDoctores, text="Buscar", command=self.buscarDoctor)
        self.btnBuscarDoctor.grid(row=0, column=2, padx=10, pady=10)

        ttk.Label(pestanaDoctores, text="Codigo:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.txIDDoctor = ttk.Entry(pestanaDoctores, width=15)
        self.txIDDoctor.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(pestanaDoctores, text="Nombre:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.txNombreDoctor = ttk.Entry(pestanaDoctores, width=45)
        self.txNombreDoctor.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(pestanaDoctores, text="Dirección:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.txDireccionDoctor = ttk.Entry(pestanaDoctores, width=45)
        self.txDireccionDoctor.grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(pestanaDoctores, text="Teléfono:").grid(row=3, column=2, padx=10, pady=5, sticky="e")
        self.txTelefonoDoctor = ttk.Entry(pestanaDoctores, width=30)
        self.txTelefonoDoctor.grid(row=3, column=3, padx=10, pady=5)

        ttk.Label(pestanaDoctores, text="Fecha de Nac.:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.txFechaNacDoctor = ttk.Entry(pestanaDoctores, width=30)
        self.txFechaNacDoctor.grid(row=4, column=1, padx=10, pady=5)

        ttk.Label(pestanaDoctores, text="Sexo:").grid(row=4, column=2, padx=10, pady=5, sticky="e")
        self.txSexoDoctor = ttk.Entry(pestanaDoctores, width=30)
        self.txSexoDoctor.grid(row=4, column=3, padx=10, pady=5)

        ttk.Label(pestanaDoctores, text="Especialidad:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.txEspecialidadDoctor = ttk.Entry(pestanaDoctores, width=30)
        self.txEspecialidadDoctor.grid(row=5, column=1, padx=10, pady=5)

        ttk.Label(pestanaDoctores, text="Contraseña:").grid(row=5, column=2, padx=10, pady=5, sticky="e")
        self.txPasswordDoctor = ttk.Entry(pestanaDoctores, width=30)
        self.txPasswordDoctor.grid(row=5, column=3, padx=10, pady=5)

        self.btnNuevoDoctor = ttk.Button(pestanaDoctores, text="Nuevo", command=self.limpiarDatosDoctor)
        self.btnNuevoDoctor.grid(row=7, column=0, padx=10, pady=10, sticky="e")

        self.btnGuardarDoctor = ttk.Button(pestanaDoctores, text="Guardar", command=self.guardarDoctor)
        self.btnGuardarDoctor.grid(row=7, column=1, padx=10, pady=10, sticky="w")

        self.btnCancelarDoctor = ttk.Button(pestanaDoctores, text="Cancelar", command=self.limpiarDatosDoctor)
        self.btnCancelarDoctor.grid(row=7, column=2, padx=10, pady=10, sticky="w")

        self.btnEditarDoctor = ttk.Button(pestanaDoctores, text="Editar", command=self.actualizarDoctor)
        self.btnEditarDoctor.grid(row=7, column=3, padx=10, pady=10, sticky="w")

        self.btnEliminarDoctor = ttk.Button(pestanaDoctores, text="Eliminar", command=self.eliminarDoctor)
        self.btnEliminarDoctor.grid(row=7, column=4, padx=10, pady=10, sticky="w")

        ttk.Label(pestanaDoctores, text="DOCTORES:").grid(row=9, column=0, padx=10, pady=10, sticky="e")
        self.btnMostrarDoctores = ttk.Button(pestanaDoctores, text="Mostrar", command=self.mostrarTodosDoctor)
        self.btnMostrarDoctores.grid(row=9, column=1, padx=10, pady=10)

        self.treeDoctores = ttk.Treeview(pestanaDoctores, columns=("codigo", "nombre", "direccion", "telefono", "fecha_nac", "sexo", "especialidad", "contrasenia"), show="headings", height=14)
        self.treeDoctores.grid(row=10, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        self.treeDoctores.column("codigo", width=50)
        self.treeDoctores.heading("codigo", text="Codigo")

        self.treeDoctores.column("nombre", width=250)
        self.treeDoctores.heading("nombre", text="Nombre")

        self.treeDoctores.column("direccion", width=250)
        self.treeDoctores.heading("direccion", text="Direccion")

        self.treeDoctores.column("telefono", width=100)
        self.treeDoctores.heading("telefono", text="Tel")

        self.treeDoctores.column("fecha_nac", width=80)
        self.treeDoctores.heading("fecha_nac", text="Fech. Nac")

        self.treeDoctores.column("sexo", width=80)
        self.treeDoctores.heading("sexo", text="Sexo")

        self.treeDoctores.column("especialidad", width=100)
        self.treeDoctores.heading("especialidad", text="Especialidad")

        self.treeDoctores.column("contrasenia", width=80)
        self.treeDoctores.heading("contrasenia", text="Contra")

        if nombre == "Administrador":
            self.notebook.add(pestanaDoctores, text="Doctores")

        #-----------------------PACIENTES-----------------------#

        pestanaPacientes = ttk.Frame(self.notebook)
        pestanaPacientes.grid_columnconfigure(0, weight=1)
        pestanaPacientes.grid_columnconfigure(1, weight=1)

        ttk.Label(pestanaPacientes, text="Ingrese Codigo:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.txIdPacienteBuscar = ttk.Entry(pestanaPacientes, width=30)
        self.txIdPacienteBuscar.grid(row=0, column=1, padx=10, pady=10)

        self.btnBuscarPaciente = ttk.Button(pestanaPacientes, text="Buscar", command=self.buscarPaciente)
        self.btnBuscarPaciente.grid(row=0, column=2, padx=10, pady=10)

        ttk.Label(pestanaPacientes, text="Codigo:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.txIDPaciente = ttk.Entry(pestanaPacientes, width=15)
        self.txIDPaciente.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(pestanaPacientes, text="Nombre:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.txNombrePaciente = ttk.Entry(pestanaPacientes, width=45)
        self.txNombrePaciente.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(pestanaPacientes, text="Dirección:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.txDireccionPaciente = ttk.Entry(pestanaPacientes, width=45)
        self.txDireccionPaciente.grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(pestanaPacientes, text="Teléfono:").grid(row=3, column=2, padx=10, pady=5, sticky="e")
        self.txTelefonoPaciente = ttk.Entry(pestanaPacientes, width=30)
        self.txTelefonoPaciente.grid(row=3, column=3, padx=10, pady=5)

        ttk.Label(pestanaPacientes, text="Fecha de Nac.:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.txFechaNacPaciente = ttk.Entry(pestanaPacientes, width=30)
        self.txFechaNacPaciente.grid(row=4, column=1, padx=10, pady=5)

        ttk.Label(pestanaPacientes, text="Sexo:").grid(row=4, column=2, padx=10, pady=5, sticky="e")
        self.txSexoPaciente = ttk.Entry(pestanaPacientes, width=30)
        self.txSexoPaciente.grid(row=4, column=3, padx=10, pady=5)

        ttk.Label(pestanaPacientes, text="Edad:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.txEdadPaciente = ttk.Entry(pestanaPacientes, width=30)
        self.txEdadPaciente.grid(row=5, column=1, padx=10, pady=5)

        ttk.Label(pestanaPacientes, text="Estatura:").grid(row=5, column=2, padx=10, pady=5, sticky="e")
        self.txEstaturaPaciente = ttk.Entry(pestanaPacientes, width=30)
        self.txEstaturaPaciente.grid(row=5, column=3, padx=10, pady=5)

        self.btnNuevoPaciente = ttk.Button(pestanaPacientes, text="Nuevo", command=self.limpiarDatosPaciente)
        self.btnNuevoPaciente.grid(row=7, column=0, padx=10, pady=10, sticky="e")

        self.btnGuardarPaciente = ttk.Button(pestanaPacientes, text="Guardar", command=self.guardarPaciente)
        self.btnGuardarPaciente.grid(row=7, column=1, padx=10, pady=10, sticky="w")

        self.btnCancelarPaciente = ttk.Button(pestanaPacientes, text="Cancelar", command=self.limpiarDatosPaciente)
        self.btnCancelarPaciente.grid(row=7, column=2, padx=10, pady=10, sticky="w")

        self.btnEditarPaciente = ttk.Button(pestanaPacientes, text="Editar", command=self.actualizarPaciente)
        self.btnEditarPaciente.grid(row=7, column=3, padx=10, pady=10, sticky="w")

        self.btnEliminarPaciente = ttk.Button(pestanaPacientes, text="Eliminar", command=self.eliminarPaciente)
        self.btnEliminarPaciente.grid(row=7, column=4, padx=10, pady=10, sticky="w")

        ttk.Label(pestanaPacientes, text="PACIENTES:").grid(row=9, column=0, padx=10, pady=10, sticky="e")
        self.btnMostrarPacientes = ttk.Button(pestanaPacientes, text="Mostrar", command=self.mostrarTodosPaciente)
        self.btnMostrarPacientes.grid(row=9, column=1, padx=10, pady=10)

        self.treePacientes = ttk.Treeview(pestanaPacientes, columns=("codigo", "nombre", "direccion", "telefono", "fecha_nac", "sexo", "edad", "estatura"), show="headings", height=14)
        self.treePacientes.grid(row=10, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        self.treePacientes.column("codigo", width=50)
        self.treePacientes.heading("codigo", text="Codigo")

        self.treePacientes.column("nombre", width=250)
        self.treePacientes.heading("nombre", text="Nombre")

        self.treePacientes.column("direccion", width=250)
        self.treePacientes.heading("direccion", text="Direccion")

        self.treePacientes.column("telefono", width=100)
        self.treePacientes.heading("telefono", text="Tel")

        self.treePacientes.column("fecha_nac", width=80)
        self.treePacientes.heading("fecha_nac", text="Fech. Nac")

        self.treePacientes.column("sexo", width=80)
        self.treePacientes.heading("sexo", text="Sexo")

        self.treePacientes.column("edad", width=100)
        self.treePacientes.heading("edad", text="Edad")

        self.treePacientes.column("estatura", width=80)
        self.treePacientes.heading("estatura", text="Estat.")

        self.notebook.add(pestanaPacientes, text="Pacientes")

        #-----------------------CITAS-----------------------#

        pestanaCitas = ttk.Frame(self.notebook)
        pestanaCitas.grid_columnconfigure(0, weight=1)
        pestanaCitas.grid_columnconfigure(1, weight=1)

        ttk.Label(pestanaCitas, text="Ingrese Codigo:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.txIdCitaBuscar = ttk.Entry(pestanaCitas, width=30)
        self.txIdCitaBuscar.grid(row=0, column=1, padx=10, pady=10)

        self.btnBuscarCita = ttk.Button(pestanaCitas, text="Buscar", command=self.buscarCita)
        self.btnBuscarCita.grid(row=0, column=2, padx=10, pady=10)

        ttk.Label(pestanaCitas, text="Codigo:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.txIDCita = ttk.Entry(pestanaCitas, width=15)
        self.txIDCita.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(pestanaCitas, text="Paciente:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.comboPacienteCita = ttk.Combobox(pestanaCitas, values=self.obtenerPacientes(), width=30)
        self.comboPacienteCita.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(pestanaCitas, text="Doctores:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.comboDoctorCita = ttk.Combobox(pestanaCitas, values=self.obtenerDoctores(), width=30)
        self.comboDoctorCita.grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(pestanaCitas, text="Dia:").grid(row=3, column=2, padx=10, pady=5, sticky="e")
        self.txDiaCita = ttk.Entry(pestanaCitas, width=30)
        self.txDiaCita.grid(row=3, column=3, padx=10, pady=5)

        ttk.Label(pestanaCitas, text="Hora:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.txHoraCita = ttk.Entry(pestanaCitas, width=30)
        self.txHoraCita.grid(row=4, column=1, padx=10, pady=5)

        self.btnNuevoCita = ttk.Button(pestanaCitas, text="Nuevo", command=self.limpiarCamposCita)
        self.btnNuevoCita.grid(row=7, column=0, padx=10, pady=10, sticky="e")

        self.btnGuardarCita = ttk.Button(pestanaCitas, text="Guardar", command=self.guardarCita)
        self.btnGuardarCita.grid(row=7, column=1, padx=10, pady=10, sticky="w")

        self.btnCancelarCita = ttk.Button(pestanaCitas, text="Cancelar", command=self.limpiarCamposCita)
        self.btnCancelarCita.grid(row=7, column=2, padx=10, pady=10, sticky="w")

        self.btnEditarCita = ttk.Button(pestanaCitas, text="Editar", command=self.actualizarCita)
        self.btnEditarCita.grid(row=7, column=3, padx=10, pady=10, sticky="w")

        self.btnEliminarCita = ttk.Button(pestanaCitas, text="Eliminar", command=self.eliminarCita)
        self.btnEliminarCita.grid(row=7, column=4, padx=10, pady=10, sticky="w")

        ttk.Label(pestanaCitas, text="CITAS:").grid(row=9, column=0, padx=10, pady=10, sticky="e")
        self.btnMostrarCitas = ttk.Button(pestanaCitas, text="Mostrar", command=self.mostrarTodasCitas)
        self.btnMostrarCitas.grid(row=9, column=1, padx=10, pady=10)

        self.treeCitas = ttk.Treeview(pestanaCitas, columns=("codigo", "paciente", "doctor", "dia", "hora"), show="headings", height=14)
        self.treeCitas.grid(row=10, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        self.treeCitas.column("codigo", width=50)
        self.treeCitas.heading("codigo", text="Codigo")

        self.treeCitas.column("paciente", width=50)
        self.treeCitas.heading("paciente", text="ID Paciente")

        self.treeCitas.column("doctor", width=50)
        self.treeCitas.heading("doctor", text="ID Doctor")

        self.treeCitas.column("dia", width=100)
        self.treeCitas.heading("dia", text="Dia")

        self.treeCitas.column("hora", width=80)
        self.treeCitas.heading("hora", text="Hora")

        self.notebook.add(pestanaCitas, text="Citas")

        #-----------------------MEDICAMENTOS-----------------------#

        pestanaMedicamento = ttk.Frame(self.notebook)
        pestanaMedicamento.grid_columnconfigure(0, weight=1)
        pestanaMedicamento.grid_columnconfigure(1, weight=1)

        ttk.Label(pestanaMedicamento, text="Ingrese Codigo:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.txIdMedicamentoBuscar = ttk.Entry(pestanaMedicamento, width=30)
        self.txIdMedicamentoBuscar.grid(row=0, column=1, padx=10, pady=10)

        self.btnBuscarMedicamento = ttk.Button(pestanaMedicamento, text="Buscar", command=self.buscarMedicamento)
        self.btnBuscarMedicamento.grid(row=0, column=2, padx=10, pady=10)

        ttk.Label(pestanaMedicamento, text="Codigo:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.txIDMedicamento = ttk.Entry(pestanaMedicamento, width=15)
        self.txIDMedicamento.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(pestanaMedicamento, text="Nombre:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.txNombreMedicamento = ttk.Entry(pestanaMedicamento, width=30)
        self.txNombreMedicamento.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(pestanaMedicamento, text="Administración:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.txAdminMedicamento = ttk.Entry(pestanaMedicamento, width=30)
        self.txAdminMedicamento.grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(pestanaMedicamento, text="Presentación:").grid(row=3, column=2, padx=10, pady=5, sticky="e")
        self.txPresMedicamento = ttk.Entry(pestanaMedicamento, width=30)
        self.txPresMedicamento.grid(row=3, column=3, padx=10, pady=5)

        ttk.Label(pestanaMedicamento, text="Fecha de Cad.:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.txFechaCad = ttk.Entry(pestanaMedicamento, width=30)
        self.txFechaCad.grid(row=4, column=1, padx=10, pady=5)

        self.btnNuevoMedicamento = ttk.Button(pestanaMedicamento, text="Nuevo", command=self.limpiarDatosMedicamento)
        self.btnNuevoMedicamento.grid(row=6, column=0, padx=10, pady=10, sticky="e")

        self.btnGuardarMedicamento = ttk.Button(pestanaMedicamento, text="Guardar", command=self.guardarMedicamento)
        self.btnGuardarMedicamento.grid(row=6, column=1, padx=10, pady=10, sticky="w")

        self.btnCancelarMedicamento = ttk.Button(pestanaMedicamento, text="Cancelar", command=self.limpiarDatosMedicamento)
        self.btnCancelarMedicamento.grid(row=6, column=2, padx=10, pady=10, sticky="w")

        self.btnEditarMedicamento = ttk.Button(pestanaMedicamento, text="Editar", command=self.actualizarMedicamento)
        self.btnEditarMedicamento.grid(row=6, column=3, padx=10, pady=10, sticky="w")

        self.btnEliminarMedicamento = ttk.Button(pestanaMedicamento, text="Eliminar", command=self.eliminarMedicamento)
        self.btnEliminarMedicamento.grid(row=6, column=4, padx=10, pady=10, sticky="w")

        ttk.Label(pestanaMedicamento, text="MEDICAMENTOS:").grid(row=10, column=0, padx=10, pady=10, sticky="e")
        self.btnMostrarMedicamentos = ttk.Button(pestanaMedicamento, text="Mostrar", command=self.mostrarTodosMedicamentos)
        self.btnMostrarMedicamentos.grid(row=10, column=1, padx=10, pady=10)

        self.treeMedicamentos = ttk.Treeview(pestanaMedicamento, columns=("codigo", "nombre", "via_admin", "presentacion", "fecha_cad"), show="headings", height=14)
        self.treeMedicamentos.grid(row=11, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        self.treeMedicamentos.column("codigo", width=50)
        self.treeMedicamentos.heading("codigo", text="Codigo")

        self.treeMedicamentos.column("nombre", width=250)
        self.treeMedicamentos.heading("nombre", text="Nombre")

        self.treeMedicamentos.column("via_admin", width=250)
        self.treeMedicamentos.heading("via_admin", text="Via de Aministracion")

        self.treeMedicamentos.column("presentacion", width=100)
        self.treeMedicamentos.heading("presentacion", text="Presentacion")

        self.treeMedicamentos.column("fecha_cad", width=100)
        self.treeMedicamentos.heading("fecha_cad", text="Fech. Cad")

        if nombre == "Administrador":
            self.notebook.add(pestanaMedicamento, text="Medicamentos")
        
        #-----------------------CONSULTAS-----------------------#

        pestanaConsultas = ttk.Frame(self.notebook)
        pestanaConsultas.grid_columnconfigure(0, weight=1)
        pestanaConsultas.grid_columnconfigure(1, weight=1)

        ttk.Label(pestanaConsultas, text="Ingrese Codigo:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.txIdConsultaBuscar = ttk.Entry(pestanaConsultas, width=30)
        self.txIdConsultaBuscar.grid(row=0, column=1, padx=10, pady=10)

        self.btnBuscarConsulta = ttk.Button(pestanaConsultas, text="Buscar", command=self.buscarConsulta)
        self.btnBuscarConsulta.grid(row=0, column=2, padx=10, pady=10)

        ttk.Label(pestanaConsultas, text="ID:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.txIDConsulta = ttk.Entry(pestanaConsultas, width=30)
        self.txIDConsulta.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(pestanaConsultas, text="ID Cita:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.comboIDCitas = ttk.Combobox(pestanaConsultas, values=self.obtenerCitas(), width=15)
        self.comboIDCitas.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(pestanaConsultas, text="Diagnostico:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.txDiagnosticoConsulta = tk.Entry(pestanaConsultas, width=30)
        self.txDiagnosticoConsulta.grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(pestanaConsultas, text="ID Medicamento:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.comboIDMedicamento = ttk.Combobox(pestanaConsultas, values=self.obtenerMedicamentos(), width=15)
        self.comboIDMedicamento.grid(row=4, column=1, padx=10, pady=5)

        self.btnNuevaConsulta = ttk.Button(pestanaConsultas, text="Nuevo", command=self.limpiarCamposConsulta)
        self.btnNuevaConsulta.grid(row=6, column=0, padx=10, pady=10, sticky="e")

        self.btnGuardarConsulta = ttk.Button(pestanaConsultas, text="Guardar", command=self.guardarConsulta)
        self.btnGuardarConsulta.grid(row=6, column=1, padx=10, pady=10, sticky="w")

        self.btnCancelarConsulta = ttk.Button(pestanaConsultas, text="Cancelar", command=self.limpiarCamposConsulta)
        self.btnCancelarConsulta.grid(row=6, column=2, padx=10, pady=10, sticky="w")

        self.btnEditarConsulta = ttk.Button(pestanaConsultas, text="Editar", command=self.actualizarConsulta)
        self.btnEditarConsulta.grid(row=6, column=3, padx=10, pady=10, sticky="w")

        self.btnEliminarConsulta = ttk.Button(pestanaConsultas, text="Eliminar", command=self.eliminarConsulta)
        self.btnEliminarConsulta.grid(row=6, column=4, padx=10, pady=10, sticky="w")

        ttk.Label(pestanaConsultas, text="CONSULTAS:").grid(row=10, column=0, padx=10, pady=10, sticky="e")
        self.btnMostrarConsultas = ttk.Button(pestanaConsultas, text="Mostrar", command=self.mostrarTodasConsultas)
        self.btnMostrarConsultas.grid(row=10, column=1, padx=10, pady=10)

        self.treeConsultas = ttk.Treeview(pestanaConsultas, columns=("codigo", "id_cita", "diagnostico", "id_medicamento"), show="headings", height=14)
        self.treeConsultas.grid(row=11, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        self.treeConsultas.column("codigo", width=50)
        self.treeConsultas.heading("codigo", text="Codigo")

        self.treeConsultas.column("id_cita", width=50)
        self.treeConsultas.heading("id_cita", text="ID Cita")

        self.treeConsultas.column("diagnostico", width=300)
        self.treeConsultas.heading("diagnostico", text="Diagnostico")

        self.treeConsultas.column("id_medicamento", width=50)
        self.treeConsultas.heading("id_medicamento", text="ID Medicamento")

        self.notebook.add(pestanaConsultas, text="Consultas")

        #-----------------------CONFG DEL NOTEBOOK-----------------------#

        self.notebook.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.pack()

        #-----------------------CERRAR SESIÓN----------------------#

        logout_button = ttk.Button(self, text="Cerrar Sesión", command=self.cerrar_sesion)
        logout_button.grid(padx=10, pady=10)

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

    #-----------------------CONFG DEL CERRAR SESIÓN-----------------------#

    def cerrar_sesion(self):
        self.master.withdraw()
        login = LoginWindow(self.master)
    
    #-----------------------CONFG DEL CRUD-----------------------#

    #!EMPLEADOS

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

        for item in self.treeEmpleados.get_children():
            self.treeEmpleados.delete(item)
    
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
        if self.validarCamposEmpleado():
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
            self.mostrarTodosEmpleados()
    
    def eliminarEmpleado(self):
        conexion = Connection()
        conexion.deleteEmpleado(self.txIdBuscar.get())
    
    def buscarEmpleado(self):
        conexion = Connection()
        empleado = conexion.searchEmpleado(self.txIdBuscar.get())
        if empleado:
            self.txID.delete(0, 'end')
            self.txNombre.delete(0, 'end')
            self.txDireccion.delete(0, 'end')
            self.txTelefono.delete(0, 'end')
            self.txFechaNac.delete(0, 'end')
            self.txSexo.delete(0, 'end')
            self.txSueldo.delete(0, 'end')
            self.txTurno.delete(0, 'end')
            self.txPassword.delete(0, 'end')
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

    def validarCamposEmpleado(self):
        if not self.txID.get() or not self.txNombre.get() or not self.txDireccion.get() or not self.txTelefono.get() or \
           not self.txFechaNac.get() or not self.txSexo.get() or not self.txSueldo.get() or not self.txTurno.get() or not self.txPassword.get():
            messagebox.showerror("Error", "Todos los campos deben ser llenados.")
            return False
        return True
    
    def mostrarTodosEmpleados(self):
        for item in self.treeEmpleados.get_children():
            self.treeEmpleados.delete(item)

        conexion = Connection()
        conn = conexion.open()
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM empleados ORDER by codigo")
            empleados = cur.fetchall()

            for empleado in empleados:
                self.treeEmpleados.insert("", "end", values=empleado)

            cur.close()
            conexion.close()
        else:
            messagebox.showerror("Error", "No se pudo conectar a la base de datos.")    
    
    #!DOCTORES

    def limpiarDatosDoctor(self):
        self.txIDDoctor.delete(0, 'end')
        self.txNombreDoctor.delete(0, 'end')
        self.txDireccionDoctor.delete(0, 'end')
        self.txTelefonoDoctor.delete(0, 'end')
        self.txFechaNacDoctor.delete(0, 'end')
        self.txSexoDoctor.delete(0, 'end')
        self.txEspecialidadDoctor.delete(0, 'end')
        self.txPasswordDoctor.delete(0, 'end')

        for item in self.treeDoctores.get_children():
            self.treeDoctores.delete(item)
    
    def guardarDoctor(self):
        conexion = Connection()
        conexion.saveDoctor(
            self.txIDDoctor.get(),
            self.txNombreDoctor.get(),
            self.txDireccionDoctor.get(),
            self.txTelefonoDoctor.get(),
            self.txFechaNacDoctor.get(),
            self.txSexoDoctor.get(),
            self.txEspecialidadDoctor.get(),
            self.txPasswordDoctor.get()
        )
    
    def actualizarDoctor(self):
        if self.validarCamposDoctor():
            conexion = Connection()
            conexion.updateDoctor(
                self.txIDDoctor.get(),
                self.txNombreDoctor.get(),
                self.txDireccionDoctor.get(),
                self.txTelefonoDoctor.get(),
                self.txFechaNacDoctor.get(),
                self.txSexoDoctor.get(),
                self.txEspecialidadDoctor.get(),
                self.txPasswordDoctor.get()
            )
            self.mostrarTodosDoctor()
    
    def eliminarDoctor(self):
        conexion = Connection()
        conexion.deleteDoctor(self.txIdDoctorBuscar.get())
    
    def buscarDoctor(self):
        conexion = Connection()
        doctor = conexion.searchDoctor(self.txIdDoctorBuscar.get())
        if doctor:
            self.txIDDoctor.delete(0, 'end')
            self.txNombreDoctor.delete(0, 'end')
            self.txDireccionDoctor.delete(0, 'end')
            self.txTelefonoDoctor.delete(0, 'end')
            self.txFechaNacDoctor.delete(0, 'end')
            self.txSexoDoctor.delete(0, 'end')
            self.txEspecialidadDoctor.delete(0, 'end')
            self.txPasswordDoctor.delete(0, 'end')
            self.txIDDoctor.insert(0, doctor[0])
            self.txNombreDoctor.insert(0, doctor[1])
            self.txDireccionDoctor.insert(0, doctor[2])
            self.txTelefonoDoctor.insert(0, doctor[3])
            self.txFechaNacDoctor.insert(0, doctor[4])
            self.txSexoDoctor.insert(0, doctor[5])
            self.txEspecialidadDoctor.insert(0, doctor[6])
            self.txPasswordDoctor.insert(0, doctor[7])
        else:
            messagebox.showerror("Error", "¡Doctor no encontrado!")

    def validarCamposDoctor(self):
        if not self.txIDDoctor.get() or not self.txNombreDoctor.get() or not self.txDireccionDoctor.get() or not self.txTelefonoDoctor.get() or \
           not self.txFechaNacDoctor.get() or not self.txSexoDoctor.get() or not self.txEspecialidadDoctor.get() or not self.txPasswordDoctor.get():
            messagebox.showerror("Error", "Todos los campos deben ser llenados.")
            return False
        return True
    
    def mostrarTodosDoctor(self):
        for item in self.treeDoctores.get_children():
            self.treeDoctores.delete(item)

        conexion = Connection()
        conn = conexion.open()
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM doctores ORDER by codigo")
            doctores = cur.fetchall()

            for doctor in doctores:
                self.treeDoctores.insert("", "end", values=doctor)

            cur.close()
            conexion.close()
        else:
            messagebox.showerror("Error", "No se pudo conectar a la base de datos.")
    
    #!PACIENTES

    def limpiarDatosPaciente(self):
        self.txIDPaciente.delete(0, 'end')
        self.txNombrePaciente.delete(0, 'end')
        self.txDireccionPaciente.delete(0, 'end')
        self.txTelefonoPaciente.delete(0, 'end')
        self.txFechaNacPaciente.delete(0, 'end')
        self.txSexoPaciente.delete(0, 'end')
        self.txEdadPaciente.delete(0, 'end')
        self.txEstaturaPaciente.delete(0, 'end')

        for item in self.treePacientes.get_children():
            self.treePacientes.delete(item)
    
    def guardarPaciente(self):
        conexion = Connection()
        conexion.savePaciente(
            self.txIDPaciente.get(),
            self.txNombrePaciente.get(),
            self.txDireccionPaciente.get(),
            self.txTelefonoPaciente.get(),
            self.txFechaNacPaciente.get(),
            self.txSexoPaciente.get(),
            self.txEdadPaciente.get(),
            self.txEstaturaPaciente.get()
        )
    
    def actualizarPaciente(self):
        if self.validarCamposPaciente():
            conexion = Connection()
            conexion.updatePaciente(
                self.txIDPaciente.get(),
                self.txNombrePaciente.get(),
                self.txDireccionPaciente.get(),
                self.txTelefonoPaciente.get(),
                self.txFechaNacPaciente.get(),
                self.txSexoPaciente.get(),
                self.txEdadPaciente.get(),
                self.txEstaturaPaciente.get()
            )
            self.mostrarTodosPaciente()
    
    def eliminarPaciente(self):
        conexion = Connection()
        conexion.deletePaciente(self.txIdPacienteBuscar.get())
    
    def buscarPaciente(self):
        conexion = Connection()
        paciente = conexion.searchPaciente(self.txIdPacienteBuscar.get())
        if paciente:
            self.txIDPaciente.delete(0, 'end')
            self.txNombrePaciente.delete(0, 'end')
            self.txDireccionPaciente.delete(0, 'end')
            self.txTelefonoPaciente.delete(0, 'end')
            self.txFechaNacPaciente.delete(0, 'end')
            self.txSexoPaciente.delete(0, 'end')
            self.txEdadPaciente.delete(0, 'end')
            self.txEstaturaPaciente.delete(0, 'end')
            self.txIDPaciente.insert(0, paciente[0])
            self.txNombrePaciente.insert(0, paciente[1])
            self.txDireccionPaciente.insert(0, paciente[2])
            self.txTelefonoPaciente.insert(0, paciente[3])
            self.txFechaNacPaciente.insert(0, paciente[4])
            self.txSexoPaciente.insert(0, paciente[5])
            self.txEdadPaciente.insert(0, paciente[6])
            self.txEstaturaPaciente.insert(0, paciente[7])
        else:
            messagebox.showerror("Error", "¡Paciente no encontrado!")

    def validarCamposPaciente(self):
        if not self.txIDPaciente.get() or not self.txNombrePaciente.get() or not self.txDireccionPaciente.get() or not self.txTelefonoPaciente.get() or \
           not self.txFechaNacPaciente.get() or not self.txSexoPaciente.get() or not self.txEdadPaciente.get() or not self.txEstaturaPaciente.get():
            messagebox.showerror("Error", "Todos los campos deben ser llenados.")
            return False
        return True
    
    def mostrarTodosPaciente(self):
        for item in self.treePacientes.get_children():
            self.treePacientes.delete(item)

        conexion = Connection()
        conn = conexion.open()
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM pacientes ORDER by codigo")
            pacientes = cur.fetchall()

            for paciente in pacientes:
                self.treePacientes.insert("", "end", values=paciente)

            cur.close()
            conexion.close()
        else:
            messagebox.showerror("Error", "No se pudo conectar a la base de datos.")

    #!CITAS

    def guardarCita(self):
        if self.validarCamposCita():
            conexion = Connection()
            conexion.saveCita(
                self.txIDCita.get(),
                self.comboPacienteCita.get(),
                self.comboDoctorCita.get(),
                self.txDiaCita.get(),
                self.txHoraCita.get()
            )
            self.mostrarTodasCitas()

    def actualizarCita(self):
        if self.validarCamposCita():
            conexion = Connection()
            conexion.updateCita(
                self.txIDCita.get(),
                self.comboPacienteCita.get(),
                self.comboDoctorCita.get(),
                self.txDiaCita.get(),
                self.txHoraCita.get()
            )
            self.mostrarTodasCitas()

    def buscarCita(self):
        conexion = Connection()
        cita = conexion.searchCita(self.txIdCitaBuscar.get())
        if cita:
            self.txIDCita.delete(0, 'end')
            self.txIDCita.insert(0, cita[0])
            self.comboPacienteCita.set(cita[1])
            self.comboDoctorCita.set(cita[2])
            self.txDiaCita.delete(0, 'end')
            self.txDiaCita.insert(0, cita[3])
            self.txHoraCita.delete(0, 'end')
            self.txHoraCita.insert(0, cita[4])
        else:
            messagebox.showerror("Error", "¡Cita no encontrada!")

    def eliminarCita(self):
        conexion = Connection()
        conexion.deleteCita(self.txIdCitaBuscar.get())
        self.mostrarTodasCitas()

    def mostrarTodasCitas(self):
        for item in self.treeCitas.get_children():
            self.treeCitas.delete(item)
        
        conexion = Connection()
        conn = conexion.open()
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM citas ORDER BY dia, hora")
            citas = cur.fetchall()
            for cita in citas:
                self.treeCitas.insert("", "end", values=cita)
            cur.close()
            conexion.close()
        else:
            messagebox.showerror("Error", "No se pudo conectar a la base de datos.")

    def validarCamposCita(self):
        if not self.txIDCita.get() or not self.comboPacienteCita.get() or not self.comboDoctorCita.get() \
                or not self.txDiaCita.get() or not self.txHoraCita.get():
            messagebox.showerror("Error", "Faltan campos por completar.")
            return False
        return True

    def obtenerPacientes(self):
        conexion = Connection()
        conn = conexion.open()
        pacientes = []
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT codigo FROM pacientes")
            pacientes = [paciente[0] for paciente in cur.fetchall()]
            cur.close()
            conexion.close()
        return pacientes

    def obtenerDoctores(self):
        conexion = Connection()
        conn = conexion.open()
        doctores = []
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT codigo FROM doctores")
            doctores = [doctor[0] for doctor in cur.fetchall()]
            cur.close()
            conexion.close()
        return doctores
    
    def limpiarCamposCita(self):
        self.txIDCita.delete(0, 'end')
        self.comboPacienteCita.set('')
        self.comboDoctorCita.set('')
        self.txDiaCita.delete(0, 'end')
        self.txHoraCita.delete(0, 'end')

        for item in self.treeCitas.get_children():
            self.treeCitas.delete(item)
    
    #!MEDICAMENTOS

    def limpiarDatosMedicamento(self):
        self.txIDMedicamento.delete(0, 'end')
        self.txNombreMedicamento.delete(0, 'end')
        self.txAdminMedicamento.delete(0, 'end')
        self.txPresMedicamento.delete(0, 'end')
        self.txFechaCad.delete(0, 'end')
        for item in self.treeMedicamentos.get_children():
            self.treeMedicamentos.delete(item)
    
    def guardarMedicamento(self):
        if self.validarCamposMedicamento():
            conexion = Connection()
            conexion.saveMedicina(
                self.txIDMedicamento.get(),
                self.txNombreMedicamento.get(),
                self.txAdminMedicamento.get(),
                self.txPresMedicamento.get(),
                self.txFechaCad.get()
            )
    
    def actualizarMedicamento(self):
        if self.validarCamposMedicamento():
            conexion = Connection()
            conexion.updateMedicina(
                self.txIDMedicamento.get(),
                self.txNombreMedicamento.get(),
                self.txAdminMedicamento.get(),
                self.txPresMedicamento.get(),
                self.txFechaCad.get()
            )
            self.mostrarTodosMedicamentos()
    
    def eliminarMedicamento(self):
        conexion = Connection()
        conexion.deleteMedicina(self.txIdMedicamentoBuscar.get())
    
    def buscarMedicamento(self):
        conexion = Connection()
        medicina = conexion.searchMedicina(self.txIdMedicamentoBuscar.get())
        if medicina:
            self.limpiarDatosMedicamento()
            self.txIDMedicamento.insert(0, medicina[0])
            self.txNombreMedicamento.insert(0, medicina[1])
            self.txAdminMedicamento.insert(0, medicina[2])
            self.txPresMedicamento.insert(0, medicina[3])
            self.txFechaCad.insert(0, medicina[4])
        else:
            messagebox.showerror("Error", "Medicina no encontrada!")

    def validarCamposMedicamento(self):
        if not self.txIDMedicamento.get() or not self.txNombreMedicamento.get() or not self.txAdminMedicamento.get() or not self.txPresMedicamento.get() or not self.txFechaCad.get():
            messagebox.showerror("Error", "Todos los campos deben ser llenados.")
            return False
        return True
    
    def mostrarTodosMedicamentos(self):
        for item in self.treeMedicamentos.get_children():
            self.treeMedicamentos.delete(item)
        conexion = Connection()
        conn = conexion.open()
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM medicamentos ORDER by codigo")
            medicamentos = cur.fetchall()
            for medicamento in medicamentos:
                self.treeMedicamentos.insert("", "end", values=medicamento)
            cur.close()
            conexion.close()
        else:
            messagebox.showerror("Error", "No se pudo conectar a la base de datos.")
    
    #!CONSULTAS

    def guardarConsulta(self):
        if self.validarCamposConsulta():
            conexion = Connection()
            conexion.saveConsulta(
                self.txIDConsulta.get(),
                self.comboIDCitas.get(),
                self.txDiagnosticoConsulta.get(),
                self.comboIDMedicamento.get()
            )

            conn = conexion.open()
            if conn:
                cur = conn.cursor()
                try:
                    #?Datos del paciente
                    cur.execute("""
                        SELECT p.nombre, p.fecha_nac, p.edad, p.sexo, p.direccion, p.telefono, p.estatura
                        FROM pacientes p
                        JOIN citas c ON p.codigo = c.paciente_id
                        WHERE c.codigo = %s
                    """, (self.comboIDCitas.get(),))
                    paciente = cur.fetchone()

                    #?Datos del medicamento
                    cur.execute("""
                        SELECT nombre FROM medicamentos WHERE codigo = %s
                    """, (self.comboIDMedicamento.get(),))
                    medicamento = cur.fetchone()

                    #?Datos del doctor
                    cur.execute("""
                        SELECT d.nombre FROM doctores d
                        JOIN citas c ON d.codigo = c.doctor_id
                        WHERE c.codigo = %s
                    """, (self.comboIDCitas.get(),))
                    doctor = cur.fetchone()

                    if paciente and medicamento and doctor:
                        self.generarPDFConsulta(paciente, medicamento, doctor, self.txDiagnosticoConsulta.get())
                    else:
                        messagebox.showerror("Error", "No se pudieron recuperar todos los datos necesarios para generar el PDF.")
                finally:
                    cur.close()
                    conexion.close()

    def actualizarConsulta(self):
        if self.validarCamposConsulta():
            conexion = Connection()
            conexion.updateConsulta(
                self.txIDConsulta.get(),
                self.comboIDCitas.get(),
                self.txDiagnosticoConsulta.get(),
                self.comboIDMedicamento.get()
            )
            self.mostrarTodasConsultas()

    def buscarConsulta(self):
        conexion = Connection()
        consulta = conexion.searchConsulta(self.txIdConsultaBuscar.get())
        if consulta:
            self.limpiarCamposConsulta()
            self.txIDConsulta.insert(0, consulta[0])
            self.comboIDCitas.set(consulta[1])
            self.txDiagnosticoConsulta.insert(0, consulta[2])
            self.comboIDMedicamento.set(consulta[3])
        else:
            messagebox.showerror("Error", "¡Consulta no encontrada!")

    def eliminarConsulta(self):
        conexion = Connection()
        conexion.deleteConsulta(self.txIdConsultaBuscar.get())
        self.mostrarTodasConsultas()

    def mostrarTodasConsultas(self):
        for item in self.treeConsultas.get_children():
            self.treeConsultas.delete(item)
        conexion = Connection()
        conn = conexion.open()
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM consultas ORDER BY codigo")
            consultas = cur.fetchall()
            for consulta in consultas:
                self.treeConsultas.insert("", "end", values=consulta)
            cur.close()
            conexion.close()
        else:
            messagebox.showerror("Error", "No se pudo conectar a la base de datos.")

    def validarCamposConsulta(self):
        if not self.txIDConsulta.get() or not self.comboIDCitas.get() or not self.comboIDMedicamento.get():
            messagebox.showerror("Error", "Faltan campos por completar.")
            return False
        return True

    def obtenerCitas(self):
        conexion = Connection()
        conn = conexion.open()
        citas = []
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT codigo FROM citas")
            citas = [cita[0] for cita in cur.fetchall()]
            cur.close()
            conexion.close()
        return citas

    def obtenerMedicamentos(self):
        conexion = Connection()
        conn = conexion.open()
        medicamentos = []
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT codigo FROM medicamentos")
            medicamentos = [medicamento[0] for medicamento in cur.fetchall()]
            cur.close()
            conexion.close()
        return medicamentos
    
    def limpiarCamposConsulta(self):
        self.txIDConsulta.delete(0, 'end')
        self.comboIDCitas.set('')
        self.comboIDMedicamento.set('')
        self.txDiagnosticoConsulta.delete(0, 'end')
        for item in self.treeConsultas.get_children():
            self.treeConsultas.delete(item)

    def generarPDFConsulta(self, paciente, medicamento, doctor, diagnostico):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        #?Título
        pdf.set_font("Arial", style='B', size=16)
        pdf.cell(200, 10, "Reporte de Consulta", ln=True, align="C")
        pdf.ln(10)

        #?Datos del paciente
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, "Datos del Paciente:", ln=True)
        pdf.cell(200, 10, f"Nombre: {paciente[0]}", ln=True)
        pdf.cell(200, 10, f"Fecha de Nacimiento: {paciente[1]}", ln=True)
        pdf.cell(200, 10, f"Edad: {paciente[2]} años", ln=True)
        pdf.cell(200, 10, f"Sexo: {paciente[3]}", ln=True)
        pdf.cell(200, 10, f"Direccion: {paciente[4]}", ln=True)
        pdf.cell(200, 10, f"Telefono: {paciente[5]}", ln=True)
        pdf.cell(200, 10, f"Estatura: {paciente[6]} cm", ln=True)
        pdf.ln(10)

        #?Datos del medicamento
        pdf.cell(200, 10, "Datos del Medicamento:", ln=True)
        pdf.cell(200, 10, f"Nombre: {medicamento[0]}", ln=True)
        pdf.cell(200, 10, f"Detalles: {diagnostico}", ln=True)
        pdf.ln(10)

        #?Datos del doctor
        pdf.cell(200, 10, "Datos del Doctor:", ln=True)
        pdf.cell(200, 10, f"Nombre: {doctor[0]}", ln=True)
        pdf.ln(20)

        #?Logo
        logo_path = os.path.join(os.getcwd(), "imagenes", "logo.png")
        if os.path.exists(logo_path):
            pdf.image(logo_path, x=80, y=pdf.get_y(), w=50)

        #?Guardar PDF
        output_path = os.path.join(os.getcwd(), "reportes", f"consulta_{self.txIDConsulta.get()}.pdf")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        pdf.output(output_path)

        messagebox.showinfo("Éxito", f"PDF generado correctamente en {output_path}.")


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    login = LoginWindow(root)
    root.mainloop()