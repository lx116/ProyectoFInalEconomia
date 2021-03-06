from django.http import request, response, HttpResponse, HttpResponseRedirect
import json, math
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def renderHome(request):
    return render(request, 'appOne.html')


# Anulidades uniformes
@csrf_exempt
def anualiadades_Uniformes(request):
    res = request.POST['data']
    data = json.loads(res)
    print(data)

    es_anticipada = data.get('pago')

    es_presente = data.get('tiempo')



    if data.get('interes') == '':
        interes = 0
    else:
        interes = float(data.get('interes')) / 100

    A = 0
    V = 0
    n = 0

    conversor = data.get('conversor_tiempo')

    mensaje = ''
    mensaje_interes = ''
    if data.get('A') == '':
        A = 0
    else:
        A = float(data.get('A'))

    if data.get('n') == '':
        n = 0
    else:
        n = float(data.get('n'))

    if data.get('V') == '':
        V = 0
    else:
        V = float(data.get('V'))

    if conversor != '':
        n = conversor_tiempo_a_meses(n, conversor)

    if interes <= 0:
        mensaje_interes = 'El valor utilizado para los resolver el problema, sera el minimo vigente en Colombia.' \
                          'Este corresponde al'
        interes = 2 / 100

    if A == 0:

        if es_presente == 'presente':
            if es_anticipada == 'anticipada':
                A = anualidadAnticipada__VP_A(V, n, interes)

            else:
                A = anualidadVencida__VP_A(V, n, interes)

        else:
            if es_anticipada == 'anticipada':
                A = anualidadAnticipada__A_VF(V, n, interes)

            else:
                A = anualidadVencida__VF_A(V, n, interes)

    elif n == 0:
        if es_presente == 'presente':
            if es_anticipada == 'anticipada':
                n = anualidadAnticipada__N(V, A, interes)

            else:
                n = anualidadVencida__VP_N(V, A, interes)

        else:
            if es_anticipada == 'anticipada':
                mensaje = 'La anualidad anticipada requiere estar en presente para funcionar correctamente cuando se ' \
                          'desconoce el tiempo. '

            else:
                n = anualidadVencdida__VF_N(V, A, interes)

    elif V == 0:
        if es_presente == 'presente':
            if es_anticipada == 'anticipada':
                V = anualidadAnticipada__VP(A, n, interes)


            else:
                V = anualidadVencida__VP(A, n, interes)

        else:
            if es_anticipada == 'anticipada':
                V = anualidadAnticipada__VF(A, n, interes)

            else:
                V = anualidadVencida__VF(A, n, interes)

    tipo_tabla = data.get('tabla')

    n = float(n)
    n = round(n)

    if tipo_tabla == 'amortizacion':
        tabla = tabla_amortizacion(V, A, interes, n)
    else:
        tabla = tabla_capitalizacion(V, A, interes, n)

    print(tabla)

    A = round(A)
    V = round(V)
    return JsonResponse(
        {'anualidad': A, 'tiempo': n, 'valor': V, 'alerta_de_error': mensaje, 'alerta_de_inters': mensaje_interes,
         'tabla': tabla, 'interes': interes})


# Anualidades Variables
@csrf_exempt
def anualidades_Variables(request):
    res = request.POST['data']
    data = json.loads(res)
    print(data)

    es_anticipada = data.get('pago')

    es_presente = data.get('tiempo')

    A = 0
    V = 0
    n = 0
    G = data.get('G')
    J = data.get('J')
    conversor = data.get('conversor_tiempo')

    interes = float(data.get('interes')) / 100

    mensaje = ''
    mensaje_interes = ''
    if data.get('A') == '':
        A = 0
    else:
        A = float(data.get('A'))

    if data.get('n') == '':
        n = 0
    else:
        n = float(data.get('n'))
        n = round(n)

    if data.get('V') == '':
        V = 0
    else:
        V = float(data.get('V'))

    n = conversor_tiempo_a_meses(n, conversor)

    if interes <= 0:
        mensaje_interes = 'El valor utilizado para los resolver el problema, sera el minimo vigente en Colombia.' \
                          'Este corresponde al 2%'
        interes = 2 / 100

    if A == 0:

        if es_presente == 'futuro':
            if es_anticipada == 'creciente':
                A = gradienteLinealCreciente__A(V, n, interes, G)
                print(A)

            else:
                A = gradietneLinealDecreciente__A(V, n, interes, G)

        else:
            mensaje = 'para poder encontrar la anualidad con gradiente lineal, usted necesita seleccionar el timepo ' \
                      'como futuro. '
    elif V == 0:
        if es_presente == 'presente':
            if es_anticipada == 'creciente':
                V = gradienteLinealCreciente__VP(V, n, interes, G)
            else:
                V = gradietneLinealDecreciente__VP(V, n, interes, G)
        else:
            if es_anticipada == 'creciente':
                V = gradienteLinealCreciente__VF(V, n, interes, G)
            else:
                V = gradietneLinealDecreciente__VF(V, n, interes, G)

    tipo_tabla = data.get('tabla')

    n = float(n)
    n = round(n)

    if tipo_tabla == 'amortizacion':
        tabla = tabla_amortizacion(V, A, interes, n)
    else:
        tabla = tabla_capitalizacion(V, A, interes, n)

    A = round(A)
    V = round(V)
    return JsonResponse(
        {'anualidad': A, 'tiempo': n, 'valor': V, 'alerta_de_error': mensaje, 'J': J, 'G': G,
         'alerta_de_inters': mensaje_interes,
         'tabla': tabla, 'interes': interes})


