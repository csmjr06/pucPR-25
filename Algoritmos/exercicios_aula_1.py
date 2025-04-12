# PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ
# Curso: Ciência da Computação
# Disciplina: Algoritmos
# Aluno: Victor de Souza Maia

# 1) Escreva um algoritmo em Python para calcular a idade de alguém, sabendo-se seu ano de nascimento.

# 2) Escreva um algoritmo em Python para calcular o valor, em reais, que deve ser pago por um cliente de uma locadora de carros. Sabe-se que:
# • O valor de locação de cada carro é 100,00 reais;
# • O cliente pode locar um único carro por vários dias.

# 3) Leia do teclado a temperatura em Celsius e imprima o equivalente emFahrenheit.
#Fórmula: (X °C × 9/5) + 32

# 4) Escrever um algoritmo para calcular a média de 4 notas.
# 5) Calcular sua idade em meses

def calcular_idade() -> None:
    """
    Lê o ano de nascimento de uma pessoa e calcula a idade.
    """
    
    nasceu_em = int(input("Digite o ano de nascimento: "))
    idade = 2021 - nasceu_em
    print(f"Você tem {idade} anos.")

# Chamada da função
calcular_idade()    

def calcular_valor_locacao() -> None:    
    """
    Calcula o valor a ser pago por um cliente de uma locadora de carros.
    """
    
    dias = int(input("Digite a quantidade de dias que o carro foi locado: "))
    valor_total = dias * 100
    print(f"O valor total a ser pago é de R${valor_total:.2f}.")
    
# Chamada da função
calcular_valor_locacao()

def converter_celsius_para_fahrenheit() -> None:
    """
    Lê a temperatura em Celsius e imprime o equivalente em Fahrenheit.
    """
    
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C equivalem a {fahrenheit:.2f}°F.")
    
# Chamada da função
converter_celsius_para_fahrenheit()

def calcular_media_notas() -> None:
    """
    Calcula a média de 4 notas.
    """
            
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print(f"A média das notas é {media:.2f}.")
    
# Chamada da função
calcular_media_notas()

def calcular_idade_em_meses() -> None:
    """
    Calcula a idade em meses.
    """
    
    idade = int(input("Digite sua idade: "))
    meses = idade * 12
    print(f"Você tem {meses} meses de idade.")

# Chamada da função
calcular_idade_em_meses()
