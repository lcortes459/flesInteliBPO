# -*- coding: utf-8 -*-

def db_tablePaises():
	db.define_table('paises',
		Field('paises_nombre'),
		Field('paises_codigo'),
		Field('paises_estado',default=True),
		Field('paises_fecha_creacion',default=fecha('all')),
		format="%(paises_nombre)s"
	)
	db.paises.id.readable =  db.paises.id.writable = False
	db.paises.paises_estado.readable =  db.paises.paises_estado.writable = False
	db.paises.paises_fecha_creacion.readable =  db.paises.paises_fecha_creacion.writable = False
	db.paises._enable_record_versioning()
	pass

def db_tableCiudades():
	if not hasattr(db,'paises'):
		db_tablePaises()
	db.define_table('ciudades',
		Field('ciudades_pais','reference paises', label="País"),
		Field('ciudades_nombre',label="Ciudad"),
		Field('ciudades_codigo',label="Codigo"),
		Field('ciudades_estado',default=True),
		Field('ciudades_fecha_creacion',default=fecha('all')),
		format="%(ciudades_nombre)s"
	)
	db.ciudades.id.readable =  db.ciudades.id.writable = False
	db.ciudades.ciudades_estado.readable =  db.ciudades.ciudades_estado.writable = False
	db.ciudades.ciudades_fecha_creacion.readable =  db.ciudades.ciudades_fecha_creacion.writable = False
	db.ciudades._enable_record_versioning()
	pass

def db_tablePlanes():
	if not hasattr(db,'ciudades'):
		db_tableCiudades()
	db.define_table('planes',
		Field('planes_tipo'),
		Field('planes_nombre'),
		Field('planes_valor'),
		Field('planes_minimo_rango_proyectos'),
		Field('planes_maximo_rango_proyectos'),
		Field('planes_estado',default=True),
		Field('planes_fecha_creacion',default=fecha('all')),
		format="%(planes_nombre)s"
	)
	db.planes.id.readable =  db.planes.id.writable = False
	db.planes.planes_estado.readable =  db.planes.planes_estado.writable = False
	db.planes.planes_fecha_creacion.readable =  db.planes.planes_fecha_creacion.writable = False
	db.planes._enable_record_versioning()
	pass

def db_tableCotizaciones():
	if not hasattr(db,'planes'):
		db_tablePlanes()
	db.define_table('cotizaciones',
		Field('cotizaciones_codigo', label="Codigo"),
		Field('cotizaciones_nombre_proyecto',label="Nombre Proyecto"),
		Field('cotizaciones_nit_proyecto',label="Nit Proyecto *"),
		Field('cotizaciones_ciudad' ,'reference ciudades' , label="Ciudad"),
		Field('cotizaciones_direccion_proyecto', label="Dirección Proyecto *"),
		Field('cotizaciones_nombre_administrador' , label="Administrador Proyecto *"),
		Field('cotizaciones_celular_administrador', label="Celular Administrador *"),
		Field('cotizaciones_email_administrador', label="Email Administrador *"),
		Field('cotizaciones_telefono_administrador', label="Telefono Administrador "),
		Field('cotizaciones_cantidad_interiores', label="Cantidad Interiores"),
		Field('cotizaciones_cantidad_predios', label="Cantidad Predios"),
		Field('cotizaciones_plan','reference planes', label="Plan seleccionado *"),
		Field('cotizaciones_observacion', label="Observaciones"),
		Field('cotizaciones_responsable_creacion'  ,label="Creador"),
		Field('cotizaciones_estado',default='Abierta'),
		Field('cotizaciones_fecha_creacion' , 'integer' ,default=int(str(fecha('fecha')).replace('-',''))),
		Field('cotizaciones_hora_creacion' , 'integer' ,default=int(str(fecha('hora')).replace(':',''))),
		format="%(cotizaciones_codigo)s"
	)
	db.cotizaciones.id.readable                                =  db.cotizaciones.id.writable = False
	#db.cotizaciones.cotizaciones_estado.readable               =  db.cotizaciones.cotizaciones_estado.writable = False
	db.cotizaciones.cotizaciones_fecha_creacion.readable       =  db.cotizaciones.cotizaciones_fecha_creacion.writable = False
	db.cotizaciones.cotizaciones_hora_creacion.readable        =  db.cotizaciones.cotizaciones_hora_creacion.writable = False
	db.cotizaciones.cotizaciones_nit_proyecto.readable         =  False
	db.cotizaciones.cotizaciones_direccion_proyecto.readable   =  False
	db.cotizaciones.cotizaciones_nombre_administrador.readable =  False
	db.cotizaciones.cotizaciones_celular_administrador.readable        =  False
	db.cotizaciones.cotizaciones_email_administrador.readable        =  False
	db.cotizaciones.cotizaciones_telefono_administrador.readable        =  False
	db.cotizaciones.cotizaciones_plan.readable        =  False
	db.cotizaciones.cotizaciones_observacion.readable        =  False
	db.cotizaciones.cotizaciones_responsable_creacion.readable        =  False
	db.cotizaciones.cotizaciones_hora_creacion.readable        =  False
	db.cotizaciones._enable_record_versioning()
	pass



