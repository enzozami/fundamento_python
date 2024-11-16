# tipos de dados
# string -> texto
# float -> n° quebrado ou inteiro
# int - > apenas n° inteiro

#variavel -> armazenar um valor
# x = 10
# nome = "Enzo"
# nome2 = "Mariany"

# print("Meu nome é:", nome)

# armazenando valores do usuario
# nome = input("Digite seu nome: ")
# print("Seu nome é:", nome)

#comando input() armazena o valor como texto por padrao
# soma = input("Digite um numero: ")
# print(soma + "10")

#utiliza-se o float para converter para numero quebrado
# soma2 = float(input("Digite um numero:"))
# print(soma2 + 100)

# utiliza-se o int para converter para numero inteiro
# soma3 = int(input("Digite um valor:"))
# print(soma3 + 15)

# ATIVIDADE 1
import os
os.system("cls")

# print("-"*10, "ATIVIDADE 1", "-"*10)
# numero = int(input("Digite um valor: "))
# ant = numero - 1
# suc = numero + 1
# print("O antecessor de", numero, "é:", ant, "\nO seu sucessor é:", suc)
# #ou
# print("Numero:", numero, "\nAntecessor:", ant, "\nSucessor:", suc)
# #ou
# print("Numero:", numero, "\nAntecessor:", numero - 1, "\nSucessor:", numero + 1)


# ATIVIDADE 2
# print("-"*10, "ATIVIDADE 2", "-"*10)
# data_nasc = int(input("Digite o seu ano de nascimento: "))
# idade = 2024 - data_nasc
# print("Você tem {0} anos.".format(idade))

# ATIVIDADE 3
# round tbm arredonda -> round(valor, casa decimal)
# print("-"*10, "ATIVIDADE 3", "-"*10)

# print("-"*10, "SUPERMERCADO", "-"*10)
# # Variaveis
# nomeProduto1 = input("Digite o nome do primeiro produto: ")
# valorProduto1 = float(input("Digite o valor do primeiro produto: R$ "))
# nomeProduto2 = input("Digite o nome do segundo produto: ")
# valorProduto2 = float(input("Digite o valor do segundo produto: R$ "))
# #Contas
# descontoProduto1 = valorProduto1 - (0.10 * valorProduto1)
# descontoProduto2 = valorProduto2 - (0.25 * valorProduto2)
# soma = descontoProduto1 + descontoProduto2
# # Resultados
# print("-"*10, "CAIXA", "-"*10)
# print("O produto {0}, com valor R$ {1:.2f}, aplicado 10% de desconto ficará: R$ {2:.2f}".format(nomeProduto1, valorProduto1, descontoProduto1))
# print("O produto {0}, com valor R$ {1:.2f}, aplicado 25% de desconto ficará: R$ {2:.2f}".format(nomeProduto2, valorProduto2, descontoProduto2))
# # Valor total 
# print("-"*10, "VALOR TOTAL DA COMPRA", "-"*10)
# print(f"O valor total da compra será de R$ {soma:.2f}")

# print("O produto ", nomeProduto1, "tem como valor de desconto R$ ", descontoProduto1)


# ATIVIDADE 4
print("-"*10, "ATIVIDADE 4", "-"*10)

print("-"*10, "CONVERSOR DE TEMPERATURA", "-"*10)

conversor = input("Selecione uma letra para converter: \nf/F -> Fahreinheit \nc/C -> Celcius \n")
temp = float(input("Digite o valor da temperatura que deseja converter: "))

if(conversor == "f" or conversor == "F"):
        fahreinheit = (temp - 32) * (5/9)
        print(f"A temperatura {temp}°C em Fahreinhei é: {fahreinheit:.2f}°F")
elif(conversor == "c" or conversor == "C"):
        celcius = (temp * (9/5)) + 32
        print(f"A temperatura {temp}°F em Celcius é de {celcius:.2f}°C")
else:
    print("Temperatura não fornecida")




# temp = float(input("Digite o valor da temperatura que deseja converter: "))
# fahreinheit = (temp - 32) * (5/9)
# print("A temperatura °C em Fahreinhei é:", fahreinheit , "°F")