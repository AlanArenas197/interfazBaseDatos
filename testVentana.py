import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Farmacia de Especialidades CUCEI - <USUARIO>")
root.geometry("750x300")

notebook = ttk.Notebook(root)
     
#-----------------------USUARIOS-----------------------#
        
pestanaUsuarios = ttk.Frame(notebook)
pestanaUsuarios.grid_columnconfigure(0, weight=1)
pestanaUsuarios.grid_columnconfigure(1, weight=1)

ttk.Label(pestanaUsuarios, text="Ingrese ID a buscar:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
txIdBuscar = ttk.Entry(pestanaUsuarios, width=30)
txIdBuscar.grid(row=0, column=1, padx=10, pady=10)

btnBuscar = ttk.Button(pestanaUsuarios, text="Buscar")
btnBuscar.grid(row=0, column=2, padx=10, pady=10)

ttk.Label(pestanaUsuarios, text="Nombre:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
txNombre = ttk.Entry(pestanaUsuarios, width=30)
txNombre.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(pestanaUsuarios, text="Correo:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
txCorreo = ttk.Entry(pestanaUsuarios, width=30)
txCorreo.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(pestanaUsuarios, text="Teléfono:").grid(row=2, column=2, padx=10, pady=5, sticky="e")
txTelefono = ttk.Entry(pestanaUsuarios, width=30)
txTelefono.grid(row=2, column=3, padx=10, pady=5)

ttk.Label(pestanaUsuarios, text="Password:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
txPassword = ttk.Entry(pestanaUsuarios, width=30)
txPassword.grid(row=3, column=1, padx=10, pady=5)

ttk.Label(pestanaUsuarios, text="Perfil:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
comboPerfil = ttk.Combobox(pestanaUsuarios, values=["Seleccione", "Admin", "Gerente", "Cajero"], state='readonly')
comboPerfil.set("Seleccione")
comboPerfil.grid(row=4, column=1, padx=10, pady=5)

btnNuevoUsuario = ttk.Button(pestanaUsuarios, text="Nuevo")
btnNuevoUsuario.grid(row=5, column=0, padx=10, pady=10, sticky="e")

btnGuardarUsuario = ttk.Button(pestanaUsuarios, text="Guardar")
btnGuardarUsuario.grid(row=5, column=1, padx=10, pady=10, sticky="w")

btnCancelarUsuario = ttk.Button(pestanaUsuarios, text="Cancelar")
btnCancelarUsuario.grid(row=5, column=2, padx=10, pady=10, sticky="w")

btnEditarUsuario = ttk.Button(pestanaUsuarios, text="Editar")
btnEditarUsuario.grid(row=5, column=3, padx=10, pady=10, sticky="w")

btnEliminarUsuario = ttk.Button(pestanaUsuarios, text="Eliminar")
btnEliminarUsuario.grid(row=5, column=4, padx=10, pady=10, sticky="w")

notebook.add(pestanaUsuarios, text="Usuarios")

#-----------------------ALMACEN-----------------------#
        
pestanaAlmacen = ttk.Frame(notebook)
pestanaAlmacen.grid_columnconfigure(0, weight=1)
pestanaAlmacen.grid_columnconfigure(1, weight=1)

ttk.Label(pestanaAlmacen, text="Ingrese ID a buscar:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
txIdBuscarProducto = ttk.Entry(pestanaAlmacen, width=30)
txIdBuscarProducto.grid(row=0, column=1, padx=10, pady=10)

btnBuscarProducto = ttk.Button(pestanaAlmacen, text="Buscar")
btnBuscarProducto.grid(row=0, column=2, padx=10, pady=10)

ttk.Label(pestanaAlmacen, text="Nombre:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
txNombreProducto = ttk.Entry(pestanaAlmacen, width=30)
txNombreProducto.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(pestanaAlmacen, text="Categoría:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
comboPerfil = ttk.Combobox(pestanaAlmacen, values=["Seleccione", "Medicamento", "Insumo", "Snacks", "Higiene", "Fotos"], state='readonly')
comboPerfil.set("Seleccione")
comboPerfil.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(pestanaAlmacen, text="Cantidad:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
txCantidadProducto = ttk.Entry(pestanaAlmacen, width=30)
txCantidadProducto.grid(row=3, column=1, padx=10, pady=5)

ttk.Label(pestanaAlmacen, text="Precio p/u:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
txPrecioProd = ttk.Entry(pestanaAlmacen, width=30)
txPrecioProd.grid(row=4, column=1, padx=10, pady=5)

ttk.Label(pestanaAlmacen, text="Fecha Exp:").grid(row=4, column=2, padx=10, pady=5, sticky="e")
txFechaExp = ttk.Entry(pestanaAlmacen, width=30)
txFechaExp.grid(row=4, column=3, padx=10, pady=5)

btnNuevoProducto = ttk.Button(pestanaAlmacen, text="Nuevo")
btnNuevoProducto.grid(row=6, column=0, padx=10, pady=10, sticky="e")

btnGuardarProducto = ttk.Button(pestanaAlmacen, text="Guardar")
btnGuardarProducto.grid(row=6, column=1, padx=10, pady=10, sticky="w")

btnCancelarProducto = ttk.Button(pestanaAlmacen, text="Cancelar")
btnCancelarProducto.grid(row=6, column=2, padx=10, pady=10, sticky="w")

btnEditarProducto = ttk.Button(pestanaAlmacen, text="Editar")
btnEditarProducto.grid(row=6, column=3, padx=10, pady=10, sticky="w")

btnEliminarProducto = ttk.Button(pestanaAlmacen, text="Eliminar")
btnEliminarProducto.grid(row=6, column=4, padx=10, pady=10, sticky="w")


notebook.add(pestanaAlmacen, text="Almacen")

#-----------------------VENTAS-----------------------#

pestanaVentas = ttk.Frame(notebook)
pestanaVentas.grid_columnconfigure(2, weight=1)
pestanaVentas.grid_columnconfigure(3, weight=1)

ttk.Label(pestanaVentas, text="Ingrese Folio a buscar:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
txFolioBuscarVenta = ttk.Entry(pestanaVentas, width=30)
txFolioBuscarVenta.grid(row=0, column=1, padx=10, pady=10)

btnBuscarVenta = ttk.Button(pestanaVentas, text="Buscar")
btnBuscarVenta.grid(row=0, column=2, padx=10, pady=10)

ttk.Label(pestanaVentas, text="Cliente:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
comboCliente = ttk.Combobox(pestanaVentas, values=["Seleccione", "<CLIENTES>"], state='readonly')
comboCliente.set("Seleccione")
comboCliente.grid(row=1, column=1, padx=10, pady=5)
        
ttk.Label(pestanaVentas, text="Producto:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
comboProducto = ttk.Combobox(pestanaVentas, values=["Seleccione", "<PRODUCTOS>"], state='readonly')
comboProducto.set("Seleccione")
comboProducto.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(pestanaVentas, text="Cantidad:").grid(row=2, column=2, pady=5, sticky="e")
txProductoCant = ttk.Entry(pestanaVentas, width=30)
txProductoCant.grid(row=2, column=3, padx=10, pady=5)

ttk.Label(pestanaVentas, text="Total:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
txTotalVenta = ttk.Entry(pestanaVentas, width=30)
txTotalVenta.grid(row=3, column=1, padx=10, pady=5)

ttk.Label(pestanaVentas, text="Pago:").grid(row=3, column=2, padx=10, pady=5, sticky="e")
txPagoVenta = ttk.Entry(pestanaVentas, width=30)
txPagoVenta.grid(row=3, column=3, padx=10, pady=5)

btnNuevoVenta = ttk.Button(pestanaVentas, text="Nuevo")
btnNuevoVenta.grid(row=4, column=0, padx=10, pady=10, sticky="e")

btnGuardarVenta = ttk.Button(pestanaVentas, text="Guardar")
btnGuardarVenta.grid(row=4, column=1, padx=10, pady=10, sticky="w")

btnCancelarVenta = ttk.Button(pestanaVentas, text="Cancelar")
btnCancelarVenta.grid(row=4, column=2, padx=10, pady=10, sticky="w")

btnEditarVenta = ttk.Button(pestanaVentas, text="Editar")
btnEditarVenta.grid(row=4, column=3, padx=10, pady=10, sticky="w")

btnEliminarVenta = ttk.Button(pestanaVentas, text="Eliminar")
btnEliminarVenta.grid(row=4, column=4, padx=10, pady=10, sticky="w")

notebook.add(pestanaVentas, text="Ventas")

#-----------------------CLIENTES-----------------------#

pestanaClientes = ttk.Frame(notebook)
pestanaClientes.grid_columnconfigure(0, weight=1)
pestanaClientes.grid_columnconfigure(1, weight=1)

ttk.Label(pestanaClientes, text="Ingrese ID a buscar:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
txIDClienteBuscar = ttk.Entry(pestanaClientes, width=30)
txIDClienteBuscar.grid(row=0, column=1, padx=10, pady=10)

btnBuscarCliente = ttk.Button(pestanaClientes, text="Buscar")
btnBuscarCliente.grid(row=0, column=2, padx=10, pady=10)

ttk.Label(pestanaClientes, text="Nombre:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
txNombreCliente = ttk.Entry(pestanaClientes, width=30)
txNombreCliente.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(pestanaClientes, text="Correo:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
txCorreoCliente = ttk.Entry(pestanaClientes, width=30)
txCorreoCliente.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(pestanaClientes, text="Teléfono:").grid(row=2, column=2, padx=10, pady=5, sticky="e")
txTelefonoCliente = ttk.Entry(pestanaClientes, width=30)
txTelefonoCliente.grid(row=2, column=3, padx=10, pady=5)

ttk.Label(pestanaClientes, text="Dirección:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
txDireccionCliente = ttk.Entry(pestanaClientes, width=30)
txDireccionCliente.grid(row=3, column=1, padx=10, pady=5)

ttk.Label(pestanaClientes, text="Puntos:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
txDireccionCliente = ttk.Entry(pestanaClientes, width=30)
txDireccionCliente.grid(row=4, column=1, padx=10, pady=5)

btnNuevoClientes = ttk.Button(pestanaClientes, text="Nuevo")
btnNuevoClientes.grid(row=5, column=0, padx=10, pady=10, sticky="e")

btnGuardarCliente = ttk.Button(pestanaClientes, text="Guardar")
btnGuardarCliente.grid(row=5, column=1, padx=10, pady=10, sticky="w")

btnCancelarCliente = ttk.Button(pestanaClientes, text="Cancelar")
btnCancelarCliente.grid(row=5, column=2, padx=10, pady=10, sticky="w")

btnEditarCliente = ttk.Button(pestanaClientes, text="Editar")
btnEditarCliente.grid(row=5, column=3, padx=10, pady=10, sticky="w")

btnEliminarCliente = ttk.Button(pestanaClientes, text="Eliminar")
btnEliminarCliente.grid(row=5, column=4, padx=10, pady=10, sticky="w")

notebook.add(pestanaClientes, text="Cliente")

#-----------------------COMPRAS-----------------------#

pestanaCompras = ttk.Frame(notebook)
pestanaCompras.grid_columnconfigure(0, weight=1)
pestanaCompras.grid_columnconfigure(1, weight=1)

ttk.Label(pestanaCompras, text="Ingrese ID a buscar:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
txIdBuscarCompra = ttk.Entry(pestanaCompras, width=30)
txIdBuscarCompra.grid(row=0, column=1, padx=10, pady=10)

btnBuscarCompra = ttk.Button(pestanaCompras, text="Buscar")
btnBuscarCompra.grid(row=0, column=2, padx=10, pady=10)

ttk.Label(pestanaCompras, text="ID:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
txIdCompra = ttk.Entry(pestanaCompras, width=30)
txIdCompra.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(pestanaCompras, text="Fecha Venta:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
txFechaCompra = ttk.Entry(pestanaCompras, width=30)
txFechaCompra.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(pestanaCompras, text="Cliente:").grid(row=1, column=2, padx=10, pady=5, sticky="e")
comboClienteCompra = ttk.Combobox(pestanaCompras, values=["Seleccione", "<CLIENTE>"], state='readonly')
comboClienteCompra.set("Seleccione")
comboClienteCompra.grid(row=1, column=3, padx=10, pady=5)

ttk.Label(pestanaCompras, text="Total:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
txFechaCompra = ttk.Entry(pestanaCompras, width=30)
txFechaCompra.grid(row=3, column=1, padx=10, pady=5)

ttk.Label(pestanaCompras, text="Método de Pago:").grid(row=3, column=2, padx=10, pady=5, sticky="e")
comboMetodoCompra = ttk.Combobox(pestanaCompras, values=["Seleccione", "Débito/Crédito", "Eféctivo"], state='readonly', width=30)
comboMetodoCompra.set("Seleccione")
comboMetodoCompra.grid(row=3, column=3, padx=10, pady=5)

ttk.Label(pestanaCompras, text="Cantidad:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
txCantCompra = ttk.Entry(pestanaCompras, width=30)
txCantCompra.grid(row=4, column=1, padx=10, pady=5)

ttk.Label(pestanaCompras, text="Rol:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
txCantCompra = ttk.Entry(pestanaCompras, width=30, state='readonly')
txCantCompra.grid(row=5, column=1, padx=10, pady=5)

btnNuevoCompra = ttk.Button(pestanaCompras, text="Nuevo")
btnNuevoCompra.grid(row=6, column=0, padx=10, pady=10, sticky="e")

btnGuardarCompra = ttk.Button(pestanaCompras, text="Guardar")
btnGuardarCompra.grid(row=6, column=1, padx=10, pady=10, sticky="w")

btnCancelarCompra = ttk.Button(pestanaCompras, text="Cancelar")
btnCancelarCompra.grid(row=6, column=2, padx=10, pady=10, sticky="w")

btnEditarCompra = ttk.Button(pestanaCompras, text="Editar")
btnEditarCompra.grid(row=6, column=3, padx=10, pady=10, sticky="w")

btnEliminarCompra = ttk.Button(pestanaCompras, text="Eliminar")
btnEliminarCompra.grid(row=6, column=4, padx=10, pady=10, sticky="w")
        
notebook.add(pestanaCompras, text="Compras")

notebook.pack(expand=True, fill='both', padx=10, pady=10)

root.mainloop()