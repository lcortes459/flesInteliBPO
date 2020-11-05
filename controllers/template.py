# -*- coding: utf-8 -*-
# from gluon.contrib.websocket_messaging import websocket_send
# from gluon.contrib.websocket_messaging import websocket_send
# from datetime import  datetime, date, timedelta, time
#import ssl


# def setRT(mensaje):
# 	print('mensaje',mensaje)
# 	# ssl._create_default_https_context = ssl._create_unverified_context
# 	try :
# 		print(1)
# 		websocket_send('http://127.0.0.1:8000', mensaje, 'mykey','mygroup')
# 	except Exception, e:
# 		print(0)
# 		print e,'Esto es un error'
# 		pass
# 	print('grupo')
# 	pass


@auth.requires_login()
def guardar():
	multi_tabla = db.ciudades
	multi_opc   = 1
	multi_data  = request.vars
	multi_idRow = 0
	data,opc = crud(multi_tabla,multi_opc,multi_data,multi_idRow)
	if data:
		return int(data)
	else:
		data = 0
		return int(data)
		pass

@auth.requires_login()
def guardarPerfil():
	multi_tabla = db.auth_group
	multi_opc   = 1
	multi_data  = request.vars
	multi_idRow = 0
	data,opc = crud(multi_tabla,multi_opc,multi_data,multi_idRow)
	if data:
		return int(data)
	else:
		data = 0
		return int(data)
		pass


@auth.requires_login()
def guardarModulo():
	multi_tabla = db.modulos
	multi_data  = request.vars
	if db(multi_tabla.codigo==request.vars.codigo).count() == 0:
		multi_opc   = 1
		multi_idRow = 0
		data,opc = crud(multi_tabla,multi_opc,multi_data,multi_idRow)
	else:
		data = 0
		pass
	return int(data)


@auth.requires_login()
def guardarAlerta():
	multi_tabla = db.alertas
	multi_data  = request.vars
	if db( (multi_tabla.prioridad==request.vars.nombre_alerta) & (multi_tabla.modulo==request.vars.modulo) ).count() == 0:
		multi_opc   = 1
		multi_idRow = 0
		data,opc = crud(multi_tabla,multi_opc,multi_data,multi_idRow)
	else:
		data = 0
		pass
	return int(data)

@auth.requires_login()
def guardarRama():
	multi_tabla = db.ramas
	multi_data  = request.vars
	if db( (multi_tabla.nombre_rama==request.vars.nombre_rama) & (multi_tabla.codigo_rama==request.vars.codigo_rama)).count() == 0:
		multi_opc   = 1
		multi_idRow = 0
		data,opc = crud(multi_tabla,multi_opc,multi_data,multi_idRow)
	else:
		data = 0
		pass
	return int(data)



@auth.requires_login()
def guardarCargo():
	multi_tabla = db.cargos
	multi_data  = request.vars
	if db(multi_tabla.nombre==request.vars.nombre).count() == 0:
		multi_opc   = 1
		multi_idRow = 0
		data,opc = crud(multi_tabla,multi_opc,multi_data,multi_idRow)
	else:
		data = 0
		pass
	return int(data)


@auth.requires_login()
def guardarEmplados():
	multi_tabla = db.empleados
	multi_data  = request.vars
	if db(multi_tabla.identificacion==request.vars.identificacion).count() == 0:
		multi_opc   = 1
		multi_idRow = 0
		data,opc = crud(multi_tabla,multi_opc,multi_data,multi_idRow)
	else:
		data = 0
		pass
	return int(data)

@auth.requires_login()
def guardarTipoAlerta():
	multi_tabla = db.tipo_alertas
	multi_data  = request.vars
	if db( (multi_tabla.nombre==request.vars.nombre) & (multi_tabla.codigo==request.vars.codigo)).count() == 0:
		multi_opc   = 1
		multi_idRow = 0
		data,opc = crud(multi_tabla,multi_opc,multi_data,multi_idRow)
	else:
		data = 0
		pass
	return int(data)


