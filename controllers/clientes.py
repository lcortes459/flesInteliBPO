# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# Clientes
@auth.requires_login()
def listClientes():
	response.title        = T("Clientes")  
	response.subTitle     = T("Listado Clientes")
	response.icono        = 'handshake'
	response.botton       = ''
	multi_dbClientes      = db.clientes
	clientes       = db( (multi_dbClientes.id>1) ).select(multi_dbClientes.ALL,orderby=multi_dbClientes.id)
	return locals()


@auth.requires_login()
def cambioEstadoCliente():
	multi_data            = request.vars
	multi_dbClientes      = db.clientes
	multi_dbUsers         = db.auth_user
	resul                 = 'error'
	if int(multi_data.opc) == 1:
		db( multi_dbClientes.id == int(multi_data.id) ).update(clientes_estado=True)
		db( multi_dbUsers.cliente == int(multi_data.id) ).update(registration_key=None)
		resul = 'success'
	else:
		db( multi_dbClientes.id == int(multi_data.id) ).update(clientes_estado=False)
		db( multi_dbUsers.cliente == int(multi_data.id) ).update(registration_key=0)
		resul = 'success'
		pass
	return resul 


# Proyectos

@auth.requires_login()
def verProyectos():
	multi_data            = request.vars
	multi_dbCliProy       = db.clientesProyectos
	multi_dbProyectos     = db.proyectos
	proyectos             = db( multi_dbCliProy.proyectos_cliente == int(multi_data.idCliente) ).select(multi_dbProyectos.ALL,\
		left=(
			multi_dbProyectos.on(multi_dbProyectos.id==multi_dbCliProy.proyectos_proyecto)))
	return locals()




@auth.requires_login()
def cambioEstadoProyecto():
	multi_data            = request.vars
	multi_dbProyectos     = db.proyectos
	multi_dbUsers         = db.auth_user
	resul                 = 'error'
	if int(multi_data.opc) == 1:
		db( multi_dbProyectos.id    == int(multi_data.id) ).update(proyectos_estado=True)
		db( multi_dbUsers.proyecto  == int(multi_data.id) ).update(registration_key=None)
		resul = 'success'
	else:
		db( multi_dbProyectos.id    == int(multi_data.id) ).update(proyectos_estado=False)
		db( multi_dbUsers.proyecto  == int(multi_data.id) ).update(registration_key=0)
		resul = 'success'
		pass
	return resul 


@auth.requires_login()
def nuevoProyecto():
	print('Nuevo Proyecto')
	multi_data            = request.vars
	multi_dbCiudades       = db.ciudades
	multi_ciudades         = db(multi_dbCiudades.ciudades_estado == True).select(multi_dbCiudades.ALL)
	return locals()


@auth.requires_login()
def guardarProyecto():
	multi_data             = request.vars
	multi_dbProyectos      = db.proyectos
	multi_dbClientesProye  = db.clientesProyectos
	multi_dbUsers          = db.auth_user
	multi_dbInteProy       = db.interioresProyectos
	resul                  = 'error'
	idProyecto             = multi_dbProyectos.insert(**multi_data)
	codigo                 = 'PROYGUA-'+str(multi_data.proyectos_cliente)+'-'+str(idProyecto)
	
	db( multi_dbProyectos.id == idProyecto).update(
		proyectos_codigo   = codigo
	)
	
	multi_dbClientesProye.insert(
		proyectos_cliente  = multi_data.proyectos_cliente,
		proyectos_proyecto = idProyecto
	)
	
	for pint in xrange(0,int(multi_data.proyectos_cantidad_interiores)):
			
		multi_dbInteProy.insert(
			interioresProyectos_proyecto    = idProyecto,
			interioresProyectos_interiores  = int(pint + 1)
		)
		pass
	
	password = multi_dbUsers.password.validate(str(multi_data.proyectos_nit_proyecto).replace('-','').replace('.','').replace(' ',''))[0]
	idUsuarioProyecto     = multi_dbUsers.insert(
		tipo              = 'Coordinador',
		cliente           = multi_data.proyectos_cliente,
		proyecto          = idProyecto,
		email             = multi_data.proyectos_email_administrador,
		password          = password,
		first_name        = 'Administrador',
		last_name         = 'Proyecto'
	)

	tmp                   = notificacionCreacionCliente(idProyecto)
	if tmp:
		resul = 'success'
	else:
		resul = 'email'
		pass
	return resul



@auth.requires_login()
def detalleProyecto():
	multi_data            = request.vars
	multi_dbProyectos     = db.proyectos
	return locals()


# Predios

@auth.requires_login()
def verPredios():
	multi_data            = request.vars
	multi_dbPredios       = db.interioresPredios
	predios               = db( multi_dbPredios.interioresPredios_interior == multi_data.idArea ).select(multi_dbPredios.ALL)
	return locals()


@auth.requires_login()
def nuevoPredio():
	multi_data            = request.vars
	multi_identi          = ['Casa','Apartamento','Lote','Oficina','Local']
	multi_pisos           = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']
	return locals()


@auth.requires_login()
def guardarPredio():
	multi_data            = request.vars
	multi_dbIntePredio    = db.interioresPredios
	multi_dbUsers         = db.auth_user
	resul                 = 'error'
	idPredio              = multi_dbIntePredio.insert(**multi_data)
	proyecto              = db.interioresProyectos[multi_data.interioresPredios_interior].interioresProyectos_proyecto
	tmpCliente            = db(db.clientesProyectos.proyectos_proyecto == proyecto).select(db.clientesProyectos.proyectos_cliente).first()
	cliente               = tmpCliente.proyectos_cliente
	codigo                = str(multi_data.interioresPredios_identificador)+'-'+str(db.interioresProyectos[multi_data.interioresPredios_interior].interioresProyectos_interiores)+'-'+str(multi_data.interioresPredios_piso)+'-'+str(multi_data.interioresPredios_predio)
	
	db( multi_dbIntePredio.id == idPredio).update(
		interioresPredios_codigo   = codigo
	)
	password = multi_dbUsers.password.validate('GUARDINWEB2020')[0]
	
	idUsuarioPredio       = multi_dbUsers.insert(
		tipo              = 'Residente',
		cliente           = cliente,
		proyecto          = proyecto,
		email             = 'email@email.com',
		password          = password,
		first_name        = 'Componente-'+str(db.interioresProyectos[multi_data.interioresPredios_interior].interioresProyectos_interiores),
		last_name         = str(multi_data.interioresPredios_identificador)+'-'+str(multi_data.interioresPredios_predio),
		registration_key  = idPredio
	)
	if idUsuarioPredio:
		resul = 'success'
		pass
	return resul 