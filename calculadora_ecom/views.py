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

    VF =A*((((1+interes)^n)-1)/(interes))

    return JsonResponse({'resultados':VF})


def anualidadVencida__VF_A(request):
    req = request.POST['data']
    data = json.loads(req)

    VF = data.get('VF')
    interes = data.get('interes')
    n = data.get('n')

    A =  VF*((interes)/(((1+interes)^n)-1))

    return JsonResponse({'resultados': A})


def anualidadVencdida__VF_N(request):
    req = request.POST['data']
    data = json.loads(req)

    VF = data.get('VF')
    interes = data.get('interes')
    A = data.get('A')

    n = (math.log(VF*interes+A)-math.log(A))/(math.log(1+interes))

    return JsonResponse({'resultados':n})

# Anualidad anticipada
def anualidadAnticipada(request):
    pass

def anualidadAnticipada__A(request):
    pass

def anualidadAnticipada__N(request):
    pass

def anualidadAnticipada__VF(request):
    pass

def anualidadAnticipada__A_VF(request):
    pass
