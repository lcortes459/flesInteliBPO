# -*- coding: utf-8 -*-
from datetime import  datetime, date, timedelta, time 


def fecha(par):
    import time
    fecha_actual = request.now
    fecha        = str(fecha_actual)[:16]
    if par == 'all':
        fecha = str(fecha_actual)[:16]
    elif par == 'fecha':
        fecha = str(fecha_actual)[:10]
    elif par == 'hora':
        fecha = time.strftime("%H:%M:%S") #Formato de 24 horas
    else:
        fecha = fecha
        pass
    return fecha


def fechaFormato(valor,opc):
    if opc == 'fecha':
        anio = str(valor)[:4]
        mes  = str(valor)[4:-2]
        dia  = str(valor)[6:]
        formato = anio+'-'+str(mes)+'-'+str(dia)
    else:
        hora = str(valor)[:2]
        minu = str(valor)[2:]
        formato = hora+':'+str(minu)
        pass
    return formato


def crud(tabla,opc,data,idRow):
	"""
		1 = Crear
		2 = Actualizar
		3 = Leer
		4 = Eliminar
	"""
	tour_dbTabla = tabla
	if int(opc) == 1:
		tour_idTabla = tour_dbTabla.insert(**data)
		return tour_idTabla,opc
	elif int(opc) == 2:
		db(tour_dbTabla.id == idRow).update(**data)
		return data,opc
	elif int(opc) == 3:
		myorder = tour_dbTabla.id
		data = db(tour_dbTabla.estado==True).select(tour_dbTabla.ALL, orderby=myorder)
		return data,opc
	else:
		db(tour_dbTabla.id == idRow).delete()
		return idRow,opc
		pass
	pass



# def selectUnique(tabla,idRow,campoResult):
# 	data = db(tabla == int(idRow)).select(tabla.str(campoResult))
# 	return data

def verificaPass():
    cambiopass =  session.auth.user.fechaactualizacionpass
    tiempo = 0
    if cambiopass=='0000-00-00':
        tiempo = 91
    elif cambiopass!=str(hr_dia)[:10]:
        formato = "%Y-%m-%d"
        fechacambiopass = datetime.strptime(cambiopass, formato)
        fechaactualpass = datetime.strptime(str(hr_dia)[:10], formato)
        actuali =  fechaactualpass - fechacambiopass
        actuali = str(actuali).split(' ')
        tiempo = actuali[0]
        pass
    return tiempo


