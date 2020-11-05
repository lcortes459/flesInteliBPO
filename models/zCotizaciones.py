# def nuevaCotizacion():
# 	multi_dbCiudades       = db.ciudades
# 	multi_dbPlanes         = db.planes
# 	multi_ciudades         = db(multi_dbCiudades.ciudades_estado == True).select(multi_dbCiudades.ALL)
# 	multi_planes           = db(multi_dbPlanes.planes_estado == True).select(multi_dbPlanes.planes_tipo,distinct=True,orderby=multi_dbPlanes.planes_tipo)
# 	ciudades               = []
# 	planes                 = []
# 	for x in multi_ciudades:
# 		ciudades.append('<option value="'+str(x.id)+'">'+str(x.ciudades_nombre)+'</option>')
# 		pass
# 	for p in multi_planes:
# 		planes.append('<option value="'+str(p.planes_tipo)+'">'+str(p.planes_tipo)+'</option>')
# 		pass
# 	cotizacion  = XML("""
# 		<form id="formularioCtz" onsubmit="return false;">

# 	        <div class="row">
# 	            <div class="form-group col-sm-12 col-md-4 col-lg-4">
# 	                <label for="cotizaciones_nombre_proyecto">Proyecto/Cliente *</label>
# 	                <input type="text" class="form-control" id="cotizaciones_nombre_proyecto" name="cotizaciones_nombre_proyecto" placeholder="Nombre Proyecto/Cliente">
# 	            </div>
# 	            <div class="form-group col-sm-12 col-md-4 col-lg-4">
# 	                <label for="cotizaciones_nit_proyecto">Nit *</label>
# 	                <input type="hidden" value="COTGUA-" id="cotizaciones_codigo" name="cotizaciones_codigo">
# 	                <input type="hidden" value="Abierta" id="cotizaciones_estado" name="cotizaciones_estado">
# 	                <input type="hidden" value="""+str(idUser)+""" id="cotizaciones_responsable_creacion" name="cotizaciones_responsable_creacion">
#                     <input type="hidden" value="""+str(int(str(fecha('fecha')).replace('-','')))+""" id="cotizaciones_fecha_creacion" name="cotizaciones_fecha_creacion">
#                     <input type="hidden" value="""+str(int(str(fecha('hora')).replace(':','')))+""" id="cotizaciones_hora_creacion" name="cotizaciones_hora_creacion">
#                     <input type="hidden" class="form-control" id="cotizaciones_cantidad_interiores" name="cotizaciones_cantidad_interiores" value="0">
# 	                <input type="text" class="form-control" id="cotizaciones_nit_proyecto" name="cotizaciones_nit_proyecto" placeholder="Nit Proyecto/Cliente">
# 	            </div>
# 	            <div class="form-group col-sm-12 col-md-4 col-lg-4">
# 	                <label for="cotizaciones_ciudad">Ciudad *</label>
# 	                <select class="form-control" style="width: 100%;" id="cotizaciones_ciudad" name="cotizaciones_ciudad">
# 	            		<option value="">Seleccione una ciudad</option>
# 	            		"""+str(" ".join(str(x) for x in ciudades))+"""
# 	              	</select>
# 	            </div>
# 	            <div class="form-group col-sm-12 col-md-4 col-lg-4">
# 	                <label for="cotizaciones_direccion_proyecto">Dirección *</label>
# 	                <input type="text" class="form-control" id="cotizaciones_direccion_proyecto" name="cotizaciones_direccion_proyecto" placeholder="Direccion Proyecto/Cliente">
# 	            </div>
# 	            <div class="form-group col-sm-12 col-md-4 col-lg-4">
# 	                <label for="cotizaciones_nombre_administrador">Administrador/Representante *</label>
# 	                <input type="text" class="form-control" id="cotizaciones_nombre_administrador" name="cotizaciones_nombre_administrador" placeholder="Administrador/Representante">
# 	            </div>
# 	            <div class="form-group col-sm-12 col-md-4 col-lg-4">
# 	                <label for="cotizaciones_telefono_administrador">Telefono (opcional)</label>
# 	                <input type="text" class="form-control" id="cotizaciones_telefono_administrador" name="cotizaciones_telefono_administrador" placeholder="Telefono Proyecto/Cliente">
# 	            </div>
# 	        </div>
# 	        <div class="row">
# 	            <div class="form-group col-sm-12 col-md-4 col-lg-4">
# 	                <label for="cotizaciones_celular_administrador">Celular *</label>
# 	                <input type="text" class="form-control" id="cotizaciones_celular_administrador" name="cotizaciones_celular_administrador" placeholder="Celular Proyecto/Cliente">
# 	            </div>
# 	            <div class="form-group col-sm-12 col-md-4 col-lg-4">
# 	                <label for="cotizaciones_email_administrador">E-mail *</label>
# 	                <input type="text" class="form-control" id="cotizaciones_email_administrador" name="cotizaciones_email_administrador" placeholder="E-mail Administrador/Representante" pattern="^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$">
# 	            </div>
# 	            <div class="form-group col-sm-12 col-md-4 col-lg-4">
# 	                <label for="cotizaciones_cantidad_interiores">Cantidad inmuebles *</label>
# 	                <input type="text" class="form-control" id="cotizaciones_cantidad_predios" name="cotizaciones_cantidad_predios" placeholder="Cantidad inmuebles">
# 	            </div>
# 	        </div>
# 	        <div class="row">
# 	            <div class="form-group col-sm-12 col-md-4 col-lg-4">
# 	                <label for="cotizaciones_tipo_plan">Tipos Plan</label>
# 	               	<select class="form-control" style="width: 100%;" id="cotizaciones_tipo_plan"  onchange="ctz.planes($(this).val());">
# 	            		<option value="">Seleccione un tipo plan</option>
# 	            		"""+str(" ".join(str(b) for b in planes))+"""
# 	              	</select>
# 	            </div>
# 	            <div class="form-group col-sm-12 col-md-4 col-lg-4">
# 	                <label for="cotizaciones_plan">Plan</label>
# 	                <input type="text" class="form-control" readonly="" id="nombre_plan">
# 	                <input type="hidden" class="form-control" id="cotizaciones_plan" name="cotizaciones_plan" value="0">
# 	               	<!--select class="form-control" disabled style="width: 100%;" id="cotizaciones_plan" name="cotizaciones_plan" onchange="ctz.valorPlan($(this).val());">
	            		
