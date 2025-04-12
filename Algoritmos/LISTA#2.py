# 1 Elabore um algoritmo que leia um nú mero inteiro e verifique se ele é par ou ímpar.

def par_ou_impar() -> None:
    """
    Lê um número inteiro e verifica se ele é par ou ímpar.
    """
    
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
    
# Chamada da função
par_ou_impar()

# Algoritmo em formato de pseudocódigo:
# 
# Início
#   Leia numero
#   Se numero % 2 == 0 então
#       Escreva "O número é par."
#   Senão
#       Escreva "O número é ímpar."
#   FimSe
# Fim

# 2. A partir do mês e ano de nascimento informado pelo usuario, elabore um algoritmo que 
# informe a idade que completará (ou já completou) em 2025. 
# Verifique se ele já pode fazer a carteira de motorista ou não, informando sua situação.

def idade_e_carteira() -> None:
    """
    Lê o mês e ano de nascimento de uma pessoa e informa a idade que ela terá em 2025.
    Verifica se a pessoa já pode fazer a carteira de motorista.
    """
    
    mes_nascimento = int(input("Digite o mês de nascimento: "))
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    
    ano_atual = 2025
    idade_em_2025 = ano_atual - ano_nascimento
    print(f"Em 2025, você terá {idade_em_2025} anos.")
    
    if idade_em_2025 >= 18:
        print("Você já pode fazer a carteira de motorista.")
    else:
        print("Você ainda não pode fazer a carteira de motorista.")
        
# Chamada da função 
idade_e_carteira()

# Algoritmo em formato de pseudocódigo:
#   
# Início
#   Leia mes_nascimento
#   Leia ano_nascimento
#   ano_atual = 2025
#   idade_em_2025 = ano_atual - ano_nascimento
#   Escreva "Em 2025, você terá", idade_em_2025, "anos."
#   Se idade_em_2025 >= 18 então
#       Escreva "Você já pode fazer a carteira de motorista."
#   Senão
#       Escreva "Você ainda não pode fazer a carteira de motorista."
#   FimSe
# Fim

# 3. Um produtor de abóboras deve verificar a classificação dos seus produtos para posterior empacotamento e venda. 
# Um de seus clientes compra apenas abóboras médias (aquelas que possuem o diâmetro (d) no intervalo 15 cm ≤ d < 20 cm). 
# Elabore um algoritmo que leia o diâ metro de uma abó bora e mostre se ela é do tipo médio ou não. 
# Caso ela nã o se encaixe na classificação, informe “produto fora das medidas”.

def classificar_abobora() -> None:
    """
    Lê o diâmetro de uma abóbora e verifica se ela é do tipo médio.
    """
    
    diametro = float(input("Digite o diâmetro da abóbora: "))
    if 15 <= diametro < 20:
        print("A abóbora é do tipo médio.")
    else:
        print("Produto fora das medidas.")

# Chamada da função
classificar_abobora()

# Algoritmo em formato de pseudocódigo:
#
# Início
#   Leia diametro
#   Se 15 <= diametro < 20 então
#       Escreva "A abóbora é do tipo médio."
#   Senão
#       Escreva "Produto fora das medidas."
#   FimSe
# Fim

# 4. Elabore um algoritmo que leia um número inteiro e mostre sua raiz quadrada (informe “Valor inválido” para números negativos).

def raiz_quadrada() -> None:
    """
    Lê um número inteiro e exibe sua raiz quadrada.
    """
    
    numero = int(input("Digite um número inteiro: "))
    if numero >= 0:
        raiz = numero ** 0.5
        print(f"A raiz quadrada de {numero} é {raiz:.2f}.")
    else:
        print("Valor inválido.")

# Chamada da função
raiz_quadrada()

# Algoritmo em formato de pseudocódigo:
#
# Início
#   Leia numero
#   Se numero >= 0 então
#       raiz = numero ** 0.5
#       Escreva "A raiz quadrada de", numero, "é", raiz
#   Senão
#       Escreva "Valor inválido."
#   FimSe
# Fim

#5. Em uma determinada papelaria a fotocó pia custa R$ 0,25, caso sejam tiradas menos de 100 có pias. 
# A partir de 100 cópias, o valor de cada fotocó pia tirada cai para R$ 0,20.
# Elabore um algoritmo que leia o número de cópias e mostre o valor a pagar pelo serviço.

