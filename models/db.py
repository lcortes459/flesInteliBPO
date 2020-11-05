# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# AppConfig configuration made easy. Look inside private/appconfig.ini
# Auth is for authenticaiton and access control
# -------------------------------------------------------------------------
from gluon.contrib.appconfig import AppConfig
from gluon.tools import Auth

# -------------------------------------------------------------------------
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

if request.global_settings.web2py_version < "2.15.5":
    raise HTTP(500, "Requires web2py 2.15.5 or newer")

# -------------------------------------------------------------------------
# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# -------------------------------------------------------------------------
# request.requires_https()

# -------------------------------------------------------------------------
# once in production, remove reload=True to gain full speed
# -------------------------------------------------------------------------
configuration = AppConfig(reload=True)

if not request.env.web2py_runtime_gae:
    # ---------------------------------------------------------------------
    # if NOT running on Google App Engine use SQLite or other DB
    # ---------------------------------------------------------------------
    db = DAL(configuration.get('db.uri'),
             pool_size=configuration.get('db.pool_size'),
             migrate_enabled=configuration.get('db.migrate'),
             check_reserved=['all'])
else:
    # ---------------------------------------------------------------------
    # connect to Google BigTable (optional 'google:datastore://namespace')
    # ---------------------------------------------------------------------
    db = DAL('google:datastore+ndb')
    # ---------------------------------------------------------------------
    # store sessions and tickets there
    # ---------------------------------------------------------------------
    session.connect(request, response, db=db)
    # ---------------------------------------------------------------------
    # or store session in Memcache, Redis, etc.
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db = MEMDB(Client()))
    # ---------------------------------------------------------------------

# -------------------------------------------------------------------------
# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
# -------------------------------------------------------------------------
response.generic_patterns = [] 
if request.is_local and not configuration.get('app.production'):
    response.generic_patterns.append('*')

# -------------------------------------------------------------------------
# choose a style for forms
# -------------------------------------------------------------------------
response.formstyle = 'bootstrap4_inline'
response.form_label_separator = ''

# -------------------------------------------------------------------------
# (optional) optimize handling of static files
# -------------------------------------------------------------------------
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

# -------------------------------------------------------------------------
# (optional) static assets folder versioning
# -------------------------------------------------------------------------
# response.static_version = '0.0.0'

# -------------------------------------------------------------------------
# Here is sample code if you need for
# - email capabilities
# - authentication (registration, login, logout, ... )
# - authorization (role based authorization)
# - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
# - old style crud actions
# (more options discussed in gluon/tools.py)
# -------------------------------------------------------------------------

# host names must be a list of allowed host names (glob syntax allowed)
auth = Auth(db, host_names=configuration.get('host.names'))

# -------------------------------------------------------------------------
# create all tables needed by auth, maybe add a list of extra fields
# -------------------------------------------------------------------------

funciones_tables()

auth.settings.extra_fields['auth_user'] = [
    Field('tipo', 'list:string', widget=SQLFORM.widgets.radio.widget),
    Field('cliente', 'reference clientes'),
    Field('proyecto', 'reference proyectos'),
    ]
# -------------------------------------------------------------------------
# create all tables needed by auth if not custom tables
# -------------------------------------------------------------------------
auth.define_tables(username=False, signature=False)
#db.auth_user.punto.label='Punto De Operación'
#db.auth_user.punto.requires = IS_NOT_EMPTY(error_message='Debe asignarle al usuario un punto de operación')
db.auth_user.tipo.requires = [
    IS_IN_SET(('Developer','Administrador','Cliente', 'Coordinador' , 'Administrativo', 'Residente','Soporte', 'stationJob')),
    IS_NOT_EMPTY(error_message='Debe ingresar un tipo de usuario'),
    ]
