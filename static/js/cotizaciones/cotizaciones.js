var ctz = {

	start: function() {
		
		this.ready();
	},
	/*
		322445690 Soacha
		3104428047 Serios
		3143137261 Salir rutina
		3124235099
	*/

	ready: function() {
		$('#idListadoCotizacionesTable').DataTable({
			"order": [[ 5, "asc" ]]
		});
		$('#btnGuardarCotizacion').click(function(event) {
			
            if ($('#cotizaciones_nombre_proyecto').val() === '') {
                template.validaCampo('Nombre Proyecto');
            } else if ($('#cotizaciones_nit_proyecto').val() === '') {
                template.validaCampo('Nit Proyecto');
            } else if ($('#cotizaciones_ciudad').val() === '') {
                template.validaCampo('Ciudad');
            } else if ($('#cotizaciones_direccion_proyecto').val() === '') {
                template.validaCampo('Dirección');
            } else if ($('#cotizaciones_nombre_administrador').val() === '') {
                template.validaCampo('Nombre Administrador');
            } else if ($('#cotizaciones_celular_administrador').val() === '') {
                template.validaCampo('Celular Administrador');
            } else if ($('#cotizaciones_email_administrador').val() === '') {
                template.validaCampo('Email Administrador');
            } else if ($('#cotizaciones_cantidad_predios').val() === '') {
                template.validaCampo('Cantidad Inmuebles');
            } else if ($('#cotizaciones_plan').val() === '') {
                template.validaCampo('Plan cotización');
            } else {


                var dat = $('#formularioCtz').serialize();
                $('#cotizaciones_telefono_administrador,#cotizaciones_observacion,#cotizaciones_nombre_proyecto,#cotizaciones_nit_proyecto,#cotizaciones_ciudad,#cotizaciones_direccion_proyecto,#cotizaciones_nombre_administrador,#cotizaciones_celular_administrador,#cotizaciones_email_administrador,#cotizaciones_cantidad_predios,#cotizaciones_plan').attr('disabled', true);
                $('#idBtnRegresarListado').hide();
                $('#botoneraGurdarCotizacion').hide();
                $('#botoneraGurdando').show();
                $.ajax({
                    url: 'nuevaCotizacion',
                    type: 'POST',
                    data: dat,
                })
                .done(function(data) {
                    console.log(data);
                    if ((data == 0) || (data === '0')) {
                        template.resulError('No se pudo crear la cotización. Verifique e intente nuevamente.');
                    } else {
                        template.resulSucces('Cotización:' + data + ' creada con éxito', 'Finalizar');
                    }
                });
            }
        });
	},
	valorPlan: function(idPlan){
		$('#valor_plan').val(' ');
		$.getJSON('valorPlanes', {idPlan: idPlan}, function(json, textStatus) {
			$.each(json, function(index, val) {
				$('#valor_plan').val(ctz.number_format(val.planes_valor));
			});
		});
	},
	planes: function(planes){
		var cantidad  = $('#cotizaciones_cantidad_predios').val();
		if (planes === '') {
			$('#valor_plan, #cotizaciones_plan,#nombre_plan').val(' ');
		}else{
			if (cantidad === '') {
				Swal.fire('Error','Campo cantidad inmuebles vacio', 'error');
				$('#cotizaciones_tipo_plan').val('');
			} else {
				$('#valor_plan, #cotizaciones_plan, #nombre_plan').val(' ');
				$.getJSON('planes', {planes: planes,cantidad:cantidad}, function(json, textStatus) {
					console.log('json',json.length);
					if (json.length === 0) {
						$('#cotizaciones_plan').val(0);
						$('#valor_plan').val(ctz.number_format(0));
					} else {
						$.each(json, function(index, val) {
							console.log('val',val);
							$('#cotizaciones_plan').val(val.id);
							$('#nombre_plan').val(val.planes_nombre);
							$('#valor_plan').val(ctz.number_format(val.planes_valor));
						});
					}
				});
			}
		}
	},
	number_format:function(amount,decimals) {
	    amount += ''; // por si pasan un numero en vez de un string
	    amount = parseFloat(amount.replace(/[^0-9\.]/g, '')); // elimino cualquier cosa que no sea numero o punto

	    decimals = decimals || 0; // por si la variable no fue fue pasada

	    // si no es un numero o es igual a cero retorno el mismo cero
	    if (isNaN(amount) || amount === 0) 
	        return parseFloat(0).toFixed(decimals);

	    // si es mayor o menor que cero retorno el valor formateado como numero
	    amount = '' + amount.toFixed(decimals);

	    var amount_parts = amount.split('.'),
	        regexp = /(\d+)(\d{3})/;

	    while (regexp.test(amount_parts[0]))
	        amount_parts[0] = amount_parts[0].replace(regexp, '$1' + '.' + '$2');

	    return amount_parts.join('.');
  	},
	siguienteDiv: function(divHide,divShow,callback,nombreProyecto) {
		$(".loader").fadeIn("slow");
		$('#'+divHide+'').hide('slow/400/fast', function() {
			$('#cardHeaderPrincipal').html('');
			$('#'+divShow+'').show('slow/400/fast', function() {
				if (callback == 'input') {
					var header = `
						<div style="float: left;">
	                        <b>Crear Cotización</b>
	                    </div>
	                    <div style="float: right;">
	                        <button class="btn btn-block btn-primary" id="idBtnRegresarListado" type="button" onclick="ctz.terminar();">
	                        	<i class="fas fa-backward"></i>
	                        </button>
	                    </div>
					`;
					$('#cardHeaderPrincipal').html(header);
					$('#cotizaciones_nombre_proyecto').focus();
				} else if (callback == 'verCotizaciones') {
					var header = `
						<div style="float: left;">
	                        <b>`+nombreProyecto+`</b>
	                    </div>
	                    <div style="float: right;">
	                        <button class="btn btn-block btn-primary"  type="button" onclick="ctz.terminar();">
	                        	<i class="fas fa-backward"></i>
	                        </button>
	                    </div>
					`;
					$('#cardHeaderPrincipal').html(header);
					$('#'+divShow+'').load(''+divShow+'',{id: callback},function(){
						// $(".loader").fadeOut("slow");
					})
				}else {
					var header = `
						<div style="float: left;">
	                        <b>`+nombreProyecto+`</b>
	                    </div>
	                    <div style="float: right;">
	                        <button class="btn btn-block btn-primary"  type="button" onclick="ctz.terminar();">
	                        	<i class="fas fa-backward"></i>
	                        </button>
	                    </div>
					`;
					$('#cardHeaderPrincipal').html(header);
					
					$('#'+divShow+'').load(''+divShow+'',{id: callback},function(){
						// $(".loader").fadeOut("slow");
					})
				}
				$(".loader").fadeOut("slow");
			});
		});
	},
	terminar: function() {
		window.location.href = '';
	},
	envioEmail: function(idContizacion) {
        Swal.fire({
		  	title: '¿Pregunta?',
		  	text: "Desea enviar la cotización a otros e-mail adicionales.",
		  	type: 'info',
		  	showCancelButton: true,
		  	confirmButtonColor: '#3085d6',
		  	cancelButtonColor: '#d33',
		  	confirmButtonText: 'SI',
		  	cancelButtonText: 'NO',
		  	allowOutsideClick: false,
	        allowEscapeKey: false,
	        showCloseButton: false,
	        allowEnterKey:false
		}).then((result) => {
		  	if (result.value) {
			  	Swal.fire({
				  	title: 'Ingrese la cantidad de e-mail a los cuales desea enviar.',
				  	input: 'number',
				  	showCancelButton: true,
				  	confirmButtonText: 'Confirmar',
				  	showLoaderOnConfirm: true,
				  	allowOutsideClick: false,
		            allowEscapeKey: false,
		            showCloseButton: false,
		            allowEnterKey:false,
				  	preConfirm: (value) => {
					  	if (!value) {
					      	return Swal.showValidationMessage(`Campo e-mail vacio`)
					    }
				  	},
				}).then((result) => {
				  	if (result.value) {
					    ctz.envioEmailMasivo(result.value,idContizacion)
				  	}
				})
		  	}else{
		  		$('#btnEmailMostar_'+idContizacion).hide()
				$('#btnEmailMostarEnvio_'+idContizacion).show();
				$.post('envioEmail', {id:idContizacion,opc:0,emails:''}, function(data, textStatus, xhr) {
		            if (data === 'success') {
		            	toastr.success('Felicidades.', 'Email enviado correctamente.', { timeOut: 2000 }, toastr.options.onHidden = function() {});
		            }else{
		            	toastr.success('Error.', 'Email no enviado.', { timeOut: 3000 }, toastr.options.onHidden = function() {});
		            }
		            $('#btnEmailMostarEnvio_'+idContizacion).hide();
		            $('#btnEmailMostar_'+idContizacion).show()
		        });
		  	}
		});
	},

	envioEmailMasivo(cantidad,idContizacion){
		var progressSteps = [];
		var texto = [];
		if (cantidad == 1) {
			progressSteps = ['1'];
			texto = ['E-mail 1'];
		}else{
			var cont = 1;
			var email = 'E-mail'
			for (var i = 0 ; i < cantidad; i++) {
				progressSteps.push(cont);
				texto.push(email+' '+cont);
				cont = cont + 1
			}
		}
		Swal.mixin({
		  	input: 'email',
  			inputPlaceholder: 'Ingresa dirección e-mail',
		  	confirmButtonText: 'Siguiente &rarr;',
		  	showCancelButton: true,
		  	allowOutsideClick: false,
            allowEscapeKey: false,
            showCloseButton: false,
            allowEnterKey:false,
		  	progressSteps: progressSteps
		}).queue(texto).then((result) => {
		  if (result.value) {
		    var answers = JSON.stringify(result.value)
		    $('#btnEmailMostar_'+idContizacion).hide()
			$('#btnEmailMostarEnvio_'+idContizacion).show();
			$.post('envioEmail', {id:idContizacion,opc:cantidad,emails:answers}, function(data, textStatus, xhr) {
	            if (data === 'success') {
	            	toastr.success('Felicidades.', 'Email enviado correctamente.', { timeOut: 2000 }, toastr.options.onHidden = function() {});
	            }else{
	            	toastr.success('Error.', 'Email no enviado.', { timeOut: 3000 }, toastr.options.onHidden = function() {});
	            }
	            $('#btnEmailMostarEnvio_'+idContizacion).hide();
	            $('#btnEmailMostar_'+idContizacion).show()
	        });
		  }
		})
	},

	primeraCotizacion: function(divShow,callback) {
		$(".loader").fadeIn("slow");
		$('#cardHeaderPrincipal').html('');
		$('#contenedorVacioCotizacion').hide('slow/400/fast', function() {
			$('#nuevaCotizacion').show('slow/400/fast', function() {
				var header = `
					<div style="float: left;">
                        <b>Crear Cotización</b>
                    </div>
                    <div style="float: right;">
                        <button class="btn btn-block btn-primary" id="idBtnRegresarListado" type="button" onclick="ctz.terminar();">
                        	<i class="fas fa-backward"></i>
                        </button>
                    </div>
				`;
				$('#cardHeaderPrincipal').html(header);
				$('#cotizaciones_nombre_proyecto').focus();
				$(".loader").fadeOut("slow");
			});
		});
	},

	ejecutarOrdenTrabajo: function(idContizacion) {
		
		Swal.fire({
            title: "Confirmación?",   
            text: "Desea realizar una orden de trabajo a está cotización",   
            type: "info",   
            showCloseButton: true,
		  	showCancelButton: true,
		  	focusConfirm: false,
            cancelButtonText: "Cancelar",   
            confirmButtonColor: "#007bff",   
            confirmButtonText: "Si, realizar",   
            closeOnConfirm: false ,
            allowOutsideClick: false,
            allowEscapeKey: false,
            showCloseButton: false,
            allowEnterKey:false
        }).then((result) => {
            if (result.value) {
		   		$('#btnEjecutarMostar_'+idContizacion).hide()
				$('#btnEjecutarMostarEjecutar_'+idContizacion).show();
				$.post('ejecutarOrdenTrabajo', {id:idContizacion}, function(data, textStatus, xhr) {
					var resulServer  = JSON.parse(data);
		            if (resulServer.resul === 'success') {
		            	toastr.success('Felicidades.', 'Orden generada correctamente.', { timeOut: 3000 }, toastr.options.onHidden = function() {
		            		$('#idDivEditar_'+idContizacion+',#idDivEmail_'+idContizacion+',#idDivEjecutar_'+idContizacion+'').hide();
		            		$('#spanEstado_'+idContizacion).hide()
		            		$('#spanEstado_ejecutado_'+idContizacion).show();
		            		$('#idTrCotizacion_'+idContizacion).remove()
		            	});
		            }else{
		            	toastr.success('Error.', 'Orden no generada.', { timeOut: 3000 }, toastr.options.onHidden = function() {});
		            }
		        });
		  	}
        });
	},

	ejecutarOrdenServicio: function(idContizacion) {

		Swal.fire({
            title: "Confirmación?",   
            text: "Desea realizar una orden de servicio a está cotización",   
            type: "info",   
            showCloseButton: true,
		  	showCancelButton: true,
		  	focusConfirm: false,
            cancelButtonText: "Cancelar",   
            confirmButtonColor: "#007bff",   
            confirmButtonText: "Si, realizar",   
            closeOnConfirm: false ,
            allowOutsideClick: false,
            allowEscapeKey: false,
            showCloseButton: false,
            allowEnterKey:false
        }).then((result) => {
            if (result.value) {

            	Swal.fire({
				  	title: '¿Pregunta?',
				  	text: "Desea enviar la orden de servicio a otros e-mail adicionales.",
				  	type: 'info',
				  	showCancelButton: true,
				  	confirmButtonColor: '#3085d6',
				  	cancelButtonColor: '#d33',
				  	confirmButtonText: 'SI',
				  	cancelButtonText: 'NO',
				  	allowOutsideClick: false,
			        allowEscapeKey: false,
			        showCloseButton: false,
			        allowEnterKey:false
				}).then((result) => {
				  	if (result.value) {
					  	Swal.fire({
						  	title: 'Ingrese la cantidad de e-mail a los cuales desea enviar.',
						  	input: 'number',
						  	showCancelButton: true,
						  	confirmButtonText: 'Confirmar',
						  	showLoaderOnConfirm: true,
						  	allowOutsideClick: false,
				            allowEscapeKey: false,
				            showCloseButton: false,
				            allowEnterKey:false,
						  	preConfirm: (value) => {
							  	if (!value) {
							      	return Swal.showValidationMessage(`Campo e-mail vacio`)
							    }
						  	},
						}).then((result) => {
						  	if (result.value) {
							    ctz.envioEmailMasivoOrdenServicio(result.value,idContizacion)
						  	}
						})
				  	}else{
				  		$('#btnEjecutarMostar_'+idContizacion).hide()
						$('#btnEjecutarMostarEjecutar_'+idContizacion).show();
						$.post('ejecutarOrdenServicio', {id:idContizacion,opc:0,emails:''}, function(data, textStatus, xhr) {
							var resulServer  = JSON.parse(data);
				            if (resulServer.resul === 'success') {
				            	toastr.success('Felicidades.', 'Orden de servicio generada correctamente.', { timeOut: 3000 }, toastr.options.onHidden = function() {
				            		$('#idDivEditar_'+idContizacion+',#idDivEmail_'+idContizacion+',#idDivEjecutar_'+idContizacion+'').hide();
				            		$('#spanEstado_'+idContizacion).hide()
				            		$('#spanEstado_ejecutado_'+idContizacion).show();
				            		$('#idTrCotizacion_'+idContizacion).remove()
				            	});
				            }else{
				            	toastr.success('Error.', 'Orden de servicio no generada.', { timeOut: 3000 }, toastr.options.onHidden = function() {});
				            }
				        });
				  	}
				});
		  	}
        });
	},
	envioEmailMasivoOrdenServicio(cantidad,idContizacion){
		var progressSteps = [];
		var texto = [];
		if (cantidad == 1) {
			progressSteps = ['1'];
			texto = ['E-mail 1'];
		}else{
			var cont = 1;
			var email = 'E-mail'
			for (var i = 0 ; i < cantidad; i++) {
				progressSteps.push(cont);
				texto.push(email+' '+cont);
				cont = cont + 1
			}
		}
		Swal.mixin({
		  	input: 'email',
  			inputPlaceholder: 'Ingresa dirección e-mail',
		  	confirmButtonText: 'Siguiente &rarr;',
		  	showCancelButton: true,
		  	allowOutsideClick: false,
            allowEscapeKey: false,
            showCloseButton: false,
            allowEnterKey:false,
		  	progressSteps: progressSteps
		}).queue(texto).then((result) => {
		  if (result.value) {
		    var answers = JSON.stringify(result.value)
		    $('#btnEjecutarMostar_'+idContizacion).hide()
			$('#btnEjecutarMostarEjecutar_'+idContizacion).show();
			$.post('ejecutarOrdenServicio', {id:idContizacion,opc:cantidad,emails:answers}, function(data, textStatus, xhr) {
				var resulServer  = JSON.parse(data);
	            if (resulServer.resul === 'success') {
	            	toastr.success('Felicidades.', 'Orden de servicio generada correctamente.', { timeOut: 3000 }, toastr.options.onHidden = function() {
	            		$('#idDivEditar_'+idContizacion+',#idDivEmail_'+idContizacion+',#idDivEjecutar_'+idContizacion+'').hide();
	            		$('#spanEstado_'+idContizacion).hide()
	            		$('#spanEstado_ejecutado_'+idContizacion).show();
	            		$('#idTrCotizacion_'+idContizacion).remove()
	            	});
	            }else{
	            	toastr.success('Error.', 'Orden de servicio no generada.', { timeOut: 3000 }, toastr.options.onHidden = function() {});
	            }
	        });
		  }
		})
	},
	cambioEstado: function(idContizacion,nombreProyecto) {

		Swal.fire({
            title: "Confirmación?",   
            text: "Desea cambiar el estado a está cotización",   
            type: "info",   
            showCloseButton: true,
		  	showCancelButton: true,
		  	focusConfirm: false,
            cancelButtonText: "Cancelar",   
            confirmButtonColor: "#007bff",   
            confirmButtonText: "Si, cambiar",   
            closeOnConfirm: false ,
            allowOutsideClick: false,
            allowEscapeKey: false,
            showCloseButton: false,
            allowEnterKey:false
        }).then((result) => {
            if (result.value) {
		   		$('#spanEstado_'+idContizacion).hide()
				$('#spanEstado_mosatrar_'+idContizacion).show();
				$.post('cambioEstado', {id:idContizacion}, function(data, textStatus, xhr) {
		            if (data === 'success') {
		            	toastr.success('Felicidades.', 'Cambio de estado realizado correctamente.', { timeOut: 3000 }, toastr.options.onHidden = function() {
		            		window.location.href = '';
							// $('#spanEstado_mosatrar_'+idContizacion).hide();
		     //        		$('#spanEstado_cancelado_'+idContizacion).show()
		     //        		$('#idDivEditar_'+idContizacion+',#idDivEmail_'+idContizacion+',#idDivEjecutar_'+idContizacion+'').hide();
		     //        		$('#idTrCotizacion_'+idContizacion).remove()
		            	});
		            }else{
		            	toastr.success('Error.', 'Cambio de estado no realizado correctamente.', { timeOut: 3000 }, toastr.options.onHidden = function() {});
		            }
		        });
		  	}
        });
	},
};

ctz.start();