def htmlModal():
    swalEstilos = URL('static','plugin_tpl/css/sweetalert.css')
    imgFondoModal = URL('static','plugin_tpl/img/bcklog1.jpg')
    nombresUsuario = session.auth.user.first_name +' '+ session.auth.user.last_name
    swalScript = URL('static','plugin_tpl/js/sweetalert.min.js')
    jqScript = URL('static','plugin_tpl/plugins/jQuery/jQuery-2.1.4.min.js')
    cierreSession = URL('default','user/logout')
    resul = XML( """
        <script src="https://cdn.jsdelivr.net/npm/sweetalert2@8"></script>
        <div class="modal fade bd-example-modal-sm" id="modalCambio" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-sm" role="document">
                <div class="modal-content" style="background-image: url(%s) ">
                  <div class="modal-header">
                    <h3 class="modal-title" id="exampleModalLabel"><b>%s</b></h3>
                    <h5>Por seguridad debe realizar cambio de contraseña para poder ingresar al sistema</h5>
                  </div>
                  <div class="modal-body">
                    <form>
                        <div class="form-group">
                            <label for="recipient-name" class="form-control-label">Contraseña Actual</label>
                            <div class="input-group">
                                <input type="password" class="form-control" id="passwordOld" placeholder="Contraseña actual" autofocus="">
                                <div class="input-group-addon" id="iconoConfirmacionactualrojo" title="Esperando ser confirmada" style="color: grey; display: no_ne;">
                                  <i class="fa fa-exclamation" aria-hidden="true"></i>
                                </div>
                                <div class="input-group-addon" id="iconoConfirmacionactualverde" title="La contraseña es diferente a la nueva" style="color: green; display: none;">
                                  <i class="fa fa-check" aria-hidden="true"></i>
                                </div>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="recipient-name" class="form-control-label">Contraseña Nueva</label>
                            <div class="input-group">
                                <input type="password" class="form-control" id="passwordOne" placeholder="Contraseña nueva" onkeyup="validacion($(this).val())">
                                <div class="input-group-addon" id="iconoConfirmacionnuevarojo" title="La contraseña debe tener minimo 8 caracteres" style="color: red; display: no_ne;">
                                  <i class="fa fa-close"></i>
                                </div>
                                <div class="input-group-addon" id="iconoConfirmacionnuevaverde" title="La contraseña cumple con el estándar de longitud" style="color: green; display: none;">
                                  <i class="fa fa-check" aria-hidden="true"></i>
                                </div>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="recipient-name" class="form-control-label">Confirmar contraseña</label>
                            <div class="input-group">
                                <input type="password" class="form-control" id="passwordTwo" placeholder="Confirmar contraseña" onkeyup="confirma()">
                                <div class="input-group-addon" id="iconoConfirmacionconfirojo" title="La contraseña es diferente a la nueva" style="color: red; display: none;">
                                  <i class="fa fa-close"></i>
                                </div>
                                <div class="input-group-addon" id="iconoConfirmacionconfiverde" title="La contraseña es igual a la nueva" style="color: green; display: no_ne;">
                                  <i class="fa fa-check" aria-hidden="true"></i>
                                </div>
                            </div>
                        </div>
                        <div class="form-check">
                            <label class="form-check-label">
                              <input type="checkbox" id="change" class="form-check-input">
                              Mostrar contraseñas
                            </label>
                        </div>
                    </form>
                  </div>
                  <div class="modal-footer">
                    <button type="button" id="btncambioContrasena" class="btn btn-primary btn-block btn-success" disabled onclick="cambioContrasena()">Cambiar contraseña</button>
                  </div>
                </div>
            </div>
        </div>
        <script src="%s"></script>
        <script src="%s"></script>
        <script>
            $(function() {
                $("#modalCambio").modal({
                    keyboard: false,
                    backdrop: false
                });
            });
            validacion = function(obj){
                var actual = $('#passwordOld').val();
                var nueva = $('#passwordOne').val();
                var confinueva = $('#passwordTwo').val();
                var tamContrasena = obj.length;

                if ( (tamContrasena>=8) && (actual!=nueva) ) {

                    $('#iconoConfirmacionnuevarojo').hide();
                    $('#iconoConfirmacionnuevaverde').show();
                    
                    if (actual!=nueva) {
                        $('#iconoConfirmacionactualrojo').hide();
                        $('#iconoConfirmacionactualverde').show();
                    }
                }else{

                    $('#iconoConfirmacionactualrojo').show();
                    $('#iconoConfirmacionactualverde').hide();

                    $('#iconoConfirmacionnuevaverde').hide();
                    $('#iconoConfirmacionnuevarojo').show();

                    $('#iconoConfirmacionconfiverde').hide();
                    $('#iconoConfirmacionconfirojo').show();
                }
                if( $('#iconoConfirmacionnuevaverde').is(":visible") && $('#iconoConfirmacionactualverde').is(":visible") && $('#iconoConfirmacionconfiverde').is(":visible") ){
                    $('#btncambioContrasena').removeAttr('disabled');
                }else{
                    $('#btncambioContrasena').prop('disabled',true);
                }
            }
            confirma = function(){
                var nueva = $('#passwordOne').val();
                var confinueva = $('#passwordTwo').val();
                if (confinueva==nueva) {
                    $('#iconoConfirmacionconfiverde').show();
                    $('#iconoConfirmacionconfirojo').hide();
                }else{
                    $('#iconoConfirmacionconfiverde').hide();
                    $('#iconoConfirmacionconfirojo').show();
                }

                if( $('#iconoConfirmacionnuevaverde').is(":visible") && $('#iconoConfirmacionactualverde').is(":visible") && $('#iconoConfirmacionconfiverde').is(":visible") ){
                    $('#btncambioContrasena').removeAttr('disabled');
                }else{
                    $('#btncambioContrasena').prop('disabled',true);
                }
            }

            var conteo = 0;

            $("#change").click(function() {
                if(conteo == 0) {
                    conteo = 1;

                    $('#passwordOld').removeAttr("type", "password");
                    $("#passwordOld").prop("type", "text");

                    $('#passwordOne').removeAttr("type", "password");
                    $("#passwordOne").prop("type", "text");

                    $('#passwordTwo').removeAttr("type", "password");
                    $("#passwordTwo").prop("type", "text");
                }else{
                    conteo = 0;

                    $('#passwordOld').removeAttr("type", "text");
                    $("#passwordOld").prop("type", "password");

                    $('#passwordOne').removeAttr("type", "text");
                    $("#passwordOne").prop("type", "password");

                    $('#passwordTwo').removeAttr("type", "text");
                    $("#passwordTwo").prop("type", "password");
                }
            }); 

            cambioContrasena = function(){
                var actual = $('#passwordOld').val();
                var nueva = $('#passwordOne').val();
                Swal.fire({
                  title: 'Confirmación',
                  text: "Seguro(a) desea cambiar la contraseña con estos datos",
                  type: 'info',
                  showCancelButton: true,
                  confirmButtonColor: '#3085d6',
                  cancelButtonColor: '#d33',
                  confirmButtonText: 'Si cambiar',
                }).then((result) => {
                    if (result.value) {
                        $.ajax({
                            url: 'cambioContrasena',
                            type: 'GET',
                            data: {actual:actual,nueva:nueva},
                        })
                        .done(function(data) {
                            if (data==0) {
                                Swal.fire({
                                  title: "Upss",
                                  text:'La contraseña actual ingresada no es valida Verifique e intente nuevamente',
                                  type: 'error',
                                  showCancelButton: false,
                                  confirmButtonColor: '#3085d6',
                                  cancelButtonColor: '#d33',
                                  confirmButtonText: 'Verificar',
                                }).then((result) => {
                                    $('#passwordOld').focus()
                                });
                            }else{
                                Swal.fire({
                                  title: "Password cambiado con éxito",
                                  text: "La session se cerrara para aplicar los cambios",
                                  type: 'success',
                                  showCancelButton: false,
                                  confirmButtonColor: '#3085d6',
                                  cancelButtonColor: '#d33',
                                  confirmButtonText: 'Terminar',
                                }).then((result) => {
                                   window.location.href="%s"
                                });
                            }
                        });
                    }
                });
            }
        </script>
    """ %(imgFondoModal,nombresUsuario,jqScript,swalScript,cierreSession))
    return resul



