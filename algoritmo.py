A = int(input("Ingrese un número: "))

B = A%100
C = B%10
D = B//10

if C==D :
    rta = "Los dos ultimos digitos son iguales"

else :
    rta = "Los dos ultimos digitos son diferentes"

print(str(rta))


