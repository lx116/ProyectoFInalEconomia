from django.http import request,response, HttpResponse,HttpResponseRedirect
import json
from django.shortcuts import render, get_object_or_404,redirect
from django.http import JsonResponse


def renderHome(request):
    return render(request,'base.html')