def db_tableordeneServicio():
	if not hasattr(db,'cotizaciones'):
		db_tableCotizaciones()
	db.define_table('ordenesServicio',
		Field('ordenesServicios_cotizacion' ,'reference cotizaciones'),
		Field('ordenesServicios_codigo'),
		Field('ordenesServicios_responsable_creacion'),
		Field('ordenesServicios_responsable_ejecucion'),
		Field('ordenesServicios_estado',default='Abierta'),
		Field('ordenesServicios_fecha_creacion' , 'integer' ,default=int(str(fecha('fecha')).replace('-',''))),
		Field('ordenesServicios_hora_creacion' , 'integer' ,default=int(str(fecha('hora')).replace(':',''))),
		Field('ordenesServicios_fecha_ejecucion' , 'integer' ,default=0),
		Field('ordenesServicios_hora_ejecucion' , 'integer' ,default=0),
		format="%(ordenesServicios_codigo)s"
	)
	db.ordenesServicio._enable_record_versioning()
	pass




def db_tableOredenTrabajo():
	if not hasattr(db,'ordenesServicio'):
		db_tableordeneServicio()
	db.define_table('ordenesTrabajo',
		Field('ordenesTrabajo_ordenServicio' ,'reference ordenesServicio'),
		Field('ordenesTrabajo_codigo'),
		Field('ordenesTrabajo_responsable_creacion'),
		Field('ordenesTrabajo_responsable_ejecucion'),
		Field('ordenesTrabajo_estado',default='Abierta'),
		Field('ordenesTrabajo_fecha_creacion' , 'integer' ,default=int(str(fecha('fecha')).replace('-',''))),
		Field('ordenesTrabajo_hora_creacion' , 'integer' ,default=int(str(fecha('hora')).replace(':',''))),
		Field('ordenesTrabajo_fecha_ejecucion' , 'integer' ,default=0),
		Field('ordenesTrabajo_hora_ejecucion' , 'integer' ,default=0),
		format="%(ordenesTrabajo_codigo)s"
	)
	db.ordenesTrabajo._enable_record_versioning()
	pass


def db_tableClientes():
	if not hasattr(db,'ordenesTrabajo'):
 		db_tableOredenTrabajo()
	db.define_table('clientes', 
		Field('clientes_nombre'),
		Field('clientes_nit'),
		Field('clientes_ordenTrabajo' ,'reference ordenesTrabajo'),
		Field('clientes_direccion'),
		Field('clientes_responsable'),
		Field('clientes_celular'),
		Field('clientes_email'),
		Field('clientes_ciudad' ,'reference ciudades'),
		Field('clientes_estado',default=True),
		Field('clientes_tipo_letra'),
		Field('clientes_cantidad_proyectos','integer',default=0),
		Field('clientes_color_corporativo'),
		Field('clientes_responsable_creacion'),
		Field('clientes_fecha_creacion' , 'integer' ,default=int(str(fecha('fecha')).replace('-',''))),
		Field('clientes_hora_creacion' , 'integer' ,default=int(str(fecha('hora')).replace(':',''))),
		format="%(clientes_nombre)s"
	)
	db.clientes._enable_record_versioning()
	pass


def db_tableClienteDocumentos():
	if not hasattr(db,'clientes'):
		db_tableClientes()
	db.define_table('clienteDocumentos', 
		Field('clienteDocumentos_cliente' ,'reference clientes'),
		Field('clienteDocumentos_logo','upload'),
		Field('clienteDocumentos_fecha_creacion' , 'integer' ,default=int(str(fecha('fecha')).replace('-',''))),
		Field('clienteDocumentos_hora_creacion' , 'integer' ,default=int(str(fecha('hora')).replace(':',''))),
	)
	db.clienteDocumentos._enable_record_versioning()
	pass


