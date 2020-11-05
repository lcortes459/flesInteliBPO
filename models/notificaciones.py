#!/usr/bin/env python
# -*- coding: utf-8 -*-
# attachments = mail.Attachment('/path/to/photo.jpg', content_id='photo'))

def notificacionCotizacion(idCotizacion,emails,opc,sms,asunto):
	print('soy la funcion que hace la notificacion')
	from gluon.tools import Mail
	mail = Mail()
	mail                     = auth.settings.mailer
	mail.settings.tls        = True
	mail.settings.server     = 'smtp.gmail.com:465'
	mail.settings.sender     = 'lcortes@intelibpo.com'
	mail.settings.login      = 'lcortes@intelibpo.com:abigel2@12'
	multi_dbCotizaciones     = db.cotizaciones
	cotizaciones             = db( multi_dbCotizaciones.id == int(idCotizacion) ).select(multi_dbCotizaciones.ALL).last()
	notificacion             = 0

	if int(opc) == 0:
		mail.send(
			to       = cotizaciones.cotizaciones_email_administrador,
			subject  = asunto,
			message  = sms,
		)
		db.trasabilidad_notificaciones.insert(
			email_notificado   = cotizaciones.cotizaciones_email_administrador,
			usuario_notificado = cotizaciones.cotizaciones_responsable_creacion,
			cotizacion         = cotizaciones.id,
			empresa            = cotizaciones.id,
			sms                = sms,
			asunto             = asunto,
		)
		notificacion = 1
	else:
		tmp = str(emails).replace('[','').replace(']','').replace('"','').replace(' ','').replace(',',' ')
		def Convert(string): 
			li = list(string.split(" ")) 
			return li 
		tmp2 = Convert(tmp)
		for x in tmp2:
			mail.send(
				to       = x,
				subject  = 'Cotización GuardianWeb',
				message  = 'Aviso Importante. Verificar nueva cotización de GuardianWeb'
			)
			tmpEnvio = db.trasabilidad_notificaciones.insert(
				email_notificado   = x,
				usuario_notificado = cotizaciones.cotizaciones_responsable_creacion,
				cotizacion         = cotizaciones.id,
				empresa            = cotizaciones.id,
				sms                = 'Aviso Importante. Verificar nueva cotización GuardianWeb',
				asunto             = 'Nueva Cotización',
			)

			print('tmpEnvio',tmpEnvio)
			pass

		mail.send(
			to       = cotizaciones.cotizaciones_email_administrador,
			subject  = asunto,
			message  = sms
		)
		db.trasabilidad_notificaciones.insert(
			email_notificado   = cotizaciones.cotizaciones_email_administrador,
			usuario_notificado = cotizaciones.cotizaciones_responsable_creacion,
			cotizacion         = cotizaciones.id,
			empresa            = cotizaciones.id,
			sms                = sms,
			asunto             = asunto,
		)
		
		notificacion = opc
		pass
	return str(notificacion)