# 	              	</select-->
# 	            </div>
# 	            <div class="form-group col-sm-12 col-md-4 col-lg-4">
# 	                <label for="planes">Valor plan</label>
# 	                <input type="text" class="form-control" readonly="" id="valor_plan">
# 	            </div>
# 	        </div>
# 	        <div class="row">
# 	            <div class="form-group col-sm-12 col-md-12 col-lg-12">
# 	                <label for="cotizaciones_observacion">Observaciones</label>
# 	                <textarea id="cotizaciones_observacion" name="cotizaciones_observacion" rows="3" class="form-control" placeholder="Observaciones.."></textarea>
# 	            </div>
# 	        </div>
# 	        <div class="row" id="botoneraGurdarCotizacion">
# 	            <div class="form-group col-sm-12 col-md-6 col-lg-6">
# 	                <a href="#!" class="btn btn-block btn-secondary" onclick="template.limpiar('formularioCtz','cotizaciones_nombre_proyecto');">Limpiar cotización</a>
# 	            </div>
# 	            <div class="form-group col-sm-12 col-md-6 col-lg-6">
# 	                <a href="#!" class="btn btn-block btn-primary" id="btnGuardarCotizacion">Crear cotización</a>
# 	            </div>
# 	        </div>
# 	        <div class="row" id="botoneraGurdando" style="display:none;">
#                 <div class="col col-12">
#                     <a href="#!" class="btn btn-primary btn-block disabled">
#                         <span class="spinner-grow spinner-grow-sm"></span>
#                         Un momento estamos guardando sus datos
#                         <span class="spinner-grow spinner-grow-sm"></span>
#                         <!-- <i class="fa fa-spinner fa-spen"></i> -->
#                     </a>
#                 </div>
#             </div>
# 	    </form>
# 	""")
# 	return cotizacion

