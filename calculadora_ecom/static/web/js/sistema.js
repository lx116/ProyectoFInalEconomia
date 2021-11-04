$(document).ready(function (){
    var seleccionarFormula
    var objeto = {}
    var seleccionarEvento
    var seleccionarSerie
    var seleccionarPago
    var seleccionarTabla

    $(".VP").keyup(function () {
        objeto['VP'] = $(this).val();

    })
    $(".VF").keyup(function () {
        objeto['VF'] = $(this).val();

    })
    $(".A").keyup(function () {
        objeto['A'] = $(this).val();
        console.log(objeto)
        console.log("aaaa")


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
        console.log(seleccionarSerie)})

    $('#seleccionarPago').change(function() {
        seleccionarPago=$(this).val()
        console.log(seleccionarPago)})

    $('#seleccionarEvento').change(function() {
        seleccionarFormula=$(this).val()
        console.log(seleccionarFormula)
        switch (seleccionarFormula)
        {
            case "VP":
                if(seleccionarSerie==="uniform")
                {

                    if(seleccionarPago==='venc')
                    {
                        document.getElementById("VP_View").style.display='none'
                        document.getElementById("VF_View").style.display='none'
                        document.getElementById("G_View").style.display='none'
                        document.getElementById("J_View").style.display='none'


                        document.getElementById("A_View").style.display='block'
                        document.getElementById("A_View").style.display='block'
                        document.getElementById("A_View").style.display='block'
                        seleccionarEvento = "vencida_VP"
                    }
                    else if (seleccionarPago==='anti')
                    {
                        document.getElementById("VP_View").style.display='none'
                        document.getElementById("VF_View").style.display='none'
                        document.getElementById("G_View").style.display='none'
                        document.getElementById("J_View").style.display='none'


                        document.getElementById("A_View").style.display='block'
                        document.getElementById("A_View").style.display='block'
                        document.getElementById("A_View").style.display='block'
                        seleccionarEvento = "anticipada_VP"
                    }

                }
                else if (seleccionarSerie==="varia")
                {

                }
                break
            case "VF":
                    if(seleccionarSerie==="uniform")
                {

                    if(seleccionarPago==='venc')
                    {
                        document.getElementById("VP_View").style.display='none'
                        document.getElementById("VF_View").style.display='none'
                        document.getElementById("G_View").style.display='none'
                        document.getElementById("J_View").style.display='none'


                        document.getElementById("A_View").style.display='block'
                        document.getElementById("A_View").style.display='block'
                        document.getElementById("A_View").style.display='block'
                        seleccionarEvento = "vencida_VF"
                    }
                    else if (seleccionarPago==='anti')
                    {
                        document.getElementById("VP_View").style.display='none'
                        document.getElementById("VF_View").style.display='none'
                        document.getElementById("G_View").style.display='none'
                        document.getElementById("J_View").style.display='none'


                        document.getElementById("Interes_View").style.display='block'
                        document.getElementById("N_View").style.display='block'
                        document.getElementById("A_View").style.display='block'
                        seleccionarEvento = "anticipada_VF"
                    }

                }
                else if (seleccionarSerie==="varia")
                {

                }
                break
            case 'VP_A':
                if(seleccionarSerie==="uniform")
                {

                    if(seleccionarPago==='venc')
                    {
                        document.getElementById("VP_View").style.display='block'
                        document.getElementById("VF_View").style.display='none'
                        document.getElementById("G_View").style.display='none'
                        document.getElementById("J_View").style.display='none'


                        document.getElementById("Interes_View").style.display='block'
                        document.getElementById("A_View").style.display='none'
                        document.getElementById("N_View").style.display='block'
                        seleccionarEvento = "vencida_VP_A"
                    }
                    else if (seleccionarPago==='anti')
                    {
                        document.getElementById("VP_View").style.display='block'
                        document.getElementById("VF_View").style.display='none'
                        document.getElementById("G_View").style.display='none'
                        document.getElementById("J_View").style.display='none'


                        document.getElementById("Interes_View").style.display='block'
                        document.getElementById("A_View").style.display='none'
                        document.getElementById("N_View").style.display='block'
                        seleccionarEvento = "anticipada_VP_A"
                    }

                }
                else if (seleccionarSerie==="varia")
                {

                }
                break
            case 'VF_A':
                if(seleccionarSerie==="uniform")
                {

                    if(seleccionarPago==='venc')
                    {
                        document.getElementById("VP_View").style.display='none'
                        document.getElementById("VF_View").style.display='block'
                        document.getElementById("G_View").style.display='none'
                        document.getElementById("J_View").style.display='none'


                        document.getElementById("Interes_View").style.display='block'
                        document.getElementById("A_View").style.display='none'
                        document.getElementById("N_View").style.display='block'
                        seleccionarEvento = "vencida_VF_A"
                    }
                    else if (seleccionarPago==='anti')
                    {
                        document.getElementById("VP_View").style.display='none'
                        document.getElementById("VF_View").style.display='block'
                        document.getElementById("G_View").style.display='none'
                        document.getElementById("J_View").style.display='none'


                        document.getElementById("Interes_View").style.display='block'
                        document.getElementById("A_View").style.display='none'
                        document.getElementById("N_View").style.display='block'
                        seleccionarEvento = "anticipada_VF_A"
                    }

                }
                else if (seleccionarSerie==="varia")
                {

                }
                break


        }
    })



    $("body").on('click','.calcular',function () {


        $('#resultado_calculo').empty()
        var convertJson = JSON.stringify(objeto)

        switch (seleccionarEvento)
        {

            case 'vencida_VP':
                    $.post("/home/anualidadVencida__VP/",{data:convertJson},function (data)
                    {
                        console.log(data)

                        var contendor = $("<h4>El resultado de su operacion es: "+ data.resultados+" </h4>")
                        $("#resultado_calculo").append(contendor)
                    })
                break
            case 'anticipada_VP':
                $.post("/home/anualidadAnticipada__VP/",{data:convertJson},function (data)
                    {
                        console.log(data)

                        var contendor = $("<h4>El resultado de su operacion es: "+ data.resultados+" </h4>")
                        $("#resultado_calculo").append(contendor)
                    })
                break
            case 'vencida_VF':
                $.post("/home/anualidadVencida__VF/",{data:convertJson},function (data)
                    {
                        console.log(data)

                        var contendor = $("<h4>El resultado de su operacion es: "+ data.resultados+" </h4>")
                        $("#resultado_calculo").append(contendor)
                    })
                break
            case 'anticipada_VF':
                $.post("/home/anualidadVencida__VF/",{data:convertJson},function (data)
                    {
                        console.log(data)

                        var contendor = $("<h4>El resultado de su operacion es: "+ data.resultados+" </h4>")
                        $("#resultado_calculo").append(contendor)
                    })
                break
            case 'vencida_VP_A':
                $.post("/home/anualidadVencida__VP_A/",{data:convertJson},function (data)
                    {
                        console.log(data)

                        var contendor = $("<h4>El resultado de su operacion es: "+ data.resultados+" </h4>")
                        $("#resultado_calculo").append(contendor)
                    })
                break
            case 'anticipada_VP_A':
                $.post("/home/anualidadAnticipada__VP_A/",{data:convertJson},function (data)
                    {
                        console.log(data)

                        var contendor = $("<h4>El resultado de su operacion es: "+ data.resultados+" </h4>")
                        $("#resultado_calculo").append(contendor)
                    })
                break
            case 'vencida_VF_A':
                $.post("/home/anualidadVencida__VF_A/",{data:convertJson},function (data)
                    {
                        console.log(data)

                        var contendor = $("<h4>El resultado de su operacion es: "+ data.resultados+" </h4>")
                        $("#resultado_calculo").append(contendor)
                    })
                break
            case 'anticipada_VF_A':
                $.post("/home/anualidadAnticipada__VF_A/",{data:convertJson},function (data)
                    {
                        console.log(data)

                        var contendor = $("<h4>El resultado de su operacion es: "+ data.resultados+" </h4>")
                        $("#resultado_calculo").append(contendor)
                    })
                break

        }
    })

});