def notificacionOrdenServicio(idFor,tipoFor,emails,opc):


	print('Estoy acaaaaaaa notificaciones')
	print('Estoy notificaciones idFor',idFor)
	print('Estoy notificaciones tipoFor', tipoFor)
	print('Estoy notificaciones opc',opc)
	print('Estoy notificaciones emails',emails)

	from gluon.tools import Mail
	mail = Mail()
	mail                     = auth.settings.mailer
	mail.settings.tls        = True
	mail.settings.server     = 'smtp.gmail.com:465'
	mail.settings.sender     = 'lcortes@intelibpo.com'
	mail.settings.login      = 'lcortes@intelibpo.com:abigel2@12'
	multi_dbCotizaciones     = db.cotizaciones
	#cotizaciones             = db( multi_dbCotizaciones.id == int(idCotizacion) ).select(multi_dbCotizaciones.ALL).last()
	notificacion             = 0
	ruta                     = realizar_formatos(idFor,tipoFor)
	asunto                   = "Nueva Orden Servicio"
	sms                      = "Se ha generado una nueva orden de servicio"
	print('ruta',ruta)

	if int(opc) == 0:

		mail.send(
			to       = db.clientes[idFor].clientes_email,
			subject  = asunto,
			message  = sms,
			attachments = mail.Attachment(ruta, content_id=db.clientes[idFor].clientes_nombre)
		)
		db.trasabilidad_notificaciones.insert(
			email_notificado   = db.clientes[idFor].clientes_email,
			usuario_notificado = db.clientes[idFor].clientes_responsable_creacion,
			cotizacion         = db.clientes[idFor].id,
			empresa            = db.clientes[idFor].id,
			sms                = sms,
			asunto             = asunto,
		)
		notificacion = 1
	else:

		tmp = str(emails).replace('[','').replace(']','').replace('"','').replace(' ','').replace(',',' ')
		def Convert(string): 
			li = list(string.split(" ")) 
			return li 
		tmp2 = Convert(tmp)
		for x in tmp2:
			mail.send(
				to       = x,
				subject  = asunto,
				message  = sms,
				attachments = mail.Attachment(ruta, content_id=db.clientes[idFor].clientes_nombre)
			)
			tmpEnvio = db.trasabilidad_notificaciones.insert(
				email_notificado   = x,
				usuario_notificado = db.clientes[idFor].clientes_responsable_creacion,
				cotizacion         = db.clientes[idFor].id,
				empresa            = db.clientes[idFor].id,
				sms                = sms,
				asunto             = asunto,
			)

			print('tmpEnvio',tmpEnvio)
			pass

		mail.send(
			to       = db.clientes[idFor].clientes_email,
			subject  = asunto,
			message  = sms,
			attachments = mail.Attachment(ruta, content_id=db.clientes[idFor].clientes_nombre)
		)
		db.trasabilidad_notificaciones.insert(
			email_notificado   = db.clientes[idFor].clientes_email,
			usuario_notificado = db.clientes[idFor].clientes_responsable_creacion,
			cotizacion         = db.clientes[idFor].id,
			empresa            = db.clientes[idFor].id,
			sms                = sms,
			asunto             = asunto,
		)
		
		notificacion = opc
		pass
	return str(notificacion)







def notificacionCreacionCliente(idCliente):
	print('soy la funcion que hace la notificacion crear cliente')
	from gluon.tools import Mail
	mail = Mail()
	mail                     = auth.settings.mailer
	mail.settings.tls        = True
	mail.settings.server     = 'smtp.gmail.com:465'
	mail.settings.sender     = 'lcortes@intelibpo.com'
	mail.settings.login      = 'lcortes@intelibpo.com:abigel2@12'
	# multi_dbCotizaciones     = db.cotizaciones
	# cotizaciones             = db( multi_dbCotizaciones.id == int(idCotizacion) ).select(multi_dbCotizaciones.ALL).last()
	# notificacion             = 0
	# print('Email', cotizaciones.cotizaciones_email_administrador)
	# mail.send(
	# 	to       = cotizaciones.cotizaciones_email_administrador,
	# 	subject  = 'Cotización GuardianWeb',
	# 	message  = 'Aviso Importante. Verificar nueva cotización de GuardianWeb'
	# )
	# db.trasabilidad_notificaciones.insert(
	# 	email_notificado   = cotizaciones.cotizaciones_email_administrador,
	# 	usuario_notificado = cotizaciones.cotizaciones_responsable_creacion,
	# 	cotizacion         = cotizaciones.id,
	# 	empresa            = cotizaciones.id,
	# 	sms                = 'Aviso Importante. Verificar nueva cotización GuardianWeb',
	# 	asunto             = 'Nueva Cotización',
	# )
	notificacion = 1
	return str(notificacion)



