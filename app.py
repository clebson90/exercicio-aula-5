print("óla professora, exercício da aula 5")

# 1-
num = int(input("Digite um número: "))
if num >= 0:
    print("Positivo")
else:
    print("Negativo")

# 2-
num = int(input("Digite um número: "))
dobro = num * 2
print("O dobro é:", dobro)

# 3-
valor = input("Digite algo: ")
print("Valor digitado:", valor)
print("Tipo da variável:", type(valor))

# 4-
num = int(input("Digite um número: "))
if num % 2 == 0:
    print("Par")
else:
    print("Ímpar")

# 5-
# Lendo como texto e convertendo para inteiro
num = int(input("Digite um número: "))
print("O triplo é:", num * 3)

# 6-
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
if n1 > n2:
    print("O maior é:", n1)
else:
    print("O maior é:", n2)

# 7
valor = int(input("Digite um valor: "))
if valor > 10:
    print("Maior que 10")
else:
    print("Menor ou igual a 10")

# 8-num = float(input("Digite um número: "))
if num >= 0:
    raiz = num ** 0.5
    print("A raiz aproximada é:", raiz)
else:
    print("Número inválido")

# 9-
valor = float(input("Digite um valor: "))
metade = valor / 2
print("A metade é:", metade)

# 10-
num = int(input("Digite um número: "))
if num >= 0 and num <= 10:
    print("Dentro do intervalo")
else:
    print("Fora do intervalo")

# 11-
num = int(input("Digite um número: "))
if num % 2 == 0 and num > 0:
    print("Par positivo")
elif num % 2 == 0 and num < 0:
    print("Par negativo")
else:
    print("Ímpar")

# 12-
n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
print("Soma:", n1 + n2)
if n1 > n2:
    print("O maior é:", n1)
elif n2 > n1:
    print("O maior é:", n2)
else:
    print("São iguais")

# 13-
num = float(input("Digite um número: "))
if num > 100:
    print("Metade:", num / 2)
else:
    print("Dobro:", num * 2)

# 14-
valor = int(input("Digite um valor: "))
if valor % 3 == 0:
    print("Múltiplo de 3")
else:
    print("Não é múltiplo")

# 15-
num = int(input("Digite um número: "))
if num >= 10 and num <= 20:
    print("Dentro")
else:
    print("Fora")

# 16-
valor = float(input("Digite um valor: "))
print("Tipo:", type(valor))
# Como foi convertido para float, calculamos o quadrado
print("Quadrado:", valor ** 2)

# 17-
idade = int(input("Digite sua idade: "))
if idade < 18:
    print("Menor de idade")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")

# 18-
num = int(input("Digite um número: "))
if num == 0:
    print("Neutro")
elif num % 2 == 0:
    if num > 0:
        print("Par positivo")
    else:
        print("Par negativo")
else:
    if num > 0:
        print("Ímpar positivo")
    else:
        print("Ímpar negativo")

# 19-
a = int(input("Número A: "))
b = int(input("Número B: "))
if a == b:
    print("São iguais")
else:
    diferenca = a - b
    print("Diferentes. Diferença:", abs(diferenca))

# 20-
valor = int(input("Digite um valor: "))
if valor >= 0 and valor <= 100:
    pass  # Não faz nada se estiver dentro
else:
    print("Valor fora do intervalo:", valor)

# 21-
num = int(input("Digite um número: "))
if num > 0:
    if num % 2 == 0 and num % 3 == 0:
        print("Múltiplo de 2 e 3")
    else:
        print("Não atende")
else:
    print("Número inválido")

# 22-
entrada = input("Digite um valor: ")
if entrada.isnumeric():
    num = int(entrada)
    if num > 10:
        print("Alto")
    else:
        print("Baixo")
else:
    print("Entrada inválida")

# 23-
n1 = int(input("N1: "))
n2 = int(input("N2: "))
n3 = int(input("N3: "))

restos = [n1 % 3, n2 % 3, n3 % 3]
restos.sort(reverse=True)
print("Restos em ordem decrescente:", restos)

# 24-
num = int(input("Digite um número: "))
if num >= 1 and num <= 100:
    if num % 2 == 0:
        print("Par no intervalo")
    else:
        print("Ímpar no intervalo")
else:
    print("Fora do intervalo")

# 25-
valor = input("Digite um valor: ")
print("Tipo original:", type(valor))
try:
    num_float = float(valor)
    print("Resultado da divisão por 2:", num_float / 2)
except:
    print("Não numérico")

# 26-
num = int(input("Digite um número: "))
if num > 0:
    if num < 10:
        print("Pequeno")
    elif num <= 100:
        print("Médio")
    else:
        print("Grande")
else:
    print("Negativo ou zero")

# 27-
n1 = int(input("N1: "))
n2 = int(input("N2: "))
if n1 > 0 and n2 > 0:
    print("Soma:", n1 + n2)
else:
    print("Produto:", n1 * n2)

# 28-
entrada = input("Digite um valor: ")
try:
    if "." in entrada:
        print("Metade (Real):", float(entrada) / 2)
    else:
        print("Dobro (Inteiro):", int(entrada) * 2)
except:
    print("Tipo inválido")

# 29-
num = int(input("Digite um número: "))
if num % 5 == 0:
    if num > 50:
        print("Múltiplo alto")
    else:
        print("Múltiplo baixo")
else:
    print("Não é múltiplo")

# 30-
entrada = input("Digite um valor: ")
if entrada.isnumeric():
    num = int(entrada)
    if num % 2 == 0:
        if num > 100:
            print("Par alto")
        else:
            print("Par baixo")
    else:
        print("Ímpar")
else:
    print("Entrada inválida")