@auth.requires_login()
def guardarTipoIdentificacion():
	multi_tabla = db.tipoIdentificacion
	multi_data  = request.vars
	if db( (multi_tabla.nombre==request.vars.nombre) & (multi_tabla.codigo==request.vars.codigo)).count() == 0:
		multi_opc   = 1
		multi_idRow = 0
		data,opc = crud(multi_tabla,multi_opc,multi_data,multi_idRow)
	else:
		data = 0
		pass

	return int(data)


@auth.requires_login()
def guardarTipoPersona():
	multi_tabla = db.tipoPersona
	multi_data  = request.vars
	if db( (multi_tabla.nombre==request.vars.nombre) & (multi_tabla.codigo==request.vars.codigo)).count() == 0:
		multi_opc   = 1
		multi_idRow = 0
		data,opc = crud(multi_tabla,multi_opc,multi_data,multi_idRow)
	else:
		data = 0
		pass

	return int(data)


@auth.requires_login()
def guardarUsuario():
	multi_tabla     = db.auth_user
	multi_data      = request.vars
	multi_usuCoor   = db.cordinadoresDolientes
	if db(multi_tabla.email==request.vars.email).count() == 0:
		multi_opc   = 1
		multi_idRow = 0
		if request.vars.rama == 'Sin asignar':
			multi_data['rama'] = None
			pass
		data,opc = crud(multi_tabla,multi_opc,multi_data,multi_idRow)
		password = multi_tabla.password.validate(str(request.vars.first_name).replace(' ','').lower())[0]
		db(multi_tabla.id==data).update(password=password)
		if request.vars.doliente == 'Sin asignar':
			tmp = ''
		else:
			db.usuario_empleado.insert(
				empleado   = request.vars.doliente,
				usuario    = data,
				asignador  = auth.user_id
				)
			pass
		if request.vars.tipo=='Coordinador':
			multi_usuCoor.insert(
				cordinador   = data,
				doliente     = data,
				)
		elif grup=='Coordinador':
			multi_usuCoor.insert(
				cordinador   = idUser,
				doliente     = data,
				)
		else:
			tmp = ''
			pass
	else:
		data = 0
		pass
	return int(data)


@auth.requires_login()
def actaulizarUsuario():
	multi_tabla     = db.auth_user
	multi_data      = {}
	multi_usuCoor   = db.cordinadoresDolientes
	
	if db(multi_tabla.id==request.vars.id).count() > 0:
		multi_opc   = 2
		multi_idRow = request.vars.id

		if request.vars.rama_update == 'Sin asignar':
			multi_data['rama'] = 1
		else:
			multi_data['rama'] = request.vars.rama_update
			pass
		multi_data['first_name'] = request.vars.first_name_update
		multi_data['last_name'] = request.vars.last_name_update
		multi_data['estado'] = request.vars.estado_update
		multi_data['email'] = request.vars.email_update
		multi_data['fecha_creacion'] = request.vars.fecha_creacion_update
		multi_data['sucursal'] = request.vars.sucursal_update
		multi_data['empresa'] = request.vars.empresa_update
		multi_data['fechaactualizacionpass'] = request.vars.fechaactualizacionpass_update
		multi_data['password'] = multi_tabla.password.validate(str(request.vars.password).replace(' ',''))[0]
		data,opc = crud(multi_tabla,multi_opc,multi_data,multi_idRow)
		data = multi_idRow
		if request.vars.doliente_update == 'Sin asignar':
			tmp = ''
		else:

			if ( db( (db.usuario_empleado.empleado==request.vars.doliente_update) & (db.usuario_empleado.usuario==multi_idRow) ).count()>0):
				tmp = 0
			else:
				if (db(db.usuario_empleado.usuario==multi_idRow).count()>0):
					db(db.usuario_empleado.usuario==multi_idRow).delete()
					pass
				db.usuario_empleado.insert(
					empleado   = request.vars.doliente_update,
					usuario    = multi_idRow,
					asignador  = idUser
				)
				pass
			pass
	else:
		data = 0
		pass
	return int(data)


