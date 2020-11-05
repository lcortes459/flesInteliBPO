var email = '';
var pass = '';
var login = {
    ready: function() {
        // Swal.fire('Algo pasa');
        var local = JSON.parse(localStorage.getItem("datosUsuario"));
        console.log(local);
        if (local) {
            console.log(local);
            if ((local.img === '0') || (local.img === 0)) {
                img = "/guardian/static/template/dist/img/user2-160x160.jpg";
            } else {
                img = "/guardian/" + local.img;
            }
            Swal.fire({
                allowOutsideClick: false,
                allowEscapeKey: false,
                allowEnterKey: false,
                title: 'Bienvenid@ nuevamente\n ' + local.nombres + '',
                text: 'Ya tenemos tus datos de acceso\n Continuar para acceder, o Validar para cambiar de usuario.',
                icon: 'success',
                showCancelButton: true,
                confirmButtonText: 'Continuar',
                cancelButtonText: 'Validar',
                closeOnConfirm: true,
                closeOnCancel: true
            }).then(function(result) {

                if (result.value) {
                    
                    email = local.usuario;
                    pass = local.pass;
                    // tpl.showPreloader('wrapper', '<b>Un momento por favor <br> Estamos alistado nuestra interfaz......</b>');
                    $.post('../ingresoUsuario', { email: email, contrasena: pass }, function(data, textStatus, xhr) {
                        if (data == 'usuario') {
                            Swal.fire({
                                allowOutsideClick: false,
                                allowEscapeKey: false,
                                allowEnterKey: false,
                                title: "Usuario Invalido",
                                text: "Verifique el usuario ingresado",
                                icon: "error",
                                callback: $('#emailIngreso').focus()
                            });
                            return false;
                        } else if (data == 'invalido') {
                            Swal.fire({
                                allowOutsideClick: false,
                                allowEscapeKey: false,
                                allowEnterKey: false,
                                title: "Información Invalido",
                                text: "Usuario/Password errados",
                                icon: "error",
                                callback: $('#emailIngreso').focus()
                            });
                            return false;
                        } else {
                            window.location.href = '';
                        }
                    });
                }else {
                    localStorage.clear();
                    $('#emailIngreso').focus();
                    email = '';
                    pass = '';
                }
            });
        } else {
            $('#btn_ingresar').click(function(event) {
                var email = $('#emailIngreso').val();
                var pass = $('#passwordIngreso').val();
                if (email == '') {
                    Swal.fire({
                        allowOutsideClick: false,
                        allowEscapeKey: false,
                        allowEnterKey: false,
                        title: "Campo Vacio",
                        text: "Debe ingresar un email",
                        icon: "error",
                        callback: $('#emailIngreso').focus()
                    });
                    return false;
                } else if (pass == '') {
                    Swal.fire({
                        allowOutsideClick: false,
                        allowEscapeKey: false,
                        allowEnterKey: false,
                        title: "Campo Vacio",
                        text: "Debe ingresar un password",
                        icon: "error",
                        callback: $('#passwordIngreso').focus()
                    });
                    return false;
                } else {
                    // tpl.showPreloader('wrapper', '<b>Estamos validando sus datos <br>Un momento por favor...</b>');
                    $('#btn_ingresar').hide();
                    $('#btn_validando').show();
                    $.post('../ingresoUsuario', { emailIngreso: email, passIngreso: pass }, function(data, textStatus, xhr) {
                        // tpl.hidePreloader('wrapper');
                        // console.log('data', JSON.parse(data));
                        var dat = JSON.parse(data);
                        console.log('dataValores', dat);
                        if (dat.multi_valores == 'usuario') {
                            Swal.fire({
                                allowOutsideClick: false,
                                allowEscapeKey: false,
                                allowEnterKey: false,
                                title: "Usuario Invalido",
                                text: "Verifique el usuario ingresado",
                                icon: "error",
                                callback: $('#emailIngreso').focus()
                            });
                            $('#btn_validando').hide();
                            $('#btn_ingresar').show();
                            return false;
                        } else if (dat.multi_valores == 'invalido') {
                            Swal.fire({
                                allowOutsideClick: false,
                                allowEscapeKey: false,
                                allowEnterKey: false,
                                title: "Información Invalida",
                                text: "Usuario/Password errados",
                                icon: "error",
                                callback: $('#emailIngreso').focus()
                            });
                            $('#btn_validando').hide();
                            $('#btn_ingresar').show();
                            return false;
                        } else if (dat.multi_valores == 'estado') {
                            Swal.fire({
                                allowOutsideClick: false,
                                allowEscapeKey: false,
                                allowEnterKey: false,
                                title: "Usuario Bloquedo",
                                text: "Comuniquese con su asesor",
                                icon: "error",
                                callback: $('#passwordIngreso').focus()
                            });
                            $('#btn_validando').hide();
                            $('#btn_ingresar').show();
                            return false;
                        } else {
                            Swal.fire({
                                allowOutsideClick: false,
                                allowEscapeKey: false,
                                allowEnterKey: false,
                                title: 'Bienvenid@ .....!',
                                text: 'FilesInteliBpo te da la bienvenida.\n Continuar para acceder',
                                icon: 'success',
                                showCancelButton: false,
                                confirmButtonText: 'Continuar',
                                closeOnConfirm: true,
                            }).then(function(result) {

                                if (result.value) {
                                   if (typeof(Storage) !== "undefined") {
                                        console.log('Si');
                                        if ($('#inputCheckbox').is(':checked')) {
                                            mi_objeto = {
                                                usuario: emailIngreso,
                                                nombres: dat.multi_valores,
                                                img: dat.img
                                            }
                                            localStorage.setItem("datosUsuario", JSON.stringify(mi_objeto));
                                            var local = JSON.parse(localStorage.getItem("datosUsuario"));
                                            window.location.href = '';
                                        } else {
                                            localStorage.clear();
                                            window.location.href = '';
                                        }
                                    } else {
                                        Swal.fire({
                                            allowOutsideClick: false,
                                            allowEscapeKey: false,
                                            allowEnterKey: false,
                                            title: "Advertencia...!",
                                            text: "El navegador que está utilizando no soporta el recordar datos",
                                            icon: "error",
                                            callback: window.location.href = ''
                                        });
                                    } 
                                }
                            });
                        }
                    });
                    return false;
                }
            });
            return false;
        }
    },
    checked: function(stra_val) {
        console.log(stra_val);
        if ((stra_val == 0) || (stra_val == '0')) {
            stra_val = 1;
        } else {
            stra_val = 0;
        }
        $('#inputCheckbox').val(stra_val);
        console.log(stra_val);
    },
};
login.ready();