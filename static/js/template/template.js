var template = {
    stars: function() {
        this.carga()
        //Swal.fire('Annnnnnn','ssssss','info');
    },
    carga() {
        
        $(function () {
            $("#example1").DataTable();
            $('#example2').DataTable({
              "paging": true,
              "lengthChange": false,
              "searching": false,
              "ordering": true,
              "info": true,
              "autoWidth": false,
            });
        });
    },
    limpiar:function(form,input) {
       $('#'+form+'')[0].reset();
       $('#'+input+'').focus();
    },
    dataTable(selector){
	    $('#selector').DataTable({
	      "paging": true,
	      "lengthChange": false,
	      "searching": false,
	      "ordering": true,
	      "info": true,
	      "autoWidth": false,
	    });
    },
    guardarData(form,table,div){
    	console.log($('#'+form+'').serialize());
    	$('#'+form+'').attr('disabled', true);
    	return false;
    },

    validaCampo(selector){
    	Swal.fire('Warning','Campo '+selector+' vacío','warning');
    },

    resulError(mensaje){
        Swal.fire('Error',''+mensaje+'','error');
    },
    resulSucces(mensaje,smsBotonOk){
        Swal.fire({
            title:'Felicidades',
            text:mensaje,
            type:'success',
            showCancelButton: false,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: smsBotonOk,
            allowOutsideClick: false,
            allowEscapeKey:false,
            allowEnterKey:false,
        }).then((result) => {
            if (result.value) {
                window.location.href=" ";
            }
        });
    },
    modales:function(header,destino,tamano) {
        /*
            
            modal-xl
            modal-lg
            modal-sm
            <h4 class="modal-title" id="idTitleModalLg"></h4>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">×</span>
          </button>
        */ 
        $('#idHeaderModal,#idModalBody,#idModalFooter').html('');
        $('#clasTamanoModal').removeClass('modal-xl');
        $('#clasTamanoModal').removeClass('modal-lg');
        $('#clasTamanoModal').removeClass('modal-sm');

        $('#idModalTemplate').modal({
            keyboard:false,
            backdrop: false
        });
        $('#clasTamanoModal').addClass(tamano);
        $('#idHeaderModal').html(`
            <h4 class="modal-title" id="idTitleModalLg">`+header+`</h4>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">×</span>
          </button>
            `
        );
        if (destino) {
            template.destino("lpModalBody",destino,false);
        }
        //$('#idModalBody').addClass('<i class="fa fa-spinner fa-spin"></i>');
        //$('#idModalFooter').addClass(footer);        
    },
    destino:function(body,destino,funcion) {
        console.log(body);
        console.log(destino);
        console.log(funcion);
       $('#'+body+'').load('modulos',{empresa:1},funcion);
    },
    updateEstado: function(est,usu){
        Swal.fire({
            title: "El estado se modificara!",   
            text: "Esta seguro de continuar el proceso?",   
            type: "info",   
            showCancelButton: true,   
            cancelButtonText: "Cancelar",   
            confirmButtonColor: "#007bff",   
            confirmButtonText: "Si, continuar",   
            closeOnConfirm: false ,
            allowOutsideClick: false,
            allowEscapeKey: false,
            allowEnterKey:false
        }).then((result) => {
            if (result.value) {
                $.post('updateEstado', {est: est, usu: usu}, function(data, textStatus, xhr) {
                    $("#div_usu_"+usu).html(data);
                    Swal.fire("Felicidades!", "Estado modificado Exitosamente!", "success");
                });
            }
        });
    },
    updateEstadoEmplado: function(est,empl){
        Swal.fire({
            title: "El estado se modificara!",   
            text: "Esta seguro de continuar el proceso?",   
            type: "info",   
            showCancelButton: true,   
            cancelButtonText: "Cancelar",   
            confirmButtonColor: "#007bff",   
            confirmButtonText: "Si, continuar",   
            closeOnConfirm: false ,
            allowOutsideClick: false,
            allowEscapeKey: false,
            allowEnterKey:false
        }).then((result) => {
            if (result.value) {
                $.post('updateEstadoEmplado', {est: est, empl: empl}, function(data, textStatus, xhr) {
                    $("#div_empl_"+empl).html(data);
                    Swal.fire("Felicidades!", "Estado modificado Exitosamente!", "success");
                });
            }
        });
    },
    asigEmpleado: function(usu){
        $('#asignarEmpleado_'+usu).load('empleados',{usu: usu});    
    },
    asignarEmpleado: function(usu,empl) {
        
        if ( (empl == 0) || (empl == '0')) {
            var texto = 'Este usuario quedara sin un empleado asignado';
            var textoFinal = 'Operación finalizada con éxito';
        } else {
            var texto = "El usuario se le asignara un empleado!";
            var textoFinal = "El empleado se ha asignado Exitosamente.";
        }
        Swal.fire({
            title: texto,   
            text: "Esta seguro de continuar el proceso?",   
            type: "info",   
            showCancelButton: true,   
            cancelButtonText: "Cancelar",   
            confirmButtonColor: "#007bff",   
            confirmButtonText: "Si, continuar",
            allowOutsideClick: false,
            allowEscapeKey: false,
            allowEnterKey:false 
        }).then((result) => {
            if (result.value) {
                
                if(empl==''){
                    Swal.fire("Error!", "Debe seleccionar un empleado!", "error");
                }else{
                    $.post('asignarEmpleado', {empl: empl, usu: usu}, function(data, textStatus, xhr) {
                        if ( (data == '0') || (data == 0)) {
                            Swal.fire("Wirning", "El usuario ya tiene un empleado asignado.", "warning");
                        } else if ( data == 'error' ) {
                            Swal.fire("Error", "No pudimos procesar su solicitud, Intente nuevemente.", "error");
                        }else {
                            $("#asignarEmpleado_"+usu).html(data);
                            Swal.fire("Felicidades", textoFinal, "success");
                        }
                    });
                }
            }
        }); 
    },
    cerrarAsigEmpl: function(usu){
        
        $.post('cerrarAsigEmpl', {usu: usu}, function(data, textStatus, xhr) {
            $("#asignarEmpleado_"+usu).html(data);
        });    
    },
    updateTipo: function(usu,tipo) {
        Swal.fire({
            title: "El Tipo de usuario  se modificara!",   
            text: "Esta seguro de continuar el proceso?",   
            type: "warning",   
            showCancelButton: true,   
            cancelButtonText: "Cancelar",   
            confirmButtonColor: "#007bff",   
            confirmButtonText: "Si, continuar!",
            allowOutsideClick: false,
            allowEscapeKey: false,
            allowEnterKey:false 
        }, 
        function(){
            if(tipo==''){
                Swal.fire("Error!", "Debe seleccionar un tipo de usuario!", "error");
            }else{
                $.post('updateTipo', {tipo: tipo, usu: usu}, function(data, textStatus, xhr) {
                    $("#tipo_"+usu).html(data);
                    Swal.fire("Felicidades!", "El tipo de usuario se ha modificado Exitosamente!", "success");
                });
            }
            
        });
    },
};
template.stars();