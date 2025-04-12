import time

# 1. Faça um algoritmo que leia três valores que representam os três lados de
#    um triângulo e verifique se são válidos, determine se o triângulo é
#    equilátero, isósceles ou escaleno.


def triangulo() -> None:
    """
    Verifica se os lados informados formam um triângulo e, se sim, classifica
    o triângulo como equilátero, isósceles ou escaleno.
    """
    
    a = float(input("Digite o valor do lado A: "))
    b = float(input("Digite o valor do lado B: ")) 
    c = float(input("Digite o valor do lado C: "))
    
    if (a < b + c) and (b < a + c) and (c < a + b):
        if a == b == c:
            print("Triângulo equilátero.")
        elif a == b or a == c or b == c:
            print("Triângulo isósceles.")
        else:
            print("Triângulo escaleno.")
    else:
        print("Não é um triângulo.")    
        
# Chamada da função
triangulo()

# 2. Faça um algoritmo que leia o ano em que uma pessoa nasceu, imprima na
#    tela quantos anos, meses e dias essa pessoa ja viveu. Leve em
#    consideração o ano com 365 dias e o mês com 30 dias.
#    (Ex: 5 anos, 2 meses e 15 dias de vida)

def idade() -> None:
    """
    Calcula a idade de uma pessoa.
    """
    
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    ano_atual = time.localtime().tm_year
    idade = ano_atual - ano_nascimento
    print(f"Você tem {idade} anos.")
    meses = idade * 12
    print(f"Você tem {meses} meses de idade.")
    dias = idade * 365
    print(f"Você tem {dias} dias de idade.")
    
# Chamada da função
idade()

# 3. Francisco tem 1,50m e cresce 2 centímetros por ano, enquanto Sara tem
#    1,10m e cresce 3 centímetros por ano. Faça um algoritmo que calcule e
#    imprima na tela em quantos anos serão necessários para que Francisco seja
#    maior que Sara.

def calcular_anos() -> None:
    """
    Calcula quantos anos são necessários para que Francisco seja maior que Sara.
    """
    ano = 0
    while True:
        f = 1.50 + 0.02 * ano
        s = 1.10 + 0.03 * ano
        if f > s:
            break
        ano += 1
    print(f"Serão necessários {ano} anos para que Francisco seja maior que Sara.")
    
# Chamada da função
calcular_anos()

# 4 Faça um algoritmo que efetue o cálculo do salário líquido de um professor.
# As informações fornecidas serão: valor da hora aula, número de aulas
# lecionadas no mês e percentual de desconto do INSS. Imprima na tela o salário líquido final.

def salario_liquido_prof(horaAula, aulasMes, percDescINSS) -> None:
    """
    Calcula o salário líquido de um professor, fornecidos o valor da hora-aula, a quantidade de aulas dadas no mês e o percentual de desconto do INSS.  
    """
    salarioBruto = horaAula * aulasMes
    descontoINSS = salarioBruto * percDescINSS / 100
    salarioLiquido = salarioBruto - descontoINSS
    print(f"O salário líquido do professor é R${salarioLiquido:.2f}")
    
# Chamada da função
salario_liquido_prof(30, 40, 11)

# 5. O custo de um carro novo ao consumidor é a soma do custo de fábrica com
# a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica).
# Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%,
# escrever um algoritmo para ler o custo de fábrica de um carro, calcular e
# escrever o custo final ao consumidor.

def custo_carro() -> None:
    """
    Calcula o custo total de um carro ao consumidor.
    """
    
    custoFabrica = float(input("Digite o custo de fábrica do carro: "))
    distribuidor = custoFabrica * 0.28
    impostos = custoFabrica * 0.45
    custoConsumidor = custoFabrica + distribuidor + impostos
    print(f"O custo total do carro ao consumidor é R${custoConsumidor:.2f}")

# Chamada da função
custo_carro()

# 6. Uma revendedora de carros usados paga a seus funcionários vendedores 
# um salário fixo por mês, mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele efetuadas. 
# Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas vendas, 
# o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do vendedor.

def salaFinalVendedor() -> None:
    """
    Calcula o salário final de um vendedor.
    """
    
    salario_fixo = float(input("Digite o salário fixo do vendedor: "))
    valorPorCarro = float(input("Digite o valor que o vendedor recebe por carro vendido: "))
    carros = float(input("Digite o numero de carros vendidos pelo funcionário no mês: "))
    vendas = float(input("Digite o valor total das vendas no mês: "))

    salarioFinal = salario_fixo + (valorPorCarro * carros) + (vendas * 0.05)
    print(f"O salário final do vendedor é R${salarioFinal:.2f}")
    