@auth.requires_login()
def actualizarEmpresas():
	multi_tabla    = db.empresas
	multi_data      = {}
	if db(multi_tabla.id==request.vars.id).count() > 0:
		multi_opc   = 2
		multi_idRow = request.vars.id
		multi_data['nombre']                        = request.vars.nombre_update
		multi_data['nit']                           = request.vars.nit_update                      
		multi_data['ciudad']                        = request.vars.ciudad_update                 
		multi_data['tipo_identificacion']           = request.vars.tipo_identificacion_update
		multi_data['tipo_persona']                  = request.vars.tipo_persona_update 
		multi_data['direccion']                     = request.vars.direccion_update        
		multi_data['celular']                       = request.vars.celular_update           
		multi_data['telefono']                      = request.vars.telefono_update             
		multi_data['representante']                 = request.vars.representante_update            
		multi_data['email']                         = request.vars.email_update       
		multi_data['estado']                        = request.vars.estado_update               
		multi_data['observacion_estado_general']    = request.vars.observacion_estado_general_update
		multi_data['fecha_creacion']                = request.vars.fecha_creacion_update
		multi_data['estado_financiero']             = request.vars.estado_financiero_update      
		multi_data['fecha_estado_financiero']       = request.vars.fecha_estado_financiero_update  
		multi_data['observacion_estado_financiero'] = request.vars.observacion_estado_financiero_update
		multi_data['estado_juridico']               = request.vars.estado_juridico_update          
		multi_data['fecha_estado_juridico']         = request.vars.fecha_estado_juridico_update    
		multi_data['observacion_estado_juridico']   = request.vars.observacion_estado_juridico_update
		multi_data['estado_legal']                  = request.vars.estado_legal_update
		multi_data['fecha_estado_legal']            = request.vars.fecha_estado_legal_update       
		multi_data['observacion_estado_legal']      = request.vars.observacion_estado_legal_update
		data,opc = crud(multi_tabla,multi_opc,multi_data,multi_idRow)
		data = multi_idRow
	else:
		data = 0
		pass
	return int(data)

@auth.requires_login()
def guardarEmpresas():
	multi_tabla     = db.empresas
	multi_sucursal  = db.sucursales
	multi_dbUsuar   = db.auth_user
	multi_data      = request.vars
	multi_dbModulos = db.modulos
	multi_dbModEmp  = db.modulosEmpresas
	if db(multi_tabla.nit==request.vars.nit).count() == 0:
		multi_opc   = 1
		multi_idRow = 0
		dataEmpresa,opc = crud(multi_tabla,multi_opc,multi_data,multi_idRow)
		multi_data['empresa_sucursal'] = dataEmpresa
		multi_data['codigo_sucursal']  = request.vars.nit
		multi_data['nombre_sucursal']  = request.vars.nombre
		multi_data['ciudad_sucursal']  = request.vars.ciudad
		multi_data['direccion_sucursal']  = request.vars.direccion
		multi_data['telefono_sucursal']  = request.vars.telefono
		multi_data['celular_sucursal']  = request.vars.celular
		multi_data['representante_sucursal']  = request.vars.representante
		multi_data['estado_sucursal']  = request.vars.estado
		multi_data['fecha_creacion_sucursal']  = request.vars.fecha_creacion
		dataSucursal,opc = crud(multi_sucursal,multi_opc,multi_data,multi_idRow)
		password = multi_dbUsuar.password.validate(request.vars.nit)[0]
		multi_usuario      = {
			'first_name':request.vars.representante,
			'last_name':request.vars.representante,
			'email':request.vars.email,
			'password': password,
			'empresa':dataEmpresa,
			'sucursal':dataSucursal,
			'tipo':'Clientes',
			'genero':'Femenino',
			'estado':True,
			'fecha_creacion':fecha('all'),
			'fechaactualizacionpass':'0000-00-00',
			'foto':'',
			'celular':request.vars.celular,
			'identificacion':request.vars.nit,
			'cargo':'Gerencia'
		}
		dataUsuario,opc = crud(multi_dbUsuar,multi_opc,multi_usuario,multi_idRow)
		db.asesorEmpresas.insert(
			empresa   = dataEmpresa,
			asesor    = idUser
			)
		multi_idPer = db(db.auth_group.role=="Clientes").select(db.auth_group.id).last()['id']
		db.auth_membership.insert(
			group_id    = multi_idPer,
			user_id     = dataUsuario
			)
		data = dataSucursal
		multi_modulos          = db(multi_dbModulos.nombre=='Ventas').select(multi_dbModulos.id).last()
		multi_dbModEmp.insert(
			modulo   = multi_modulos.id,
			empresa  = dataEmpresa
			)
	else:
		data = 0
		pass
	return int(data)


