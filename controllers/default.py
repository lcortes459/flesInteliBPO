# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------
from gluon.contrib.websocket_messaging import websocket_send
from gluon.contrib.user_agent_parser import mobilize

# ---- example index page ----
@auth.requires_login()
#@mobilize
def index():
    response.title   = T("Dashboard")  
    response.subTitle = T("Listado Dashboard")
    response.icono   = 'dashboard'
    response.botton       = ''
    print('grup',grup)
    if grup=='Asesor':
        redirect(URL('ventas','requisiciones'))
    elif grup==['Cliente']:
        redirect(URL('proyectos','listado'))
    elif grup=='Area':
        redirect(URL('clientes','areas'))
    elif grup=='Administrativo':
        redirect(URL('gerente','index'))
    elif grup=='Cli_Turno':
        redirect(URL('cliente','index'))
    elif grup=='Coordinador':
        redirect(URL('proyectos','proyecto'))
    else:
        #websocket_send('http://127.0.0.1:8888', 'Hello World', 'mykey', 'mygroup')
        # import gluon.contrib.simplejson
        # response.title = T("Dashboard requisiciones")
        # res = asivamosMes('all')
        pass
    return locals()

def start():
    iniciales()
    pass


def requisicionesModulos():
    import gluon.contrib.simplejson
    multi_data     = request.vars
    response.title = T("Asi vamos "+str(db.modulos[multi_data.idModulo].nombre))
    categorias = []
    datos       = []
    res    = []
    sql = """
        SELECT
            COUNT(*) as Cantidad,
            re.estado
        FROM
            requisiciones as re
        INNER JOIN modulos as m on
            m.id = re.modulo
        WHERE
            re.modulo = """+str(multi_data.idModulo)+"""
        GROUP BY
            re.estado
    """
    tmp           = db.executesql(sql)
    for x in tmp:
        #res.append(x[1],)
        res.append(
            dict(
                estado = x[1],
                cantidad = x[0]
            )
        )
        #colores.append('#ED561B',)
        pass
    # datos      = gluon.contrib.simplejson.dumps(datos)
    # categorias = gluon.contrib.simplejson.dumps(categorias)
    # colores    = gluon.contrib.simplejson.dumps(colores)
    return locals()

def asivamosMesDef():
    import gluon.contrib.simplejson
    res = asivamosMes(request.vars.tipo)
    return gluon.contrib.simplejson.dumps(res)

def asiVamosDatos():
    multi_data     = request.vars
    multi_requi    = db.requisiciones
    multi_requisi  = db( (multi_requi.estado==multi_data.estado) & (multi_requi.modulo==multi_data.idModulo) ).select(multi_requi.ALL)
    return locals()

def ingresoUsuario():
    import gluon.contrib.simplejson
    multi_emailIngreso    = request.vars.emailIngreso
    multi_passIngreso     = request.vars.passIngreso
    multi_users           = db.auth_user
    multi_tmp             = db().select(multi_users.ALL)
    multi_consul          = db(multi_users.email==multi_emailIngreso).count()
    multi_consulEsta      = db( (multi_users.registration_key) & (multi_users.email==multi_emailIngreso) ).count()
    print('multi_emailIngreso',multi_emailIngreso)
    print('multi_passIngreso',multi_passIngreso)
    print('multi_consulEsta',multi_consulEsta)
    if multi_consul==0:
        multi_valores =dict(multi_valores="usuario")
    elif multi_consulEsta==1:
        multi_valores =dict(multi_valores="estado")
    else:
        multi_Autentic = auth.login_bare(multi_emailIngreso,multi_passIngreso)
        if multi_Autentic:
            multi_valores = str(session.auth.user.first_name)+' '+str(session.auth.user.last_name)
            img = 0
            multi_valores = dict(multi_valores=multi_valores,img=img)
        else:
            # print(00)
            multi_valores = dict(multi_valores="invalido")
            pass
        pass
    return gluon.contrib.simplejson.dumps(multi_valores)
    
# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
