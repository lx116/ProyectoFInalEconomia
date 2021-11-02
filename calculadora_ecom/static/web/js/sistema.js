$(document).ready(function (){
    var seleccionarFormula
    var objeto = {}

    $(".seleccionarFOrmula").keyup(function () {
        seleccionarFormula = $(this).val();

    })

    $(".VP").keyup(function () {
        objeto['VP'] = $(this).val();

    })
    $(".VF").keyup(function () {
        objeto['VF'] = $(this).val();

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
    $(".n").keyup(function () {
        objeto['n'] = $(this).val();

    })

    switch (seleccionarFormula) {
        case 1:
            $("body").on('click','.calcular',function () {
                var convertToJson = objeto

                $.post("/home/anualidadVencida__VP/",{data:convertToJson},function (data){

                })
            })

    }

})