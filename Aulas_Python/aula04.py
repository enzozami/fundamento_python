import os
os.system("cls")

# estrutra de repetição

# for i in range(5): # i começa em 0 e vai até range - 1
#     print("olá!")
#     print(i)

# for senai in range(10):
#     print(senai)

# for com 2 parametros

# for i in range(5, 15): # começa em 5 e vai até range - 1
#     print(i)

# for i in range(1, 10, 2): # começa em 1 e vai até range - 1 incrementando de 2 em 2
#     print(i)


# ATIVIDADE 1
# print("*"*10, "ATIVIDADE 1", "*"*10)
# for i in range(7, 78):
#     print(i)

# ATIVIDADE 2
# print("*"*10, "ATIVIDADE 2", "*"*10)
# for i in range(-1, -31, -1):
#     print(i)

# ATIVIDADE 3 
# print("*"*10, "ATIVIDADE 3", "*"*10)
# print("-"*10, "TABUADA", "-"*10)

# numero = int(input("Digite o valor desejado para tabuada: "))

# print(f"A tabuada de {numero} é: ")

# for i in range(1, 11):
#     tabuada = numero * i
#     print(f"{numero} * {i} = {tabuada}")

# print("-"*10, "TABUADA FINALIZADA", "-"*10)


##DESAFIO
# print("*"*10, "DESAFIO", "*"*10)

# maiorNumero = int(input("Digite um número: ")) 

# for i in range(4):
#     numero = int(input("Digite um número: "))
#     if numero > maiorNumero:
#         maiorNumero = numero    

# print(maiorNumero)

## OUTRA RESOLUÇÃO mas aceita apenas numero POSITIVO
# print("*"*10, "DESAFIO", "*"*10)

# maiorNumero = 0 

# for i in range(5):
#     numero = int(input("Digite um número: "))
#     if numero > maiorNumero:
#         maiorNumero = numero    

# print(maiorNumero)

## COM DOIS IFS
# print("*"*10, "DESAFIO", "*"*10)

# maiorNumero = 0

# for i in range(5):
#     numero = int(input("Digite um número: "))
#     if i == 0:
#         maiorNumero = numero   
#     if numero > maiorNumero:
#         maiorNumero = numero
        

# print(maiorNumero)


# DESAFIO 2
print("*"*10, "DESAFIO", "*"*10)

preco = float(input("Digite o valor do pão: "))

print("*"*10, "TABELA DE PREÇOS", "*"*10)
for i in range(1, 51):
    valorPao = preco * i
    print(f"{i} pães = R$ {valorPao:.2f}")
print("*"*10, "FIM DA TABELA", "*"*10)


qntd = int(input("Quantos pães você deseja levar: "))
total = qntd * preco
print(f"O valor da compra será de R$ {total:.2f}")

formaPagamento = int(input("Qual será a forma de pagamento? \nNOTA2 \nNOTA5 \nNOTA10 \nNOTA20 \nNOTA50 \n"))

# PRIMEIRA FORMA PENSADA UTILIZANDO NUMERO ESPECÍFICO
# if formaPagamento == 2:
#     troco = total - 2
#     if troco > 0:
#         print(f"VALOR INSUFICIENTE! FALTAM: R$ {troco:.2f}")
#     elif troco == 0:
#         print(f"Obrigado pela compra, volte sempre!") 
#     else:
#         print(f"O Valor de troco será R$ {troco * -1:.2f}")
# elif formaPagamento == 5:
#     troco = total - 5
#     if troco > 0:
#         print(f"VALOR INSUFICIENTE! FALTAM: R$ {troco:.2f}")
#     elif troco == 0:
#         print(f"Obrigado pela compra, volte sempre!") 
#     else:
#         print(f"O Valor de troco será R$ {troco * -1:.2f}")
# elif formaPagamento == 10:
#     troco = total - 10
#     if troco > 0:
#         print(f"VALOR INSUFICIENTE! FALTAM: R$ {troco:.2f}")
#     elif troco == 0:
#         print(f"Obrigado pela compra, volte sempre!") 
#     else:
#         print(f"O Valor de troco será R$ {troco * -1:.2f}")
# elif formaPagamento == 20:
#     troco = total - 20
#     if troco > 0:
#         print(f"VALOR INSUFICIENTE! FALTAM: R$ {troco:.2f}")
#     elif troco == 0:
#         print(f"Obrigado pela compra, volte sempre!") 
#     else:
#         print(f"O Valor de troco será R$ {troco * -1:.2f}")
# elif formaPagamento == 50:
#     troco = total - 50
#     if troco > 0:
#         print(f"VALOR INSUFICIENTE! FALTAM: R$ {troco:.2f}")
#     elif troco == 0:
#         print(f"Obrigado pela compra, volte sempre!") 
#     else:
#         print(f"O Valor de troco será R$ {troco * -1:.2f}")

troco = formaPagamento - total
falta = total - formaPagamento

if formaPagamento > total:
    print(f"O Valor de troco será R$ {troco:.2f}")
elif total > formaPagamento:
    print(f"VALOR INSUFICIENTE! FALTAM: R$ {falta:.2f}")
else:
    print(f"Obrigado pela compra, volte sempre!") 


print("*"*10, "FIM DO DESAFIO", "*"*10)