# # def verCotizacion(idCotizacion):
# # 	multi_dbCotizaciones  = db.cotizaciones
# # 	cotizaciones          = db( multi_dbCotizaciones.id == int(idCotizacion) ).select(multi_dbCotizaciones.ALL)
# # 	return cotizacion

# def ordenesTrabajos(idCotizacion):
# 	multi_dbCotizaciones   = db.cotizaciones
# 	multi_dbOrdenesTraba   = db.ordenesTrabajo
# 	multi_dbClientes       = db.clientes
# 	multi_dbProyectos      = db.proyectos
# 	multi_dbClientesProye  = db.clientesProyectos
# 	multi_dbUsers          = db.auth_user
# 	multi_dbInteProy       = db.interioresProyectos
# 	idCliente              = 0
# 	idProyecto             = 0
# 	idOrden                = 0
# 	nombreCliente          = ''
# 	nombreProyecto         = ''
# 	datosCotizacion        = db(multi_dbCotizaciones.id == idCotizacion).select(multi_dbCotizaciones.ALL)
# 	if datosCotizacion:
# 		for x in datosCotizacion:
# 			idOrden = multi_dbOrdenesTraba.insert(
# 				ordenesTrabajo_cotizacion           = x.id,
# 				ordenesTrabajo_responsable_creacion = idUser
# 			)
# 			db( multi_dbCotizaciones.id == idCotizacion).update(
# 				cotizaciones_estado = 'Orden de trabajo'
# 			)
# 			print('Datos idOrden', idOrden)
# 			codigo                = 'ORDGUA-'+str(idOrden)
# 			db( multi_dbOrdenesTraba.id == idOrden).update(
# 				ordenesTrabajo_codigo = codigo
# 			)
# 			idCliente = multi_dbClientes.insert(
# 				clientes_nombre                = x.cotizaciones_nombre_proyecto,
# 				clientes_nit                   = x.cotizaciones_nit_proyecto,
# 				clientes_ordenTrabajo          = idOrden,
# 				clientes_responsable_creacion  = idUser,
# 				clientes_responsable           = x.cotizaciones_nombre_administrador,
# 				clientes_celular               = x.cotizaciones_celular_administrador,
# 				clientes_email                 = x.cotizaciones_email_administrador,
# 				clientes_ciudad                = x.cotizaciones_ciudad
# 			)
# 			print('Datos idCliente', idCliente)
# 			idProyecto  = multi_dbProyectos.insert(
# 				proyectos_cliente                 = idCliente,
# 				proyectos_nombre_proyecto         = x.cotizaciones_nombre_proyecto,
# 				proyectos_nit_proyecto            = x.cotizaciones_nit_proyecto,
# 				proyectos_ciudad                  = x.cotizaciones_ciudad,
# 				proyectos_direccion_proyecto      = x.cotizaciones_direccion_proyecto,
# 				proyectos_nombre_administrador    = x.cotizaciones_nombre_administrador,
# 				proyectos_celular_administrador   = x.cotizaciones_celular_administrador,
# 				proyectos_email_administrador     = x.cotizaciones_email_administrador,
# 				proyectos_telefono_administrador  = x.cotizaciones_telefono_administrador,
# 				proyectos_cantidad_interiores     = x.cotizaciones_cantidad_interiores,
# 				proyectos_cantidad_predios        = x.cotizaciones_cantidad_predios,
# 				proyectos_responsable_creacion    = idUser,
# 			)
# 			codigo                = 'PROYGUA-'+str(idCliente)+'-'+str(idProyecto)
# 			db( multi_dbProyectos.id == idProyecto).update(
# 				proyectos_codigo = codigo
# 			)
# 			print('Datos idProyecto', idProyecto)

# 			for pint in xrange(0,int(x.cotizaciones_cantidad_interiores)):
			
