$(document).ready(function (){
    var seleccionarFormula
    var objeto = {}

    $(".seleccionarFormula").keyup(function () {
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
        console.log(objeto)

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

    switch (seleccionarFormula) {
        case 1:

            var contendor=
                $("<div class='container'>" +
                    "<div class='row margin_TopDef'><label for='A'>A<input type='number' class='A' id='A'></label></div>" +
                    "<div class='row margin_TopDef'><label for='n'>N<input type='number' class='n' id='n'></label></div>"+
                    "<div class='row margin_TopDef'><label for='interes'>Interes<input type='number' class='interes' id='interes'></label></div>"+
                    "<div class='row margin_TopDef'><button class='calcular'>CALCULAR</button></div> "+
                    "</div>")
                $('abc').append(contendor)

            $("body").on('click','.calcular',function () {
            var convertJson = JSON.stringify(objeto)
            $.post("/home/anualidadVencida__VP/",{data:convertJson},function (data){

        })
                break;

    })
    }





})