def getFotoZoom(r,ws,hs):
    if 'empleados_foto' in r:
        img = r.empleados_foto
    elif 'logo' in r:
        img = r.logo
    if img:
        resul = XML(""" <img   src="%s"  width="%s" height="%s" > """  %(URL('default','download/%s' %(img)),ws,hs) )
    else:
        ff = """ <img src="%s"  width="%s" height="%s"> """ %(URL('static','images/img/user7-128x128.jpg'),ws,hs)
        fh = """ <img src="%s"  width="%s" height="%s"> """ %(URL('static','images/img/user2-160x160.jpg'),ws,hs)
        if r.empleados_genero:
            if r.empleados_genero[0] == 'Femenino':
                resul = XML(ff)
            else:
                resul = XML(fh)
        else:
            resul = ''
    return resul

def getCliente(r):
    if r.cliente:
        resul = db.clientes[r.cliente].razon_social
    else:
        resul = ''
    return resul



# def userGetEstado(r,tabla):
#     tablaDB = tabla
#     print('tablaDB',tablaDB)
#     if tabla == 'auth_user':
#         estado = tablaDB[r].registration_key 
#           # 
#         if (estado==None) or (estado==''):
#             resul = XML("""<div id="div_usu_%s" title='Desactivar Usuario'><a href="#!" onclick="users.updateEstado(0,'%s')" class="btn btn-social-icon bg-green"><i class="fa fa-check"></i></a></div>""" %(r.id,r.id))
#         else:
#             resul = XML("""<div id="div_usu_%s" title='Activar Usuario'><a href="#!" onclick="users.updateEstado(1,'%s')" class="btn btn-social-icon bg-red"><i class="fa fa-close"></i></a></div>""" %(r.id,r.id))
#     else:
#         estado = tablaDB[r].empleados_estado