def db_tableProyectos():
	if not hasattr(db,'clienteDocumentos'):
		db_tableClienteDocumentos()
	db.define_table('proyectos', 
		Field('proyectos_codigo',),
		Field('proyectos_nombre_proyecto'),
		Field('proyectos_nit_proyecto'),
		Field('proyectos_ciudad' ,'reference ciudades'),
		Field('proyectos_direccion_proyecto',),
		Field('proyectos_nombre_administrador'),
		Field('proyectos_celular_administrador'),
		Field('proyectos_email_administrador'),
		Field('proyectos_telefono_administrador'),
		Field('proyectos_cantidad_interiores'),
		Field('proyectos_cantidad_predios'),
		Field('proyectos_responsable_creacion'),
		Field('proyectos_tipo_letra'),
		Field('proyectos_color_corporativo'),
		Field('proyectos_fecha_creacion' , 'integer' ,default=int(str(fecha('fecha')).replace('-',''))),
		Field('proyectos_hora_creacion' , 'integer' ,default=int(str(fecha('hora')).replace(':',''))),
		Field('proyectos_estado',default=True),
		format="%(proyectos_nombre_proyecto)s"
	)
	db.proyectos.id.readable =  db.proyectos.id.writable = False
	db.proyectos.proyectos_fecha_creacion.readable =  db.proyectos.proyectos_fecha_creacion.writable = False
	db.proyectos.proyectos_hora_creacion.readable =  db.proyectos.proyectos_hora_creacion.writable = False
	db.proyectos._enable_record_versioning()
	pass


def db_tableProyectoDocumentos():
	if not hasattr(db,'proyectos'):
		db_tableProyectos()
	db.define_table('proyectosDocumentos', 
		Field('proyectosDocumentos_proyecto' ,'reference proyectos'),
		Field('proyectosDocumentos_logo','upload'),
		Field('proyectosDocumentos_manual_convivencia','upload'),
		Field('proyectosDocumentos_fecha_creacion' , 'integer' ,default=int(str(fecha('fecha')).replace('-',''))),
		Field('proyectosDocumentos_hora_creacion' , 'integer' ,default=int(str(fecha('hora')).replace(':',''))),
	)
	db.proyectosDocumentos._enable_record_versioning()
	pass


def db_tableClientesProyectos():
	if not hasattr(db,'proyectosDocumentos'):
		db_tableProyectoDocumentos()
	db.define_table('clientesProyectos', 
		Field('proyectos_cliente' ,'reference clientes'),
		Field('proyectos_proyecto' ,'reference proyectos'),
		Field('clientesProyectos_fecha_creacion' , 'integer' ,default=int(str(fecha('fecha')).replace('-',''))),
		Field('clientesProyectos_hora_creacion' , 'integer' ,default=int(str(fecha('hora')).replace(':',''))),
	)
	db.clientesProyectos._enable_record_versioning()
	pass



def db_tableInterioresProyectos():
	if not hasattr(db,'clientesProyectos'):
		db_tableClientesProyectos()
	db.define_table('interioresProyectos', 
		Field('interioresProyectos_proyecto' ,'reference proyectos'),
		Field('interioresProyectos_interiores'),
		Field('interioresProyectos_fecha_creacion' , 'integer' ,default=int(str(fecha('fecha')).replace('-',''))),
		Field('interioresProyectos_hora_creacion' , 'integer' ,default=int(str(fecha('hora')).replace(':',''))),
	)
	db.interioresProyectos._enable_record_versioning()
	pass


def db_tableInterioresPredios():
	if not hasattr(db,'interioresProyectos'):
		db_tableInterioresProyectos()
	db.define_table('interioresPredios', 
		Field('interioresPredios_interior' ,'reference interioresProyectos'),
		Field('interioresPredios_identificador'),
		Field('interioresPredios_piso'),
		Field('interioresPredios_predio'),
		Field('interioresPredios_codigo'),
		Field('interioresPredios_estado',default=False),
		Field('interioresPredios_responsable_creacion'),
		Field('interioresPredios_fecha_creacion' , 'integer' ,default=int(str(fecha('fecha')).replace('-',''))),
		Field('interioresPredios_hora_creacion' , 'integer' ,default=int(str(fecha('hora')).replace(':',''))),
	)
	db.interioresPredios._enable_record_versioning()
	pass


