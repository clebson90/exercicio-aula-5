# 1-
nota = int(input("Digite um número entre 0 e 10: "))
while (nota < 0 or nota > 10):
    print("Número inválido")
    nota = int(input("Digite um número entre 0 e 10: "))
else:
    print("número válido")

# 2-
senha = int(input("digite a senha "))
while senha != (1234):
    print("senha inválida")
    senha = int(input("digite a senha "))
else:
    print("senha válida")

#3-
n = int(input("Digite um número: "))
i = 1
while (i <= n):
    print(i)
    i = i + 1
print("Fim do programa")

#4-
soma = 0
while True:
    n = int(input("Digite um número: "))
    if n < 0:
        print("Número negativo, encerrando o programa.")
        break
    soma += n
print("A soma dos números digitados é:", soma)

#5-
while True:
    numero = int(input("Digite um número (0 para parar): "))
    if numero == 0:
        break
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é ímpar")

#6-
maior = 0
while True:
    numero = int(input("Digite um número (0 para parar): "))
    if numero == 0:
        break
    if numero > maior:
        maior = numero
print(f"O maior número digitado foi: {maior}")

#7-
soma = 0
contador = 0
while True:
    nota = float(input("Digite uma nota (-1 para parar): "))
    if nota == -1:
        break
    if 0 <= nota <= 10:
        soma += nota
        contador += 1
if contador > 0:
    media = soma / contador
    print(f"A média das notas válidas é: {media}")
else:
    print("Nenhuma nota válida digitada.")

#8-
numero = int(input("Digite um número para ver a tabuada: "))
i = 1
while i <= 10:
    print(f"{numero} x {i} = {numero * i}")
    i += 1

#9-
positivos = 0
negativos = 0
while True:
    numero = int(input("Digite um número (0 para parar): "))
    if numero == 0:
        break
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")

#10-
numero_secreto = 42  # Número fixo
palpite = 0
while palpite != numero_secreto:
    palpite = int(input("Adivinhe o número (1-100): "))
    if palpite < numero_secreto:
        print("Seu palpite é menor!")
    elif palpite > numero_secreto:
        print("Seu palpite é maior!")
print("Parabéns! Você acertou o número!")