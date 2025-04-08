# 1. Faça um algoritmo que imprima a tabuada de 1 a 10.
def tabuada():
    """
    Função que imprime a tabuada de 1 a 10.
    """
    for i in range(1, 11):
        print(f"Tabuada do {i}:")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print()
    
# Chamada da função
tabuada()

#2. Construa a tabela de multiplicação de 1 a 10 utilizando apenas um laço de repetição.
def tabuada2():
    """
    Função que imprime a tabuada de 1 a 10 usando apenas um laço de repetição.
    """
    for i in range(1, 101):
        if i % 10 == 0:
            print(f"Tabuada do {i // 10}:")
            for j in range(1, 11):
                print(f"{i // 10} x {j} = {(i // 10) * j}")
            print()
    
# Chamada da função
tabuada2()

#3. Leia três números do teclado e verificar se o primeiro é maior que a soma dos outros dois
def tamanho_numeros():
    """
    Lê três números do teclado e verifica se o primeiro é maior que a soma dos outros dois.
    """
    
    A = int(input("Digite um número: "))
    B = int(input("Digite o segundo número: "))
    C = int(input("Digite o terceiro número: "))
    
    somaBC = B + C
    
    if A > somaBC:
        print(f"O número {A} é maior que a soma de {B} e {C}.")
    else:
        print(f"A soma de {B} e {C} é maior que o número {A}.")

# Chamada da função
tamanho_numeros()

"""4.  Leia dois valores reais do teclado, calcular e imprimir na tela:
a) A soma destes valores b) O produto deles c) O quociente entre eles
"""
def operacaoNumeros():
    """
    Função que lê dois números do teclado e exibe a soma, subtração, multiplicação e divisão entre eles.
    """
    
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    
    soma = numero1 + numero2
    subtracao = numero1 - numero2
    multiplicacao = numero1 * numero2
    divisao = numero1 / numero2
    
    print(f"Soma: {soma}")
    print(f"Subtração: {subtracao}")
    print(f"Multiplicação: {multiplicacao}")
    print(f"Divisão: {divisao}")
    
#5. Ler 4 números inteiros e calcular a soma dos que forem par
    
def soma_pares():
    """
    Função que lê 4 números do teclado e exibe a soma dos números pares.
    """
    soma = 0
    for i in range(1, 5):
        n = int(input(f"Digite o {i}º número: "))
        if n % 2 == 0:
            soma += n
    print(f"A soma dos números pares é: {soma}")
    
#chama a função
soma_pares()
 
#6. Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos. Exemplo: 120 é
# triangular, pois 4 * 5 * 6 = 120. Dado um inteiro não-negativo n, verificar se n é triangular

def natural_triangular():
    """
    
    """
    while True:
        n = int(input("Digite um número não-negativo: "))
        if n >= 0:
            break
        else:
            print("Número inválido. Tente novamente.")
    i = 1
    while True:
        if i * (i + 1) * (i + 2) == n:
            print(f"{n} é um número triangular.")
            break
        elif i * (i + 1) * (i + 2) > n:
            print(f"{n} não é um número triangular.")
            break
        i += 1

# Chamada da função
natural_triangular()

#7. A Amplitude amostral é uma médida de dispersão, ela é calculada como a diferença entre o valor máximo e o valor mínimo
# de uma amostra. Elabore um programa que leia um vetor de 10 posições inteiras e então mostre o valor máximo, o valor
# mínimo e a amplitude amostral do conjunto fornecido

def amplitudeAmostral():
    """
    Função que lê 10 números do teclado e calcula a amplitude amostral.
    """
    numeros = []
    for i in range(10):
        numero = int(input(f"Digite o {i+1}º número: "))
        numeros.append(numero)
        
    maior = max(numeros)
    menor = min(numeros)
    amplitude = maior - menor
    
    print(f"A amplitude amostral é: {amplitude}")
    
# Chamada da função
amplitudeAmostral()

"""8. Elabore um programa que leia um vetor de 10 posições inteiras. Depois, solicite para o usuário um número que ele gostaria de
pesquisar neste vetor, caso o número exista no vetor, mostre em qual(is) posição(ões) ele foi encontrado e quantas ocorrências
foram detectadas
""" 

