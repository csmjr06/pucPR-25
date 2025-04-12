# PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ
# Curso: Ciência da Computação
# Disciplina: Algoritmos
# Aluno: Victor de Souza Maia

# Exercícios de Fixação - Aula 4

#1 Implemente um programa em Python para ler do teclado a nota de um aluno. Verifique se o valor lido é uma nota válida (maior que 7). Se não for, ler este valor até que a mesma seja válida.
def nota_valida():
    nota = -1
    while nota <7:
        nota = float(input("Digite a nota: "))

#2 Implemente um programa em Python para ler do teclado números. Caso o usuário forneça um numero igual a -1, o programa deve fornecer a média dos números e encerrar.
def media():
    soma = 0
    numero = 0
    numeros = 0
    while numero != -1:
        numeros += 1
        numero = float(input("Digite um numero: "))
        soma = (soma + numero)
    media = soma/(numeros-1)
    print(f"A média de numeros coletatos é: {media}")

#3  Implemente um programa em Python para imprimir na tela o somatório dos N primeiros números inteiros a partir do 1. Sendo N lido do teclado.
def somatorio():
    n = int(input("Digite um numero: "))
    soma = 0
    i = 1
    while i <= n:
        soma += i
        i += 1
    print(f"O somatório dos {n} primeiros números inteiros é: {soma}")
    
#4  Escreva um programa que recebe 10 números do teclado e exibe a quantidade de números pares e impares lidos.
def par_impar():
    pares = 0
    impares = 0
    i = 0
    while i < 10:
        numero = int(input("Digite um numero: "))
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
        i += 1
    print(f"Quantidade de numeros pares: {pares}")
    print(f"Quantidade de numeros impares: {impares}")

#5 Utilizando import time, use a função time.sleep(1) e construa um cronômetro. 
# (O cronometro não pode mostrar só segundos, deve mostrar minutos e horas).

import time
import os
def cronometro():
    segundos = 0
    minutos = 0
    horas = 0
    while True:
        print(f"{horas}h:{minutos}m:{segundos}s")
        time.sleep(1)
        segundos += 1
        if segundos == 60:
            minutos += 1
            segundos = 0
        if minutos == 60:
            horas += 1
            minutos = 0

cronometro()