# 				multi_dbInteProy.insert(
# 					interioresProyectos_proyecto    = idProyecto,
# 					interioresProyectos_interiores  = int(pint + 1)
# 				)
# 				pass

# 			multi_dbClientesProye.insert(
# 				proyectos_cliente  = idCliente,
# 				proyectos_proyecto = idProyecto
# 			)
# 			password = multi_dbUsers.password.validate(str(x.cotizaciones_nit_proyecto).replace('-','').replace('.','').replace(' ',''))[0]
# 			idUsuarioCliente      = multi_dbUsers.insert(
# 				tipo              = 'Cliente',
# 				cliente           = idCliente,
# 				proyecto          = 0,
# 				email             = x.cotizaciones_email_administrador,
# 				password          = password,
# 				first_name        = 'Usuario',
# 				last_name         = 'Cliente'
# 			)
# 			print('Datos idUsuarioCliente', idUsuarioCliente)
# 			idUsuarioProyecto     = multi_dbUsers.insert(
# 				tipo              = 'Coordinador',
# 				cliente           = idCliente,
# 				proyecto          = idProyecto,
# 				email             = x.cotizaciones_email_administrador,
# 				password          = password,
# 				first_name        = 'Administrador',
# 				last_name         = 'Proyecto'
# 			)
# 			print('Datos idUsuarioProyecto', idUsuarioProyecto)
# 			tmp                   = notificacionCreacionCliente(idProyecto)
# 			if tmp:
# 				email = 1
# 			else:
# 				email = 0
# 				pass
# 			pass
# 		pass
# 	return idCliente,idOrden,nombreCliente,nombreProyecto,email



# def documentos(idEmpresa):
# 	docDbEmpresas   = db.fileEmpresas
# 	if db(docDbEmpresas.empresa_sucursal==idEmpresa).count()>0:
# 		req = db(docDbEmpresas.empresa_sucursal==idEmpresa).select(docDbEmpresas.ALL)
# 	else:
# 		req = 'documentos'
# 		pass
# 	return req



# def ordenesDeServicio(idCotizacion,opc,emails):

# 	print('Estoy acaaaaaaa')
# 	print('Estoy idCotizacion',idCotizacion)
# 	print('Estoy opc', opc)
# 	print('Estoy emails',emails)
# 	multi_dbCotizaciones   = db.cotizaciones
# 	multi_dbOrdenesServ    = db.ordenesServicio
# 	multi_dbOrdenesTraba   = db.ordenesTrabajo
# 	multi_dbClientes       = db.clientes
# 	multi_dbProyectos      = db.proyectos
# 	multi_dbClientesProye  = db.clientesProyectos
# 	multi_dbUsers          = db.auth_user
# 	multi_dbInteProy       = db.interioresProyectos
# 	idCliente              = 0
# 	idProyecto             = 0
# 	idOrden                = 0
# 	nombreCliente          = ''
# 	nombreProyecto         = ''
# 	datosCotizacion        = db(multi_dbCotizaciones.id == idCotizacion).select(multi_dbCotizaciones.ALL)
# 	if datosCotizacion:
# 		for ctz in datosCotizacion:

# 			#  Crear orden de servicio

# 			idOrdenSer = multi_dbOrdenesServ.insert(
# 				ordenesServicios_cotizacion           = ctz.id,
# 				ordenesServicios_responsable_creacion = idUser
# 			)

# 			#  Crear codigo de la orden de servicio
# 			print('Datos idOrdenSer', idOrdenSer)
# 			codigoServ               = 'ORDSERGUA-'+str(idOrdenSer)
# 			db( multi_dbOrdenesServ.id == idOrdenSer).update(
# 				ordenesServicios_codigo = codigoServ
# 			)

# 			#  Actualizar la cotización
# 			db( multi_dbCotizaciones.id == idCotizacion).update(
# 				cotizaciones_estado = 'Orden de servicio'
# 			)

# 			#  Crear orden de trabajo

