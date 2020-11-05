var ctz = {

	start: function() {
		
		this.ready();
	},

	ready: function() {
		$('#idListadoClientesTable').DataTable({
			"order": [[ 0, "asc" ]]
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
            } else if ($('#cotizaciones_cantidad_interiores').val() === '') {
                template.validaCampo('Cantidad Interiores');
            } else if ($('#cotizaciones_cantidad_predios').val() === '') {
                template.validaCampo('Cantidad Predios');
            } else if ($('#cotizaciones_plan').val() === '') {
                template.validaCampo('Plan cotización');
            } else {
                var dat = $('#formularioCtz').serialize();
                $('#cotizaciones_telefono_administrador,#cotizaciones_observacion,#cotizaciones_nombre_proyecto,#cotizaciones_nit_proyecto,#cotizaciones_ciudad,#cotizaciones_direccion_proyecto,#cotizaciones_nombre_administrador,#cotizaciones_celular_administrador,#cotizaciones_email_administrador,#cotizaciones_cantidad_interiores,#cotizaciones_cantidad_predios,#cotizaciones_plan').attr('disabled', true);
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
		if (planes === '') {
			document.getElementById('cotizaciones_plan').innerHTML = " ";
			document.getElementById('cotizaciones_plan').disabled = true;
		}else{
			document.getElementById('cotizaciones_plan').innerHTML = " ";
			document.getElementById('cotizaciones_plan').disabled = true;
			var data = new Array();
			data.push('<option value="">Seleccione un plan</option>');
			$.getJSON('planes', {planes: planes}, function(json, textStatus) {
				$.each(json, function(index, val) {
					data.push('<option value="'+val.id+'">'+val.planes_nombre+'</option>');
				});
				document.getElementById('cotizaciones_plan').disabled = false;	
				$('#cotizaciones_plan').html(data);
			});
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
	verProyectos: function(divHide,divShow,title,idCliente) {
		$(".loader").fadeIn("slow");
		$('#'+divHide+'').hide('slow/400/fast', function() {
			$('#cardHeaderPrincipal').html('');
			$('#'+divShow+'').show('slow/400/fast', function() {
				var header = `
					<div style="float: left;">
                        <b>`+title+`</b>
                    </div>
                    <div style="float: right;">
                    	<div class="row">
                    		<div class="nav-item col-sm-6 col-md-6">
                        		<button class="btn btn-block btn-secondary" id="idBtnRegresarListado" type="button" onclick="ctz.terminar();">
                        			<i class="fas fa-backward"></i>
                        		</button>
                        	</div>
                        	<div class="nav-item col-sm-6 col-md-6">
                        		<button class="btn btn-block btn-primary" id="idBtnRegresarListado" type="button" onclick="ctz.nuevoProyecto('listadoProyectos','nuevoProyecto',`+idCliente+`,'`+title+`');">
                        			<i class="fas fa-plus"></i>
                        		</button>
                        	</div>
                        </div>
                    </div>
				`;
				$('#cardHeaderPrincipal').html(header);
				$('#'+divShow+'').load('verProyectos',{idCliente:idCliente},function(){
					$(".loader").fadeOut("slow");
				});
			});
		});
	},
	
	terminar: function() {
		window.location.href = '';
	},
	envioEmail: function(idContizacion) {
		$('#btnEmailMostar_'+idContizacion).hide()
		$('#btnEmailMostarEnvio_'+idContizacion).show();
		$.post('envioEmail', {id:idContizacion}, function(data, textStatus, xhr) {
            if (data === 'success') {
            	toastr.success('Felicidades.', 'Email enviado correctamente.', { timeOut: 2000 }, toastr.options.onHidden = function() {});
            }else{
            	toastr.success('Error.', 'Email no enviado.', { timeOut: 3000 }, toastr.options.onHidden = function() {});
            }
            $('#btnEmailMostarEnvio_'+idContizacion).hide();
            $('#btnEmailMostar_'+idContizacion).show()
        });
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
                        <button class="btn btn-block btn-primary" id="idBtnRegresarListado" type="button" onclick="ctz.terminar();">Regresar Listado De Cotizaciones</button>
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
					console.log('data', JSON.parse(data));
					var resulServer  = JSON.parse(data);
		            if (resulServer.resul === 'success') {
		            	toastr.success('Felicidades.', 'Orden generada correctamente.', { timeOut: 3000 }, toastr.options.onHidden = function() {
							// $('#btnEjecutarMostarEjecutar_'+idContizacion).hide();
		     //        		$('#btnEjecutarFinalEjecutar_'+idContizacion).show();
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
	cambioEstado: function(idCliente,nombreCliente,opc) {
		if ( (opc === 0) || (opc === '0') ) {

			var html = `
				<p>Recuerde que al <b>desactivar</b> a <b>`+nombreCliente+`</b> todos los usuarios de este quedaran inhabilitados para ingresar a GuardianWeb.</p>
			`;
		}else{

			var html = `
				<p>Recuerde que al <b>activar</b> a <b>`+nombreCliente+`</b> todos los usuarios de este quedaran habilitados para ingresar a GuardianWeb.</p>
			`;
		}
		Swal.fire({
            title: "Confirmación?",
            type: "info",   
            html: html,
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
		   		$('#spanEstado_'+idCliente).hide()
				$('#spanEstado_mosatrar_'+idCliente).show();
				$.post('cambioEstadoCliente', {id:idCliente,opc:opc}, function(data, textStatus, xhr) {

		            if ( (data === 'success') && ( (opc === 0) || (opc === '0') ) ) {
		            	
		            	toastr.success('Felicidades.', ''+nombreCliente+' bloqueado con éxito.', { timeOut: 3000 }, toastr.options.onHidden = function() {
		            		$('#idTdCliente_'+idCliente).html(' ');
		            		$('#idTdCliente_'+idCliente).html(`
								<span 
									class="badge badge-danger" 
									id="spanEstado_`+idCliente+`" 
									style="cursor:pointer;" 
									onclick="ctz.cambioEstado(`+idCliente+`, '`+nombreCliente+`',1);">
									Bloqueado
								</span>
								<span class="badge badge-seco ndary" style="display: none;cursor:none;" id="spanEstado_mosatrar_`+idCliente+`">
			        				<i class="fas fa-spinner fa-spin" style="color: white;"></i>
			        			</span>
		            		`);
		            	});
		            } else if ( (data === 'success') && ( (opc === 1) || (opc === '1') ) ) {
		            	
		            	toastr.success('Felicidades.', ''+nombreCliente+' activado con éxito.', { timeOut: 3000 }, toastr.options.onHidden = function() {
		            		$('#idTdCliente_'+idCliente).html(' ');
		            		$('#idTdCliente_'+idCliente).html(`
								<span 
									class="badge badge-success" 
									id="spanEstado_`+idCliente+`" 
									style="cursor:pointer;" 
									onclick="ctz.cambioEstado(`+idCliente+`,' `+nombreCliente+`',0);">
									Activo
								</span>
								<span class="badge badge-secondary" style="display: none;cursor:none;" id="spanEstado_mosatrar_`+idCliente+`">
			        				<i class="fas fa-spinner fa-spin" style="color: white;"></i>
			        			</span>
		            		`);
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