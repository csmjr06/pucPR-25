# PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ
# Curso: Ciência da Computação
# Disciplina: Algoritmos
# Aluno: Victor de Souza Maia

# 1. Escreva um algoritmo que solicite um número inteiro ao usuário, calcule e exiba seu antecessor e sucessor.

def exibir_antecessor_sucessor() -> None:
    """
    Solicita um número inteiro ao usuário, calcula e exibe seu antecessor e sucessor.
    
    Retorno:
    None: A função apenas imprime os resultados na tela.
    """
    numero = int(input("Digite um número inteiro: "))
    antecessor = numero - 1
    sucessor = numero + 1
    print(f"O antecessor de {numero} é {antecessor} e o sucessor é {sucessor}.")

# Chamada da função
exibir_antecessor_sucessor()

# 2. Faça um algoritmo que leia o ano de nascimento de uma pessoa e calcule a idade que completará em 2025.

def calcular_idade_2025() -> None:
    """
    Lê o ano de nascimento de uma pessoa e calcula a idade que completará em 2025.
    """
    
    nasceu_em = int(input("Digite o ano de nascimento: "))
    idade_em_2025 = 2025 - nasceu_em
    print(f"Em 2025, você terá {idade_em_2025} anos.")
    
# Chamada da função
calcular_idade_2025()

# 3. Faça um algoritmo que receba o salário de um profissional e calcule quantos salário mínimos ele recebe.

def salarios_minimos() -> None:
    """
    Lê o salário de uma pessoa e calcula quantos salários mínimos ela recebe.
    """
    
    salario = float(input("Digite o salário da pessoa: "))
    salario_minimo = 1100
    qtd_salarios_minimos = salario / salario_minimo
    print(f"O salário informado equivale a {qtd_salarios_minimos:.2f} salários mínimos.")

# Chamada da função
salarios_minimos()

# 4. Faça um algoritmo que recebe o valor de um produto e calcule os seguintes valores: (1) a vista com 5% de desconto; (2) o valor da parcela em 2x; (3) o valor da parcela em 3x com acréscimo de 5% no valor total.

def formas_de_pagamento () -> None:
    """
    Lê o valor de uma compra e exibe as formas de pagamento disponíveis.
    """
    
    valor_compra = float(input("Digite o valor do produto: "))
    print(f"Formas de pagamento para uma compra de R${valor_compra:.2f}:")
    print("1) À vista no dinheiro ou cheque, com 5% de desconto: R${valor_compra * 0.95:.2f}")
    print("2) Em 2x com parcelas iguais: R${valor_compra / 2:.2f}")
    print("3) Em 3x com juros de 5% e parcelas iguais a: R${(valor_compra * 1.05) / 3:.2f}")
    
# Chamada da função
formas_de_pagamento()

# 5. Faça um algoritmo que calcule o consumo médio de um automóvel (medido em km/l), solicitando como entrada a distância total percorrida (KM) e o volume de combustível consumido para percorrê-la (litros).

def consumo_medio() -> None:
    """
    Lê a distância percorrida por um carro e a quantidade de litros de combustível consumidos e calcula o consumo médio.
    """
    
    distancia = float(input("Digite a distância percorrida (em km): "))
    litros = float(input("Digite a quantidade de litros de combustível consumidos: "))
    consumo = distancia / litros
    print(f"O consumo médio do carro foi de {consumo:.2f} km/l.")
    
# Chamada da função
consumo_medio()

# 6.

def quantidade_de_tinta() -> None: 
    """
    Calcula a quantidade de tinta necessária para pintar um tanque cilindico
    """

    custo_lata = 50.00
    volume_lata = 5.00
    rendimento_lata = 3.00
    raio = float(input("Digite o raio do tanque cilindrico: "))
    altura = float(input("Digite a altura do tanque cilindrico: "))
    volume = 3.14 * raio ** 2 * altura
    qtd_latas = volume / rendimento_lata
    preco = qtd_latas * custo_lata
    print(f"Para pintar o tanque cilindrico, você precisará de {qtd_latas:.2f} latas de tinta, totalizando R${preco:.2f}.")
    
# Chamada da função
quantidade_de_tinta()