# Chamada da função
salaFinalVendedor()

# 7. Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. 
# Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). 
# Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', 
# senão escrever a mensagem 'Saldo Negativo'.

def saldoConta() -> None:
    """
    Calcula o saldo da conta de um cliente e verifica se está positivo ou negativo.
    """
    
    numeroConta = int(input("Digite o número da conta: "))
    saldo = float(input("Digite o saldo da conta: "))
    debito = float(input("Digite o valor do débito: "))
    credito = float(input("Digite o valor do crédito: "))
    
    saldoFinal = saldo - debito + credito
    if saldoFinal >= 0:
        print(f"Saldo positivo: R${saldoFinal:.2f}")
    else:
        print(f"Saldo negativo: R${saldoFinal:.2f}")
    
# Chamada da função
saldoConta()

# 8. Faça um algoritmo para ler um número que é um código de usuário. 
# Caso este código seja diferente de um código armazenado internamente no 
# algoritmo (igual a 1234) deve ser apresentada a mensagem ‘Usuário inválido!’. 
# Caso o Código seja correto, deve ser lido outro valor que é a senha. 
# Se esta senha estiver incorreta (a certa é 9999) deve ser mostrada a mensagem ‘senha incorreta’. 
# Caso a senha esteja correta, deve ser mostrada a mensagem ‘Acesso permitido’.

def consultaCodigo() -> None:
    """
    Consulta o preço de um produto a partir de seu código.
    """
    codigo001 = 1234
    senha001 = 9999
    
    codigo = int(input("Digite o código do usuário: "))
    if codigo == codigo001:
        senha = int(input("Digite a senha: "))
        if senha == senha001:
            print("Acesso permitido.")
        else:
            print("Senha incoreta.")
    else:
        print("Código inválido.")
        
# Chamada da função
consultaCodigo()
    
# 9. Uma empresa quer verificar se um empregado está qualificado para a aposentadoria ou não. 
# Para estar em condições, um dos seguintes requisitos deve ser satisfeito: 
# - Ter no mínimo 65 anos de idade. - Ter trabalhado no mínimo 30 anos. 
# - Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos. 
# Com base nas informações acima, faça um algoritmo que leia: o número do empregado (código), 
# o ano de seu nascimento e o ano de seu ingresso na empresa. 
# O programa deverá escrever a idade e o tempo de trabalho do empregado e a mensagem 'Requerer aposentadoria' ou 'Não requerer'.

def consultaAposentadoria() -> None:
    """
    Calcula se uma pessoa está apta para requerer aposentadoria.
    """
    
    codigo = int(input("Digite o número do empregado: "))
    idade = int(input("Digite o ano de nascimento: "))
    tempoContribuicao = int(input("Digite o ano de ingresso na empresa: "))
    
    anoAtual = time.localtime().tm_year
    idadeAtual = anoAtual - idade
    tempoTrabalhado = anoAtual - tempoContribuicao
    
    if (idadeAtual >= 65 and tempoTrabalhado >= 30) or (idadeAtual >= 60 and tempoTrabalhado >= 25):
        print(f"Idade do funcionário: {idadeAtual} anos")
        print(f"Tempo de trabalho: {tempoTrabalhado} anos")
        print("Requerer aposentadoria.")
    else:
        print(f"Idade do funcionário: {idadeAtual} anos")
        print(f"Tempo de trabalho: {tempoTrabalhado} anos")
        print("Não requerer aposentadoria.")
        
# Chamada da função
consultaAposentadoria()

# 10.Considere quatro moedas, de 25 centavos, 10, 5 e 1. 
# Construa um programa que pergunte ao usuário quanto ele quer receber de troco e em seguida 
# imprima a quantidade de moedas necessárias pra pagar o troco, entregando sempre o menor número possível de moedas. 
# O programa deve ter um loop que obrigue o usuário colocar um valor positivo.

def moedas() -> None:
    """
    Calcula a quantidade de moedas necessárias para pagar um troco.
    """
       
    while True:
        troco = int(input("Digite o valor do troco (em centavos): "))
        if troco > 0:
            break
        print("O valor do troco deve ser positivo.")
    
    
    quantidade = troco // 25
    troco %= 25
    if quantidade > 0:
        print(f"{quantidade} moeda(s) de 25 centavos")
    
    quantidade = troco // 10
    troco %= 10
    if quantidade > 0:
        print(f"{quantidade} moeda(s) de 10 centavos")
    
    quantidade = troco // 5
    troco %= 5
    if quantidade > 0:
        print(f"{quantidade} moeda(s) de 5 centavos")
    
    if troco > 0:
        print(f"{troco} moeda(s) de 1 centavo")
                
# Chamada da função
moedas()