def valor_fotocopia() -> None:
    """
    Lê o número de cópias e exibe o valor a pagar pelo serviço.
    """
    
    num_copias = int(input("Digite o número de cópias: "))
    if num_copias < 100:
        valor = num_copias * 0.25
    else:
        valor = num_copias * 0.20
    print(f"O valor a pagar pelo serviço é R${valor:.2f}.")

# Chamada da função
valor_fotocopia()

# Algoritmo em formato de pseudocódigo:
#
# Início
#   Leia num_copias
#   Se num_copias < 100 então
#       valor = num_copias * 0.25
#   Senão
#       valor = num_copias * 0.20
#   FimSe
#   Escreva "O valor a pagar pelo serviço é R$", valor
# Fim

# 6. Tendo como dados de entrada a altura (h) e o sexo de uma pessoa (use 1 - masculino e 2 - feminino) elabore um algoritmo 
# que calcule o peso ideal (p) do usuário utilizando asseguintes fórmulas:
# para homens: p = (72.7 * h) - 58
# para mulheres: p = (62.1 * h) - 44.7

def peso_ideal() -> None:
    """
    Lê a altura e o sexo de uma pessoa e calcula o peso ideal.
    """
    
    altura = float(input("Digite a altura da pessoa: "))
    sexo = int(input("Digite o sexo da pessoa (1 - masculino, 2 - feminino): "))
    if sexo == 1:
        peso = (72.7 * altura) - 58
    elif sexo == 2:
        peso = (62.1 * altura) - 44.7
    else:
        print("Sexo inválido.")
        return
    print(f"O peso ideal para a pessoa é {peso:.2f} kg.")
    
# Chamada da função
peso_ideal()

# Algoritmo em formato de pseudocódigo:
#
# Início
#   Leia altura
#   Leia sexo
#   Se sexo == 1 então
#       peso = (72.7 * altura) - 58
#   Senão Se sexo == 2 então
#       peso = (62.1 * altura) - 44.7
#   Senão
#       Escreva "Sexo inválido."
#       Retorne
#   FimSe
#   Escreva "O peso ideal para a pessoa é", peso, "kg."
# Fim

# 7. O IMC (Índice de Massa Corporal) é calculado através da seguinte fórmula: IMC = massa / altura2
# Elabore um algoritmo que leia a massa (em quilogramas) e a altura (em metros) do
# usuário e mostre o valor do IMC e se ele está na faixa considerada “normal” segundo o critério apresentado na tabela da 
# OMS (Organizaçã o Mundial de Saú de): 18,5 ≤ IMC<25. 
# Caso não esteja, calcule sua massa máxima considerada normal (usando IMC igual a 24,9).

def imc() -> None:
    """
    Lê a massa e a altura de uma pessoa e calcula o IMC.
    Verifica se o IMC está na faixa considerada normal.
    """
    
    massa = float(input("Digite a massa da pessoa (em kg): "))
    altura = float(input("Digite a altura da pessoa (em m): "))
    imc = massa / altura ** 2
    print(f"O IMC da pessoa é {imc:.2f}.")
    if 18.5 <= imc < 25:
        print("IMC na faixa considerada normal.")
    else:
        massa_maxima = 24.9 * altura ** 2
        print(f"IMC fora da faixa normal. A massa máxima considerada normal é {massa_maxima:.2f} kg.") 
        
# Chamada da função
imc()

# Algoritmo em formato de pseudocódigo:
#
# Início
#   Leia massa
#   Leia altura
#   imc = massa / altura ** 2
#   Escreva "O IMC da pessoa é", imc
#   Se 18.5 <= imc < 25 então
#       Escreva "IMC na faixa considerada normal."
#   Senão
#       massa_maxima = 24.9 * altura ** 2
#       Escreva "IMC fora da faixa normal. A massa máxima considerada normal é", massa_maxima, "kg."
#   FimSe
# Fim

# 8. Em um determinado estacionamento a primeira hora custa R$ 8,00, que é o valor mínimo praticado. 
# Após uma hora o valor é fracionado, R$ 1,50 a cada 15 minutos. 
# Elabore um algoritmo que leia um número inteiro correspondente a quantidade de minutos usados no estacionamento e 
# mostre a mensagem “Valor mínimo, R$ 8,00” ou “Valor fracionado, R$ x”, no qual x será́ o valor a pagar calculado pelo algoritmo.

def valor_estacionamento() -> None:
    """
    Lê a quantidade de minutos usados no estacionamento e exibe o valor a pagar.
    """
    
    minutos = int(input("Digite a quantidade de minutos usados no estacionamento: "))
    if minutos <= 60:
        print("Valor mínimo, R$ 8,00")
    else:
        valor_fracionado = 8 + (minutos - 60) // 15 * 1.5
        print(f"Valor fracionado, R$ {valor_fracionado:.2f}")