def notiActivaDestiEmpresa(idEmpresa,asunto,sms):
	print('soy la funcion que hace la notificacion notiActivaDestiEmpresa')
	from gluon.tools import Mail
	mail = Mail()
	#mail                     = auth.settings.server 
	mail                     = auth.settings.mailer
	mail.settings.tls        = True
	mail.settings.server     = 'mail.cictemporal.com:465'
	mail.settings.sender     = 'admin@cictemporal.com'
	mail.settings.login      = 'admin@cictemporal.com:(qiX4=Q[gBs1'
	# mail.settings.tls        = 'smtp.tls'
	multi_dbEmpresas         = db.empresas
	multi_dbModEmp           = db.modulosEmpresas
	notificacion             = 0
	mods                     = db(multi_dbModEmp.empresa==idEmpresa).select(multi_dbModEmp.modulo)
	if mods:
		for x in mods:
			modUsuario       = db(db.usuarioModulo.modulo==x.modulo).select(db.usuarioModulo.usuario).first()
			if modUsuario:
				emails       = db(db.auth_user.id==modUsuario.usuario).select(db.auth_user.email).first()
				mail.send(
					to       = emails.email,
					subject  = asunto,
					message  = sms
				)
				db.trasabilidad_notificaciones.insert(
					email_notificado   = emails.email,
					usuario_notificado = modUsuario.usuario,
					requisicion        = 0,
					empresa            = idEmpresa,
					sms                = sms,
					asunto             = asunto,
					)
				notificacion = 1
			else:
				notificacion = 0
				pass
			pass
	else:
		notificacion = 0
		pass
	return int(notificacion)



def notiActivaDestiModulo(idEmpresa,asunto,sms,idModulo):
	from gluon.tools import Mail
	mail = Mail()
	mail                     = auth.settings.mailer
	mail.settings.tls        = True
	mail.settings.server     = 'mail.cictemporal.com: 465'
	mail.settings.sender     = 'admin@cictemporal.com'
	mail.settings.login      = 'admin@cictemporal.com:(qiX4=Q[gBs1'
	multi_dbEmpresas         = db.empresas
	multi_dbModEmp           = db.modulosEmpresas
	notificacion             = 0

	modUsuario               = db(db.usuarioModulo.modulo==idModulo).select(db.usuarioModulo.usuario).first()
	if modUsuario:
		emails               = db(db.auth_user.id==modUsuario.usuario).select(db.auth_user.email).first()
		mail.send(
			to       = emails.email,
			subject  = asunto,
			message  = sms
		)
		notificacion = 1
		db.trasabilidad_notificaciones.insert(
			email_notificado   = emails.email,
			usuario_notificado = modUsuario.usuario,
			requisicion        = 0,
			empresa            = idEmpresa,
			sms                = sms,
			asunto             = asunto,
			estado             = notificacion
			)
	else:
		notificacion = 0
		db.trasabilidad_notificaciones.insert(
			email_notificado   = emails.email,
			usuario_notificado = modUsuario.usuario,
			requisicion        = 0,
			empresa            = idEmpresa,
			sms                = sms,
			asunto             = asunto,
			estado             = notificacion
			)
		pass
	return int(notificacion)


def notiAsignaDesasignatiEmpresa(idEmpresa,asunto,sms,idAsesor):
	from gluon.tools import Mail
	mail = Mail()
	mail                     = auth.settings.mailer
	mail.settings.tls        = True
	mail.settings.server     = 'mail.cictemporal.com: 465'
	mail.settings.sender     = 'admin@cictemporal.com'
	mail.settings.login      = 'admin@cictemporal.com:(qiX4=Q[gBs1'
	multi_dbEmpresas         = db.empresas
	multi_dbModEmp           = db.modulosEmpresas
	notificacion             = 0
	
	if idAsesor:
		emails               = db(db.auth_user.id==idAsesor).select(db.auth_user.email).first()
		mail.send(
			to       = emails.email,
			subject  = asunto,
			message  = sms
		)
		notificacion = 1
		db.trasabilidad_notificaciones.insert(
			email_notificado   = emails.email,
			usuario_notificado = idAsesor,
			requisicion        = 0,
			empresa            = idEmpresa,
			sms                = sms,
			asunto             = asunto,
			estado             = notificacion
			)
	else:
		notificacion = 0
		db.trasabilidad_notificaciones.insert(
			email_notificado   = emails.email,
			usuario_notificado = idAsesor,
			requisicion        = 0,
			empresa            = idEmpresa,
			sms                = sms,
			asunto             = asunto,
			estado             = notificacion
			)
		pass
	return int(notificacion)



