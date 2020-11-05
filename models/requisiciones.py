# # -*- coding: utf-8 -*-

# def reqActivasTotales(tipo):
# 	multi_requi       = db.requisiciones
# 	if tipo == 'all':
# 		res		      = db( (multi_requi.estado=='Activa') | (multi_requi.estado=='Proceso')).count()
# 	else:
# 		#print('idUser',idUser)
# 		if tipo=='asesor':
# 			sql           = """
# 				SELECT
# 					COUNT(*)
# 				FROM
# 					requisiciones
# 				WHERE
# 					requisiciones.estado in ('Activa','Proceso')
# 				AND 
# 					requisiciones.creador = """+str(idUser)+"""
# 			""" 
# 			res		      = db.executesql(sql)
# 		else:
# 			sql           = """
# 				SELECT
# 					COUNT(*)
# 				FROM
# 					requisiciones
# 				WHERE
# 					requisiciones.estado in ('Activa','Proceso')
# 				AND 
# 					requisiciones.modulo = """+str(modAsigUsu(grup))+"""
# 			""" 
# 			res		      = db.executesql(sql)
# 			pass
# 		#print(res)
# 		pass
# 	# res           = []
# 	return res


# def modAsigUsu(tipo):
# 	multi_usuCoor     = db.cordinadoresDolientes
# 	if tipo=='Asesor':
# 		cordUsu                = db(multi_usuCoor.doliente==idUser).select(multi_usuCoor.cordinador).first()
# 		if cordUsu:
# 			modUsuario         = db(db.usuarioModulo.usuario==cordUsu.cordinador).select(db.usuarioModulo.modulo).first()
			
# 			if modUsuario:
# 				modulo         = modUsuario.modulo 
# 			else:
# 				modulo = 0	
# 				pass

# 		else:
# 			modulo = 0
# 			pass
# 	elif tipo == 'Clientes':
# 		modulo = 0
# 	else:	
# 		modUsuario    = db(db.usuarioModulo.usuario==idUser).select(db.usuarioModulo.modulo).first()
# 		if modUsuario:
# 			modulo         = modUsuario.modulo 
# 		else:
# 			modulo = 0	
# 			pass
# 		pass
# 	return int(modulo)

# def reqActivasTotalesModulos(modulo):

# 	multi_requi   = db.requisiciones
# 	res		      = db(multi_requi.estado=='Activa').count()
# 	res           = []
# 	if modulo == 'all':
# 		sql           = """
# 			SELECT 
# 				COUNT(*) as Cantidad,
# 				m.nombre as modulo,
# 				m.id
# 			FROM 
# 				requisiciones as re
# 			INNER JOIN 
# 				modulos as m on m.id = re.modulo
# 			WHERE 
# 				re.estado = 'Activa'
# 			GROUP BY 
# 				re.modulo
# 		""" 
# 	else:
# 		if modulo == 'asesor':
# 			campo  = "re.creador"
# 			condicion = idUser
# 		else:
# 			campo     = "re.modulo"
# 			condicion = str(modAsigUsu(grup))
# 			pass
# 		sql           = """
# 			SELECT
# 				COUNT(*) as Cantidad,
# 				e.nombre,
# 				e.id
# 			FROM
# 				requisiciones as re
# 			INNER JOIN sucursales as s on
# 				s.id = re.sucursal
# 			INNER JOIN empresas as e on 
# 				e.id = s.empresa_sucursal
# 			WHERE
# 				"""+str(campo)+""" = """+str(condicion)+""" 
# 			GROUP BY
# 				e.id
# 		"""
# 		pass
# 	res = db.executesql(sql)
# 	return res


# def reqAsesores(all):
# 	return res

# def asivamosMes(tipo):
	
# 	res = []
# 	if tipo == 'all':
# 		sql = """
			
# 			SELECT
# 				COUNT(*) as Cantidad,
# 				m.nombre as modulo,
# 				m.id
# 			FROM
# 				requisiciones as re
# 			INNER JOIN modulos as m on
# 				m.id = re.modulo
# 			WHERE
# 				MONTH(re.fecha_creacion) = MONTH(CURRENT_DATE)
# 			GROUP BY
# 				re.modulo

