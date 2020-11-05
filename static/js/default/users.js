var emailIngreso = '';
var img;
var ing = {
    stars: function() {
        this.carga();
    },
    carga() {
        var local = JSON.parse(localStorage.getItem("datosUsuario"));
        if (local) {
            $('#body').removeClass('class name');
            $('#body').addClass('hold-transition lockscreen');
            $('#divLogin').hide();
            $('#divLockScreen').show();

            if ((local.img === '0') || (local.img === 0)) {
                img = "/guardian/static/template/dist/img/user2-160x160.jpg";
            } else {
                img = "/guardian/" + local.img;
            }
            $('#divImg,#divNombreUsuario').html('');
            $('#divNombreUsuario').html(local.nombres);
            $('#divImg').html("<img src=" + img + " alt='User Image'>");
        } else {
            $('#btnIngreso').click(function(event) {

                var emailIngreso = $('#emailIngreso').val();
                var passIngreso = $('#passIngreso').val();
                if (emailIngreso == '') {
                    toastr.error('Campo email vacío', 'Debe ingresar un email', { timeOut: 3000 }, toastr.options.onHidden = function() { $('#emailIngreso').focus(); });
                    return false;
                } else if (passIngreso == '') {
                    toastr.error('Campo password vacío', 'Debe ingresar un password', { timeOut: 3000 }, toastr.options.onHidden = function() { $('#passIngreso').focus(); });
                    return false;
                } else {
                    $('#emailIngreso,#passIngreso,#btnIngreso,#olvidePss').attr("disabled", true);
                    $('#btns_ingreso,#olvidePss').hide();
                    $('#validando').show();
                    $.post('../ingresoUsuario', { email: email, contrasena: passIngreso }, function(data, textStatus, xhr) {

                        var dat = JSON.parse(data);
                        if (dat.multi_valores == 'usuario') {
                            toastr.error('Error', 'Email no encontrtado', { timeOut: 2000 }, toastr.options.onHidden = function() {
                                $('#emailIngreso,#passIngreso,#btnIngreso,#olvidePss').attr("disabled", false);
                                $('#validando').hide();
                                $('#btns_ingreso,#olvidePss').show();
                                $('#emailIngreso').focus();
                            });
                        } else if (dat.multi_valores == 'invalido') {
                            toastr.error('Error', 'Password Invalido', { timeOut: 2000 }, toastr.options.onHidden = function() {
                                $('#emailIngreso,#passIngreso,#btnIngreso,#olvidePss').attr("disabled", false);
                                $('#validando').hide();
                                $('#btns_ingreso,#olvidePss').show();
                                $('#passIngreso').focus();
                            });
                        } else if (dat.multi_valores == 'estado') {
                            toastr.error('Usuario Bloquedo. Comuniquese con su asesor.', 'Error', { timeOut: 10000 }, toastr.options.onHidden = function() {
                                $('#emailIngreso,#passIngreso,#btnIngreso,#olvidePss').attr("disabled", false);
                                $('#validando').hide();
                                $('#btns_ingreso,#olvidePss').show();
                                $('#passIngreso').focus();
                            });
                        } else {

                            if (typeof(Storage) !== "undefined") {
                                if ($('#inputCheckbox').is(':checked')) {
                                    mi_objeto = {
                                        usuario: emailIngreso,
                                        nombres: dat.multi_valores,
                                        img: dat.img
                                    }
                                    localStorage.setItem("datosUsuario", JSON.stringify(mi_objeto));
                                    var local = JSON.parse(localStorage.getItem("datosUsuario"));
                                    toastr.success('Datos correctos.', 'En un momento sera redireccionado a GuardianWeb', { timeOut: 3000 }, toastr.options.onHidden = function() { window.location.href = '../../default/index'; });
                                } else {
                                    localStorage.clear();
                                    toastr.success('Datos correctos.', 'En un momento sera redireccionado a GuardianWeb', { timeOut: 3000 }, toastr.options.onHidden = function() { window.location.href = '../../default/index'; });
                                }
                            } else {
                                toastr.info('Advertencia.', 'El navegador que está utilizando no soporta el recordar datos', { timeOut: 3000 }, toastr.options.onHidden = function() { window.location.href = '../../default/index'; });

                            }
                        }
                    });
                }
            });
        }
    },
    limpiarSession: function() {
        localStorage.clear();
        location.reload();
    },

    ingresoSession: function() {
        var local = JSON.parse(localStorage.getItem("datosUsuario"));
        emailIngreso = local.usuario;
        var passIngreso = $('#passwordSession').val();
        if (passIngreso == '') {
            toastr.error('Campo password vacío', 'Debe ingresar un password', { timeOut: 3000 }, toastr.options.onHidden = function() { $('#passIngreso').focus(); });
            return false;
        } else {
            $('#FormIngresoSession,#ingOtroUsuario').hide();
            $('#validandoSession').show();
            $.post('../ingresoUsuario', { emailIngreso: emailIngreso, passIngreso: passIngreso }, function(data, textStatus, xhr) {

                var dat = JSON.parse(data);
                if (dat.multi_valores == 'usuario') {
                    toastr.error('Error', 'Email no encontrtado', { timeOut: 3000 }, toastr.options.onHidden = function() { $('#emailIngreso').focus(); });
                } else if (dat.multi_valores == 'invalido') {
                    toastr.error('Error', 'Password Invalido', { timeOut: 2000 }, toastr.options.onHidden = function() {

                        $('#validandoSession').hide();
                        $('#FormIngresoSession,#ingOtroUsuario').show();
                        $('#passwordSession').focus();
                    });
                }else if (dat.multi_valores == 'estado') {
                    toastr.error('Usuario Bloquedo. Comuniquese con su asesor.', 'Error', { timeOut: 10000 }, toastr.options.onHidden = function() {
                        $('#emailIngreso,#passIngreso,#btnIngreso,#olvidePss').attr("disabled", false);
                        $('#validando').hide();
                        $('#btns_ingreso').show();
                        $('#passIngreso').focus();
                    });
                } else {

                    if (typeof(Storage) !== "undefined") {
                        if ($('#inputCheckbox').is(':checked')) {
                            mi_objeto = {
                                usuario: emailIngreso,
                                nombres: dat.multi_valores,
                                img: dat.img
                            }
                            localStorage.setItem("datosUsuario", JSON.stringify(mi_objeto));
                            var local = JSON.parse(localStorage.getItem("datosUsuario"));
                            toastr.success('Datos correctos.', 'En un momento sera redireccionado a GuardianWeb', { timeOut: 3000 }, toastr.options.onHidden = function() { window.location.href = '../../default/index'; });
                        } else {
                            localStorage.clear();
                            toastr.success('Datos correctos.', 'En un momento sera redireccionado a GuardianWeb', { timeOut: 3000 }, toastr.options.onHidden = function() { window.location.href = '../../default/index'; });
                        }
                    } else {
                        toastr.info('Advertencia.', 'El navegador que está utilizando no soporta el recordar datos', { timeOut: 3000 }, toastr.options.onHidden = function() { window.location.href = '../../default/index'; });

                    }
                }
            });
        }
    },
};
ing.stars();