def notiRequisiciones(idEmpresa,asunto,sms,rama,modulo):
	from gluon.tools import Mail
	mail = Mail()
	mail                     = auth.settings.mailer
	mail.settings.tls        = True
	mail.settings.server     = 'mail.mail.cictemporal.com: 465'
	mail.settings.sender     = 'admin@cictemporal.com'
	mail.settings.login      = 'admin@cictemporal.com:s@eii2@19'
	multi_dbEmpresas         = db.empresas
	multi_dbModEmp           = db.modulosEmpresas
	notificacion             = 0
	
	if rama:
		emails               = db(db.auth_user.rama==rama).select(db.auth_user.email,db.auth_user.id)

		if emails:
			for x in emails:
				mail.send(
					to       = x.email,
					subject  = asunto,
					message  = sms
				)
				notificacion = 1
				db.trasabilidad_notificaciones.insert(
					email_notificado   = x.email,
					usuario_notificado = x.id,
					requisicion        = 0,
					empresa            = idEmpresa,
					sms                = sms,
					asunto             = asunto,
					estado             = notificacion
					)

				emialCoordi  = db(db.cordinadoresDolientes.doliente==x.id).select(db.cordinadoresDolientes.cordinador).last()
				mail.send(
					to       = db.auth_user[emialCoordi.cordinador].email,
					subject  = asunto,
					message  = sms
				)
				db.trasabilidad_notificaciones.insert(
					email_notificado   = db.auth_user[emialCoordi.cordinador].email,
					usuario_notificado = emialCoordi.cordinador,
					requisicion        = 0,
					empresa            = idEmpresa,
					sms                = sms,
					asunto             = asunto,
					estado             = notificacion
					)
				pass
			pass
	else:
		notificacion = 0
		db.trasabilidad_notificaciones.insert(
			email_notificado   = '',
			usuario_notificado = 0,
			requisicion        = 0,
			empresa            = idEmpresa,
			sms                = sms,
			asunto             = asunto,
			estado             = notificacion
			)
		pass
	return int(notificacion)



"""
	#from gluon.contrib.sms_utils import SMSCODES, sms_email
	# email = sms_email('57 (310) 391-5810','T-Mobile USA (tmail)')
	# mail.send(to=email, subject='test', message='test')
	# from twilio.rest import Client

	# account_sid = "ACd71aebd3b4b29a46023e211e20d21a68"
	# auth_token = "57a8cd34bad1f8d13f28a104b3ef396f"
	# client = Client(account_sid, auth_token)

	# message = client.messages.create(
	# 	body ="Aviso Importante. Revisa Soe de inmediato. Verificar la creacion de la empresa: "+str(nombre)+"", # mensaje
	# 	to = "+573103915810", # 3108136913remplazamos con nuestro numero o al que queramos enviar el sms
	# 	from_= "+16789296482"
	# ) # el numero que nos asigno twilio

	# print (message.sid)
	# from twilio.rest import Client

	# # client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
	# account_sid = "ACd71aebd3b4b29a46023e211e20d21a68"
	# auth_token = "57a8cd34bad1f8d13f28a104b3ef396f"
	# client = Client(account_sid, auth_token)
	# # this is the Twilio sandbox testing number
	# from_whatsapp_number='whatsapp:+16789296482'
	# # replace this number with your own WhatsApp Messaging number
	# to_whatsapp_number='whatsapp:+573103915810'

	# client.messages.create(body='Aviso Importante. Revisa Soe de inmediato.',
	#                        from_=from_whatsapp_number,
	#                        to=to_whatsapp_number)
"""