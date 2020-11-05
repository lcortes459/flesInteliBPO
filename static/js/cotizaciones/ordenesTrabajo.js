var ord = {

	start: function() {
		
		this.ready();
	},

	ready: function() {
		$('#idListadoOrdenesTable').DataTable({
			"order": [[ 0, "asc" ]]
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
	verOrden: function(divHide,divShow,idOrden) {
		$(".loader").fadeIn("slow");
		$('#'+divHide+'').hide('slow/400/fast', function() {
			$('#cardHeaderPrincipal').html('');
			$('#'+divShow+'').show('slow/400/fast', function() {
				
				var header = `
					<div style="float: left;">
                        <b>Detalle de la orden</b>
                    </div>
                    <div style="float: right;">
                    	<div class="row">
                    		<div class="nav-item col-sm-12 col-md-12">
                        		<button class="btn btn-block btn-secondary" id="idBtnRegresarProyectos"  type="button" onclick="ord.regresarOrdenes('verOrden','listadoOrdenes',`+idOrden+`);">
                        			<i class="fas fa-backward"></i>
                        		</button>
                        	</div>
                        </div>
                    </div>
				`;
				$('#cardHeaderPrincipal').html(header);
				$('#'+divShow+'').load('detalleOrden',{idOrden:idOrden},function(){
					$(".loader").fadeOut("slow");
				});
			});
		});
	},

	regresarOrdenes : function(divHide,divShow,idCliente,title){
		$(".loader").fadeIn("slow");
		$('#'+divHide+'').hide('slow/400/fast', function() {
			$('#cardHeaderPrincipal').html('');
			$('#'+divShow+'').show('slow/400/fast', function() {
				var header = `
					<div style="float: left;">
						<i class="fas fa-list"></i>
                        <b>Listado Ordenes Trabajo</b>
                    </div>
				`;
				$('#cardHeaderPrincipal').html(header);
				$(".loader").fadeOut("slow");
			});
		});
	},
	terminar: function() {
		window.location.href = '';
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

ord.start();