# Chamada da função
valor_estacionamento()

# Algoritmo em formato de pseudocódigo:
#
# Início
#   Leia minutos
#   Se minutos <= 60 então
#       Escreva "Valor mínimo, R$ 8,00"
#   Senão
#       valor_fracionado = 8 + (minutos - 60) // 15 * 1.5
#       Escreva "Valor fracionado, R$ ", valor_fracionado
#   FimSe
# Fim

# 9. A partir da idade informada de uma pessoa, elabore um algoritmo que informe a sua classe eleitoral, 
# sabendo que menores de 16 não votam (não votante), 
# que o voto é obrigatório para adultos entre 18 e 65 anos (eleitor obrigatório) e que 
# o voto é opcional para eleitores entre 16 e 18, ou maiores de 65 anos (eleitor facultativo)

def classe_eleitoral() -> None:
    """
    Lê a idade de uma pessoa e informa sua classe eleitoral.
    """
    
    idade = int(input("Digite a idade da pessoa: "))
    if idade < 16:
        print("Não votante.")
    elif 16 <= idade < 18 or idade >= 65:
        print("Eleitor facultativo.")
    else:
        print("Eleitor obrigatório.")
        
# Chamada da função
classe_eleitoral()

# Algoritmo em formato de pseudocódigo:
#
# Início
#   Leia idade
#   Se idade < 16 então
#       Escreva "Não votante."
#   Senão Se 16 <= idade < 18 ou idade >= 65 então
#       Escreva "Eleitor facultativo."
#   Senão
#       Escreva "Eleitor obrigatório."
#   FimSe
# Fim

# 10.Elabore um algoritmo que, dada a idade de um nadador, mostre sua classificação segundo uma das seguintes categorias:
# • 5 até 7 anos: Infantil A;
# • 8 até 10 anos: Infantil B;
# • 11 até 13 anos: Juvenil A;
# • 14 até 17 anos: Juvenil B;
# • Maiores de 18 anos: Adulto.

def classificacao_nadador() -> None:
    """
    Lê a idade de um nadador e mostra sua classificação.
    """
    
    idade = int(input("Digite a idade do nadador: "))
    if 5 <= idade <= 7:
        print("Infantil A.")
    elif 8 <= idade <= 10:
        print("Infantil B.")
    elif 11 <= idade <= 13:
        print("Juvenil A.")
    elif 14 <= idade <= 17:
        print("Juvenil B.")
    else:
        print("Adulto.")
        
# Chamada da função
classificacao_nadador()

# Algoritmo em formato de pseudocódigo:
#
# Início
#   Leia idade
#   Se 5 <= idade <= 7 então
#       Escreva "Infantil A."
#   Senão Se 8 <= idade <= 10 então
#       Escreva "Infantil B."
#   Senão Se 11 <= idade <= 13 então
#       Escreva "Juvenil A."
#   Senão Se 14 <= idade <= 17 então
#       Escreva "Juvenil B."
#   Senão
#       Escreva "Adulto."
#   FimSe
# Fim

# 11.

massa=float(input("Digite a massa do boxeador em kg: "))
massa_libras = massa * 2.20462262
if massa_libras >= 201:
    print("Categoria Peso-pesado.")
elif 176 <= massa_libras <= 200:
    print("Categoria Cruzador.")
elif 169 <= massa_libras <= 175:
    print("Categoria Meio-pesado.")
elif 161 <= massa_libras <= 168:
    print("Categoria Super-médio.")
else:
    print("Categora inferiora Super-médio.")

# Algoritmo em formato de pseudocódigo:
#
# Início
#   Leia massa
#   massa_libras = massa * 2.20462262
#   Se massa_libras >= 201 então    
#       Escreva "Categoria Peso-pesado."
#   Senão Se 176 <= massa_libras <= 200 então
#       Escreva "Categoria Cruzador."
#   Senão Se 169 <= massa_libras <= 175 então
#       Escreva "Categoria Meio-pesado."
#   Senão Se 161 <= massa_libras <= 168 então
#       Escreva "Categoria Super-médio."
#   Senão
#       Escreva "Categora inferiora Super-médio."
#   FimSe
# Fim