#         if (estado==True) or (estado==1):
#             resul = XML("""<div id="div_usu_%s" title='Desactivar Usuario'><a href="#!" onclick="users.updateEstado(0,'%s')" class="btn btn-social-icon bg-green"><i class="fa fa-check"></i></a></div>""" %(r.id,r.id))
#         else:
#             resul = XML("""<div id="div_usu_%s" title='Activar Usuario'><a href="#!" onclick="users.updateEstado(1,'%s')" class="btn btn-social-icon bg-red"><i class="fa fa-close"></i></a></div>""" %(r.id,r.id))
#         pass
#     return resul

def userGetEstado(r):
    resul  = ''
    if r:
        estado = r.registration_key
        if (estado==None) or (estado==''):
            resul = XML("""<div id="div_usu_%s" title='Desactivar usuario'><a href="#!" onclick="template.updateEstado(0,'%s')" class="btn btn-social-icon bg-green"><i class="fa fa-check"></i></a></div>""" %(r.id,r.id))
        else:
            resul = XML("""<div id="div_usu_%s" title='Activar usuario'><a href="#!" onclick="template.updateEstado(1,'%s')" class="btn btn-social-icon bg-red"><i class="fa fa-times"></i></a></div>""" %(r.id,r.id))
            pass
        pass
    return resul


def emplGetEstado(r):
    resul  = ''
    if r:
        estado = r.empleados_estado
        if (estado==True) or (estado=='True'):
            resul = XML("""<div id="div_empl_%s" title='Desactivar ampleado'><a href="#!" onclick="template.updateEstadoEmplado(0,'%s')" class="btn btn-social-icon bg-green"><i class="fa fa-check"></i></a></div>""" %(r.id,r.id))
        else:
            resul = XML("""<div id="div_empl_%s" title='Activar empleado'><a href="#!" onclick="template.updateEstadoEmplado(1,'%s')" class="btn btn-social-icon bg-red"><i class="fa fa-times"></i></a></div>""" %(r.id,r.id))
            pass
        pass
    return resul



def getFotoUsuario(id):
    lastIdEmplado   = db(db.usuario_empleado.usuario_empleado_usuario==id).select(db.usuario_empleado.ALL).last()
    if lastIdEmplado:
        empleado = db.empleados[lastIdEmplado.usuario_empleado_empleado]
        
        if empleado.empleados_foto:
            resul = URL('default','download/%s' %(empleado.empleados_foto))
        else:
            ff = URL('static','images/img/user7-128x128.jpg')
            fh = URL('static','images/img/user2-160x160.jpg')
            if empleado.empleados_genero:
                if empleado.empleados_genero[0] == 'Femenino':
                    resul = ff
                else:
                    resul = fh
            else:
                resul = ''
    else:
        resul = URL('static','images/logoGuardianweb.png')
        pass
    return resul



def getCodigoPredio(r):
    resul = URL('static','img/icons/%s' %(f))

    return resul



def estadoGetEstado(r):
    estado = r.est
    if (estado==None) or (estado=='') or (estado==False):
        resul = XML("""<div id="div_usu_%s" title='Habilitar'><a href="#!" onclick="app.updateEstado(1,'%s')" class="btn btn-social-icon bg-red"><i class="fa fa-close"></i></a></div>""" %(r.id,r.id))
    else:
        resul = XML("""<div id="div_usu_%s" title='Desactivar'><a href="#!" onclick="app.updateEstado(0,'%s')" class="btn btn-social-icon bg-green"><i class="fa fa-check"></i></a></div>""" %(r.id,r.id))
    return resul


def SetMoneda(num, simbolo="$", n_decimales=2):
    """Convierte el numero en un string en formato moneda
    SetMoneda(45924.457, 'RD$', 2) --> 'RD$ 45,924.46'     
    """
    #num = float(num)
    #con abs, nos aseguramos que los dec. sea un positivo.
    n_decimales = abs(n_decimales)
    #se redondea a los decimales idicados.
    num = round(num, n_decimales)
    #se divide el entero del decimal y obtenemos los string
    num, dec = str(num).split(".")
    #si el num tiene menos decimales que los que se quieren mostrar,
    #se completan los faltantes con ceros.
    dec += "0" * (n_decimales - len(dec))
    #se invierte el num, para facilitar la adicion de comas.
    num = num[::-1]
    #se crea una lista con las cifras de miles como elementos.
    l = [num[pos:pos+3][::-1] for pos in range(0,50,3) if (num[pos:pos+3])]
    l.reverse()
    #se pasa la lista a string, uniendo sus elementos con comas.
    num = str.join(".", l)
    #si el numero es negativo, se quita una coma sobrante.
    try:
        if num[0:2] == "-,":
            num = "-%s" % num[2:]
    except IndexError:
        pass
    #si no se especifican decimales, se resulrna un numero entero.
    if not n_decimales:
        return "%s%s" % (simbolo, num)
    return "%s%s" % (simbolo, num)