# 			idOrdenTra = multi_dbOrdenesTraba.insert(
# 				ordenesTrabajo_cotizacion           = ctz.id,
# 				ordenesTrabajo_ordenServicio        = idOrdenSer,
# 				ordenesTrabajo_responsable_creacion = idUser
# 			)
			
# 			codigoTra                = 'ORDTRAGUA-'+str(idOrdenTra)

# 			db( multi_dbOrdenesTraba.id == idOrdenTra).update(
# 				ordenesTrabajo_codigo = codigoTra
# 			)

# 			#  Crear cliente 
			
# 			idCliente = multi_dbClientes.insert(
# 				clientes_nombre                = ctz.cotizaciones_nombre_proyecto,
# 				clientes_nit                   = ctz.cotizaciones_nit_proyecto,
# 				clientes_ordenTrabajo          = idOrdenTra,
# 				clientes_responsable_creacion  = idUser,
# 				clientes_responsable           = ctz.cotizaciones_nombre_administrador,
# 				clientes_celular               = ctz.cotizaciones_celular_administrador,
# 				clientes_email                 = ctz.cotizaciones_email_administrador,
# 				clientes_ciudad                = ctz.cotizaciones_ciudad
# 			)
# 			print('Datos idCliente', idCliente)

# 			#  Crear proyecto

# 			idProyecto  = multi_dbProyectos.insert(
# 				proyectos_cliente                 = idCliente,
# 				proyectos_nombre_proyecto         = ctz.cotizaciones_nombre_proyecto,
# 				proyectos_nit_proyecto            = ctz.cotizaciones_nit_proyecto,
# 				proyectos_ciudad                  = ctz.cotizaciones_ciudad,
# 				proyectos_direccion_proyecto      = ctz.cotizaciones_direccion_proyecto,
# 				proyectos_nombre_administrador    = ctz.cotizaciones_nombre_administrador,
# 				proyectos_celular_administrador   = ctz.cotizaciones_celular_administrador,
# 				proyectos_email_administrador     = ctz.cotizaciones_email_administrador,
# 				proyectos_telefono_administrador  = ctz.cotizaciones_telefono_administrador,
# 				proyectos_cantidad_interiores     = ctz.cotizaciones_cantidad_interiores,
# 				proyectos_cantidad_predios        = ctz.cotizaciones_cantidad_predios,
# 				proyectos_responsable_creacion    = idUser,
# 			)
# 			codigo                = 'PROYGUA-'+str(idCliente)+'-'+str(idProyecto)
# 			db( multi_dbProyectos.id == idProyecto).update(
# 				proyectos_codigo = codigo
# 			)
# 			print('Datos idProyecto', idProyecto)

# 			#  Crear proyecto cliente
# 			multi_dbClientesProye.insert(
# 				proyectos_cliente  = idCliente,
# 				proyectos_proyecto = idProyecto
# 			)

# 			#  Crear usuario cliente y proyecto

# 			password = multi_dbUsers.password.validate(str(ctz.cotizaciones_nit_proyecto).replace('-','').replace('.','').replace(' ',''))[0]
# 			idUsuarioCliente      = multi_dbUsers.insert(
# 				tipo              = 'Cliente',
# 				cliente           = idCliente,
# 				proyecto          = None,
# 				email             = ctz.cotizaciones_email_administrador,
# 				password          = password,
# 				first_name        = 'Usuario',
# 				last_name         = 'Cliente'
# 			)
# 			print('Datos idUsuarioCliente', idUsuarioCliente)
# 			idUsuarioProyecto     = multi_dbUsers.insert(
# 				tipo              = 'Coordinador',
# 				cliente           = idCliente,
# 				proyecto          = idProyecto,
# 				email             = ctz.cotizaciones_email_administrador,
# 				password          = password,
# 				first_name        = 'Administrador',
# 				last_name         = 'Proyecto'
# 			)
# 			print('Datos idUsuarioProyecto', idUsuarioProyecto)

# 			tmp     = notificacionOrdenServicio(idCliente,'cliente',emails,opc)
# 			if tmp:
# 				email = 1
# 			else:
# 				email = 0
# 				pass
# 			pass
# 		pass
# 	return idCliente


