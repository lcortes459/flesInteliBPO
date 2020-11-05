var piso = 0;
var tmpPiso = 0;
var ctz = {

	start: function() {
		
		this.ready();
	},

	ready: function() {
		$('#idListadoProyectosTable').DataTable({
			"order": [[ 6, "asc" ]]
		});

		$('#idListadoPrediosTable').DataTable({
			"order": [[ 0, "asc" ]]
		});
	},
	guardarProyecto: function() {

		if ($('#proyectos_nombre_proyecto').val() === '') {
            template.validaCampo('Nombre Proyecto');
        } else if ($('#proyectos_nit_proyecto').val() === '') {
            template.validaCampo('Nit Proyecto');
        } else if ($('#proyectos_ciudad').val() === '') {
            template.validaCampo('Ciudad');
        } else if ($('#proyectos_direccion_proyecto').val() === '') {
            template.validaCampo('Dirección');
        } else if ($('#proyectos_nombre_administrador').val() === '') {
            template.validaCampo('Nombre Administrador');
        } else if ($('#proyectos_celular_administrador').val() === '') {
            template.validaCampo('Celular Administrador');
        } else if ($('#proyectos_email_administrador').val() === '') {
            template.validaCampo('Email Administrador');
        } else if ($('#proyectos_cantidad_interiores').val() === '') {
            template.validaCampo('Cantidad Interiores');
        } else if ($('#proyectos_cantidad_predios').val() === '') {
            template.validaCampo('Cantidad Predios');
        } else {
            var dat = $('#formularioProyecto').serialize();
            $(`#proyectos_telefono_administrador,
            	#proyectos_tipo_letra,
            	#proyectos_nombre_proyecto,
            	#proyectos_nit_proyecto,
            	#proyectos_ciudad,
            	#proyectos_direccion_proyecto,
            	#proyectos_nombre_administrador,
            	#proyectos_celular_administrador,
            	#proyectos_email_administrador,
            	#proyectos_cantidad_interiores,
            	#proyectos_cantidad_predios,
            	#proyectos_color_corporativo`).attr('disabled', true);
            $('#idBtnRegresarProyectos').hide();
            $('#botoneraGurdarProyecto').hide();
            $('#botoneraGurdando').show();
            $.ajax({
                url: 'guardarProyecto',
                type: 'POST',
                data: dat,
            })
            .done(function(data) {
                console.log(data);
                if ((data == 0) || (data === '0')) {
                    template.resulError('No se pudo crear el proyecto '+$('#proyectos_nombre_proyecto').val()+'. Verifique e intente nuevamente.');
                } else {
                    template.resulSucces('Proyecto: '+$('#proyectos_nombre_proyecto').val()+' creado con éxito', 'Finalizar');
                }
            });
        }
	},
	nuevoProyecto : function(divHide,divShow,idCliente,title){
		console.log('divHide',divHide);
		console.log('divShow',divShow);
		$(".loader").fadeIn("slow");
		$('#'+divHide+'').hide('slow/400/fast', function() {
			$('#cardHeaderPrincipal').html('');
			$('#'+divShow+'').show('slow/400/fast', function() {
				var header = `
					<div style="float: left;">
                        <b>Nuevo proyecto</b>
                    </div>
                    <div style="float: right;">
                    	<div class="row">
                    		<div class="nav-item col-sm-12 col-md-12">
                        		<button class="btn btn-block btn-secondary" id="idBtnRegresarProyectos"  type="button" onclick="ctz.regresarProyectos('nuevoProyecto','listadoProyectos',`+idCliente+`,'`+title+`');">
                        			<i class="fas fa-backward"></i>
                        		</button>
                        	</div>
                        </div>
                    </div>
				`;
				$('#cardHeaderPrincipal').html(header);
				$('#'+divShow+'').load('nuevoProyecto',{idCliente:idCliente},function(){
					$(".loader").fadeOut("slow");
					template.limpiar('formularioProyecto','proyectos_nombre_proyecto');
				});
			});
		});
	},

	regresarProyectos : function(divHide,divShow,idCliente,title){
		//$(".loader").fadeIn("slow");
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
				//$(".loader").fadeOut("slow");
			});
		});
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
                        <button class="btn btn-block btn-primary" id="idBtnRegresarListado" type="button" onclick="ctz.terminar();">Regresar Listado De Clientes</button>
                    </div>
				`;
				$('#cardHeaderPrincipal').html(header);
				$('#'+divShow+'').load('verProyectos',{idCliente:idCliente},function(){
					$(".loader").fadeOut("slow");
				})
			});
		});
	},

	// Predios

	verPredios: function(divHide,divShow,idArea,title) {
		$(".loader").fadeIn("slow");
		$('#'+divHide+'').hide('slow/400/fast', function() {
			$('#titlePredios,#btnNuevoPredioDiv').html('');
			$('#'+divShow+'').show('slow/400/fast', function() {
				$('#titlePredios').html(title);
				$('#btnNuevoPredioDiv').html(`
					<button class="btn btn-block btn-primary" id="idBtnRegresarListado" type="button" onclick="ctz.nuevoPredio('predios','nuevoPredio',`+idArea+`);">
                        <i class="fas fa-plus"></i>
                    </button>
				`);
				$('#verPredios').load('verPredios',{idArea:idArea},function(){
					$(".loader").fadeOut("slow");
				})
			});
		});
	},

	nuevoPredio : function(divHide,divShow,idArea){
		$(".loader").fadeIn("slow");
		$('#'+divHide+'').hide('slow/400/fast', function() {
			$('#'+divShow+'').show('slow/400/fast', function() {
				$('#nuevoPredios').load('nuevoPredio',{idArea:idArea},function(){
					$(".loader").fadeOut("slow");
					template.limpiar('formularioPredio','interioresPredios_piso');
				});
			});
		});
	},

	regresarGeneral: function(divHide,divShow){
		//$(".loader").fadeIn("slow");
		$('#'+divHide+'').hide('slow/400/fast', function() {
			$('#'+divShow+'').show('slow/400/fast', function() {
				//$(".loader").fadeOut("slow");
			});
		});
	},
	identificadorPredio: function(opt){
		if (opt === 'Apartamento') {
			$('#divPiso').show();
			$('.predio').removeClass('form-group col-sm-12 col-md-6 col-lg-6');
			$('.predio').addClass('form-group col-sm-12 col-md-4 col-lg-4');
			$('#piso').focus();
			piso = 1;
		}else{
			piso = 0;
			if (opt!='') {
				$('#divPiso').hide();
				$('.predio').removeClass('form-group col-sm-12 col-md-4 col-lg-4');
				$('.predio').addClass('form-group col-sm-12 col-md-6 col-lg-6');
				$('#interioresPredios_predio').focus();
				$('#interioresPredios_piso').val(1);
			}else{
				$('#divPiso').hide();
				$('.predio').removeClass('form-group col-sm-12 col-md-4 col-lg-4');
				$('.predio').addClass('form-group col-sm-12 col-md-6 col-lg-6');
			}
		}
	},

	pisoPredio: function(opt){
		if (opt!='') {
			$('#interioresPredios_piso').val('');
			$('#interioresPredios_piso').val(opt);
			tmpPiso = opt;
		}else{
			tmpPiso = 0
		}	
	},
	guardarPredio: function() {

		if ($('#interioresPredios_identificador').val() === '') {
            template.validaCampo('Identificador');
        } else if ( (piso == 1) && ( tmpPiso == 0 )) {
            template.validaCampo('Número piso');
        } else if ($('#interioresPredios_predio').val() === '') {
            template.validaCampo('Nombre predio');
        } else {
            var dat = $('#formularioPredio').serialize();
            $(`#interioresPredios_piso,
            	#interioresPredios_predio,#piso`).attr('disabled', true);
            $('#idBtnRegresarComponentes').hide();
            $('#botoneraGurdarPredio').hide();
            $('#botoneraGurdando').show();
            $.ajax({
                url: 'guardarPredio',
                type: 'POST',
                data: dat,
            })
            .done(function(data) {
                console.log(data);
                if (data == 'erro'){
                    template.resulError('No se pudo crear el predio '+$('#interioresPredios_predio').val()+'. Verifique e intente nuevamente.');
                } else {
                    template.resulSucces('Predio: '+$('#interioresPredios_predio').val()+' creado con éxito', 'Finalizar');
                }
            });
        }
	},
	// Fin predios

	terminar: function() {
		window.location.href = '';
	},
	cambioEstadoProyecto: function(idCliente,nombreCliente,opc) {
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
		   		$('#spanEstado_proyecto_'+idCliente).hide()
				$('#spanEstado_mosatrar_proyecto_'+idCliente).show();
				$.post('cambioEstadoProyecto', {id:idCliente,opc:opc}, function(data, textStatus, xhr) {

		            if ( (data === 'success') && ( (opc === 0) || (opc === '0') ) ) {
		            	
		            	toastr.success('Felicidades.', ''+nombreCliente+' bloqueado con éxito.', { timeOut: 3000 }, toastr.options.onHidden = function() {
		            		$('#idTdProyecto_'+idCliente).html(' ');
		            		$('#idTdProyecto_'+idCliente).html(`
								<span 
									class="badge badge-danger" 
									id="spanEstado_proyecto_`+idCliente+`" 
									style="cursor:pointer;" 
									onclick="ctz.cambioEstado(`+idCliente+`, '`+nombreCliente+`',1);">
									Bloqueado
								</span>
								<span class="badge badge-seco ndary" style="display: none;cursor:none;" id="spanEstado_mosatrar_proyecto_`+idCliente+`">
			        				<i class="fas fa-spinner fa-spin" style="color: white;"></i>
			        			</span>
		            		`);
		            	});
		            } else if ( (data === 'success') && ( (opc === 1) || (opc === '1') ) ) {
		            	
		            	toastr.success('Felicidades.', ''+nombreCliente+' activado con éxito.', { timeOut: 3000 }, toastr.options.onHidden = function() {
		            		$('#idTdProyecto_'+idCliente).html(' ');
		            		$('#idTdProyecto_'+idCliente).html(`
								<span 
									class="badge badge-success" 
									id="spanEstado_proyecto_`+idCliente+`" 
									style="cursor:pointer;" 
									onclick="ctz.cambioEstado(`+idCliente+`,' `+nombreCliente+`',0);">
									Activo
								</span>
								<span class="badge badge-secondary" style="display: none;cursor:none;" id="spanEstado_mosatrar_proyecto_`+idCliente+`">
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
	detalleProyecto: function(divHide,divShow,idProyecto,nombreProyecto,nombreCliente,idCliente) {
		$(".loader").fadeIn("slow");
		$('#'+divHide+'').hide('slow/400/fast', function() {
			$('#cardHeaderPrincipal').html('');
			$('#'+divShow+'').show('slow/400/fast', function() {
				var header = `
					<div style="float: left;">
                        <b>`+nombreProyecto+`</b>
                    </div>
                    <div style="float: right;">
                        <button class="btn btn-block btn-secondary" id="idBtnRegresarListadoProyectos" type="button" onclick="ctz.regresarProyecto('`+divShow+`','`+divHide+`','Listado Proyectos(`+nombreProyecto+`)','`+nombreCliente+`','`+idCliente+`');">
                			<i class="fas fa-backward"></i>
                		</button>
                    </div>
				`;
				$('#cardHeaderPrincipal').html(header);
				$('#'+divShow+'').load('detalleProyecto',{idProyecto:idProyecto},function(){
					$(".loader").fadeOut("slow");
				})
			});
		});
	},
	regresarProyecto: function(divHide,divShow,title,nombreCliente,idCliente){
		//$(".loader").fadeIn("slow");
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
                        		<button class="btn btn-block btn-primary" id="idBtnRegresarListado" type="button" onclick="ctz.nuevoProyecto('listadoProyectos','nuevoProyecto',`+idCliente+`,'Listado Proyectos(`+nombreCliente+`)');">
                        			<i class="fas fa-plus"></i>
                        		</button>
                        	</div>
                        </div>
                    </div>
				`;
				$('#cardHeaderPrincipal').html(header);
				//$(".loader").fadeOut("slow");
			});
		});
	}

};

ctz.start();