# 		"""

# 		sql = """
			
# 			SELECT
# 				COUNT(*) as Cantidad,
# 				m.nombre as modulo,
# 				m.id
# 			FROM
# 				requisiciones as re
# 			INNER JOIN modulos as m on
# 				m.id = re.modulo
# 			GROUP BY
# 				re.modulo

# 		"""
# 		tmp		      = db.executesql(sql)
# 		for x in tmp:
# 			res.append(
# 				dict(
# 					modulo    = x[1],
# 					cantidad  = x[0],
# 					idModulo  = x[2]
# 				)
# 			)
# 			pass
# 		# tmp = []
# 	else:
# 		tmp = []
# 		pass
# 	return res



# def verCotizacion(idCotizacion):
# 	multi_dbCotizaciones  = db.cotizaciones
# 	cotizaciones          = db( multi_dbCotizaciones.id == int(idCotizacion) ).select(multi_dbCotizaciones.ALL).last()
# 	cotizHtml = XML("""
# 		<div class="row">
# 	        <div class="col-sm-12 col-xl-6">
# 	            <ul class="list-group">
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Codigo</b>
# 	                    <span class="">
# 	                        <b> """+str(cotizaciones.cotizaciones_codigo)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Nit</b>
# 	                    <span class="">
# 	                        <b>"""+str(cotizaciones.cotizaciones_nit_proyecto)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Ciudad</b>
# 	                    <span class="">
# 	                        <b>"""+str(db.ciudades[cotizaciones.cotizaciones_ciudad].ciudades_nombre)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Dirección</b>
# 	                    <span class="">
# 	                        <b>"""+str(cotizaciones.cotizaciones_direccion_proyecto)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Administrador/Representante</b>
# 	                    <span class="">
# 	                        <b>"""+str(cotizaciones.cotizaciones_nombre_administrador)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Telefono</b>
# 	                    <span class="">
# 	                        <b>"""+str(cotizaciones.cotizaciones_telefono_administrador)+"""</b>
# 	                    </span>
# 	                </li>
# 	                 <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Interiores</b>
# 	                    <span class="">
# 	                        <b>"""+str(cotizaciones.cotizaciones_cantidad_interiores)+"""</b>
# 	                    </span>
# 	                </li>
# 	            </ul>
# 	        </div>
# 	        <div class="col-sm-12 col-xl-6">
# 	            <ul class="list-group">
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Valor</b>
# 	                    <span class="">
# 	                        <b> """+str(SetMoneda(float(db.planes[cotizaciones.cotizaciones_plan].planes_valor)))+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Celular</b>
# 	                    <span class="">
# 	                        <b>"""+str(cotizaciones.cotizaciones_celular_administrador)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Email</b>
# 	                    <span class="">
# 	                        <b>"""+str(cotizaciones.cotizaciones_email_administrador)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Estado</b>
# 	                    <span class="">
# 	                      <b>"""+str(cotizaciones.cotizaciones_estado)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Responsable</b>
# 	                    <span class="">
# 	                        <b>"""+str(db.auth_user[cotizaciones.cotizaciones_responsable_creacion].first_name)+""" """+str(db.auth_user[cotizaciones.cotizaciones_responsable_creacion].last_name)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <!-- Dabriela Vargas -->
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Fecha Creación</b>
# 	                    <span class="">
# 	                        <b>"""+str(fechaFormato(cotizaciones.cotizaciones_fecha_creacion,'fecha'))+""" """+str(fechaFormato(cotizaciones.cotizaciones_hora_creacion,'hora'))+"""</b>
# 	                    </span>
# 	                </li>
# 	                 <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Predios</b>
# 	                    <span class="">
# 	                        <b>"""+str(cotizaciones.cotizaciones_cantidad_predios)+"""</b>
# 	                    </span>
# 	                </li>
# 	            </ul>
# 	        </div>
# 	    </div>
# 	""")
# 	return cotizHtml


