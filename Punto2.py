numero= int(input("Ingrese el numero hasta el cual quiere verificar los numeros primos gemelos :"))
primo = 2
prime = []
noesprimo = []
while primo <= numero:
    if primo not in noesprimo :
        prime.append(primo)        
        for i in range(primo*2, numero+1, primo):
            noesprimo .append(i)            
    primo += 1
print("los primos gemelos hasta este numero  son :")   
for p in prime:
    if p+2 in prime:
        print(p, p+2)
