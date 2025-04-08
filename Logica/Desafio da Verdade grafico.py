import random
import pygame
import sys


# Inicializa o Pygame
pygame.init()

# Configurações da tela
largura, altura = 1080, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Desafio da Verdade")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (255, 0, 0)

# Fontes
fonte = pygame.font.Font(None, 36)

# Função para desenhar texto na tela
def desenhar_texto(texto, fonte, cor, superficie, x, y):
    textoobj = fonte.render(texto, True, cor)
    textorect = textoobj.get_rect()
    textorect.topleft = (x, y)
    superficie.blit(textoobj, textorect)

# Função para desenhar botão
def desenhar_botao(texto, cor, x, y, largura, altura):
    pygame.draw.rect(tela, cor, (x, y, largura, altura))
    desenhar_texto(texto, fonte, branco, tela, x + 10, y + 10)

# Função principal do jogo
def jogo():
    pontuacao = 0
    rodada = 1
    
    def tela_inicial():
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = evento.pos
                    if 100 <= mouse_x <= 300 and 400 <= mouse_y <= 450:
                        return 1
                    elif 500 <= mouse_x <= 700 and 400 <= mouse_y <= 450:
                        return 2
            
            tela.fill(branco)
            desenhar_texto("Desafio da Verdade", fonte, preto, tela, 250, 100)
            desenhar_texto("Escolha o nível:", fonte, preto, tela, 300, 300)
            desenhar_botao("Nível 1", verde, 100, 400, 200, 50)
            desenhar_botao("Nível 2", vermelho, 500, 400, 200, 50)
            pygame.display.flip()

    # Chamada da tela inicial para selecionar o nível
    nivel = tela_inicial()

    while rodada <= 5:
        p = random.choice([True, False])
        q = random.choice([True, False])
        r = random.choice([True, False])
        
        resP = "V" if p else "F"
        resQ = "V" if q else "F"
        resR = "V" if r else "F"
        
        propP = random.choice(["P", "NOT_P"])
        propQ = random.choice(["Q", "NOT_Q"])
        propR = random.choice(["R", "NOT_R"])
        operador = random.choice(["AND", "OR", "XOR", "->", "<->"])
        operador2 = random.choice(["AND", "OR", "XOR", "->", "<->"])
        
        if nivel == 1:
            pergunta = f"{rodada} - P = {resP}, Q = {resQ} : Qual o resultado de {propP} {operador} {propQ}?"
        elif nivel == 2:
            pergunta = f"{rodada} - P = {resP}, Q = {resQ}, R = {resR} : Qual o resultado de ({propP} {operador} {propQ}) {operador2} {propR}?"
        
        resposta = None
        while resposta is None:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = evento.pos
                    if 100 <= mouse_x <= 200 and 500 <= mouse_y <= 550:
                        resposta = "V"
                    elif 300 <= mouse_x <= 400 and 500 <= mouse_y <= 550:
                        resposta = "F"
            
            tela.fill(branco)
            desenhar_texto(pergunta, fonte, preto, tela, 50, 100)
            desenhar_botao("V", verde, 100, 500, 100, 100)
            desenhar_botao("F", vermelho, 300, 500, 100, 100)
            desenhar_texto(f"Pontuação: {pontuacao}", fonte, preto, tela, 600, 50)
            pygame.display.flip()
        
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
    
    tela.fill(branco)
    desenhar_texto(f"Você fez {pontuacao} pontos!", fonte, preto, tela, 50, 200)
    pygame.display.flip()
    pygame.time.wait(3000)

# Chamada da função principal do jogo
jogo()