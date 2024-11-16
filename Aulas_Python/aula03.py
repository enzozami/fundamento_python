import os
os.system("cls")

# CONDICIONAL IF ELSE ELIF (se nao)
# STRING , INT, FLOAT, BOOLEAN (TRUE / FALSE)
# OPERADORES CONDICIONAIS:
# < <= > >= != == and or 
# operador and retorna false se apenas 1 ou mais condições forem falsas
# operador or retorna verdadeiro se apenas 1 ou mais condições forem verdadeiras

# x = 10 

# if x == 10:
#     print("verdadeiro")
# else:
#     print("false")

# escola = "senai"
# if escola != "senai":
#     print("verdadeiro")
# else:
#     print("falso")

# ATIVIDADE 1
# print("-"*10, "ATIVIDADE 1", "-"*10)

# idade = int(input("Digite sua idade: "))

# if idade < 0 or idade > 120:
#     print("Sua idade é inválida! Digite sua idade verdadeira!")
# elif idade < 18:
#     print("Você é menor de idade!")
# else: 
#     print("Você é maior de idade!")


# ATIVIDADE 2
# print("-"*10, "ATIVIDADE 2", "-"*10)

# nota1 = float(input("Digite a primeira nota: "))   
# nota2 = float(input("Digite a segunda nota: "))

# media = (nota1+nota2)/2
# print(f"A média é {media:.1f}")

# if media < 5:
#     print("O aluno está reprovado.")
# elif media <= 7:
#     print("O aluno está de recuperação")
# else:
#     print("O aluno está aprovado")

# ATIVIDADE 3
print("-"*10, "ATIVIDADE 3", "-"*10)

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso/(altura*altura)

print(f"Seu IMC é: {imc:.2f}")

if imc < 17:
    print("Muito abaixo do peso.")
elif imc < 18.50:
    print("Abaixo do peso.")
elif imc < 25:
    print("Peso normal.")
elif imc < 30:
    print("Acima do peso.")
elif imc < 35:
    print("Obesidade 1")
elif imc < 40:
    print("Obesidade 2 (severa)")
else:
    print("Obesidade 3 (mórbida)")