# db.auth_user.first_name.requires = IS_NOT_EMPTY(error_message='Debe ingresar un nombre')
# db.auth_user.last_name.requires = IS_NOT_EMPTY(error_message='Debe ingresar un apellido')
# db.auth_user.genero.requires = [
#     IS_IN_SET(('Femenino', 'Masculino')),
#     IS_NOT_EMPTY(error_message='Debe ingresar un genero'),
#     ]
# db.auth_user.tipo_seguimiento.readable = False
# db.auth_user.foto.requires = IS_EMPTY_OR(IS_IMAGE(extensions=('png',), error_message='Debe ingresar una imagen con formato PNG'))
# db.auth_user.foto.represent = lambda foto, r : getFotoZoom(r,35,35)
db.auth_user.registration_key.writable = db.auth_user.registration_key.readable = True
db.auth_user.registration_key.label='Estado'
db.auth_user.registration_key.represent = lambda id, r: userGetEstado(r)
db.auth_user._enable_record_versioning()
# db.auth_user.tipo.represent = lambda id, r: getTipo(r)
# db.auth_user.tipo_seguimiento.represent = lambda id, r: getTipoSeguimiento(r)
# db.auth_user.punto.represent = lambda id, r: getPunto(r)



#db.auth_user.cliente.represent = lambda id, r: getCliente(r)


# -------------------------------------------------------------------------
# configure email
# -------------------------------------------------------------------------
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else configuration.get('smtp.server')
mail.settings.sender = configuration.get('smtp.sender')
mail.settings.login = configuration.get('smtp.login')
mail.settings.tls = configuration.get('smtp.tls') or False
mail.settings.ssl = configuration.get('smtp.ssl') or False

# -------------------------------------------------------------------------
# configure auth policy
# -------------------------------------------------------------------------
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

# -------------------------------------------------------------------------  
# read more at http://dev.w3.org/html5/markup/meta.name.html               
# -------------------------------------------------------------------------
response.meta.author = configuration.get('app.author')
response.meta.description = configuration.get('app.description')
response.meta.keywords = configuration.get('app.keywords')
response.meta.generator = configuration.get('app.generator')
response.show_toolbar = configuration.get('app.toolbar')

# -------------------------------------------------------------------------
# your http://google.com/analytics id                                      
# -------------------------------------------------------------------------
response.google_analytics_id = configuration.get('google.analytics_id')

# -------------------------------------------------------------------------
# maybe use the scheduler
# -------------------------------------------------------------------------
if configuration.get('scheduler.enabled'):
    from gluon.scheduler import Scheduler
    scheduler = Scheduler(db, heartbeat=configuration.get('scheduler.heartbeat'))



# db.define_table('cargos', 
#     Field('cargos_codigo'),
#     Field('cargos_nombre'),
#     Field('cargos_cliente', 'reference clientes'),
#     Field('cargos_proyecto', 'reference proyectos'),
#     Field('cargos_estado',default=True),
#     Field('cargos_fecha_creacion' , 'integer' ,default=int(str(fecha('fecha')).replace('-',''))),
#     Field('cargos_hora_creacion' , 'integer' ,default=int(str(fecha('hora')).replace(':','').replace(' ','').replace('.',''))),
# )


db.define_table('empleados', 
    Field('empleados_nombres', label='Nombres Apellidos'),
    Field('empleados_identificacion', label='Identificación'),
    Field('empleados_celular', label='Celular'),
    # Field('empleados_cargo','reference cargos', label=''),
    #Field('empleados_ciudad','reference ciudades', label=''),
    Field('empleados_cliente', 'reference clientes', label=''),
    #Field('empleados_proyecto', 'reference proyectos', label=''),
    Field('empleados_fecha_ingreso', label='Fecha Ingreso'),
    Field('empleados_fecha_nacimiento', label='Fecha Nacimiento'),
    Field('empleados_contacto_emergancia', label='Contacto Emergencia'),
    Field('empleados_parentesco_emergancia', label='Parentezco Contacto'),
    Field('empleados_telefono_emergancia', label='Celular Contacto'),
    Field('empleados_direccion_recidencia', label='Dirección Domicilio'),
    Field('empleados_email', label='Email'),
    Field('empleados_genero' , 'list:string', widget=SQLFORM.widgets.radio.widget, label='Genero'),
    Field('empleados_observaciones', 'text',label='Observaciones'),
    Field('empleados_estado',default=True , label="Estado"),
    Field('empleados_fecha_creacion' , 'integer' ,default=int(str(fecha('fecha')).replace('-',''))),
    Field('empleados_hora_creacion' , 'integer' ,default=int(str(fecha('hora')).replace(':','').replace(' ','').replace('.',''))),
    Field('empleados_foto','upload'),
)
db.empleados.id.readable                        =  db.empleados.id.writable = False
db.empleados.empleados_foto.readable            =  False
db.empleados.empleados_cliente.readable         =  db.empleados.empleados_cliente.writable = False
db.empleados.empleados_estado.writable          = False
db.empleados.empleados_fecha_creacion.readable  =  db.empleados.empleados_fecha_creacion.writable = False
db.empleados.empleados_hora_creacion.readable   =  db.empleados.empleados_hora_creacion.writable = False
db.empleados.empleados_observaciones.readable   =  db.empleados.empleados_observaciones.writable = False

