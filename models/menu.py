# # -*- coding: utf-8 -*-


response.menu = []


def is_session():
    return True if auth.is_logged_in() else False

if is_session():
    idUser               = auth.user.id
    nameUser             = "%s %s" %(auth.user.first_name,auth.user.last_name)
    emailUser            = auth.user.email
    grup                 = auth.user.tipo
    proyecto             = auth.user.proyecto
    empresa              = auth.user.cliente 
    estado               = auth.user.registration_key
    pass

# lpAllTables()



def plantilla():
    if grup==['Cliente']:
        plantilla = 'templateClientes.html'
    elif ( (grup==['Asesor']) | (grup==['Asesor Ventas'])):
        plantilla = 'templateAsesor.html'
    elif grup==['Coordinador']:
        plantilla = 'templateCoordinador.html'
    elif grup==['Administrador']:
        plantilla = 'template.html'
    elif grup==['stationJob']:
        plantilla = 'templateStationJob.html'
    else:
        plantilla = 'templateDeveloper.html'
        pass

    return plantilla
