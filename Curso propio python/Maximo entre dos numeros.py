
#Tenemos que ver el 12

a=int(input("Introduce un numero: "))

b=int(input("Introduce un segundo numero: "))


def DevuelveMax(a,b):
    if a<=b:
        print("El numero mas grande es: ",b)
   # elif a==b:
    #    print("El numero mas grande es: ",a)
    else: 
        print("El numero mas grande es: ",a)
        

print(DevuelveMax(a,b))