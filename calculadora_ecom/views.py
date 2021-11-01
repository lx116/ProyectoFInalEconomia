from django.http import request, response, HttpResponse, HttpResponseRedirect
import json, math
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse


def renderHome(request):
    return render(request, 'appOne.html')


# formulas

# Valor presente de una Anualidad Vencida y Pagos

def anualidadVencida__VP(request):
    req = request.POST['data']
    data = json.loads(req)

    A = data.get('A')
    n = data.get('n')
    interes = data.get('interes')

    vp = A * ((((1 + interes) ^ n) - 1) / (interes * ((1 + interes) ^ n)))

    return JsonResponse({'resultados': vp})


def anualidadVencida__VP_A(request):
    req = request.POST['data']
    data = json.loads(req)

    VP = data.get('VP')
    n = data.get('n')
    interes = data.get('interes')

    A = VP * ((((1 + interes) ^ n) - 1) / (interes * ((1 + interes) ^ n)))

    return JsonResponse({'resultados': A})


def anualidadVencida__VP_N(request):
    req = request.POST['data']
    data = json.loads(req)

    vp = data.get('VP')
    A = data.get('A')
    interes = data.get('interes')

    n = (math.log(A) - math.log(A - (interes * vp))) / (math.log(1 + interes))

    return JsonResponse({'resultados': n})


# Valor Final de una Anualidad Vencida y Pagos

def anualidadVencida__VF(request):
    req = request.POST['data']
    data = json.loads(req)

    A = data.get('A')
    interes = data.get('interes')
    n = data.get('n')

    VF = A * ((((1 + interes) ^ n) - 1) / (interes))

    return JsonResponse({'resultados': VF})


def anualidadVencida__VF_A(request):
    req = request.POST['data']
    data = json.loads(req)

    VF = data.get('VF')
    interes = data.get('interes')
    n = data.get('n')

    A = VF * (interes / (((1 + interes) ^ n) - 1))

    return JsonResponse({'resultados': A})


def anualidadVencdida__VF_N(request):
    req = request.POST['data']
    data = json.loads(req)

    VF = data.get('VF')
    interes = data.get('interes')
    A = data.get('A')

    n = (math.log(VF * interes + A) - math.log(A)) / (math.log(1 + interes))

    return JsonResponse({'resultados': n})


# Anualidad anticipada
def anualidadAnticipada(request):
    req = request.POST['data']
    data = json.loads(req)

    A = data.get('A')
    n = data.get('n')
    interes = data.get('interes')

    VP = (A * (1 + interes) * (math.pow((1 + interes), n) - 1) / (interes * math.pow((1 + interes), n)))

    return JsonResponse({'resultados': VP})


def anualidadAnticipada__A(request):
    req = request.POST['data']
    data = json.loads(req)

    VP = data.get('VP')
    n = data.get('n')
    interes = data.get('interes')

    A = VP * ((interes * (1 + interes) ^ n) / (((1 + interes) ^ n) - 1)) / (1 + interes)

    return JsonResponse({'resultados': A})


def anualidadAnticipada__N(request):
    req = request.POST['data']
    data = json.loads(req)

    VP = data.get('VP')
    A = data.get('A')
    interes = data.get('interes')

    n = ((math.log(A) - math.log(A - interes * (VP - A))) / (math.log(1 + interes))) + 1

    return JsonResponse({'resultados': n})


def anualidadAnticipada__VF(request):
    req = request.POST['data']
    data = json.loads(req)

    A = data.get('A')
    n = data.get('n')
    interes = data.get('interes')

    VF = A * (((1 + interes) ^ (n + 1)) - (1 + interes) / (interes))

    return JsonResponse({'resultados': VF})


def anualidadAnticipada__A_VF(request):
    req = request.POST['data']
    data = json.loads(req)

    n = data.get('n')
    interes = data.get('interes')
    VF = data.get('VF')

    A = VF / (math.pow((1 + interes), (n + 1)) - ((1 + interes) ^ n)) / interes

    return JsonResponse({'reulstados': A})


