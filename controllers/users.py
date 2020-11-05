# -*- coding: utf-8 -*-


@auth.requires_login()
def updateEstado():
	r = request.vars
	u = db.auth_user
	if r.est == "0":
		estado = '1'
	else:
		estado = None
		pass
	u[r.usu] = dict(registration_key=estado)
	resul = userGetEstado(u[r.usu])
	return resul



@auth.requires_login()
def perfil():
	response.title = T("Perfil")
	response.subTitle = T("Mi Perfil")
	response.icono   = 'profile'
	response.botton       = ''
	# multi_data             = request.vars
	# multi_dbUsuarios       = db.auth_user
	# multi_dbRamas          = db.ramas
	# multi_dbEmpleados      = db.empleados
	# multi_dbUsuEmple       = db.usuario_empleado
	# multi_usuCoor          = db.cordinadoresDolientes
	# multi_usuario          = []
	# multi_usu              = db(multi_dbUsuarios.id==idUser).select(multi_dbUsuarios.ALL)
	# for x in multi_usu:

	# 	union = db(multi_dbUsuEmple.usuario==x.id).select(multi_dbEmpleados.id,multi_dbEmpleados.nombres,left=(\
	# 		multi_dbEmpleados.on(multi_dbEmpleados.id==multi_dbUsuEmple.empleado),multi_dbUsuarios.on(multi_dbUsuarios.id==multi_dbUsuEmple.usuario))).first()
		
	# 	rama = db(multi_dbRamas.id==x.rama).select(multi_dbRamas.nombre_rama,multi_dbRamas.id).first()

	# 	if rama:
	# 		ramas  = rama.nombre_rama
	# 		idRamas = rama.id
	# 	else:
	# 		ramas  = 'Sin asignar'
	# 		idRamas= 'Sin asignar'
	# 		pass

	# 	if union:
	# 		empleado = union.nombres
	# 		idEmpleado = union.id
	# 	else:
	# 		empleado = 'Sin asignar'
	# 		idEmpleado = 0
	# 		pass

	# 	multi_usuario.append(
	# 		dict(
	# 			usuario    = x,
	# 			empleado   = empleado,
	# 			rama       = ramas,
	# 			idRama     = idRamas,
	# 			idEmpleado = idEmpleado
	# 			)
	# 		)
	# 	pass
	return locals()


def empleados():
	multiData          = request.vars
	multi_dbEmpleados  = db.empleados
	empleados          = db( (multi_dbEmpleados.empleados_cliente == empresa) & (multi_dbEmpleados.empleados_estado == True)).select(multi_dbEmpleados.id,multi_dbEmpleados.empleados_nombres)
	return locals()

def getEmpladoAsigar(id):
	multi_dbEmpleados    = db.usuario_empleado
	if db (multi_dbEmpleados.usuario_empleado_usuario == id).count() > 0:
		empleado    = db( multi_dbEmpleados.usuario_empleado_usuario == id ).select(multi_dbEmpleados.usuario_empleado_empleado).last()
		resul = XML("""<a href="#!" 
						  class="btn btn-success btn-block"
						  onclick="template.asigEmpleado("""+str(id)+""");" 
					><b>"""+str(db.empleados[empleado.usuario_empleado_empleado].empleados_nombres)+"""</b></span>""")
	else:
		resul = XML("""
			<a 	href="#!" 
				class="btn btn-block btn-primary" 
				onclick="template.asigEmpleado("""+str(id)+""");"
			>Agregar</a>
		""")
		pass
	return resul


def asignarEmpleado():
	multi_data        = request.vars
	multi_dbUsuEmple  = db.usuario_empleado
	multi_res         = 'error'

	if db(( multi_dbUsuEmple.usuario_empleado_empleado==multi_data.empl) & (multi_dbUsuEmple.usuario_empleado_usuario==multi_data.usu) ).count() > 0:
		multi_res = 0
	elif str(multi_data.empl) == '0':
		db(multi_dbUsuEmple.usuario_empleado_usuario==multi_data.usu).delete()
		multi_res = getEmpladoAsigar(multi_data.usu) 
	else:
		multi_dbUsuEmple.insert(
			usuario_empleado_empleado = multi_data.empl,
			usuario_empleado_usuario  = multi_data.usu
			)
		multi_res = getEmpladoAsigar(multi_data.usu) 
		pass
	return multi_res


def cerrarAsigEmpl():
	multi_data        = request.vars
	multi_res         = 'error'
	multi_res = getEmpladoAsigar(multi_data.usu)
	return multi_res

