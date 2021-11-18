$(document).ready(function (){
    var seleccionarFormula
    var objeto = {}
    var seleccionarEvento
    var seleccionarSerie
    var seleccionarPago
    var seleccionarTabla
    var seleccionarTempo


    objeto['V']=0
    objeto['A']=0
    objeto['G']=0
    objeto['interes']=0
    objeto['J']=0
    objeto['n']=0


    $(".V").keyup(function () {
        objeto['V'] = $(this).val();
    })
    $(".A").keyup(function () {
        objeto['A'] = $(this).val();
    })
    $(".G").keyup(function () {
        objeto['G'] = $(this).val();
    })
    $(".J").keyup(function () {
        objeto['G'] = $(this).val();
    })
    $(".interes").keyup(function () {
        objeto['interes'] = $(this).val();
    })
    $(".N").keyup(function () {
        objeto['n'] = $(this).val();
    })

    $('#seleccionarSerie').change(function() {
        seleccionarSerie=$(this).val()
        //esta tiene que modificar los inputs de seleccionar formula

        })

    $('#seleccionarTabla').change(function () {
        seleccionarTabla=$(this).val()

        objeto['tabla']=seleccionarTabla
    })

    $('#seleccionarPago').change(function() {
        seleccionarPago=$(this).val()

        objeto['pago']= seleccionarPago
        //esta modifica a nivel de envio en el post, no es requerida para los inputs
        //Tambien debe ser modificada a nivel de front, para dar a escoger entre creciente y decreciente sin tener que agregar otro estamento.
        })

    $('#seleccionarTempo').change(function () {
        seleccionarTempo = $(this).val()

        objeto['tiempo']= seleccionarTempo
        //Esta tiene que modificar el valor entre presente y futuro
    })


    $("body").on('click','.calcular',function () {



        $('#resultado_calculo').empty()
        var convertJson = JSON.stringify(objeto)

        if(seleccionarSerie==='uniforme')
        {
            $.post("/home/anualidades_uniformes/",{data:convertJson},function (data) {
            console.log(data)
        })}
        else if (seleccionarSerie==='variable')
            {
                $.post("/home/anualidades_Variables/",{data:convertJson},function (data) {

                })
            }
        else
            {
                alert('Para continuar es necesario que seleccione un tipo de serie, de lo contraio el programa no continuara.')
            }

    })

});
