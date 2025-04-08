# Imprime a tabela de conversão de metros para milhas
print("Tabela de Conversão de Metros para Milhas")
print("Km\tMetros\t\tMilhas")
for km in range(20, 170, 10):
    metros = km * 1000
    milhas = metros / 1609.344
    print(f"{km}\t{metros}\t\t{milhas:.4f}")
    
# Função que recebe temperatura em Celsius e retorna em Fahrenheit
def celsius_para_fahrenheit(celsius: float) -> float:
    """
    Converte uma temperatura de Celsius para Fahrenheit.
    """
    
    return (celsius * 9/5) + 32 
    
# Teste da função
temperatura_celsius = float(input("Digite a temperatura em Celsius: "))
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius}°C equivalem a {temperatura_fahrenheit:.2f}°F.")

# Escreva a função maximo que recebe 2 números inteiros como parâmetro e devolve o maior deles.

def maximo(num1: int, num2: int) -> int:
    """
    Recebe dois números inteiros e retorna o maior deles.
    """
    
    if num1 > num2:
        return num1
    else:
        return num2
    
# Teste da função
numero1 = int(input("Digite o primeiro número: "))  
numero2 = int(input("Digite o segundo número: "))
maior = maximo(numero1, numero2)    
print(f"O maior número é {maior}.")

# Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função

def maior_primo(numero: int) -> int:
    """
    Recebe um número inteiro e retorna o maior número primo menor ou igual a ele.
    """
    
    def eh_primo(num: int) -> bool:
        """
        Verifica se um número é primo.
        """
        
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    
    for i in range(numero, 1, -1):
        if eh_primo(i):
            return i
        
        
# Teste da função
numero = int(input("Digite um número inteiro maior ou igual a 2: "))
primo = maior_primo(numero) 
print(f"O maior número primo menor ou igual a {numero} é {primo}.")

# Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.

def vogal(letra: str) -> bool:
    """
    Recebe um caractere e retorna True se for uma vogal e False se for uma consoante.
    """
    
    vogais = "aeiouAEIOU"
    return letra in vogais

# Teste da função
caractere = input("Digite um caractere: ")
if vogal(caractere):
    print(f"{caractere} é uma vogal.")
else:
    print(f"{caractere} é uma consoante.")

# Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros correspondentes à largura e à altura de um retângulo, respectivamente. O programa deve imprimir uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída.

def desenha_retangulo(largura: int, altura: int) -> None:
    """
    Desenha um retângulo com a largura e altura informadas.
    """
    
    for i in range(altura):
        print("#" * largura)    
        
# Teste da função
largura = int(input("Digite a largura do retângulo: "))
altura = int(input("Digite a altura do retângulo: "))
desenha_retangulo(largura, altura)
 
 #Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.
 
def desenha_retangulo_vazio(largura: int, altura: int) -> None:
    """
    Desenha um retângulo vazio com a largura e altura informadas.
    """
    
    for i in range(altura):
        if i == 0 or i == altura - 1:
            print("#" * largura)
        else:
            print("#" + " " * (largura - 2) + "#")
            
# Teste da função
largura = int(input("Digite a largura do retângulo: "))
altura = int(input("Digite a altura do retângulo: "))
desenha_retangulo_vazio(largura, altura)
        
         