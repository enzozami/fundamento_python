import os
os.system ("cls")

#DICIONARIO -> KEY AND VALUE (CHAVE E VALOR)

# atribuindo valores na criação
# dicionario = {"escola": "bayeux", "nota":10}

#adicionando valores no dicionario
#dicionario[key]=value
# dicionario["data"]="26/08/2023"
# dicionario[100]=200
# dicionario[True]=False
# print(dicionario)

# print(dicionario["escola"])

#remover valores .pop() .clear()
#pop -> remove pelo valor da chave (exclui a chave e o valor)
# dicionario.pop("data")

#clear -> exclui todos os valores
# dicionario.clear()
# print(dicionario)

#percorrer o dicionario
# for key, value in dicionario.items():
#     print(key, value, sep="--->")


#ATIVIDADE 1
# print("*"*15, "ATIVIDADE 1", "*"*15)

# cadastro={}

# cadastro["Nome: "] = nome = input("Digite seu nome: ")
# cadastro["Idade: "] = idade = int(input("Digite sua idade: "))
# cadastro["Telefone: "] = fone = input("Digite seu telefone: ")
# cadastro["Endereço: "] = endereco = input("Digite seu endereço: ")

# print(cadastro["Nome: "])



#ATIVIDADE 2
# print("*"*15, "ATIVIDADE 2", "*"*15)

# cadastro={}

# cadastro["Nome"] = nome = input("Digite seu nome: ")
# cadastro["Idade"] = idade = int(input("Digite sua idade: "))
# cadastro["CPF"] = cpf = input("Digite seu CPF: ")

# if cadastro["Idade"] < 18:
#     print(f"Cadastro não permitido")
# else:
#     print(f"Nome: {cadastro["Nome"]} \nIdade: {cadastro["Idade"]} \nCPF: {cadastro["CPF"]}")
# print(cadastro["Nome: "])




# DESAFIO
print("*"*15, "DESAFIO", "*"*15)

print("RESPONDA COM SIM OU NAO")
soma = 0

perguntas = {}
perguntas["a"] = (input("Telefonou para a vítima? "))
perguntas["b"] = (input("Esteve no local do crime? "))
perguntas["c"] = (input("Mora perto da vítima? "))
perguntas["d"] = (input("Devia para a vítima? "))
perguntas["e"] = (input("Já trabalhou com a vítima? "))

for key, value in perguntas.items():
    if perguntas[key] == "sim":
        soma = soma + 1

if soma == 2:
    print("Suspeito")
elif soma == 3 or soma == 4:
    print("Cúmplice")
elif soma == 5:
    print("Assassino")
else:
    print("Inocente")