# Tabla de amortizacion
def tabla_amortizacion(V, A, interes, n):

    V = float(V)
    tabla = []
    array = []
    n = int(n)
    pago_capital = 0
    monto = V

    cuota = V * (((1 + interes) ** n)*interes) / (((1 + interes) ** n) - 1)
    print(cuota)
    for i in range(n):
        for j in range(1):
            array = []

            interes_amortizacion = monto * interes
            pago_capital = cuota - interes_amortizacion
            monto = monto - pago_capital

            array.append(round(cuota))

            array.append(round(interes_amortizacion))
            array.append(round(pago_capital))
            array.append(round(monto))

        tabla.append(array)

    return tabla

# Tabla de capitalizacion
def tabla_capitalizacion(V, A, interes, n):
    V = float(V)
    print(interes)
    print(V)
    tabla = []
    saldo = A
    n = int(n)

    array = []

    for i in range(n):
        for j in range(1):
            array = []
            interes_capitalizable = 0
            abono = 0

            interes_capitalizable = V * interes
            abono = V + interes_capitalizable
            saldo = saldo + abono

            array.append(round(V))
            array.append(round(interes_capitalizable))
            array.append(round(abono))
            array.append(round(saldo))

        tabla.append(array)

    return tabla


# formulas

# Anualidades vencidas para encontrar A

def anualidadVencida__VP_A(V, n, interes):
    A = V * ((((1 + interes) ** n) - 1) / (interes * ((1 + interes) ** n)))

    return A


def anualidadVencida__VF_A(V, n, interes):
    A = V * (interes / (((1 + interes) ** n) - 1))

    return A


# Anulidades anticipadas para encontrar A
def anualidadAnticipada__VP_A(V, n, interes):
    A = V * ((interes * (1 + interes) ** n) / (((1 + interes) ** n) - 1)) / (1 + interes)

    return A


def anualidadAnticipada__A_VF(V, n, interes):
    A = V / (math.pow((1 + interes), (n + 1)) - ((1 + interes) ** n)) / interes

    return A


# Conversor de tiempo
def conversor_tiempo_a_meses(n, conversor):
    if conversor == 'anual':
        n = n * 12
    elif conversor == 'semestre':
        n = n * 6
    elif conversor == 'trimestre':
        n = n * 3
    elif conversor == 'bimenseual':
        n = n * 2
    else:
        n = n

    return n

# Anuliadad vencida para encontrar N
def anualidadVencida__VP_N(V, A, interes):
    n = (math.log(A) - math.log(A - (interes * V))) / math.log(1 + interes)

    return n


def anualidadVencdida__VF_N(V, A, interes):
    n = (math.log((V * interes) + A) - math.log(A)) / math.log(1 + interes)

    return n


# Anualidad anticipada para encontrar N
def anualidadAnticipada__N(V, A, interes):
    n = ((math.log(A) - math.log(A - interes * (V - A))) / (math.log(1 + interes))) + 1

    return n


# Anualidad anticipada para encontrar el valor
def anualidadAnticipada__VP(A, n, interes):
    VP = (A * (1 + interes) * (math.pow((1 + interes), n) - 1) / (interes * math.pow((1 + interes), n)))

    vp = "{:.2f}".format(VP)

    return VP


def anualidadAnticipada__VF(A, n, interes):
    VF = A * (((1 + interes) ** (n + 1)) - (1 + interes) / (interes))

    VF = "{:.2f}".format(VF)

    return VF


# Anualidad vencida para encontrar el valor
def anualidadVencida__VP(A, n, interes):
    vp = A * ((((1 + interes) ** n) - 1) / (interes * ((1 + interes) ** n)))

    vp = "{:.2f}".format(vp)

    return vp


def anualidadVencida__VF(A, n, interes):
    VF = A * ((((1 + interes) ** n) - 1) / (interes))
    VF = "{:.2f}".format(VF)
    return VF


# Gradientes crecientes_A
def gradienteLinealCreciente__A(V, n, interes, G):
    G = float(G)

    A = V - (G / interes) * (((((1 + interes) ** n) - 1) / interes) - n) / (((1 + interes) ** n) - 1) / interes

    return A


# Gradiente decreciente_A


def gradienteLinealCreciente__VP(A, n, interes, G):
    G = float(G)

    VP = A * ((((1 + interes) ** n) - 1) / (interes * (1 + interes) ** n)) + (G / interes) * (
            ((((1 + interes) ** n) - 1) / (interes * (1 + interes) ** n)) - (n / (
            (1 + interes) ** n)))

    return VP


def gradienteLinealCreciente__VF(A, n, interes, G):
    G = float(G)

    VF = A * ((((1 + interes) ** n) - 1) / interes) + (G / interes) * (((1 + interes) ** n) - n)

    return VF


# Gradiente lineas decreciente

def gradietneLinealDecreciente__VP(A, n, interes, G):
    G = float(G)

    VP = A * ((((1 + interes) ** n) - 1) / (interes * (1 + interes) ** n)) - (G / interes) * (
            ((((1 + interes) ** n) - 1) / (interes * (1 + interes) ** n)) - (n / (
            (1 + interes) ** n)))

    return JsonResponse({'resultados': VP})


def gradietneLinealDecreciente__VF(A, n, interes, G):
    G = float(G)

    VF = A * ((((1 + interes) ** n) - 1) / interes) - (G / interes) * (((((1 + interes) ** n) - 1) / interes) - n)

    return JsonResponse({'resultados': VF})


def gradietneLinealDecreciente__A(V, n, interes, G):
    G = float(G)
    A = V + (G / interes) * (((((1 + interes) ** n) - 1) / interes) - n) / ((((1 + interes) ** n) - 1) / interes)

    return A
