# Programa para saber si un número es par o impar

x = int(input("Digite un número:"))
r = x%2

if r==0:
    msj="PAR"
else: 
    msj="IMPAR"
print("El número :" + str(x)+ " es:"+ msj)