@auth.requires_login()
def guardarEmpresasRequisicion():
	import gluon.contrib.simplejson
	multi_tabla            = db.empresas
	multi_sucursal         = db.sucursales
	multi_dbUsuar          = db.auth_user
	multi_data             = request.vars
	multi_dbRequisiciones  = db.requisiciones
	multi_tema             = db.requisiciones_terminos
	multi_usuCoor          = db.cordinadoresDolientes
	multi_dbModEmp         = db.modulosEmpresas
	multi_dbModulos        = db.modulos

	cordUsu                = db(multi_usuCoor.doliente==idUser).select(multi_usuCoor.cordinador).first()
	print('cordUsu',cordUsu)
	if cordUsu:
		print('Hay un coordinador asignado')
		modUsuario         = db(db.usuarioModulo.usuario==cordUsu.cordinador).select(db.usuarioModulo.modulo).first()
		print('modUsuario',modUsuario)
		if modUsuario:
			print('Hay un módulo asignado')
			modulo        = modUsuario.modulo 
			#db(multi_dbRamas.modulo==modUsuario.modulo).select(multi_dbRamas.ALL)
		else:
			modulo = None	
			pass
	else:
		modulo = None
		pass
	if db(multi_tabla.nit==request.vars.nit).count() == 0:
		multi_opc   = 1
		multi_idRow = 0
		dataEmpresa,opc = crud(multi_tabla,multi_opc,multi_data,multi_idRow)
		multi_data['empresa_sucursal'] = dataEmpresa
		multi_data['codigo_sucursal']  = request.vars.nit
		multi_data['nombre_sucursal']  = request.vars.nombre
		multi_data['ciudad_sucursal']  = request.vars.ciudad
		multi_data['direccion_sucursal']  = request.vars.direccion
		multi_data['telefono_sucursal']  = request.vars.telefono
		multi_data['celular_sucursal']  = request.vars.celular
		multi_data['representante_sucursal']  = request.vars.representante
		multi_data['estado_sucursal']  = request.vars.estado
		multi_data['fecha_creacion_sucursal']  = request.vars.fecha_creacion
		dataSucursal,opc = crud(multi_sucursal,multi_opc,multi_data,multi_idRow)
		password = multi_dbUsuar.password.validate(request.vars.nit)[0]
		multi_usuario      = {
			'first_name':request.vars.representante,
			'last_name':request.vars.representante,
			'email':request.vars.email,
			'password': password,
			'empresa':dataEmpresa,
			'sucursal':dataSucursal,
			'tipo':'Clientes',
			'genero':'Femenino',
			'fecha_creacion':fecha('all'),
			'fechaactualizacionpass':'0000-00-00',
			'foto':'',
			'celular':request.vars.celular,
			'identificacion':request.vars.nit,
			'cargo':'Gerencia'
		}
		dataUsuario,opc = crud(multi_dbUsuar,multi_opc,multi_usuario,multi_idRow)

		db.asesorEmpresas.insert(
			empresa   = dataEmpresa,
			asesor    = idUser
			)
		
		# multi_idPer = db(db.auth_group.role=="Clientes").select(db.auth_group.id).last()['id']
		
		# db.auth_membership.insert(
		# 	group_id    = multi_idPer,
		# 	user_id     = dataUsuario
		# 	)
		nombre = 'Creación del Cliente'+' '+str(request.vars.nombre).upper()
		datRequisicion = multi_dbRequisiciones.insert(
			nombre   = nombre,
			sucursal = dataSucursal,
			empresa  = dataEmpresa,
			ramas    = rama,
			modulo   = modulo,
			#valor = ,
			#observaciones = ,
			creador = idUser,
			descripcion = nombre,
			)
		db(multi_dbRequisiciones.id==datRequisicion).update(codigo='REQ'+str(idUser)+str(datRequisicion))
		datTemas = multi_tema.insert(
			requisicion      = datRequisicion,
			temas            = nombre,
			observaciones    = nombre,
			creador_tema     = idUser,
			documento        = '')
		data = dict(
			resul         = 'successs',
			empresa       = dataEmpresa,
			sucursal      = dataSucursal,
			usuario       = dataUsuario,
			requi         = datRequisicion,
			nombreEmpresa = request.vars.nombre
			)
		multi_modulos          = db(multi_dbModulos.nombre=='Ventas').select(multi_dbModulos.id).last()
		multi_dbModEmp.insert(
			modulo   = multi_modulos.id,
			empresa  = dataEmpresa
			)

		#notifacion = notificacion(request.vars.nombre)
		#setRT(notifacion)
		# if notifacion:
		# 	print('notifacion',notifacion)
		# 	pass
	else:
		data = dict(
			resul         = 'error',
			empresa       = 0,
			sucursal      = 0,
			usuario       = 0,
			requi         = 0,
			nombreEmpresa = 0,
			)
		pass
	return gluon.contrib.simplejson.dumps(data)

