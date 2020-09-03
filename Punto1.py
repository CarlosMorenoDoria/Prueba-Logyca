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
Number=int(input("Ingrese un numero: "))
prime=2
contador=1
print ("Los Numeros primos hasta este numero son: ")
while contador<=Number:
    if primo(prime):
        print (contador, prime)
        contador+=1
    prime+=1