def cantSucur(r):
    s = db.sucursales
    resul = db(s.cliente==r).count()
    return resul

def getNom(r,s):
    resul = "%s%s(%s)" % (r,'    ',s)
    return resul



def getEvent(start,end):
    ag = db.agenda
    u = db.auth_user
    c = db.sucursales
    n = db.novedades_agenda
    pto = auth.user.punto
    cli_usu = auth.user.cliente
    events = []

    if ( (rol[0]==2) | (rol[0]==5) ):
        agenda = db(  (ag.cliente==cli_usu) & (ag.fecha_inicio >= str(start)+' 00:00') & (ag.fecha_fin <= str(end)+' 23:59')).select(ag.ALL, u.id,u.first_name,u.tipo,u.last_name,u.foto,c.sucursal,n.nombre,
            left=[u.on(ag.id_usuario == u.id),c.on(ag.id_sucursal == c.id),n.on(ag.id_novedad == n.id)])
    else:
        agenda = db( (ag.p_operacion==pto) &  (ag.fecha_inicio >= str(start)+' 00:00') & (ag.fecha_fin <= str(end)+' 23:59')).select(ag.ALL, u.id,u.first_name,u.tipo,u.last_name,u.foto,c.sucursal,n.nombre,
            left=[u.on(ag.id_usuario == u.id),c.on(ag.id_sucursal == c.id),n.on(ag.id_novedad == n.id)])
        pass

    for item in agenda:

        usAsesor = item.auth_user.first_name+ ' '+ item.auth_user.last_name
        usFoto = item.auth_user.foto
        usImg = getFotoUsuario(item.auth_user.id)
        tipo= item.auth_user.tipo[0]


        #Agenda
        agId = item.agenda.id
        agInicio = item.agenda.fecha_inicio
        agFin = item.agenda.fecha_fin
        agNotas = item.agenda.notas
        estado = item.agenda.id_estado
        color = item.agenda.color

        #CLientes
        if (item.agenda.id_sucursal!=''):
            if item.agenda.id_sucursal==None:
                cNombre = item.novedades_agenda.nombre
                sTitle = item.novedades_agenda.nombre    
            else:
                cNombre = '<small><b>Visitar Sucursal</b>:</small><br>'+item.sucursales.sucursal
                sTitle ='Visitar Sucursal: '+item.sucursales.sucursal    
                pass
            pass

        if item.agenda.id_estado==3:
            color = 'green'
        elif item.agenda.id_estado==2:
            color = 'orange'
        else:
            color = item.agenda.color
            pass

        obj={'estado':estado,'tipo':tipo,'id':agId,'title':usAsesor, 'start':agInicio, 'end':agFin,'cliente':cNombre,'asesor': usAsesor,'nota':agNotas,'foto':usImg,'details':sTitle,'color':color}
        events.append(obj)

    return json.dumps(events)




AVG_EARTH_RADIUS = 6371  # in km


def haversine(point1, point2, miles=False):
    from math import radians, cos, sin, asin, sqrt
    """ Calculate the great-circle distance bewteen two points on the Earth surface.

    :input: two 2-tuples, containing the latitude and longitude of each point
    in decimal degrees.

    Example: haversine((45.7597, 4.8422), (48.8567, 2.3508))

    :output: Returns the distance bewteen the two points.
    The default unit is kilometers. Miles can be returned
    if the ``miles`` parameter is set to True.

    """
    # unpack latitude/longitude
    lat1, lng1 = point1
    lat2, lng2 = point2

    # convert all latitudes/longitudes from decimal degrees to radians
    lat1, lng1, lat2, lng2 = map(radians, (lat1, lng1, lat2, lng2))

    # calculate haversine
    lat = lat2 - lat1
    lng = lng2 - lng1
    d = sin(lat * 0.5) ** 2 + cos(lat1) * cos(lat2) * sin(lng * 0.5) ** 2
    h = 2 * AVG_EARTH_RADIUS * asin(sqrt(d))
    if miles:
        return h * 0.621371  # in miles
    else:
        return h  # in kilometers sucur = qr_sucur = db(r.id_sucursal==sucur.id).select(sucur.qr).first()['qr']