# def verOrden(idOrden):
# 	multi_dbOrdenesTrabajo  = db.ordenesTrabajo
# 	ordenes                 = db(multi_dbOrdenesTrabajo.id == idOrden).select(multi_dbOrdenesTrabajo.ALL).last()
# 	if ordenes.ordenesTrabajo_responsable_ejecucion: 
# 		nombre   = db.auth_user[ordenes.ordenesTrabajo_responsable_ejecucion].first_name 
# 		apellido = db.auth_user[ordenes.ordenesTrabajo_responsable_ejecucion].last_name 
# 	else: 
# 		nombre   = 'Sin'
# 		apellido = 'asignar'
# 		pass

# 	if ordenes.ordenesTrabajo_fecha_ejecucion != 0: 
# 		fecha   = fechaFormato(ordenes.ordenesTrabajo_fecha_ejecucion,'fecha')
# 		hora    = fechaFormato(ordenes.ordenesTrabajo_hora_ejecucion,'fecha')
# 	else: 
# 		fecha   = 'Sin'
# 		hora    = 'ejecución'
# 		pass

# 	ordenHtml = XML("""
# 		<div class="row">
# 	        <div class="col-sm-12 col-xl-12">
# 	            <ul class="list-group">
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Codigo cotización</b>
# 	                    <span class="">
# 	                        <b> """+str(db.cotizaciones[ordenes.ordenesTrabajo_cotizacion].cotizaciones_codigo)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Codigo orden</b>
# 	                    <span class="">
# 	                        <b>"""+str(ordenes.ordenesTrabajo_codigo)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Responsable creación</b>
# 	                    <span class="">
# 	                        <b>"""+str(db.auth_user[ordenes.ordenesTrabajo_responsable_creacion].first_name)+""" """+str(db.auth_user[ordenes.ordenesTrabajo_responsable_creacion].last_name)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Fecha Creación</b>
# 	                    <span class="">
# 	                        <b>"""+str(fechaFormato(ordenes.ordenesTrabajo_fecha_creacion,'fecha'))+""" """+str(fechaFormato(ordenes.ordenesTrabajo_hora_creacion,'hora'))+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Responsable ejecución</b>
# 	                    <span class="">
# 	                        <b>"""+str(nombre)+""" """+str(apellido)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Fecha Ejecucion</b>
# 	                    <span class="">
# 	                        <b>"""+str(fecha)+""" """+str(hora)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Estado</b>
# 	                    <span class="">
# 	                      <b>"""+str(ordenes.ordenesTrabajo_estado)+"""</b>
# 	                    </span>
# 	                </li>
# 	            </ul>
# 	        </div>
# 	    </div>
# 	""")
# 	return ordenHtml


# def verCliente(idCliente):
# 	multi_dbClientes        = db.clientes
# 	clientes                = db( multi_dbClientes.id == idCliente ).select(multi_dbClientes.ALL).last()
# 	if ( (clientes.clientes_estado == True) | (clientes.clientes_estado == 'True') ):
# 		estado  = '<span class="badge badge-success">Activo</span>'
# 	else:
# 		estado  = '<span class="badge badge-danger">Bloqueado</span>'
# 		pass
# 	clienteHtml = XML("""
# 		<div class="row">
# 	        <div class="col-sm-12 col-xl-6">
# 	            <ul class="list-group">
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Nit</b>
# 	                    <span class="">
# 	                        <b> """+str(clientes.clientes_nit)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Nombre/Razón social</b>
# 	                    <span class="">
# 	                        <b>"""+str(clientes.clientes_nombre)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Ciudad</b>
# 	                    <span class="">
# 	                        <b>"""+str(db.ciudades[clientes.clientes_ciudad].ciudades_nombre)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Dirección</b>
# 	                    <span class="">
# 	                        <b>"""+str(clientes.clientes_direccion)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Administrador/Representante</b>
# 	                    <span class="">
# 	                        <b>"""+str(clientes.clientes_responsable)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Celular</b>
# 	                    <span class="">
# 	                        <b>"""+str(clientes.clientes_celular)+"""</b>
# 	                    </span>
# 	                </li>
# 	            </ul>
# 	        </div>
# 	        <div class="col-sm-12 col-xl-6">
# 	            <ul class="list-group">
# 	            	<li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Email</b>
# 	                    <span class="">
# 	                        <b>"""+str(clientes.clientes_email)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Código orden</b>
# 	                    <span class="">
# 	                        <b> """+str(db.ordenesTrabajo[clientes.clientes_ordenTrabajo].ordenesTrabajo_codigo)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Estado</b>
# 	                    <span class="">
# 	                      <b>"""+str(estado)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Responsable creación</b>
# 	                    <span class="">
# 	                        <b>"""+str(db.auth_user[clientes.clientes_responsable_creacion].first_name)+""" """+str(db.auth_user[clientes.clientes_responsable_creacion].last_name)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Fecha creación</b>
# 	                    <span class="">
# 	                        <b>"""+str(fechaFormato(clientes.clientes_fecha_creacion,'fecha'))+""" """+str(fechaFormato(clientes.clientes_hora_creacion,'hora'))+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Catindad proyectos</b>
# 	                    <span class="badge badge-success">
# 	                        <b>"""+str(clientes.clientes_cantidad_proyectos)+"""</b>
# 	                    </span>
# 	                </li>
# 	            </ul>
# 	        </div>
# 	    </div>
# 	""")
# 	return clienteHtml