def buscaNumero():
    """
    Função que lê 10 números do teclado e verifica se um número está na lista e impreme a posição dele.
    Se não estiver, imprime que o número não está na lista.
    """
    numeros = []
    for i in range(10):
        numero = int(input(f"Digite o {i+1}º número: "))
        numeros.append(numero)
        
    busca = int(input("Digite o número a ser buscado: "))
    
    if busca in numeros:
        print(f"O número {busca} está na posicão {numeros.index()} da lista.")
    else:
        print(f"O número {busca} não está na lista.")
    
# Chamada da função
buscaNumero()

#9. Desenvolva um programa que leia 10 números inteiros e armazene-os em um vetor chamado vLido. Depois, crie dois outros
# vetores: vPares, contendo somente os números pares de vLido, e vImpares contendo somente os números ímpares de vLido.
# Os vetores vPares e vLido não deverão conter zeros. Mostre então os três vetores.

def pares_impares():
    """
    Função que lê 10 números do teclado e separa pares e ímpares em outras duas listas e imprime.
    """
    vPares = []
    vImpares = []
    for i in range(10):
        numero = int(input(f"Digite o {i+1}º número: "))
        if numero % 2 == 0:
            vPares.append(numero)
        else:
            vImpares.append(numero)
    # Imprime os números pares e ímpares
    print(f"Números pares: {vPares}")
    print(f"Números ímpares: {vImpares}")
# Chamada da função
pares_impares()

"""
10. Escreva um programa que leia um vetor de números inteiros de 10 posições, aceitando apenas valores positivos. Modifique
então o vetor de forma que, tenhamos primeiro todos os números pares, depois, os números impares. Mostre o vetor antes de
depois da modificação.
"""
def positivosParesImpares():
    """
    Função que lê 10 números do teclado e guarda somente positivos e ordena primeiro os pares e depois os ímpares.
    """
    pares = []
    impares = []
    for i in range(10):
        numero = int(input(f"Digite o {i+1}º número: "))
        if numero > 0:
            if numero % 2 == 0:
                pares.append(numero)
            else:
                impares.append(numero)
    vFinal = pares + impares
    print(f"O vetor final é: {vFinal}")
# Chamada da função
positivosParesImpares()

#11. Construa um programa que sugira uma aposta de Mega-Sena ou seja, um algoritmo que gera e mostra um conjunto de 6
# números aleatórios entre [1, 60] sem repetição. Em seguida, obtenha a aposta do usuário (sem repetição) e indique quantos acertos ele teve.

import random
def bilheteMegaSena():
    """
    Função que gera 6 números aleatórios e não repetidos entre 1 e 60 e imprime. O usuário entra com 6 números, separados por um espaço, e verifica auntos números acertou.
    """
    numeros = random.sample(range(1, 61), 6)
    aposta = []
    aposta = input("Digite os 6 números separados por espaço: ").split()
    aposta = [int(x) for x in aposta]   
    acertos = 0
    for i in range(6):
        if aposta[i] in numeros:
            acertos += 1
    print(f"Os números sorteados foram: {numeros}")
    print(f"Você acertou {acertos} números.")
    
# Chamada da função
bilheteMegaSena()


"""12. Desenvolva um programa que leia um vetor de 20 posições inteiras e o coloque em ordem crescente, utilizando a seguinte
estratégia de ordenação:
• selecione o elemento do vetor de 20 posições que apresenta o menor valor;
• troque este elemento pelo primeiro;
• repita estas operações, envolvendo agora apenas os 19 elementos restantes (trocando o de menor valor com a segunda
posição), depois os 18 elementos (trocando o de menor valor com a terceira posição), depois os 17, 16 e assim por diante,
até restar um único elemento, o maior deles
"""

def selecao_direta():
    """
    Colocar um vetor de 20 posições inteiras em ordem crescente, utilizando o método de seleção direta.
    """
    vetor = []
    for i in range(20):
        numero = int(input(f"Digite o {i+1}º número: "))
        vetor.append(numero)
    print(f"Vetor original: {vetor}")
    for i in range(len(vetor)):
        menor = i
        for j in range(i + 1, len(vetor)):
            if vetor[j] < vetor[menor]:
                menor = j
        vetor[i], vetor[menor] = vetor[menor], vetor[i]
    print(f"Vetor ordenado: {vetor}")
# Chamada da função
selecao_direta()

