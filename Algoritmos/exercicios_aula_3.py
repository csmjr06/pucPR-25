# PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ
# Curso: Ciência da Computação
# Disciplina: Algoritmos
# Aluno: Victor de Souza Maia

# Exercícios de Fixação

# 1) Escreva um algoritmo que dado o peso de um boxeador, informea categoria a qual ele pertence, seguindo a tabela abaixo:
# Categoria Peso (Kg)
# Palha Menor que 50 Kg
# Pluma 50 - 59,99
# Leve 60 - 75,99
# Pesado 76 - 87,99
# Super Pesado Maior que 88 Kg

def categoria_boxeador() -> None:
    """
    Lê o peso de um boxeador e exibe sua categoria.
    """
    
    peso = float(input("Digite o peso do boxeador: "))
    
    if peso < 50:
        print("Palha")
    elif peso < 59.99:
        print("Pluma")
    elif peso < 75.99:
        print("Leve")
    elif peso < 87.99:
        print("Pesado")
    else:
        print("Superpesado")
        
# Chamada da função
categoria_boxeador()

# 2) Escreva um programa que recebe como entrada três números e os exibe ordenado

def ordena_numeros() -> None:
    """
    Lê 3 números inteiros e os exibe em ordem crescente.
    """
    
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    
    if num1 <= num2 and num1 <= num3:
        menor = num1
        if num2 <= num3:
            meio = num2
            maior = num3
        else:
            meio = num3
            maior = num2
    elif num2 <= num1 and num2 <= num3:
        menor = num2
        if num1 <= num3:
            meio = num1
            maior = num3
        else:
            meio = num3
            maior = num1
    else:
        menor = num3
        if num1 <= num2:
            meio = num1
            maior = num2
        else:
            meio = num2
            maior = num1
            
    print(f"Os números em ordem crescente são: {menor}, {meio}, {maior}.")
    
# Chamada da função
ordena_numeros()

# 3) Escreva um programa que recebe como entrada uma nota e a presença doaluno. Posteriormente exibe uma mensagem caso o aluno possua presença maior
# que 70% e o seu conceito. Caso contrário, o estudante está reprovado.
# Conceito Nota
# A Nota maior que 9
# B Nota maior que 8
# C Nota maior que 7
# D Nota maior que 6
# E Nota maior que 4
# F Nota menor ou igual a 4

def nota_presenca() -> None:
    """
    Lê a nota e a porcentagem de presenças de um aluno e informa seu conceito.
    """
    
    nota = float(input("Digite a nota do aluno: "))
    presencas = float(input("Digite a porcentagem de precsenças: "))
    
    if nota > 9 and presencas >= 70:
        print("Aprovado com conceito A")
    elif nota > 8 and presencas >= 70:
        print("Aprovado com conceito B")
    elif nota > 7 and presencas >= 70:
        print("Aprovado com conceito C")
    elif nota > 6 and presencas >= 70:
        print("Aprovado com conceito D")
    elif nota > 4 and presencas >= 70:
        print("Aprovado com conceito E")
    elif nota <= 4 and presencas >= 70:
        print("Aprovado com conceito F")
    else:
        print("Reprovado por falta")
        
# Chamada da função
nota_presenca()

# 4) 

def horas_de_funcionamento() -> None:
    """
    Lê a hora atual e informa se a PUCPR está em horário de funcionamento.
    """
    
    hora_atual = int(input("Digite a hora atual: "))
    minutos = int(input("Digite os minutos atuais: "))
    hora_atual += minutos / 60
    hora_abertura = 7.5
    hora_fechamento = 23.17
    
    if hora_abertura <= hora_atual or hora_fechamento >= hora_atual:
        print("Nesse horário, a PUC PR não está em funcionamento.")
    else:
        print("Nesse horário, a PUC PR não está em funcionamento.")
        
# Chamada da função
horas_de_funcionamento()