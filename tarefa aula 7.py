#1-
num = int(input("Digite um número inteiro positivo: "))
if num > 1:
    cont_divisores = 0
    for i in range(1, num + 1):
        if num % i == 0:
            cont_divisores += 1
    if cont_divisores == 2:
        print(f"O número {num} é primo.")
    else:
        print(f"O número {num} não é primo.")
else:
    print("Números menores ou iguais a 1 não são considerados primos.")

#2-
n = int(input("Digite um número n (n > 1): "))

if n > 1:
    divisores = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisores += 1
    print(f"O número {n} tem {divisores} divisores.")
else:
    print("Entrada inválida.")

#3-
while True:
    num = int(input("Digite um número positivo (ou negativo para parar): "))
    if num < 0:
        break
    print(f"O dobro de {num} é {num * 2}")

#4-
otimo = 0
bom = 0
regular = 0

for i in range(15):
    print(f"Espectador {i+1}:")
    voto = int(input("Sua opinião (3-Ótimo, 2-Bom, 1-Regular): "))
    if voto == 3:
        otimo += 1
    elif voto == 2:
        bom += 1
    elif voto == 1:
        regular += 1

print(f"\nTotal Ótimo: {otimo}")
print(f"Total Bom: {bom}")
print(f"Total Regular: {regular}")

#5-
opcao = "sim"
while opcao.lower() != "nao":
    distancia = float(input("Distância percorrida (Km): "))
    tempo = float(input("Tempo gasto (horas): "))
    if tempo > 0:
        velocidade = distancia / tempo
        print(f"Velocidade média: {velocidade:.2f} Km/h")
    else:
        print("O tempo deve ser maior que zero.")
    opcao = input("Deseja continuar? (sim/nao): ")