@auth.requires_login()
def index():
	response.title       = T("Configuraciones | Usuarios")
	response.subTitle    = T("Mis Usuarios")
	response.icono       = 'user-cog'
	response.botton      = ''
	multi_dbUsuarios     = db.auth_user

	links                = []
	multi_dbUsuarios.cliente.default  = empresa
	if ( (grup == ['Developer']) | (grup == ['Administrador']) ):
		multi_dbUsuarios.id.readable               =  multi_dbUsuarios.id.writable = False
		multi_dbUsuarios.cliente.readable          =  multi_dbUsuarios.cliente.writable = False
		multi_dbUsuarios.proyecto.readable         =  multi_dbUsuarios.proyecto.writable = False
		query                                      = ( multi_dbUsuarios.cliente==empresa )            
	elif ( (grup == ['Cliente']) | (grup == ['Administrativo'])):
		multi_dbUsuarios.id.readable               =  multi_dbUsuarios.id.writable = False
		multi_dbUsuarios.proyecto.readable         =  multi_dbUsuarios.proyecto.writable = False
		query                                      = ( multi_dbUsuarios.cliente==empresa )
	else:
		multi_dbUsuarios.id.readable               =  multi_dbUsuarios.id.writable = False
		multi_dbUsuarios.cliente.readable          =  multi_dbUsuarios.cliente.writable = False
		multi_dbUsuarios.proyecto.readable         =  multi_dbUsuarios.proyecto.writable = False
		query                                      = ( multi_dbUsuarios.proyecto==proyecto )
		pass

	links = [
		dict(header='Empleado', body=lambda r: DIV( getEmpladoAsigar(r.id), _id='asignarEmpleado_%s' %r.id ) )
	]

	print('query',query)
	print('grup',grup)

	usuarios             = SQLFORM.grid(
		query,
		deletable        = False,
		details          = False,
		csv              = False,
		maxtextlength    = 150,
		editable         = True,
        paginate         = 100,
        links            = links,
		orderby          = multi_dbUsuarios.id

	) 
	return locals()




@auth.requires_login()
def usuariosInfo():
	multi_data             = request.vars
	multi_dbUsuarios       = db.auth_user
	multi_dbRamas          = db.ramas
	multi_dbEmpleados      = db.empleados
	multi_dbUsuEmple       = db.usuario_empleado
	multi_usuCoor          = db.cordinadoresDolientes
	multi_usuario          = []
	multi_usu              = db(multi_dbUsuarios.id==multi_data.idUsuario).select(multi_dbUsuarios.ALL)
	# 1018485877
	if grup=='Clientes':
		tmp = ''
	elif grup=='Coordinador':
		tipos                      = ['Asesor','Coordinador']
		for x in multi_usu:
			modUsuario             = db(db.usuarioModulo.usuario==idUser).select(db.usuarioModulo.modulo).first()
			multi_ramas            = db(multi_dbRamas.modulo==modUsuario.modulo).select(multi_dbRamas.ALL)
			if x.tipo == 'Coordinador':
				multi_empleados = []
				selec = 'disabled'
			else:
				# multi_empleados,opc    = crud(multi_dbEmpleados,3,'','')
				multi_empleados        = db(multi_dbEmpleados.empresa==empresa).select(multi_dbEmpleados.ALL)
				selec = ''
				pass
			union = db(multi_dbUsuEmple.usuario==x.id).select(multi_dbEmpleados.id,multi_dbEmpleados.nombres,left=(\
				multi_dbEmpleados.on(multi_dbEmpleados.id==multi_dbUsuEmple.empleado),multi_dbUsuarios.on(multi_dbUsuarios.id==multi_dbUsuEmple.usuario))).first()
			
			rama = db(multi_dbRamas.id==x.rama).select(multi_dbRamas.nombre_rama,multi_dbRamas.id).first()

			if rama:
				ramas  = rama.nombre_rama
				idRamas = rama.id
			else:
				ramas  = 'Sin asignar'
				idRamas= 'Sin asignar'
				pass

			if union:
				empleado = union.nombres
				idEmpleado = union.id
			else:
				empleado = 'Sin asignar'
				idEmpleado = 0
				pass

			multi_usuario.append(
				dict(
					usuario    = x,
					empleado   = empleado,
					rama       = ramas,
					idRama     = idRamas,
					idEmpleado = idEmpleado
					)
				)
			pass
	else:
		tipos                  = ['Administrador','Coordinador','Asesor']
		cordUsu                = db(multi_usuCoor.doliente==multi_data.idUsuario).select(multi_usuCoor.cordinador).first()
		if cordUsu:
			modUsuario         = db(db.usuarioModulo.usuario==cordUsu.cordinador).select(db.usuarioModulo.modulo).first()
			if modUsuario:
				multi_ramas        = db(multi_dbRamas.modulo==modUsuario.modulo).select(multi_dbRamas.ALL)
			else:
				multi_ramas = []	
				pass
		else:
			multi_ramas = []
			pass

		for x in multi_usu:
			if ( (x.tipo == 'Administrador') | (x.tipo == 'Developer')):
				multi_empleados = []
				selec = 'disabled'
			else:
				# multi_empleados,opc    = crud(multi_dbEmpleados,3,'','')
				multi_empleados        = db(multi_dbEmpleados.empresa==empresa).select(multi_dbEmpleados.ALL)
				selec = ''
				pass
			union = db(multi_dbUsuEmple.usuario==x.id).select(multi_dbEmpleados.id,multi_dbEmpleados.nombres,left=(\
				multi_dbEmpleados.on(multi_dbEmpleados.id==multi_dbUsuEmple.empleado),multi_dbUsuarios.on(multi_dbUsuarios.id==multi_dbUsuEmple.usuario))).first()
			
			rama = db(multi_dbRamas.id==x.rama).select(multi_dbRamas.nombre_rama,multi_dbRamas.id).first()

			if rama:
				ramas  = rama.nombre_rama
				idRamas = rama.id
			else:
				ramas  = 'Sin asignar'
				idRamas= 'Sin asignar'
				pass

			if union:
				empleado = union.nombres
				idEmpleado = union.id
			else:
				empleado = 'Sin asignar'
				idEmpleado = 0
				pass

			multi_usuario.append(
				dict(
					usuario    = x,
					empleado   = empleado,
					rama       = ramas,
					idRama     = idRamas,
					idEmpleado = idEmpleado
					)
				)
			pass
		pass
	return locals()