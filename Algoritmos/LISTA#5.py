# PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ
# Curso: Ciência da Computação
# Disciplina: Algoritmos
# Aluno: Victor de Souza Maia

""" 1. Desenvolva um programa que leia uma matriz quadrada de números inteiros de dimensão (4×4), e então coloque em um outro
vetor de 4 posições o maior valor encontrado na coluna da matriz cujo índice é o mesmo do vetor, ou seja, o maior valor da
coluna zero da matriz na posição zero do vetor e assim por diante. Mostre então a matriz, o vetor e a média aritmética do
vetor """

def matriz() -> None:
    """
    Lê uma matriz quadrada de números inteiros de dimensão (4×4), e então coloca em um outro vetor de 4 posições o maior valor
    encontrado na coluna da matriz cujo índice é o mesmo do vetor, ou seja, o maior valor da coluna zero da matriz na posição zero
    do vetor e assim por diante. Mostra então a matriz, o vetor e a média aritmética do vetor.
    """
    matriz = []
    vetor = []
    print("Digite os valores da matriz 4x4: ")
    for i in range(4):
        matriz.append([])
        for j in range(4):
            matriz[i].append(int(input(f"Digite o valor da posição ({i+1}, {j+1}): ")))

    for i in range(4):
        maior = matriz[0][i]
        for j in range(4):
            if matriz[j][i] > maior:
                maior = matriz[j][i]
        vetor.append(maior)
        
    print("Matriz: ")
    for i in range(4):
        for j in range(4):
            print(matriz[i][j], end=" ")
        print()

    print("Vetor: ")

    for i in range(4):
        print(vetor[i], end=" ")
    print()
    
    media = sum(vetor) / 4
    print(f"Média aritmética do vetor: {media}")
    
# Chamada da função
# matriz()

""" 2. Implemente um programa que permita multiplicar uma matriz de ordem (3×3) de números inteiros fornecida pelo usuário por
um número também fornecido pelo usuário."""

def multiplicar_matriz() -> None:
    """ Multiplica uma matriz de ordem (3×3) de números inteiros fornecida pelo usuário por um número também fornecido pelo usuário. """
   
    matriz = []
    print("Digite os valores da matriz 3x3: ")
    for i in range(3):
        matriz.append([])
        for j in range(3):
            matriz[i].append(int(input(f"Digite o valor da posição ({i+1}, {j+1}): ")))
    
    numero = int(input("Digite um número: "))
    
    for i in range(3):
        for j in range(3):
            matriz[i][j] *= numero
    
    print("Matriz multiplicada: ")
    for i in range(3):
        for j in range(3):
            print(matriz[i][j], end=" ")
        print()

# Chamada da função
# multiplicar_matriz()

""" 3. Elabore um programa que preencha uma matriz quadrada (4x4) de números inteiros, sorteados dentro do intervalo 100 a 999,
    garantindo que não haverá nenhuma repetição (os 16 números devem ser únicos). Encontre então o valor do menor elemento
da linha em que se encontra o maior elemento da matriz. Mostre a matriz e os dois valores encontrados.
"""
def matriz_4_sorteada() -> None:
    """
    Preenche uma matriz quadrada (4x4) de números inteiros, sorteados dentro do intervalo 100 a 999, garantindo que não haverá REPETIÇÃO.
    Encontra então o valor do menor elemento da linha em que se encontra o maior elemento da matriz. Mostra a matriz e os dois valores encontr
    """
    import random
    matriz = []
    numeros = []
    for i in range(100, 1000):
        numeros.append(i)
    random.shuffle(numeros)
    k = 0
    for i in range(4):
        matriz.append([])
        for j in range(4):
            matriz[i].append(numeros[k])
            k += 1
    print("Matriz: ")
    for i in range(4):
        for j in range(4):
            print(matriz[i][j], end=" ")
        print()
  
    maior = matriz[0][0]
    
    for i in range(4):
        for j in range(4):
            if matriz[i][j] > maior:
                maior = matriz[i][j]
                linha = i
    menor = matriz[linha][0]
    for i in range(4):
        if matriz[linha][i] < menor:
            menor = matriz[linha][i]

    print(f"O maior elemento da matriz é: {maior}")
    print(f"O menor elemento da linha em que se encontra o maior elemento da matriz é: {menor}")
    
# Chamada da função
# matriz_4_sorteada()