def db_tablePropietarios():
	if not hasattr(db,'interioresPredios'):
		db_tableInterioresPredios()
	db.define_table('propietarios', 
		Field('propietarios_nombres'),
		Field('propietarios_apellidos'),
		Field('propietarios_identificacion'),
		Field('propietarios_genero'),
		Field('propietarios_fecha_nacimiento'),
		Field('propietarios_celular'),
		Field('propietarios_fecha_creacion' , 'integer' ,default=int(str(fecha('fecha')).replace('-',''))),
		Field('propietarios_hora_creacion' , 'integer' ,default=int(str(fecha('hora')).replace(':',''))),
	)
	db.propietarios._enable_record_versioning()
	pass


def db_tableResidentes():
	if not hasattr(db,'propietarios'):
		db_tablePropietarios()
	db.define_table('residentes', 
		Field('residentes_nombres'),
		Field('residentes_apellidos'),
		Field('residentes_identificacion'),
		Field('residentes_genero'),
		Field('residentes_fecha_nacimiento'),
		Field('residentes_celular'),
		Field('residentes_fecha_creacion' , 'integer' ,default=int(str(fecha('fecha')).replace('-',''))),
		Field('residentes_hora_creacion' , 'integer' ,default=int(str(fecha('hora')).replace(':',''))),
	)
	db.residentes._enable_record_versioning()
	pass


def db_tablePropietariosPredios():
	if not hasattr(db,'residentes'):
		db_tableResidentes()
	db.define_table('propietariosPredios', 
		Field('propietariosPredios_predio', 'reference interioresPredios'),
		Field('propietariosPredios_propietario', 'reference propietarios'),
		Field('propietariosPredios_estado', default = True),
		Field('propietariosPredios_fecha_creacion' , 'integer' ,default=int(str(fecha('fecha')).replace('-',''))),
		Field('propietariosPredios_hora_creacion' , 'integer' ,default=int(str(fecha('hora')).replace(':',''))),
	)
	db.propietariosPredios._enable_record_versioning()
	pass


def db_tableResidentesPredios():
	if not hasattr(db,'propietariosPredios'):
		db_tablePropietariosPredios()
	db.define_table('residentesPredios', 
		Field('residentesPredios_predio', 'reference interioresPredios'),
		Field('residentesPredios_residente', 'reference residentes'),
		Field('residentesPredios_estado', default = True),
		Field('residentesPredios_fecha_creacion' , 'integer' ,default=int(str(fecha('fecha')).replace('-',''))),
		Field('residentesPredios_hora_creacion' , 'integer' ,default=int(str(fecha('hora')).replace(':',''))),
	)
	db.residentesPredios._enable_record_versioning()
	pass



def db_tableProveedores():
	db.define_table('proveedores',
		Field('proveedores_nombre'),
		Field('proveedores_codigo'),
		Field('proveedores_estado',default=True),
		Field('proveedores_fecha_creacion',default=fecha('all')),
		format="%(proveedores_nombre)s"
	)
	db.proveedores.id.readable =  db.proveedores.id.writable = False
	db.proveedores.proveedores_estado.readable =  db.proveedores.proveedores_estado.writable = False
	db.proveedores.proveedores_fecha_creacion.readable =  db.proveedores.proveedores_fecha_creacion.writable = False
	db.proveedores._enable_record_versioning()
	pass


def db_tableEmpresasAvi():
	if not hasattr(db,'residentesPredios'):
		db_tableResidentesPredios()
	db.define_table('empresasAvi',
		Field('empresasAvi_nombre'),
		Field('empresasAvi_codigo'),
		Field('empresasAvi_estado',default=True),
		Field('empresasAvi_fecha_creacion',default=fecha('all')),
		format="%(empresasAvi_nombre)s"
	)
	db.empresasAvi.id.readable =  db.empresasAvi.id.writable = False
	db.empresasAvi.empresasAvi.estado.readable =  db.empresasAvi.empresasAvi.estado.writable = False
	db.empresasAvi.empresasAvi.fecha_creacion.readable =  db.empresasAvi.empresasAvi.fecha_creacion.writable = False
	db.empresasAvi._enable_record_versioning()
	pass