# 12. Em uma determinada loja de eletrodomésticos, os produtos podem ser adquiridos da seguinte forma:
# Opção 1: Condição à vista, Cálculo: 8% de desconto sobre o valor do produto.
# Opção 2: Condição em 2x, Cálculo: 4% de desconto sobre o valor do produto, dividido em duas vezes
# Opção 3: Condição em 3x, Cálculo: valor do produto sem desconto, dividido em três vezes
# Opção 4: Condição em 4x, Cálculo: 4% de acréscimo, dividido em quatro vezes
# Elabore um algoritmo que leia a opção do cliente e o preço de tabela do produto, 
# mostrando então o valor calculado conforme a condição escolhida.

def forma_pagamento() -> None:
    """
    Lê a opção de pagamento e o preço de tabela do produto e mostra o valor calculado conforme a condição escolhida.
    """
    
    opcao = int(input("Digite a opção de pagamento (1, 2, 3 ou 4): "))
    preco = float(input("Digite o preço de tabela do produto: "))
    if opcao == 1:
        preco_final = preco * 0.92
    elif opcao == 2:
        preco_final = preco * 0.96
    elif opcao == 3:
        preco_final = preco
    elif opcao == 4:
        preco_final = preco * 1.04
    else:
        print("Opção inválida.")
        return
    print(f"O valor a ser pago é R${preco_final:.2f}.")
    
# Chamada da função
forma_pagamento()

# Algoritmo em formato de pseudocódigo:
#
# Início
#   Leia opcao
#   Leia preco
#   Se opcao == 1 então
#       preco_final = preco * 0.92
#   Senão Se opcao == 2 então
#       preco_final = preco * 0.96
#   Senão Se opcao == 3 então
#       preco_final = preco
#   Senão Se opcao == 4 então
#       preco_final = preco * 1.04
#   Senão
#       Escreva "Opção inválida."
#       Retorne
#   FimSe
#   Escreva "O valor a ser pago é R$", preco_final
# Fim

# 13. Escreva um algoritmo que leia três números inteiros e mostre o valor do maior deles.

def maior_numero() -> None:
    """
    Lê 3 números inteiros e mostra o valor do maior deles.
    """
    
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))
    num3 = int(input("Digite o terceiro número inteiro: "))
    if num1 >= num2 and num1 >= num3:
        maior = num1
    elif num2 >= num1 and num2 >= num3:
        maior = num2
    else:
        maior = num3
    print(f"O maior número é {maior}.")

# Chamada da função
maior_numero()

# Algoritmo em formato de pseudocódigo:
#
# Início
#   Leia num1
#   Leia num2
#   Leia num3
#   Se num1 >= num2 e num1 >= num3 então
#       maior = num1
#   Senão Se num2 >= num1 e num2 >= num3 então
#       maior = num2    
#   Senão
#       maior = num3
#   FimSe
#   Escreva "O maior número é", maior
# Fim

# 14.Escreva um algoritmo que leia três números inteiros e mostre-os em ordem decrescente.

def ordem_decrescente() -> None:
    """
    Lê 3 números inteiros e mostra-os em ordem decrescente.
    """
    
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))
    num3 = int(input("Digite o terceiro número inteiro: "))
    if num1 >= num2 and num1 >= num3:
        maior = num1
        if num2 >= num3:
            meio = num2
            menor = num3
        else:
            meio = num3
            menor = num2
    elif num2 >= num1 and num2 >= num3:
        maior = num2
        if num1 >= num3:
            meio = num1
            menor = num3
        else:
            meio = num3
            menor = num1
    else:
        maior = num3
        if num1 >= num2:
            meio = num1
            menor = num2
        else:
            meio = num2
            menor = num1
    print(f"Os números em ordem decrescente são: {maior}, {meio}, {menor}.")    
    
# Chamada da função
ordem_decrescente()

# Algoritmo em formato de pseudocódigo:
#
# Início
#   Leia num1
#   Leia num2
#   Leia num3
#   Se num1 >= num2 e num1 >= num3 então    
#       maior = num1
#       Se num2 >= num3 então
#           meio = num2
#           menor = num3
#       Senão
#           meio = num3
#           menor = num2
#       FimSe
#   Senão Se num2 >= num1 e num2 >= num3 então
#       maior = num2
#       Se num1 >= num3 então
#           meio = num1
#           menor = num3
#       Senão
#           meio = num3
#           menor = num1
#       FimSe
#   Senão
#       maior = num3
#       Se num1 >= num2 então
#           meio = num1
#           menor = num2
#       Senão
#           meio = num2
#           menor = num1
#       FimSe
#   FimSe
#   Escreva "Os números em ordem decrescente são:", maior, ",", meio, ",", menor
# Fim
