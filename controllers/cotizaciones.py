# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- Cotizaciones ----
@auth.requires_login()
def nuevaCotizacion():
	multi_data            = request.vars
	multi_dbCotizaciones  = db.cotizaciones
	idInsert              = multi_dbCotizaciones.insert(**multi_data)
	codigo                = 'COTGUA-'+str(idInsert)
	db( multi_dbCotizaciones.id == idInsert).update(
		cotizaciones_codigo = codigo
	)
	tmp                   = notificacionCotizacion(idInsert,'',0,'Aviso Importante. Verificar nueva cotización de GuardianWeb','Cotización GuardianWeb')
	if str(tmp) == '1':
		resul = str(codigo)
	else:
		resul = '0'
		pass
	return resul



@auth.requires_login()
def listCotizaciones():
	response.title        = T("Cotizaciones")  
	response.subTitle     = T("Listado Cotizaciones")
	response.icono        = 'list'
	multi_dbCotizaciones  = db.cotizaciones
	cotizaciones       = db( multi_dbCotizaciones.cotizaciones_estado == 'Abierta' ).select(multi_dbCotizaciones.ALL,orderby=multi_dbCotizaciones.id)
	if len(cotizaciones)> 0:
		response.botton       = """<button class="btn btn-block btn-primary" type="button" onclick="ctz.siguienteDiv('listadoCotizaciones','nuevaCotizacion','input');"><i class="fa fa-plus"></i></button>"""
	else:
		response.botton       = ''
		pass
	return locals()



@auth.requires_login()
def verCotizaciones():
	multi_data            = request.vars
	return locals()

def valorPlanes():
	import gluon.contrib.simplejson
	multi_data         = request.vars
	multi_dbPlanes     = db.planes
	planes             = db( multi_data.idPlan == multi_dbPlanes.id ).select(multi_dbPlanes.planes_valor)
	return gluon.contrib.simplejson.dumps(planes.as_list())


def planes():
	import gluon.contrib.simplejson
	multi_data         = request.vars
	multi_dbPlanes     = db.planes
	planes             = db( str(multi_data.planes) == multi_dbPlanes.planes_tipo ).select(multi_dbPlanes.planes_tipo,multi_dbPlanes.id,multi_dbPlanes.planes_nombre,\
		multi_dbPlanes.planes_minimo_rango_proyectos,multi_dbPlanes.planes_maximo_rango_proyectos)
	print('Data:', multi_data)
	planValor  = []
	for x in planes:
		print('x',x)
		if ( (int(multi_data.cantidad) >= int(x.planes_minimo_rango_proyectos)) & (int(multi_data.cantidad) <= int(x.planes_maximo_rango_proyectos)) ):
			planValor    = db( multi_dbPlanes.id == x.id ).select(multi_dbPlanes.planes_valor,multi_dbPlanes.id,multi_dbPlanes.planes_nombre)
			pass
		pass
	print('planValor',planValor)
	if len(planValor) > 0:
		return gluon.contrib.simplejson.dumps(planValor.as_list())
	else:
		return gluon.contrib.simplejson.dumps(planValor)
		pass

@auth.requires_login()
def editarCotizaciones():
	multi_data            = request.vars
	multi_dbCotizaciones  = db.cotizaciones
	cotizaciones          = db( multi_dbCotizaciones.id == int(multi_data.id) ).select(multi_dbCotizaciones.ALL)
	return locals()


@auth.requires_login()
def envioEmail():
	multi_data            = request.vars
	resul                 = 'error'
	tmp                   = notificacionCotizacion(multi_data.id,multi_data.emails,multi_data.opc,'Aviso Importante. Verificar nueva cotización de GuardianWeb','Cotización GuardianWeb')
	if int(tmp) > 0:
		resul = 'success'
	else:
		resul = 'error'
		pass
	return resul


@auth.requires_login()
def cambioEstado():
	multi_data            = request.vars
	multi_dbCotizaciones  = db.cotizaciones
	db( multi_dbCotizaciones.id == int(multi_data.id) ).update(cotizaciones_estado="Cancelada")
	resul = 'success'
	return resul 



# Odenes de trabajo

