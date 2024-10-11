s = "A função replace aa substitui a parte de um texto por outro texto"
s2 = s.replace("aa", "123")

print("Frase original = "+s)
print("Frase alterada = "+s2)

print(id(s))
print(id(s2))