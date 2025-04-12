# PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ
# Curso: Ciência da Computação
# Disciplina: Algoritmos
# Aluno: Victor de Souza Maia

# 1. Imprima os números de 1 até 99, com incremento de 2
def imprimir_numeros() -> None:
    """
    Imprime os números de 1 a 99 com incremento de 2.
    """
    
    for i in range(1, 100, 2):
        print(i)
        
# Chamada da função
imprimir_numeros()

#2. Imprima os números de 50 até 0 com decremento de 5.
def imprimir_numeros_decremento() -> None:
    """
    Imprime os números de 50 a 0 com decremento de 5.
    """
    
    for i in range(50, -1, -5):
        print(i)
        
# Chamada da função
imprimir_numeros_decremento()

#3. Imprima os números de -100 até 100, com incremento de 10.

def imprimir_numeros_negativos() -> None:
    """
    Imprime os números de -100 a 100 com incremento de 10.
    """
    
    for i in range(-100, 101, 10):
        print(i)
        
# Chamada da função
imprimir_numeros_negativos()

#4. Imprima os números múltiplos de 4 existentes no intervalo aberto de 1 a 100.

def multiplos_de_4() -> None:
    """
    Imprime os múltiplos de 4 entre 1 e 100.
    """
    
    for i in range(1, 101):
        if i % 4 == 0:
            print(i)
            
# Chamada da função
multiplos_de_4()

# 5. 

def imprimir_impares() -> None:
    """
    Imprime os números ímpares
    """
    n = int(input("Digite um número: "))
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(i)
            
# Chamada da função
imprimir_impares()