@auth.requires_login()
def updatePassword():
	multi_data    = request.vars
	multi_tabla   = db.auth_user
	password      = multi_tabla.password.validate(str(request.vars.password).replace(' ',''))[0]
	print('multi_data', multi_data)
	if db(multi_tabla.id==request.vars.idUsuario).count()>0:
		db(multi_tabla.id==request.vars.idUsuario).update(password=password)
		data      = request.vars.idUsuario
	else:
		data      = 0
		pass
	return data

@auth.requires_login()	
def guardarRequisicion():
	multi_data     = request.vars['file']
	res = 0
	print('multi_data',multi_data)
	notifacion = notificacion(multi_data.nombreEmpresa,multi_data.idEmpresa)
	if notifacion:
		print('notifacion',notifacion)
		pass
	return res


@auth.requires_login()
def guardarSucursal():
	multi_sucursal = db.sucursales
	multi_dbUsuar  = db.auth_user
	multi_data     = request.vars
	if db( (multi_sucursal.codigo==request.vars.codigo) & (multi_sucursal.empresa==request.vars.empresa)).count() == 0:
		multi_opc   = 1
		multi_idRow = 0
		dataSucursal,opc = crud(multi_sucursal,multi_opc,multi_data,multi_idRow)
		password = multi_dbUsuar.password.validate(request.vars.codigo)[0]
		multi_usuario      = {
			'first_name':request.vars.representante,
			'last_name':request.vars.representante,
			'email':request.vars.email,
			'password': password,
			'sucursal':dataSucursal,
			'tipo':'Administrativo Cliente',
			'genero':'Femenino',
			'estado':True,
			'fecha_creacion':fecha('all'),
			'fechaactualizacionpass':'0000-00-00',
			'foto':'',
			'celular':request.vars.celular,
			'identificacion':request.vars.codigo
		}
		dataUsuario,opc = crud(multi_dbUsuar,multi_opc,multi_usuario,multi_idRow)
		multi_idPer = db(db.auth_group.role=="Administrativo Cliente").select(db.auth_group.id).last()['id']
		db.auth_membership.insert(
			group_id    = multi_idPer,
			user_id     = dataUsuario
			)
		data = dataSucursal
	else:
		data = 0
		pass
	return int(data)


@auth.requires_login()
def modulos():
	multi_data        = request.vars
	print('multi_data',multi_data)
	multi_dbModulos   = db.modulos
	multi_dbModEmp    = db.modulosEmpresas
	# multi_modulos     = db(multi_dbModulos.empresa==multi_data.empresa).select(multi_dbModulos.ALL) 
	multi_modulos = []
	print('multi_modulos',multi_modulos)
	return locals()