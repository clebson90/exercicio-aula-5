from math import trunc
nome = input("Qual seu nome?")
idade = input("Qual sua idade?")
peso = float(input("Qual seu peso?"))
altura = float(input("Qual sua altura?"))
imc = peso/(altura**2)
print(f" seu nome é {nome} \n sua idade é {idade} \n seu peso é {peso} \n sua altura é {altura} ")
print(f"seu imc é: {trunc(imc)}")
if (imc <= 17):
    print("você está muito abaixo do peso")
elif (imc <= 17) and (imc > 18.5):
    print("você está abaixo do peso")
elif (imc >= 18.5) and (imc < 25):
    print("você está no peso ideal")
elif (imc >= 25) and (imc < 30):
    print("você está sobrepeso")
elif (imc >= 30) and (imc < 35):
    print("você está obeso")
elif (imc >= 35) and (imc < 40):
    print("você está com obesidade severa")
else:
    print("você está com obsidade morbida")