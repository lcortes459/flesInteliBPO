# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
@auth.requires_login()
def listado():
    response.title   = T("Proyectos")  
    response.subTitle = T("Listado Proyectos")
    response.icono   = ''
    # response.botton       = """
    #     <button class="btn btn-block btn-primary" id="idBtnRegresarListado" type="button" onclick="pro.nuevoProyecto('listadoProyectos','nuevoProyecto');">
    #         <i class="fas fa-plus"></i>
    #     </button>
    # """
    response.botton       = ''
    multi_dbCliProy       = db.clientesProyectos
    multi_dbProyectos     = db.proyectos
    proyectos             = db( multi_dbCliProy.proyectos_cliente == empresa ).select(multi_dbProyectos.ALL,\
        left=(
            multi_dbProyectos.on(multi_dbProyectos.id==multi_dbCliProy.proyectos_proyecto)))
    return locals()


@auth.requires_login()
def proyecto():
    response.title   = T("Proyectos")  
    response.subTitle = T("Listado Proyectos")
    response.icono   = 'home'
    response.botton       = ''
    return locals()


@auth.requires_login()
def detalleProyecto():
    multi_data            = request.vars
    multi_dbProyectos     = db.proyectos
    return locals()