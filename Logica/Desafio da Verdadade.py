import random

def desafioDaVerdade() -> None:
    """
    Jogo de perguntas e respostas sobre tabela verdade.
    """
    
    print("Escolha o nível de dificuldade:")
    print("1 - Fácil (2 Variáveis)")
    print("2 - Médio3 (3 Variáveis)")
    
    while True:
        try:
            nivel = int(input("Digite o número correspondente ao nível: "))
            if nivel not in [1, 2]:
                raise ValueError
            break
        except ValueError:
            print("Nível inválido. Por favor, escolha um número de 1 ou 2.")
    
    pontuacao = 0
    rodada = 1
    while rodada <= 5:
        p = random.choice([True, False])
        q = random.choice([True, False])
        r = random.choice([True, False])
        
        if p:
            resP = "V"
        else:
            resP = "F"
            
        if q:
            resQ = "V" 
        else:
            resQ = "F"
            
        if r:
            resR = "V"
        else:
            resR = "F"
        
        propP = random.choice(["P", "NOT_P"])
        propQ = random.choice(["Q", "NOT_Q"])
        propR = random.choice(["R", "NOT_R"])
        operador = random.choice(["AND", "OR", "XOR", "->", "<->"])
        operador2 = random.choice(["AND", "OR", "XOR", "->", "<->"])
        
        if nivel == 1:
            print(f"{rodada} - P = {resP}, Q = {resQ} : Qual o resultado de {propP} {operador} {propQ}?")
        elif nivel == 2:
            print(f"{rodada} - P = {resP}, Q = {resQ}, R = {resR} : Qual o resultado de ({propP} {operador} {propQ}) {operador2} {propR}?")
        resposta = input("Digite V para Verdadeiro ou F para Falso: ").upper()
        
        if propP == "NOT_P":
            p = not p
        if propQ == "NOT_Q":
            q = not q
        if propR == "NOT_R":
            r = not r
        
        if operador == "AND":
            resultado = p and q
        elif operador == "OR":
            resultado = p or q
        elif operador == "XOR":
            resultado = p != q
        elif operador == "->":
            resultado = not p or q
        elif operador == "<->":
            resultado = p == q
        
        if nivel == 2:
                
            if operador2 == "AND":
                resultado = resultado and r
            elif operador2 == "OR":
                resultado = resultado or r
            elif operador2 == "XOR":
                resultado = resultado != r
            elif operador2 == "->":
                resultado = not resultado or r
            elif operador2 == "<->":
                resultado = resultado == r
        
        if (resposta == "V" and resultado) or (resposta == "F" and not resultado):
            pontuacao += 1
        rodada += 1
    
    print(f"Você fez {pontuacao} pontos!")
    
    if  pontuacao == 5:
        print(f"Parabéns, você acertou todas! Você é um gênio!")
    elif pontuacao == 4:
        print(f"Quase lá, você acertou {pontuacao}!")
    elif pontuacao == 3:
        print(f"Você acertou {pontuacao}! Mais atenção na próxima.")
    elif pontuacao == 0:
        print(f"Você não acertou nenhuma! Estude mais.")
    else:    
        print(f"Você acertou apenas {pontuacao}! Estude mais.")
        
# Chamada da função
desafioDaVerdade()