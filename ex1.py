def cifra_cesar_descriptografar(texto, deslocamento):
    resultado = ""

    for char in texto:
        # Verifica se o caractere é uma letra
        if char.isalpha():
            # Define o limite do alfabeto baseado se é maiúscula ou minúscula
            base = ord('A') if char.isupper() else ord('a')
            # Aplica o deslocamento negativo e trata o wrap-around
            novo_char = chr((ord(char) - base - deslocamento) % 26 + base)
            resultado += novo_char
        else:
            resultado += char  # Não altera caracteres que não são letras

    return resultado

# Solicita ao usuário o texto criptografado e o deslocamento
texto_criptografado_usuario = input("Digite o texto a ser descriptografado: ")
deslocamento_usuario = int(input("Digite o valor do deslocamento: "))

# Descriptografa o texto
texto_descriptografado = cifra_cesar_descriptografar(texto_criptografado_usuario, deslocamento_usuario)

# Exibe o resultado
print("Texto descriptografado:", texto_descriptografado)