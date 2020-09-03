import json
from django.shortcuts import render,HttpResponse
from django.core import serializers

from Punto4.models import tabla_numerosprimos,tabla_primosgemelos
# Create your views here.
def home(request):
    return render(request,'index.html')

def numerosprimos(request):

    def verificardato(Dato):
        try:
            tabla_numerosprimos.objects.get(key=Dato)
            return True
        except tabla_numerosprimos.DoesNotExist:
            return False
    def verificarprimo(Data):
        try:
            tabla_numerosprimos.objects.get(primo=Data)
            return True
        except tabla_numerosprimos.DoesNotExist:
            return False
    def primo(Dato):
        if Dato==2:
            return True
        if Dato%2==0:
            return False
        i=3
        while i**2<=Dato:
            if Dato%i==0:
                return False
            i=i+2
        return True
    Dato=int(request.GET.get('numero'))
    numero = verificardato(Dato)
    if numero == False:
        prime=2
        contador=1
        while contador<=Dato:
            data = verificarprimo(prime)
            if data == False:
                if primo(prime):                
                    num=tabla_numerosprimos(key=contador,primo=prime)
                    contador+=1
                    num.save()
                prime+=1
            else:
                prime+=1
                contador+=1
        return HttpResponse("Numeros Primos almacenados en Base de Datos")
    else:
        last_ten = tabla_numerosprimos.objects.all().order_by('key')[:Dato]
        last_ten_in_ascending_order = reversed(last_ten)
        print(last_ten_in_ascending_order)       
        qs_json = serializers.serialize('json', last_ten_in_ascending_order)
        return render(request,'numerosprimos.html',{'primos':last_ten})

def primogemelos(request):
    def verificarconsulta(Dato):
        try:
            prueba=tabla_primosgemelos.objects.filter(verificarconsulta=Dato).first()
            if prueba == None:
                return False
            else:
                return True
        except tabla_primosgemelos.DoesNotExist:
            return False
    def verificargemelos(Data):
        try:
            tabla_primosgemelos.objects.get(gemelos=Data)
            return True
        except tabla_primosgemelos.DoesNotExist:
            return False
    numero= int(request.GET.get('numero'))
    print(numero)
    Dato= verificarconsulta(numero)
    consulta=tabla_primosgemelos.objects.all().last()
    con=consulta.verificarconsulta
    print(con)
    if con < numero:
        if Dato == False :
            primo = 2
            prime = []
            noesprimo = []
            contador = 1
            while primo <= numero:
                if primo not in noesprimo:
                    prime.append(primo)            
                    for i in range(primo*2, numero+1, primo):
                        noesprimo.append(i)
                primo += 1
            print("los primos gemelos hasta este numero  son :") 
            for p in prime:
                if p+2 in prime:
                    primo1=str(p)
                    primo2=str(p+2)
                    gemelos = primo1+"-"+primo2
                    Data=verificargemelos(gemelos)
                    if Data == False :          
                        num=tabla_primosgemelos(key=contador,gemelos=gemelos,verificarconsulta=numero)
                        num.save()
                    contador+=1
            return HttpResponse("Primos Gemelos almacenados en Base de datos")

    else:

        last_ten = tabla_primosgemelos.objects.all().order_by('key')[:numero]
        last_ten_in_ascending_order = reversed(last_ten)       
        qs_json = serializers.serialize('json', last_ten_in_ascending_order)
        return render(request,'primosgemelos.html',{'gemelos':last_ten})
        