def getQr(qr):
    r = db.sucursales[qr]
    an= '25%'
    alt = '25%'
    resul = XML("""<img  class="center-block"  src="%s"  width="%s" height="%s" >"""  %(URL('default','download/%s' %(r.qr)),an,alt) )   
    return resul


def getUsuariosCliente(idCliente):
    multi_dbUsers = db.auth_user
    ctna              = db( (multi_dbUsers.cliente == idCliente) & ( (multi_dbUsers.registration_key == None) | (multi_dbUsers.registration_key == 'None') | (multi_dbUsers.registration_key == '')) ).count() 
    resul = XML("""
        <a  
            class="btn btn-app" 
            style="margin: 0px 10px 0px 0px; min-width: 30px; height: 35px;"
        >
            <span class="badge badge-primary" style="font-size: 12px;">"""+str(ctna)+"""</span>
            <i class="fa fa-users" style="color: grey;margin-top:-7px;"></i> 
        </a>
    """)
    return resul


def getNotificacionesCliente(idCliente):
    multi_dbNotificaciones = db.notificaciones_cliente_proyectos
    ctna              = db(multi_dbNotificaciones.notificaciones_cliente_proyectos_cliente == idCliente).count() 
    resul = XML("""
        <a  
            class="btn btn-app" 
            style="margin: 0px 10px 0px 0px; min-width: 30px; height: 35px;"
        >
            <span class="badge badge-primary" style="font-size: 12px;">"""+str(ctna)+"""</span>
            <i class="fa fa-bell" style="color: grey;margin-top:-7px;"></i> 
        </a>
    """)
    return resul


def getNotificacionesProyecto(idProyecto):
    multi_dbNotificaciones = db.notificaciones_cliente_proyectos
    ctna              = db(multi_dbNotificaciones.notificaciones_cliente_proyectos_proyecto == idProyecto).count() 
    resul = XML("""
        <a  
            class="btn btn-app" 
            style="margin: 0px 10px 0px 0px; min-width: 30px; height: 35px;"
        >
            <span class="badge badge-primary" style="font-size: 12px;">"""+str(ctna)+"""</span>
            <i class="fa fa-bell" style="color: grey;margin-top:-7px;"></i> 
        </a>
    """)
    return resul


def getUsuariosProyectos(idProyecto):
    multi_dbUsers = db.auth_user
    ctna              = db( (multi_dbUsers.proyecto == idProyecto) & ( (multi_dbUsers.registration_key == None) | (multi_dbUsers.registration_key == 'None') | (multi_dbUsers.registration_key == '')) ).count() 
    resul = XML("""
        <a  
            class="btn btn-app" 
            style="margin: 0px 10px 0px 0px; min-width: 30px; height: 35px;"
        >
            <span class="badge badge-primary" style="font-size: 12px;">"""+str(ctna)+"""</span>
            <i class="fa fa-users" style="color: grey;margin-top:-7px;"></i> 
        </a>
    """)   
    return resul

def getProyectosCliente(idCliente):
    multi_dbClientesProyectos = db.clientesProyectos
    multi_dbProyectos         = db.proyectos
    ctna              = db( (multi_dbClientesProyectos.proyectos_cliente == idCliente) & (multi_dbProyectos.proyectos_estado == True)).select(multi_dbClientesProyectos.ALL,\
        left = (
            multi_dbProyectos.on(multi_dbProyectos.id == multi_dbClientesProyectos.proyectos_proyecto)
            )) 
    resul = XML("""
        <a  
            class="btn btn-app" 
            style="margin: 0px 10px 0px 0px; min-width: 30px; height: 35px;"
            onclick="ctz.verProyectos('listadoClientes','verProyectos','Listado Proyectos ("""+str(db.clientes[idCliente].clientes_nombre)+""")',"""+str(idCliente)+""");"
        >
            <span class="badge badge-primary" style="font-size: 12px;">"""+str(len(ctna))+"""</span>
            <i class="fa fa-home" style="color: grey;margin-top:-7px;"></i> 
        </a>
    """)
    return resul