@auth.requires_login()
def ejecutarOrdenTrabajo():
	import gluon.contrib.simplejson
	multi_data            = request.vars
	idCliente,idOrden,nombreCliente,nombreProyecto,email  = ordenesTrabajos(multi_data.id)
	if idCliente > 0:
		data  = dict(
			idCliente       = idCliente,
			idOrden         = idOrden,
			nombreCliente   = nombreCliente,
			nombreProyecto  = nombreProyecto,
			resul           = 'success'
		)
	else:
		data  = dict(
			resul           = 'error'
		)
		pass
	return gluon.contrib.simplejson.dumps(data)


@auth.requires_login()
def ordenesTrabajo():
	response.title          = T("Ordenes Trabajo")  
	response.subTitle       = T("Listado Ordenes Trabajo")
	response.icono          = 'list'
	multi_dbOrdenesTrabajo  = db.ordenesTrabajo
	ordenesTrabajo          = db( multi_dbOrdenesTrabajo.ordenesTrabajo_estado == 'Abierta' ).select(multi_dbOrdenesTrabajo.ALL)

	if len(ordenesTrabajo)> 0:
		response.botton       = ''
	else:
		url                   = URL('cotizaciones','listCotizaciones')
		response.botton       = """<a href=" """+str(url)+""" " class="btn btn-block btn-primary" type="button">Ir a cotizaciones</a>"""
		pass
	return locals()



@auth.requires_login()
def detalleOrden():
	multi_data              = request.vars
	# multi_dbOrdenesTrabajo  = db.ordenesTrabajo
	# multi_dbClientes        = db.clientes
	# multi_dbProyectos       = db.proyectos
	# cotizTmp                = db( multi_dbOrdenesTrabajo.id == multi_data.idOrden ).select(multi_dbOrdenesTrabajo.ordenesTrabajo_cotizacion).last()
	# cotizacion              = cotizTmp.ordenesTrabajo_cotizacion
	# clienTmp                = db( multi_dbClientes.clientes_ordenTrabajo == multi_data.idOrden ).select(multi_dbClientes.id).last()
	# cliente                 = clienTmp.id
	# proyecTmp               = db( multi_dbProyectos.proyectos_cliente == cliente ).select(multi_dbProyectos.id).first()
	# proyecto                = proyecTmp.id
	print('multi_data',multi_data)
	return locals()



# Odenes de servicio

@auth.requires_login()
def ejecutarOrdenServicio():
	import gluon.contrib.simplejson
	multi_data            = request.vars
	print('multi_data',multi_data)
	idCliente = ordenesDeServicio(
		multi_data.id,
		multi_data.opc,
		multi_data.emails
	)
	if idCliente > 0:
		data  = dict(
			idCliente       = idCliente,
			idOrden         = 'idOrden',
			nombreCliente   = 'nombreCliente',
			nombreProyecto  = 'nombreProyecto',
			resul           = 'success'
		)
	else:
		data  = dict(
			resul           = 'error'
		)
		pass
	return gluon.contrib.simplejson.dumps(data) 



@auth.requires_login()
def ordenesServicio():
	response.title           = T("Ordenes Trabajo")  
	response.subTitle        = T("Listado Ordenes Servicio")
	response.icono           = 'list'
	multi_dbOrdenesServicio  = db.ordenesServicio
	ordenesServicio          = db( multi_dbOrdenesServicio.ordenesServicios_estado == 'Abierta' ).select(multi_dbOrdenesServicio.ALL)

	if len(ordenesServicio)> 0:
		response.botton       = ''
	else:
		url                   = URL('cotizaciones','listCotizaciones')
		response.botton       = """<a href=" """+str(url)+""" " class="btn btn-block btn-primary" type="button">Ir a cotizaciones</a>"""
		pass
	return locals()



@auth.requires_login()
def detalleOrdenServ():
	multi_data              = request.vars
	multi_dbOrdenesServicio  = db.ordenesServicio
	multi_dbClientes        = db.clientes
	multi_dbProyectos       = db.proyectos
	cotizTmp                = db( multi_dbOrdenesServicio.id == multi_data.idOrden ).select(multi_dbOrdenesServicio.ordenesTrabajo_cotizacion).last()
	cotizacion              = cotizTmp.ordenesTrabajo_cotizacion
	clienTmp                = db( multi_dbClientes.clientes_ordenTrabajo == multi_data.idOrden ).select(multi_dbClientes.id).last()
	cliente                 = clienTmp.id
	proyecTmp               = db( multi_dbProyectos.proyectos_cliente == cliente ).select(multi_dbProyectos.id).first()
	proyecto                = proyecTmp.id
	return locals()
