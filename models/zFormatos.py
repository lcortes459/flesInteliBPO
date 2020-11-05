# # -*- coding: utf-8 -*-

# from openpyxl import load_workbook
# from openpyxl import Workbook
# from openpyxl.utils import get_column_letter


# def realizar_formatos(idFor,opc):

# 	if opc == 'cliente':
# 		nit           = db.clientes[idFor].clientes_nit
# 		nombre        = db.clientes[idFor].clientes_nombre
# 	else:
# 		nit           = db.proyectos[idFor].proyectos_nit_proyecto
# 		nombre        = db.proyectos[idFor].proyectos_nombre_proyecto
# 		pass
# 	wb            = Workbook()
# 	ws1           = wb.active
# 	ws1.title     = "Parqueaderos"
# 	ws1['A1']     = 'Nit_proyecto'
# 	ws1['B1']     = 'Distribución'
# 	ws1['C1']     = 'Tipo_Parqueadero'
# 	ws1['D1']     = 'Parqueadero'
# 	ws1['A2']     = nit
# 	ws1['B2']     = 'Zotano'
# 	ws1['C2']     = 'Residencial'
# 	ws1['D2']     = '0001'
# 	ws2           =  wb.create_sheet()
# 	ws2.title     = "Depositos"
# 	ws2['A1']     = 'Nit_proyecto'
# 	ws2['B1']     = 'Distribución'
# 	ws2['C1']     = 'Tipo_Deposito'
# 	ws2['D1']     = 'Deposito'
# 	ws2['A2']     = nit
# 	ws2['B2']     = 'Zotano'
# 	ws2['C2']     = 'Residencial'
# 	ws2['D2']     = '0001'
# 	ws3           =  wb.create_sheet()
# 	ws3.title     =  "Inmuebles"
# 	ws3['A1']     = 'Nit_proyecto'
# 	ws3['B1']     = 'Distribución'
# 	ws3['C1']     = 'Tipo_Inmueble'
# 	ws3['D1']     = 'Inmueble'
# 	ws3['E1']     = 'Nombre_Propietario'
# 	ws3['F1']     = 'Identificación_Propietario'
# 	ws3['G1']     = 'Celular_Propietario'
# 	ws3['H1']     = 'E-mail_Propietario'
# 	ws3['I1']     = 'Nombre_Residente'
# 	ws3['J1']     = 'Identificación_Residente'
# 	ws3['K1']     = 'Celular_Residente'
# 	ws3['L1']     = 'E-mail_Residente'
# 	ws3['M1']     = 'Cantidad_Depositos'
# 	ws3['N1']     = 'Depositos'
# 	ws3['O1']     = 'Cantidad_Parqueaderos'
# 	ws3['P1']     = 'Parqueaderos'
# 	ws3['A2']     = nit
# 	ws3['B2']     = 'Torre 1'
# 	ws3['C2']     = 'Apartamento'
# 	ws3['D2']     = '101'
# 	ws3['E2']     = 'Ramon Valdez'
# 	ws3['F2']     = '10101010'
# 	ws3['G2']     = '1234567890'
# 	ws3['H2']     = 'propietario@email.com'
# 	ws3['I2']     = 'Florinda Meza'
# 	ws3['J2']     = '20202020'
# 	ws3['K2']     = '0123456789'
# 	ws3['L2']     = 'residente@email.com'
# 	ws3['M2']     = '1'
# 	ws3['N2']     = '0001'
# 	ws3['O2']     = '1'
# 	ws3['P2']     = '0001'
# 	wb.save(filename = '/tmp/'+str(str(nombre).replace(' ','_'))+'.xlsx')
# 	resul = '/tmp/'+str(str(nombre).replace(' ','_'))+'.xlsx'
# 	return str(resul)