# def verProyecto(idProyecto):
# 	multi_dbProyectos     = db.proyectos
# 	proyectos          = db( multi_dbProyectos.id == int(idProyecto) ).select(multi_dbProyectos.ALL).last()
# 	if ( (proyectos.proyectos_estado == True) | (proyectos.proyectos_estado == 'True') ):
# 		estado  = '<span class="badge badge-success">Activo</span>'
# 	else:
# 		estado  = '<span class="badge badge-danger">Bloqueado</span>'
# 		pass
# 	proyecHtml = XML("""
# 		<div class="row">
# 	        <div class="col-sm-12 col-xl-6">
# 	            <ul class="list-group">
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Codigo proyecto</b>
# 	                    <span class="">
# 	                        <b> """+str(proyectos.proyectos_codigo)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Nit</b>
# 	                    <span class="">
# 	                        <b>"""+str(proyectos.proyectos_nit_proyecto)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Nombre proyecto</b>
# 	                    <span class="">
# 	                        <b>"""+str(proyectos.proyectos_nombre_proyecto)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Ciudad</b>
# 	                    <span class="">
# 	                        <b>"""+str(db.ciudades[proyectos.proyectos_ciudad].ciudades_nombre)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Dirección</b>
# 	                    <span class="">
# 	                        <b>"""+str(proyectos.proyectos_direccion_proyecto)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Administrador/Representante</b>
# 	                    <span class="">
# 	                        <b>"""+str(proyectos.proyectos_nombre_administrador)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Telefono</b>
# 	                    <span class="">
# 	                        <b>"""+str(proyectos.proyectos_telefono_administrador)+"""</b>
# 	                    </span>
# 	                </li>
# 	            </ul>
# 	        </div>
# 	        <div class="col-sm-12 col-xl-6">
# 	            <ul class="list-group">
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Celular</b>
# 	                    <span class="">
# 	                        <b>"""+str(proyectos.proyectos_celular_administrador)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Email</b>
# 	                    <span class="">
# 	                        <b>"""+str(proyectos.proyectos_email_administrador)+"""</b>
# 	                    </span>
# 	                </li>
# 	            	<li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Interiores</b>
# 	                    <span class="">
# 	                        <b>"""+str(proyectos.proyectos_cantidad_interiores)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Predios</b>
# 	                    <span class="">
# 	                        <b>"""+str(proyectos.proyectos_cantidad_predios)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Responsable</b>
# 	                    <span class="">
# 	                        <b>"""+str(db.auth_user[proyectos.proyectos_responsable_creacion].first_name)+""" """+str(db.auth_user[proyectos.proyectos_responsable_creacion].last_name)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Estado</b>
# 	                    <span class="">
# 	                      <b>"""+str(estado)+"""</b>
# 	                    </span>
# 	                </li>
# 	                <li class="list-group-item d-flex list-group-item-action justify-content-between align-items-center">
# 	                    <b>Fecha Creación</b>
# 	                    <span class="">
# 	                        <b>"""+str(fechaFormato(proyectos.proyectos_fecha_creacion,'fecha'))+""" """+str(fechaFormato(proyectos.proyectos_hora_creacion,'hora'))+"""</b>
# 	                    </span>
# 	                </li>
# 	            </ul>
# 	        </div>
# 	    </div>
# 	""")
# 	return proyecHtml