db.empleados.empleados_fecha_ingreso.readable = False
db.empleados.empleados_fecha_nacimiento.readable = False
db.empleados.empleados_parentesco_emergancia.readable = False
db.empleados.empleados_genero.readable = False

db.empleados.empleados_nombres.requires = IS_NOT_EMPTY(error_message='Debe ingresar un nombre y un apellido')
db.empleados.empleados_identificacion.requires = IS_NOT_EMPTY(error_message='Debe ingresar una identificación')
db.empleados.empleados_genero.requires = [
    IS_IN_SET(('Femenino', 'Masculino')),
    IS_NOT_EMPTY(error_message='Debe ingresar un genero'),
]
db.empleados.empleados_foto.represent = lambda empleados_foto, r : getFotoZoom(r,35,35)
db.empleados.empleados_estado.represent = lambda id, r: emplGetEstado(r)
db.empleados._enable_record_versioning()
db.define_table('usuario_empleado',
    Field('usuario_empleado_empleado','reference empleados'),
    Field('usuario_empleado_usuario','reference auth_user'),
)
db.usuario_empleado._enable_record_versioning()


db.define_table('trasabilidad_notificaciones', 
    Field('email_notificado'),
    Field('usuario_notificado','reference auth_user'),
    Field('cotizacion'),
    Field('cliente'),
    Field('sms'),
    Field('asunto'),
    Field('estado'),
    Field('fecha_notifcacion',default=fecha('all')),
)
db.trasabilidad_notificaciones._enable_record_versioning()

db.define_table('notificaciones_cliente_proyectos', 
    Field('notificaciones_cliente_proyectos_cliente', 'reference clientes'),
    Field('notificaciones_cliente_proyectos_proyecto', 'reference proyectos'),
    Field('notificaciones_cliente_proyectos_sms'),
    Field('notificaciones_cliente_proyectos_asunto'),
    Field('notificaciones_cliente_proyectos_estado',default='notificado'),
    Field('notificaciones_cliente_proyectos_fecha_creacion' , 'integer' ,default=int(str(fecha('fecha')).replace('-',''))),
    Field('notificaciones_cliente_proyectos_hora_creacion' , 'integer' ,default=int(str(fecha('hora')).replace(':','').replace(' ','').replace('.',''))),
)
db.notificaciones_cliente_proyectos._enable_record_versioning()


db.define_table('usuario_predio',
    Field('usuario_predio_predio','reference interioresPredios'),
    Field('usuario_predio_usuario','reference auth_user'),
)
db.usuario_predio._enable_record_versioning()


# -------------------------------------------------------------------------
# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.
#
# More API examples for controllers:
#
# >>> db.mytable.insert(myfield='value')
# >>> rows = db(db.mytable.myfield == 'value').select(db.mytable.ALL)
# >>> for row in rows: print row.id, row.myfield
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# after defining tables, uncomment below to enable auditing
# -------------------------------------------------------------------------
# auth.enable_record_versioning(db)