# Gradiente lienal clasico Creciente

def gradienteLinealCreciente__VP(request):
    req = request.POST['data']
    data = json.loads(req)

    A = data.get('A')
    n = data.get('n')
    interes = data.get('interes')
    G = data.get('G')

    VP = A * ((math.pow((1 + interes), n) - 1) / (interes * math.pow((1 + interes), n))) + (G / interes)(
        ((math.pow((1 + interes), n) - 1) / (interes(1 + interes) * n)) - (n / (1 + interes) * n))

    return JsonResponse({'resultados': VP})


def gradienteLinealCreciente__VF(request):
    req = request.POST['data']
    data = json.loads(req)

    A = data.get('A')
    n = data.get('n')
    interes = data.get('interes')
    G = data.get('G')

    VF = A * ((math.pow((1 + interes), n) - 1) / interes) + (G / interes) * (
            ((math.pow((1 + interes), n) - 1) / interes) - n)

    return JsonResponse({'resultados': VF})


def gradienteLinealCreciente__A(request):
    req = request.POST['data']
    data = json.loads(req)

    n = data.get('n')
    interes = data.get('interes')
    G = data.get('G')
    VF = data.get('VF')

    A = VF - (G / interes) * (((math.pow((1 + interes), n) - 1) / interes) - n) / (
            (math.pow((1 + interes), n) - 1) / interes)

    return JsonResponse({'resultados': A})


# Gradiente lineas decreciente

def gradietneLinealDecreciente__VP(request):
    req = request.POST['data']
    data = json.loads(req)

    A = data.get('A')
    n = data.get('n')
    interes = data.get('interes')
    G = data.get('G')

    VP = A * ((math.pow((1 + interes), n) - 1) / (interes * math.pow((1 + interes) ^ n))) - (G / interes) * (
            ((math.pow((1 + interes), n) - 1) / (interes * math.pow((1 + interes), n))) - (
            n / math.pow((1 + interes), n)))

    return JsonResponse({'resultados': VP})


def gradietneLinealDecreciente__VF(request):
    req = request.POST['data']
    data = json.loads(req)

    A = data.get('A')
    n = data.get('n')
    interes = data.get('interes')
    G = data.get('G')

    VF = A * ((math.pow((1 + interes), n) - 1) / interes) - (G / interes) * (
            ((math.pow((1 + interes), n) - 1) / interes) - n)

    return JsonResponse({'resultados': VF})


def gradietneLinealDecreciente__A(request):
    req = request.POST['data']
    data = json.loads(req)

    n = data.get('n')
    interes = data.get('interes')
    G = data.get('G')
    VF = data.get('VF')

    A = VF + (G / interes) * (((math.pow((1 + interes), n) - 1) / interes) - n) / (
            (math.pow((1 + interes), n) - 1) / interes)

    return JsonResponse({'resultados': A})


# Gradiente geometrico creciente

def gradietneGeometricoCreciente(request):
    VP = 0
    req = request.POST['data']
    data = json.loads(req)

    A = data.get('A')
    n = data.get('n')
    interes = data.get('interes')
    J = data.get('J')

    if interes != J:
        VP = A * ((math.pow((1 + interes), n) - (math.pow((1 + J), n))) / ((interes - J) * math.pow((1 + interes), n)))
    elif interes == J:
        VP = ((n * A) / (1 + interes))

    return JsonResponse({'resultados': VP})


# Gradiente geoemtrico decreciente

def gradienteGeometricoDecrecietne(request):
    VP = 0
    req = request.POST['data']
    data = json.loads(req)

    A = data.get('A')
    n = data.get('n')
    interes = data.get('interes')
    J = data.get('J')

    if interes != J:
        VP = A * ((math.pow((1 + interes), n) - (math.pow((1 + J) ^ n))) / ((interes + J) * math.pow((1 + interes), n)))
    elif interes == J:
        VP = (A / (1 + interes))

    return JsonResponse({'request': VP})
