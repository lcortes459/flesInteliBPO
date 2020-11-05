# -*- coding: utf-8 -*-


@auth.requires_login()
def paises():
	response.title       = T("Configuraciones | Paises")
	response.subTitle    = T("Mis Paises")
	response.icono       = 'globe'
	response.botton       = ''
	multi_dbPaises       = db.paises
	#multi_dbEmpleados.empleados_cliente.default  = empresa
	#query                = ( multi_dbEmpleados.empleados_cliente==empresa )
	links = []
	paises            = SQLFORM.grid(
		multi_dbPaises,
			deletable        = False,
			details          = False,
			csv              = False,
			maxtextlength    = 50,
			editable         = True,
			paginate         = 100,
			links            = links,
			orderby          = multi_dbPaises.id
		)
	return locals()



@auth.requires_login()
def ciudades():
	response.title       = T("Configuraciones | Ciudades")
	response.subTitle    = T("Mis Ciudades")
	response.icono       = 'map'
	response.botton       = ''
	multi_dbCiudades     = db.ciudades
	#multi_dbEmpleados.empleados_cliente.default  = empresa
	#query                = ( multi_dbEmpleados.empleados_cliente==empresa )
	links = []
	ciudades            = SQLFORM.grid(
		multi_dbCiudades,
			deletable        = False,
			details          = False,
			csv              = False,
			maxtextlength    = 50,
			editable         = True,
			paginate         = 100,
			links            = links,
			orderby          = multi_dbCiudades.id
		) 
	return locals()


@auth.requires_login()
def planes():
	response.title        = T("Configuraciones | Planes")
	response.subTitle     = T("Mis Planes")
	response.icono        = 'credit-card'
	response.botton       = ''
	multi_dbPlanes        = db.planes
	links = []
	planes                = SQLFORM.grid(
		multi_dbPlanes,
			deletable        = False,
			details          = False,
			csv              = False,
			maxtextlength    = 50,
			editable         = True,
			paginate         = 100,
			links            = links,
			orderby          = multi_dbPlanes.id
		) 
	return locals()


@auth.requires_login()
def proveedores():
	db_tableProveedores()
	response.title        = T("Configuraciones | proveedores")
	response.subTitle     = T("Mis proveedores")
	response.icono        = 'shopping-cart'
	response.botton       = ''
	multi_dbProveedores   = db.proveedores
	links = []
	proveedores                = SQLFORM.grid(
		multi_dbProveedores,
			deletable        = False,
			details          = False,
			csv              = False,
			maxtextlength    = 50,
			editable         = True,
			paginate         = 100,
			links            = links,
			orderby          = multi_dbProveedores.id
		) 
	return locals()




def getProyectoAsigar(id):
	multi_dbEmpleados    = db.empleados
	if db ( (multi_dbEmpleados.empleados_proyecto) & (multi_dbEmpleados.id==id) ).count()==0:
		reto = XML("""<span class=" label label-success" style="width:150px; font-size: 15px;"><b>Total</b></span>""")
	else:
		reto = XML("""<span class=" label label-warning" style="width:150px; font-size: 15px;"><b>Eventos</b></span>""")
		pass
	return reto



@auth.requires_login()
def empleados():
	response.title       = T("Configuraciones | Empleados")
	response.subTitle    = T("Mis Empleados")
	response.icono       = 'address-book'
	response.botton       = ''
	multi_dbEmpleados    = db.empleados
	multi_dbEmpleados.empleados_cliente.default  = empresa
	links = []
	# if grup=='Administrativo':
	# 	query                = ( multi_dbEmpleados.empleados_proyecto==proyecto )
	# elif grup=='Supervisor':
	# 	query                = ( multi_dbEmpleados.empleados_proyecto==proyecto )
	# else:
	# 	query                = ( multi_dbEmpleados.empleados_cliente==empresa )
	# 	# links = [
	# 	# 	dict(header='Proyecto', body=lambda r: DIV( getProyectoAsigar(r.id), _id='proyecto_%s' %r.id ) )
	# 	# ]
	# 	pass
	query                = ( multi_dbEmpleados.empleados_cliente==empresa )
	empleados            = SQLFORM.grid(
		query,
			deletable        = False,
			details          = False,
			csv              = False,
			maxtextlength    = 50,
			editable         = True,
			paginate         = 100,
			links            = links,
			orderby          = multi_dbEmpleados.id
		) 
	return locals()







