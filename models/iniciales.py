# -*- coding: utf-8 -*-

def limpiar():
	db.executesql("""DROP DATABASE guardianweb;""")
	db.executesql("""CREATE DATABASE guardianweb;""")
	pass

def iniciales():
	guard_dbPaises     = db.paises
	guard_dbCiudades   = db.ciudades
	guard_dbPlanes     = db.planes
	guard_dbCotiza     = db.cotizaciones
	guard_dbOrdSer	   = db.ordenesServicio
	guard_dbOrdTra     = db.ordenesTrabajo
	guard_dbClientes   = db.clientes
	guard_dbProyectos  = db.proyectos
	guard_dbPerfiles   = db.auth_group
	guard_dbUsuarios   = db.auth_user
	guard_dbPermisos   = db.auth_membership
	guard_dbemple      = db.empleados
	guard_dbemp_usu    = db.usuario_empleado
	guard_dbCliePro    = db.clientesProyectos

	

	#  Pais -Ciudades -Planes
	guard_idPais       = guard_dbPaises.insert(paises_nombre='Colombia',paises_codigo=57)
	ciudades = [  
	    "Bogotá",
	    "Medellín",
	    "Cali",
	    "Bucaramanga",
	    "Barranquilla",
	    "Pereira",
	    "Cartagena",
	    "Cucuta",
	]
	con = 1
	for x in ciudades:
		guard_dbCiudades.insert(
			ciudades_pais   = guard_idPais,
			ciudades_nombre = x,
			ciudades_codigo = con
			)
		con = con + 1
		pass

	guard_plan       = []

	#  Cotizacion
	idCotiza      = guard_dbCotiza.insert(
		cotizaciones_codigo = 'COTZ-01',
		cotizaciones_nombre_proyecto = 'Brujula Soluciones Integrales',
		cotizaciones_nit_proyecto = '102030',
		cotizaciones_ciudad = 1,
		cotizaciones_direccion_proyecto = 'Calle 98 # 8 - 28',
		cotizaciones_nombre_administrador = 'Wilson Rodriguez',
		cotizaciones_celular_administrador = '1234567890',
		cotizaciones_email_administrador = 'email@email.com',
		cotizaciones_telefono_administrador = '1234567',
		cotizaciones_cantidad_interiores = '0',
		cotizaciones_cantidad_predios = '1',
		cotizaciones_plan = None,
		cotizaciones_observacion = 'Observacion',
		cotizaciones_responsable_creacion = None,
		cotizaciones_estado = 'Cerrada'
	)

	#  OrdenServicio
	idOrdenSer      = guard_dbOrdSer.insert(
		ordenesServicios_cotizacion = idCotiza,
		ordenesServicios_codigo = 'ORDSER-01',
		ordenesServicios_responsable_creacion = None,
		ordenesServicios_responsable_ejecucion = None,
		ordenesServicios_estado = 'Cerrada'
	)


	#  OrdenTrabajo
	idOrdenTra      = guard_dbOrdTra.insert(
		ordenesTrabajo_ordenServicio =   idOrdenSer,
		ordenesTrabajo_codigo =  'ORDTRA-01',
		ordenesTrabajo_responsable_creacion =  None,
		ordenesTrabajo_responsable_ejecucion =   None,
		ordenesTrabajo_estado  = 'Cerrada'
	)


	#  Cliente
	idCliente      = guard_dbClientes.insert( 
		clientes_nombre = 'Brujula Soluciones Integrales',
		clientes_nit = '102030',
		clientes_ordenTrabajo = 1,
		clientes_direccion = 'Calle 98 # 8 - 28',
		clientes_responsable = 'Wilson Rodriguez',
		clientes_celular = '1234567890',
		clientes_email = 'email@email.com',
		clientes_ciudad = 1,
		clientes_tipo_letra = '',
		clientes_cantidad_proyectos = 1,
		clientes_color_corporativo = '',
		clientes_responsable_creacion = None
	)



	#  Proyecto
	idProyecto      = guard_dbProyectos.insert(
		proyectos_codigo = 'PRO-01',
		proyectos_nombre_proyecto = 'Brujula Soluciones Integrales',
		proyectos_nit_proyecto = '102030',
		proyectos_ciudad = 1,
		proyectos_direccion_proyecto = 'Calle 98 # 8 - 28',
		proyectos_nombre_administrador = 'Wilson Rodriguez',
		proyectos_celular_administrador = '1234567890',
		proyectos_email_administrador = 'email@email.com',
		proyectos_telefono_administrador = '1234567',
		proyectos_cantidad_interiores = 0,
		proyectos_cantidad_predios = 1,
		proyectos_responsable_creacion = None,
		proyectos_tipo_letra = '',
		proyectos_color_corporativo = ''
	)
	idProyecto      = guard_dbCliePro.insert(
		proyectos_cliente = idCliente,
		proyectos_proyecto = idProyecto
	)
	#  Usuarios

	idUsuarioDeveloper       = guard_dbUsuarios.insert(
		first_name = 'Developer',
		last_name = 'FullStack',
		email = 'developer@bsi.com',
		password =  db.auth_user.password.validate('abigel2@12')[0],
		cliente = idCliente,
		tipo = 'Developer',
		proyecto =  idProyecto,
	)

	idGerente       = guard_dbUsuarios.insert(
		first_name = 'Gerente',
		last_name = 'General',
		email = 'gerencia@bsi.com',
		password =  db.auth_user.password.validate('gerenciabsi')[0],
		cliente = idCliente,
		tipo = 'Administrador',
		proyecto =  idProyecto,
	)

	
	#  Empleados
	idEmpleGerente    = guard_dbemple.insert(
		empleados_nombres = 'Wilson Rodriguez',
		empleados_identificacion =  '102030',
		empleados_celular =  '1234567890',
		empleados_cliente =  1,
		empleados_proyecto =  1,
		empleados_fecha_ingreso =  '20200101',
		empleados_fecha_nacimiento =  '20200101',
		empleados_contacto_emergancia =  'Javier Rodriguez',
		empleados_parentesco_emergancia =  'Hermana',
		empleados_telefono_emergancia =  '1234567890',
		empleados_direccion_recidencia =  'Centro',
		empleados_email =  'email@email.com',
		empleados_genero =  'Masculino',
		empleados_observaciones =  'Gerente',

	)
	idEmpleDev    =  guard_dbemple.insert(
		empleados_nombres = 'Luis Cortes',
		empleados_identificacion = '906030',
		empleados_celular =  '1234567890',
		empleados_cliente =  1,
		empleados_proyecto =  1,
		empleados_fecha_ingreso =  '20200101',
		empleados_fecha_nacimiento =  '20200101',
		empleados_contacto_emergancia =  'Kelly Cortes',
		empleados_parentesco_emergancia =  'Hermana',
		empleados_telefono_emergancia =  '1234567890',
		empleados_direccion_recidencia =  'Soacha',
		empleados_email =  'email@email.com',
		empleados_genero =  'Masculino',
		empleados_observaciones =  'Developer',
	)

	guard_dbemp_usu.insert(
	    usuario_empleado_empleado = idEmpleGerente,
	    usuario_empleado_usuario = idGerente,
	)

	guard_dbemp_usu.insert(
	    usuario_empleado_empleado = idEmpleDev,
	    usuario_empleado_usuario = idUsuarioDeveloper,
	)

