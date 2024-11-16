import os
os.system("cls")


# ESTRUTURA DE REPETIÇÃO -> WHILE (ENQUANTO)

# x = 100
# while x==100:
#     print("ola")
#     x = 99

# while com variavel incremental
# i = 0 
# while i < 10:
#     print("repetindo 10x")
#     i+=1
# else: 
#     print("fim do programa")

# n = 0 
# while n != 10:
#     n = int(input("digite um numero "))
#     print("repetindo")
# else:
#     print("cabou o programa")

# ATIVIDADE 1
# print("*"*10, "ATIVIDADE 1", "*"*10)

# x = 2
# while x <= 18:
#     print(x)
#     x+=1


# ATIVIDADE 2
# print("*"*10, "ATIVIDADE 2", "*"*10)

# x = 0
# while x >= -50:
#     print(x)
#     x-=1


# ATIVIDADE 3
# print("*"*10, "ATIVIDADE 3", "*"*10)

# nome = ""
# cpf = ""
# idade = ""

# x = 0
# while x < 4:
#     print("1 - CADASTRAR NOME | 2 - CADASTRAR CPF | 3 - CADASTRAR IDADE | 4 - SAIR DO PROGRAMA")
#     numero = int(input("Digite um número: "))
#     if numero == 1:
#         nome = input("CADASTRAR NOME: ")
#     elif numero == 2:
#         cpf = input("CADASTRAR CPF: ")
#     elif numero == 3:
#         idade = int(input("CADASTRAR IDADE: "))
#     elif numero == 4:
#         print("DADOS CADASTRADOS")
#         print(f"Nome: {nome}")
#         print(f"CPF: {cpf}")
#         print(f"IDADE: {idade}")
#         print("SAIU DO PROGRAMA")
#         x = 5
#     else:
#         print("OPÇÃO INVÁLIDA")
#         x = 5

# OUTRA RESOLUÇÃO
# print("*"*10, "ATIVIDADE 3", "*"*10)

# nome = ""
# cpf = ""
# idade = ""

# numero = 0
# while numero != 4:
#     print("1 - CADASTRAR NOME | 2 - CADASTRAR CPF | 3 - CADASTRAR IDADE | 4 - SAIR DO PROGRAMA")
#     numero = int(input("Digite um número: "))
#     if numero == 1:
#         nome = input("CADASTRAR NOME: ")
#     elif numero == 2:
#         cpf = input("CADASTRAR CPF: ")
#     elif numero == 3:
#         idade = int(input("CADASTRAR IDADE: "))
#     elif numero != 4:
#         print("OPÇÃO INVÁLIDA")
# else:
#     print("DADOS CADASTRADOS")
#     print(f"Nome: {nome}")
#     print(f"CPF: {cpf}")
#     print(f"IDADE: {idade}")
#     print("SAIU DO PROGRAMA")








# ESTRUTURA DE DADOS
# TIPOS DE DADOS: string, float, intl boolean
#LISTA

#adicionando os valores na declaração da variavel
#lista = ["senai", 100, 5.5, True, False]
# lista = []

# ADICIONANDO VALORES NA LISTA
# lista.append("escola")
# lista.append(50)
# lista.append(5.5)
# lista.append("senai")
# lista.append(18)
# lista.append(55.3)
# print(lista)

# excluir um valor da lista -> .pop() .remove() .clear()
# .pop() -> exclui pelo indice do elemento
# lista.pop(2)

# .remove() -> excluir pelo valor
# lista.remove("senai")

# .clear() -> excluir TODOS os valores da lista
# lista.clear()

#capturar/recuperar um valor especifico
# print(lista[4])
# print(lista)

#percorrendo uma lista
#len() -> retorna o tamanho total da lista
# for i in range(len(lista)):
#     print(lista[i])


# ATIVIDADE 4
# print("-"*10, "ATIVIDADE 4", "-"*10)

# lista = []
# numero = 0
# while numero != 4:
#     print("DIGITE 1 - ADICIONAR NOVO PRODUTO \nDIGITE 2 - REMOVER UM PRODUTO \nDIGITE 3 - REMOVER TODOS OS ITENS \nDIGITE 4 - SAIR DO PROGRAMA \nDIGITE 5 - EXIBIR TODOS OS PRODUTOS")
#     numero = int(input("Digite um valor: "))
#     if numero == 1:
#         nome = input("Digite o nome do produto que deseja adicionar: ")
#         lista.append(nome)
#     elif numero == 2:
#         nome = input("Digite o nome do produto que deseja remover: ")
#         lista.remove(nome)
#     elif numero == 3:
#         lista.clear()
#     elif numero == 5:
#         for i in range(len(lista)):
#             print(lista[i])
#     else:
#         print("Opção inválida")
# else:
#     print("SAIU DO PROGRAMA")


# ATIVIDADE 4
print("-"*10, "ATIVIDADE 5", "-"*10)

soma = 0
lista = []
for i in range(10):
    lista.append(float(input("Digite um número: ")))
else:
    for i in range(10):
        print(lista[i])
for i in range(len(lista)):
    soma+=lista[i]
else:
    print(f"O valor da soma será de {soma}")