def db_tableClientesAvi():
	if not hasattr(db,'empresasAvi'):
		db_tableEmpresasAvi()
	db.define_table('clientesAvi',
		Field('clientesAvi_empresa' ,'reference empresasAvi'),
		Field('clientesAvi_nombre'),
		Field('clientesAvi_codigo'),
		Field('clientesAvi_estado',default=True),
		Field('clientesAvi_fecha_creacion',default=fecha('all')),
		format="%(clientesAvi_nombre)s"
	)
	db.clientesAvi.id.readable =  db.clientesAvi.id.writable = False
	db.clientesAvi.clientesAvie.stado.readable =  db.clientesAvi.clientesAvi.estado.writable = False
	db.clientesAvi.clientesAvi.fecha_creacion.readable =  db.clientesAvi.clientesAvi.fecha_creacion.writable = False
	db.clientesAvi._enable_record_versioning()
	pass



def db_tableSegmentosAvi():
	if not hasattr(db,'clientesAvi'):
		db_tableClientesAvi()
	db.define_table('segmentosAvi',
		Field('segmentosAvi_cliente' ,'reference clientesAvi'),
		Field('segmentosAvi_nombre'),
		Field('segmentosAvi_codigo'),
		Field('segmentosAvi_estado',default=True),
		Field('segmentosAvi_fecha_creacion',default=fecha('all')),
		format="%(segmentosAvi_nombre)s"
	)
	db.segmentosAvi.id.readable =  db.segmentosAvi.id.writable = False
	db.segmentosAvi.segmentosAvi.estado.readable =  db.segmentosAvi.segmentosAvi.estado.writable = False
	db.segmentosAvi.segmentosAvi.fecha_creacion.readable =  db.segmentosAvi.segmentosAvi.fecha_creacion.writable = False
	db.segmentosAvi._enable_record_versioning()
	pass


def db_tableasignacionesAvi():
	if not hasattr(db,'segmentosAvi'):
		db_tableSegmentosAvi()
	db.define_table('asignacionesAvi',
		Field('asignacionesAvi_segmento' ,'reference segmentosAvi'),
		Field('asignacionesAvi_nombre'),
		Field('asignacionesiAvi_codigo'),
		Field('asignacionesAvi_estado',default=True),
		Field('asignacionionesAvi_fecha_creacion',default=fecha('all')),
		format="%(asignacionAvi_nombre)s"
	)
	db.asignacionesAvi.id.readable =  db.asignacionesAvi.id.writable = False
	db.asignacionesAvi.asignacionesAvi.estado.readable =  db.asignacionesAvi.asignacionesAvi.estado.writable = False
	db.asignacionesAvi.asignacionesAvi.fecha_creacion.readable =  db.asignacionesAvi.asignacionesAvi.fecha_creacion.writable = False
	db.asignacionesAvi._enable_record_versioning()
	pass


def db_tableCargues():
	if not hasattr(db,'asignacionesAvi'):
		db_tableasignacionesAvi()
	db.define_table('cargues',
		Field('cargueFiles_asignaciones' ,'reference asignacionesAvi'),
		Field('cargue_nombre'),
		Field('cargue_codigo'),
		Field('cargue_estado',default=True),
		Field('cargue_fecha_creacion',default=fecha('all')),
		format="%(cargue_nombre)s"
	)
	db.cargues.id.readable =  db.cargues.id.writable = False
	db.cargues.cargue_estado.readable =  db.cargues.cargue_estado.writable = False
	db.cargues.cargue_fecha_creacion.readable =  db.cargues.cargue_fecha_creacion.writable = False
	db.cargues._enable_record_versioning()
	pass



def db_tableCarguesFiles():
	if not hasattr(db,'cargues'):
		db_tableCargues()
	db.define_table('cargueFiles', 
		Field('cargueFiles_cargue' ,'reference cargues'),
		Field('cargueFiles_file','upload'),
		Field('cargueFiles_fecha_creacion' , 'integer' ,default=int(str(fecha('fecha')).replace('-',''))),
		Field('cargueFiles_hora_creacion' , 'integer' ,default=int(str(fecha('hora')).replace(':',''))),
	)
	db.cargueFiles._enable_record_versioning()
	pass

def funciones_tables():
	db_tableResidentesPredios()
	pass

