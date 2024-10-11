import os
os.system("cls")
print("Programa que determine se o numero digitado é a) par ou impar, b) positivo ou negativo ou c) inteiro ou decimal")

valor = float(input("informe um numero: "))

print("1 - par ou impar")
print("2 - positivo ou negativo")
print("3 - inteiro ou decimal")
opcao = input("Escolha uma opção: ")

if(opcao == "1"):
    if(valor % 2 == 0):
        print("Valor é par")
    else:
        print("Valor é impar")
elif(opcao == "2"):
    if(valor < 0):
        print("Valor é negativo")
    elif(valor > 0):
        print("Valor é positivo")
    else:
        print("Valor é igual a zero")
elif(opcao == "3"):
    if(valor == int(valor)):
        print("Valor é inteiro")
    else:
        print("Valor é decimal")
else:
    print("Opção invalida")
print("Fim do programa")