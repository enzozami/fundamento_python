import os
os.system("cls")

#FUNÇÕES
#print() input() append() pop() clear() len()
#FUNÇÃO SERVE PARA EXECUTAR UM TRECHO DE CÓDIGO (SCRIPT)

#funcao sem parametro
# def primeiraFuncao():
#     print("Executando minha primeira função")

# primeiraFuncao()

#funcao com parametro
# def segundaFuncao(a, b):
#     print(a + b)

# segundaFuncao(20, 30)

#escopo de funcao 
# x = 100 
# def escopo():
#     global x
#     x = 50
# escopo()
# print(x)
# se nn colocar global, o x dentro do escopo vai valer 50 apenas dentro da função, se colocar global vai valer pro codigo completo


# ATIVIDADE 1
# print("*"*15, "ATIVIDADE 1", "*"*15)

# def calc(a, b, c):
#     soma = a + b + c
#     multiplicacao = a * b * c
#     divisao = a / b / c
#     subtracao = a - b - c
#     print(f"A soma de {a} + {b} + {c} = {soma:.2f}")
#     print(f"A multiplicacao de {a} * {b} * {c} = {multiplicacao:.2f}")
#     print(f"A divisão de {a} / {b} / {c} = {divisao:.2f}")
#     print(f"A subtração de {a} - {b} - {c} = {subtracao:.2f}")

# calc(
#     float(input("Digite o primeiro valor: ")),
#     float(input("Digite o segundo valor: ")),
#     float(input("Digite o terceiro valor: "))
#     )


# ATIVIDADE 2
# print("*"*15, "ATIVIDADE 2", "*"*15)

# conversao = 5.75

# def dolar_real():
#     real = dolar * conversao
#     print(f"O valor de $ {dolar:.2f} em reais fica: R$ {real:.2f}")

# def real_dolar():
#     dolar = real / conversao 
#     print(f"O valor de R$ {real:.2f} em dolares fica: $ {dolar:.2f}")

# print("DIGITE 1 - Converter dólar em real \nDIGITE 2 - Converter real em dólar \n DIGITE 3 - Sair do programa")
# numero = 0
# while numero != 3:
#     numero = int(input("Digite um número: "))
#     if numero == 1:
#         dolar = float(input("Digite o valor em DOLAR para converter: $ "))
#         dolar_real()
#     elif numero == 2:
#         real = float(input("Digite o valor em DOLAR para converter: R$ "))
#         real_dolar()
#     elif numero != 3:
#         print("Opção Inválida!")
# else: 
#     print("Sair do programa")



# ATIVIDADE 3
# print("*"*15, "ATIVIDADE 3", "*"*15)

# valorDeposito = 0
# valorSaque = 0
# def deposito():
#     global valorDeposito
#     lista.append(f"Depósito: R$ {valorDeposito:.2f}")

# def saque():
#     global valorSaque
#     lista.append(f"Saque: R$ {valorSaque:.2f}")

# def extrato():
#     valorExtrato = valorDeposito - valorSaque
#     print("*"*41)
#     print(f"Seu Saldo: R$ {valorExtrato:.2f}") 
#     print("*"*41)
#     print("*"*15, "HISTÓRICO", "*"*15)
#     for i in range(len(lista)):
#         print(lista[i])
#     print("*"*41)

# print("DIGITE 1 - Realizar Deposito \nDIGITE 2 - Realizar Saque \nDIGITE 3 - Emitir Extrato \nDIGITE 4 - Sair do Programa")
# lista = []
# aux = 0 
# while aux != 4:
#     aux = float(input("Digite um número: "))
#     if aux == 1:
#         valorDeposito = float(input("Insira o valor que deseja realizar Deposito: R$ "))
#         deposito()
#     elif aux == 2:
#         valorSaque = float(input("Insira o valor que deseja realizar Saque: R$ "))
#         saque()
#     elif aux == 3:
#         extrato()
#     elif aux != 4:
#         print("Opção Inválida")
# else:
#     print("Saiu do programa")


# OUTRA SOLUÇÃO
valorDeposito = 0
valorSaque = 0
def deposito():
    global valorDeposito
    valorDeposito = float(input("Insira o valor que deseja realizar Deposito: R$ "))
    lista.append(f"Depósito: R$ {valorDeposito:.2f}")

def saque():
    global valorSaque
    valorSaque = float(input("Insira o valor que deseja realizar Saque: R$ "))
    lista.append(f"Saque: R$ {valorSaque:.2f}")

def extrato():
    valorExtrato = valorDeposito - valorSaque
    print("*"*41)
    print(f"Seu Saldo: R$ {valorExtrato:.2f}") 
    print("*"*41)
    print("*"*15, "HISTÓRICO", "*"*15)
    for i in range(len(lista)):
        print(lista[i])
    print("*"*41)

print("DIGITE 1 - Realizar Deposito \nDIGITE 2 - Realizar Saque \nDIGITE 3 - Emitir Extrato \nDIGITE 4 - Sair do Programa")
lista = []
aux = 0 
while aux != 4:
    aux = float(input("Digite um número: "))
    if aux == 1:
        deposito()
    elif aux == 2:
        saque()
    elif aux == 3:
        extrato()
    elif aux != 4:
        print("Opção Inválida")
else:
    print("Saiu do programa")