# def verPredio(idArea):
# 	pass

# def configuracionZonas(idProyecto):
# 	multi_dbProyectos  = db.proyectos
# 	multi_dbInteProy   = db.interioresProyectos
# 	proyectos          = db( multi_dbInteProy.interioresProyectos_proyecto == int(idProyecto) ).select(multi_dbInteProy.ALL)
# 	zonasHtml          = ''
# 	if proyectos:
# 		for x in proyectos:
# 			predios        = db(db.interioresPredios.interioresPredios_interior == x.id).count()
# 			if predios == 0:
# 				propietarios = 0
# 				residentes   = 0
# 				novedades    = 0
# 			else:
# 				propietarios = 999999
# 				residentes   = 999999
# 				novedades    = 999999
# 				pass
# 			zonasHtml += """ 
# 				<div class="col-md-3">
# 	        		<div class="card card-widget widget-user">
# 	          			<div class="widget-user-header bg-info">
# 							<h5 class="widget-user-desc">Componente """+str(x.interioresProyectos_interiores)+"""</h5>
# 	          			</div>
# 		              	<div class="widget-user-image">
# 			                <img class="img-circle elevation-2" src=" """+str(getFotoUsuario(idUser))+"""" alt="User Avatar">
# 			            </div>
# 		              	<div class="card-footer p-0">
# 			                <ul class="nav flex-column">
# 			                  	<li class="nav-item">
# 				                    <a href="#!" class="nav-link" style="color:#000000;" onclick="ctz.verPredios('areasGenerales','predios',"""+str(x.id)+""",'Listado de predios (Componente """+str(x.interioresProyectos_interiores)+""")')">
# 				                      Predios <span class="float-right badge bg-info">"""+str(predios)+"""</span>
# 				                    </a>
# 			                  	</li>
# 			                  	<li class="nav-item">
# 				                    <a href="#!" class="nav-link" style="color:#000000;" onclick="alert("""+str(x.id)+""")">
# 				                      Propietarios <span class="float-right badge bg-info">"""+str(propietarios)+"""</span>
# 				                    </a>
# 			                  	</li>
# 			                  	<li class="nav-item">
# 				                    <a href="#!" class="nav-link" style="color:#000000;" onclick="alert("""+str(x.id)+""")">
# 				                      Residentes <span class="float-right badge bg-info">"""+str(residentes)+"""</span>
# 				                    </a>
# 			                  	</li>
# 			                  	<li class="nav-item">
# 				                    <a href="#!" class="nav-link" style="color:#000000;" onclick="alert("""+str(x.id)+""")">
# 				                      Novedades <span class="float-right badge bg-info">"""+str(novedades)+"""</span>
# 				                    </a>
# 			                 	</li>
# 			                </ul>
# 		              	</div>
# 	              	</div>
# 	            </div>
# 			"""
# 			pass
# 	else:
# 		zonasHtml += """
# 			<div class="container" id="contenedorVacioCotizacion">
# 				<div class="row">
# 					<div class="col col-lg-12">
# 						<blockquote>
# 		                  <p>En estos momentos no tienes Componentes creadps.</p>
# 		                  <small>Para crear un Componente <cite title="Source Title"><a href="#!" onclick="ctz.primeraCotizacion();">Click aquí..</a></cite></small>
# 		                </blockquote>
# 					</div>	
# 				</div>
# 			</div>	
# 		"""
# 		pass
# 	return zonasHtml


# def configuracionFormatosDatos(idProyecto):
# 	resul =  """
# 		<div class="container" id="contenedorVacioCotizacion">
# 			<div class="row">
# 				<div class="col col-lg-12">
# 					<blockquote>
# 	                  <p>En estos momentos no tienes Componentes creadps.</p>
# 	                  <small>Para crear un Componente <cite title="Source Title"><a href="#!">Click aquí..</a></cite></small>
# 	                </blockquote>
# 				</div>	
# 			</div>
# 		</div>
# 	"""	
# 	return resul