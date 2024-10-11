import os
os.system("cls")

texto = "toda string em python é imutavel"

novalista=texto.split(" ")
print(texto.split(" "))
print(novalista)
print(novalista[3]+" "+novalista[5])
print(id(texto))
print(id(novalista))