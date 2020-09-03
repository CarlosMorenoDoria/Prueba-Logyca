from django.shortcuts import render,HttpResponse
from collections import defaultdict
from itertools import zip_longest
import json
# Create your views here.

def numeroprimo(request):
    def primo(x):
        if x==2:
            return True
        if x%2==0:
            return False
        i=3
        while i**2<=x:
            if x%i==0:
                return False
            i=i+2
        return True
    x=int(request.GET.get('numero'))
    prime=2
    contador=1
    d = defaultdict(list)
    lista_cont = []
    lista_prime = []
    while contador<=x:
        if primo(prime):
            lista_cont.append(contador)
            contador+=1
            lista_prime.append(prime)
        prime+=1

    for a, b in zip(lista_cont, lista_prime):
        d[a].append(b)
    print(dict(d))
    app_json = json.dumps(d)
    return HttpResponse(app_json)

def primosgemelos(request):
    def grouper(n, iterable, fillvalue=None):
        args = [iter(iterable)] * n
        return zip_longest(fillvalue=fillvalue, *args)
    numero= int(request.GET.get('numero'))
    print(numero)
    primo = 2
    prime = []
    noesprimo = []
    resultado = []
    keys = []
    contador = 1
    d = defaultdict(list)
    while primo <= numero:
        if primo not in noesprimo :
            prime.append(primo)            
            for i in range(primo*2, numero+1, primo):
                noesprimo.append(i)
        primo += 1
    print("los primos gemelos hasta este numero  son :")
    for p in prime:
        if p+2 in prime:
            keys.append(contador)
            resultado.append(p)
            resultado.append(p+2)
            contador+=1
    for a, b in zip(keys,grouper(2,resultado)):
        d[a].append(b)
    app_json = json.dumps(d)
    return HttpResponse(app_json)