""" 4. Escreva um programa que preencha uma matriz quadrada de números inteiros de dimensão (5×5) com valores inteiros (dentro
do intervalo 10 a 99).
"""
def matriz_5():
    """
    Preenche e retorna uma matriz quadrada de números inteiros de dimensão (5×5) com valores inteiros (dentro do intervalo 10 a 99).
    """
    matriz = []
    for i in range(5):
        matriz.append([])
        for j in range(5):
            while True:
                valor = int(input(f"Digite o valor da posição ({i+1}, {j+1}) (entre 10 e 99): "))
                if 10 <= valor <= 99:
                    matriz[i].append(valor)
                    break
                else:
                    print("Valor inválido. Tente novamente.")
    print("Matriz original: ")
    for i in range(5):
        for j in range(5):
            print(matriz[i][j], end=" ")
        print()
    return matriz

# Para cada uma das matrizes a seguir, mostre a matriz original e mostre a matriz de acordo com somente os valores pedidos.
#4a) linhas centrais
def matriz_5_linhas_centrais():
    """
    Mostra a matriz original e a matriz de acordo com somente os valores das linhas centrais.
    """
    mat = matriz_5()
    print("Matriz com linhas centrais: ")
    for i in range(5):
        for j in range(5):
            if i == 2 or j == 2:
                print(mat[i][j], end=" ")
            else:
                print("  ", end=" ")
        print()
# Chamada da função
# matriz_5_linhas_centrais()

# 4b) Bordas externas   
def matriz_5_bordas():
    """
    Mostra a matriz original e a matriz de acordo com somente os valores das bordas externas.
    """
    mat = matriz_5()
    print("Matriz com bordas externas: ")
    for i in range(5):
        for j in range(5):
            if i == 0 or i == 4 or j == 0 or j == 4:
                print(mat[i][j], end=" ")
            else:
                print("  ", end=" ")
        print()
# Chamada da função
# matriz_5_bordas()

# 4c) Imprimir diagonais [a12, a23, a34, a45] e [a21, a32, a43, a54]
def matriz_5_diagonais():
    """
    Mostra a matriz original e a matriz de acordo com somente os valores das diagonais [a12, a23, a34, a45] e [a21, a32, a43, a54].
    """
    mat = matriz_5()
    print("Matriz com diagonais: ")
    for i in range(5):
        for j in range(5):
            if (i == j + 1) or (i == j - 1):
                print(mat[i][j], end=" ")
            else:
                print("  ", end=" ")
        print()
# Chamada da função
# matriz_5_diagonais()

# 4d)
def matriz_5_xadrez():
    """
    Mostra a matriz original em formato de um tabuleiro de xadrez, apenas com os valores 1 + j impares.
    """
    mat = matriz_5()
    print("Matriz com x: ")
    for i in range(5):
        for j in range(5):
            if ((i + j) % 2 != 0):
                print(mat[i][j], end=" ")
            else:
                print("  ", end=" ")
        print()
# Chamada da função
# matriz_5_xadrez()

# 6. Montar uma tabela contendo as distâncias entre as cidades abaixo:
# Curitiba a Florianópolis: 310 km
# Curitiba a Porto Alegre: 716 km
# Curitiba a São Paulo: 408 km
# Curitiba a Rio de Janeiro: 852 km
# Florianópolis a Porto Alegre: 470 km
# Florianópolis a São Paulo: 705 km
# Florianópolis a Rio de Janeiro: 1144 km
# Porto Alegre a São Paulo: 1119 km
# Porto Alegre a Rio de Janeiro: 1553 km
# São Paulo a Rio de Janeiro: 429 km
# Construa um programa que inicialize uma matriz contendo as distências apresentadas na tabela acima. O programa deve
# informar ao usuário o tempo necessário para percorrer a distância entre duas cidades fornecidas.

def matriz_distancias():
    """
    Monta uma tabela contendo as distâncias entre as cidades e informa o tempo necessário para percorrer a distância entre duas cidades fornecidas.
    """
    cidades = ["Curitiba", "Florianópolis", "Porto Alegre", "São Paulo", "Rio de Janeiro"]
    distancias = [
        [0, 310, 716, 408, 852],
        [310, 0, 470, 705, 1144],
        [716, 470, 0, 1119, 1553],
        [408, 705, 1119, 0, 429],
        [852, 1144, 1553, 429, 0]
    ]
    print("Tabela de distâncias entre as cidades: ")
    print(" " * 15, end="")
    for cidade in cidades:
        print(f"{cidade:>15}", end="")
    print()
    for i in range(len(cidades)):
        print(f"{cidades[i]:<15}", end="")
        for j in range(len(cidades)):
            print(f"{distancias[i][j]:>15}", end="")
        print()
    cidade1 = int(input("Digite o número da primeira cidade (0 a 4): "))
    cidade2 = int(input("Digite o número da segunda cidade (0 a 4): ")) 
    tempo = distancias[cidade1][cidade2] / 80
    print(f"O tempo necessário para percorrer a distância entre {cidades[cidade1]} e {cidades[cidade2]} é de {tempo:.2f} horas.")
# Chamada da função
# matriz_distancias()

