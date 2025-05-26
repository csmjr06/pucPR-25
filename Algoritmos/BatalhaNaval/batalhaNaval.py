"""
Desenvolver um jogo completo e funcional de Batalha Naval em Python, aplicando conceitos fundamentais de programação, como manipulação de matrizes bidimensionais, funções, estruturas de repetição, condicionais, validação de entrada, encapsulamento e exibição formatada no terminal.
"""

# Batalha Naval - Jogo Completo em Python

import random
import time
from colorama import init, Fore, Style

# Menu Inicial
def menu_inicial():
    """
    Exibe o menu inicial do jogo e coleta as configurações do usuário.
    Retorna -> Tamanho do tabuleiro e modo de jogo escolhido.
    """
    print("Bem-vindo ao Batalha Naval!")
    print("Escolha o tamanho do tabuleiro (mínimo 10x10):")
    
    while True:
        try:
            tamanho = int(input("Digite o tamanho do tabuleiro (ex: 10 para 10x10): "))
            if tamanho >= 10:
                break
            else:
                print("Tamanho inválido. Deve ser maior ou igual a 10.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
    
    print("\nEscolha o modo de jogo:")
    print("1 - Jogador vs Jogador")
    print("2 - Jogador vs IA")
    
    while True:
        modo = input("Digite 1 ou 2: ")
        if modo in ['1', '2']:
            break
        else:
            print("Opção inválida. Por favor, digite 1 ou 2.")
    
    return tamanho, modo

# Configuração do Tabuleiro
def configurar_tabuleiro(tamanho):
    """
    Cria duas matrizes bidimensionais para o tabuleiro do jogador. 
    Retorna -> Duas matrizes: uma para o próprio tabuleiro e outra para os ataques realizados.
    """
    tabuleiro = [['~' for _ in range(tamanho)] for _ in range(tamanho)]
    ataques = [['~' for _ in range(tamanho)] for _ in range(tamanho)]
    
    return tabuleiro, ataques

"""Exibir Tabuleiro
def mostrar_tabuleiro(tabuleiro, ataques):
    
    Exibe o tabuleiro do jogador e a matriz de ataques realizados.
    
    tamanho = len(tabuleiro)
    
    # Cabeçalhos das colunas
    print("  " + " ".join(chr(65 + i) for i in range(tamanho)))
    
    # Linhas do tabuleiro
    for i in range(tamanho):
        print(f"{i + 1} " + " ".join(tabuleiro[i]))
    
    print("\nAtaques Realizados:")
    print("  " + " ".join(chr(65 + i) for i in range(tamanho)))
    
    for i in range(tamanho):
        print(f"{i + 1} " + " ".join(ataques[i]))
    
    print("\n") """
    
# Posicionar Navios
def posicionar_navios(tabuleiro):
    """
    Permite ao jogador posicionar seus navios no tabuleiro.
    """
    navios = {
        "Encouraçado": 5,
        "Porta-aviões": 4,
        "Contratorpedeiro": 3,
        "Submarino": 2
    }
    
    for navio, tamanho in navios.items():
        while True:
            print(f"\nPosicione seu {navio} ({tamanho} casas):")
            posicao = input("Digite a coordenada inicial (ex: A1) e a orientação (H para horizontal, V para vertical): ").upper()
            
            if len(posicao) < 3 or len(posicao) > 4:
                print("Entrada inválida. Tente novamente.")
                continue
            
            coluna = ord(posicao[0]) - 65
            linha = int(posicao[1:]) - 1
            orientacao = posicao[2] if len(posicao) == 4 else 'H'
            
            if orientacao not in ['H', 'V']:
                print("Orientação inválida. Use 'H' para horizontal ou 'V' para vertical.")
                continue
            
            if orientacao == 'H':
                if coluna + tamanho > len(tabuleiro) or any(tabuleiro[linha][coluna + i] != '~' for i in range(tamanho)):
                    print("Posição inválida. Tente novamente.")
                    continue
                for i in range(tamanho):
                    tabuleiro[linha][coluna + i] = 'N'
            else:
                if linha + tamanho > len(tabuleiro) or any(tabuleiro[linha + i][coluna] != '~' for i in range(tamanho)):
                    print("Posição inválida. Tente novamente.")
                    continue
                for i in range(tamanho):
                    tabuleiro[linha + i][coluna] = 'N'
            
            print(f"{navio} posicionado com sucesso!")
            break

# Realizar Ataque
def realizar_ataque(tabuleiro, ataques):
    """
    Processa o ataque do jogador, atualizando as matrizes de ataques e tabuleiro.
    Retorna -> True se o ataque foi bem-sucedido (acerto), False se foi um erro.
    """
    tamanho = len(tabuleiro)
    
    while True:
        ataque = input("Digite as coordenadas do ataque (ex: A1): ").upper()
        
        if len(ataque) < 2 or len(ataque) > 3:
            print("Entrada inválida. Tente novamente.")
            continue
        
        coluna = ord(ataque[0]) - 65
        linha = int(ataque[1:]) - 1
        
        if coluna < 0 or coluna >= tamanho or linha < 0 or linha >= tamanho:
            print("Coordenadas fora dos limites. Tente novamente.")
            continue
        
        if ataques[linha][coluna] != '~':
            print("Você já atacou essa posição. Tente outra.")
            continue
        
        ataques[linha][coluna] = 'O'  # Marca o ataque na matriz de ataques
        
        if tabuleiro[linha][coluna] == 'N':
            tabuleiro[linha][coluna] = 'X'  # Acerto
            print("Acertou!")
            return True
        else:
            print("Errou!")
            return False

def verificar_vitoria(tabuleiro):
    """
    Verifica se todos os navios de um jogador foram afundados.
    Retorna -> True se o jogador perdeu (todos os navios afundados), False caso contrário.
    """
    for linha in tabuleiro:
        if 'N' in linha:  # Se ainda houver partes de navios não atingidas
            return False
    return True
def delay(segundos):
    """ 
    Implementa uma pausa programada para simular o tempo de espera entre turnos.
    """
    time.sleep(segundos)

# Jogo Principal
init(autoreset=True)

def mostrar_tabuleiro(tabuleiro, ataques, mostrar_navios=False):
    """
    Exibe o tabuleiro do jogador e a matriz de ataques realizados, com cores.
    Se mostrar_navios=True, mostra os navios no tabuleiro.
    """
    tamanho = len(tabuleiro)
    print("  " + " ".join(chr(65 + i) for i in range(tamanho)))
    for i in range(tamanho):
        linha_str = []
        for j in range(tamanho):
            celula = tabuleiro[i][j]
            if celula == '~':
                linha_str.append(Fore.BLUE + '~' + Style.RESET_ALL)
            elif celula == 'N':
                if mostrar_navios:
                    linha_str.append(Fore.YELLOW + 'N' + Style.RESET_ALL)
                else:
                    linha_str.append(Fore.BLUE + '~' + Style.RESET_ALL)
            elif celula == 'X':
                linha_str.append(Fore.RED + 'X' + Style.RESET_ALL)
            else:
                linha_str.append(celula)
        print(f"{i + 1} " + " ".join(linha_str))
    print("\nAtaques Realizados:")
    print("  " + " ".join(chr(65 + i) for i in range(tamanho)))
    for i in range(tamanho):
        linha_str = []
        for j in range(tamanho):
            celula = ataques[i][j]
            if celula == '~':
                linha_str.append(Fore.BLUE + '~' + Style.RESET_ALL)
            elif celula == 'O':
                linha_str.append(Fore.LIGHTBLACK_EX + 'O' + Style.RESET_ALL)
            elif celula == 'X':
                linha_str.append(Fore.RED + 'X' + Style.RESET_ALL)
            else:
                linha_str.append(celula)
        print(f"{i + 1} " + " ".join(linha_str))
    print("\n")

def registrar_jogada(arquivo, texto):
    with open(arquivo, "a", encoding="utf-8") as f:
        f.write(texto + "\n")

def posicionar_navios(tabuleiro, jogador_nome, arquivo_log):
    """
    Permite ao jogador posicionar seus navios no tabuleiro, mostrando o tabuleiro a cada passo.
    """
    navios = {
        "Encouraçado": 5,
        "Porta-aviões": 4,
        "Contratorpedeiro": 3,
        "Submarino": 2
    }
    for navio, tamanho_navio in navios.items():
        while True:
            mostrar_tabuleiro(tabuleiro, [['~']*len(tabuleiro) for _ in range(len(tabuleiro))], mostrar_navios=True)
            print(f"\n{jogador_nome}, posicione seu {navio} ({tamanho_navio} casas):")
            posicao = input("Digite a coordenada inicial (ex: A1) e a orientação (H para horizontal, V para vertical): ").upper()
            if len(posicao) < 3 or len(posicao) > 4:
                print("Entrada inválida. Tente novamente.")
                continue
            coluna = ord(posicao[0]) - 65
            try:
                linha = int(posicao[1:-1]) - 1 if len(posicao) == 4 else int(posicao[1:]) - 1
            except ValueError:
                print("Entrada inválida. Tente novamente.")
                continue
            orientacao = posicao[-1] if posicao[-1] in ['H', 'V'] else 'H'
            if orientacao not in ['H', 'V']:
                print("Orientação inválida. Use 'H' para horizontal ou 'V' para vertical.")
                continue
            if linha < 0 or linha >= len(tabuleiro) or coluna < 0 or coluna >= len(tabuleiro):
                print("Coordenadas fora dos limites. Tente novamente.")
                continue
            if orientacao == 'H':
                if coluna + tamanho_navio > len(tabuleiro) or any(tabuleiro[linha][coluna + i] != '~' for i in range(tamanho_navio)):
                    print("Posição inválida. Tente novamente.")
                    continue
                for i in range(tamanho_navio):
                    tabuleiro[linha][coluna + i] = 'N'
            else:
                if linha + tamanho_navio > len(tabuleiro) or any(tabuleiro[linha + i][coluna] != '~' for i in range(tamanho_navio)):
                    print("Posição inválida. Tente novamente.")
                    continue
                for i in range(tamanho_navio):
                    tabuleiro[linha + i][coluna] = 'N'
            print(f"{navio} posicionado com sucesso!")
            registrar_jogada(arquivo_log, f"{jogador_nome} posicionou {navio} em {posicao}")
            break

def realizar_ataque(tabuleiro, ataques, jogador_nome, arquivo_log):
    """
    Processa o ataque do jogador, atualizando as matrizes de ataques e tabuleiro.
    Retorna -> True se o ataque foi bem-sucedido (acerto), False se foi um erro.
    """
    tamanho = len(tabuleiro)
    while True:
        ataque = input(f"{jogador_nome}, digite as coordenadas do ataque (ex: A1): ").upper()
        if len(ataque) < 2 or len(ataque) > 3:
            print("Entrada inválida. Tente novamente.")
            continue
        coluna = ord(ataque[0]) - 65
        try:
            linha = int(ataque[1:]) - 1
        except ValueError:
            print("Entrada inválida. Tente novamente.")
            continue
        if coluna < 0 or coluna >= tamanho or linha < 0 or linha >= tamanho:
            print("Coordenadas fora dos limites. Tente novamente.")
            continue
        if ataques[linha][coluna] != '~':
            print("Você já atacou essa posição. Tente outra.")
            continue
        if tabuleiro[linha][coluna] == 'N':
            tabuleiro[linha][coluna] = 'X'
            ataques[linha][coluna] = 'X'
            print(Fore.GREEN + "Acertou!" + Style.RESET_ALL)
            registrar_jogada(arquivo_log, f"{jogador_nome} atacou {ataque}: ACERTOU")
            return True
        else:
            ataques[linha][coluna] = 'O'
            print(Fore.LIGHTBLACK_EX + "Errou!" + Style.RESET_ALL)
            registrar_jogada(arquivo_log, f"{jogador_nome} atacou {ataque}: ERROU")
            return False

def jogo():
    """Função principal que controla o fluxo do jogo, com interface simples e registro de partidas."""
    while True:
        print("="*40)
        print("BATALHA NAVAL".center(40))
        print("="*40)
        print("1 - Iniciar nova partida")
        print("2 - Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == '2':
            print("Obrigado por jogar Batalha Naval!")
            break
        elif escolha != '1':
            print("Opção inválida.")
            continue

        tamanho, modo = menu_inicial()
        arquivo_log = f"partida_batalha_naval_{int(time.time())}.txt"
        registrar_jogada(arquivo_log, f"Partida iniciada. Tamanho do tabuleiro: {tamanho}, Modo: {'PvP' if modo=='1' else 'PvE'}")

        tabuleiro_jogador1, ataques_jogador1 = configurar_tabuleiro(tamanho)
        tabuleiro_jogador2, ataques_jogador2 = configurar_tabuleiro(tamanho)

        print("\nJogador 1, posicione seus navios:")
        posicionar_navios(tabuleiro_jogador1, "Jogador 1", arquivo_log)
        mostrar_tabuleiro(tabuleiro_jogador1, ataques_jogador1, mostrar_navios=True)

        if modo == '1':
            print("\nJogador 2, posicione seus navios:")
            posicionar_navios(tabuleiro_jogador2, "Jogador 2", arquivo_log)
            mostrar_tabuleiro(tabuleiro_jogador2, ataques_jogador2, mostrar_navios=True)
        else:
            # IA posiciona navios aleatoriamente
            navios = {
                "Encouraçado": 5,
                "Porta-aviões": 4,
                "Contratorpedeiro": 3,
                "Submarino": 2
            }
            for navio, tamanho_navio in navios.items():
                while True:
                    orientacao = random.choice(['H', 'V'])
                    if orientacao == 'H':
                        linha = random.randint(0, tamanho - 1)
                        coluna = random.randint(0, tamanho - tamanho_navio)
                        if all(tabuleiro_jogador2[linha][coluna + i] == '~' for i in range(tamanho_navio)):
                            for i in range(tamanho_navio):
                                tabuleiro_jogador2[linha][coluna + i] = 'N'
                            registrar_jogada(arquivo_log, f"IA posicionou {navio} em {chr(65+coluna)}{linha+1}{orientacao}")
                            break
                    else:
                        linha = random.randint(0, tamanho - tamanho_navio)
                        coluna = random.randint(0, tamanho - 1)
                        if all(tabuleiro_jogador2[linha + i][coluna] == '~' for i in range(tamanho_navio)):
                            for i in range(tamanho_navio):
                                tabuleiro_jogador2[linha + i][coluna] = 'N'
                            registrar_jogada(arquivo_log, f"IA posicionou {navio} em {chr(65+coluna)}{linha+1}{orientacao}")
                            break

        turno = 0
        while True:
            if turno % 2 == 0:  # Jogador 1
                print("\nTurno do Jogador 1:")
                mostrar_tabuleiro(tabuleiro_jogador2, ataques_jogador1)
                acerto = realizar_ataque(tabuleiro_jogador2, ataques_jogador1, "Jogador 1", arquivo_log)
                if verificar_vitoria(tabuleiro_jogador2):
                    print(Fore.GREEN + "Jogador 1 venceu!" + Style.RESET_ALL)
                    registrar_jogada(arquivo_log, "Jogador 1 venceu!")
                    break
            else:  # Jogador 2 ou IA
                if modo == '1':
                    print("\nTurno do Jogador 2:")
                    mostrar_tabuleiro(tabuleiro_jogador1, ataques_jogador2)
                    acerto = realizar_ataque(tabuleiro_jogador1, ataques_jogador2, "Jogador 2", arquivo_log)
                    if verificar_vitoria(tabuleiro_jogador1):
                        print(Fore.GREEN + "Jogador 2 venceu!" + Style.RESET_ALL)
                        registrar_jogada(arquivo_log, "Jogador 2 venceu!")
                        break
                else:  # Modo IA
                    print("\nTurno da IA:")
                    delay(2)
                    # IA faz ataque aleatório
                    while True:
                        linha = random.randint(0, tamanho - 1)
                        coluna = random.randint(0, tamanho - 1)
                        if ataques_jogador2[linha][coluna] == '~':
                            if tabuleiro_jogador1[linha][coluna] == 'N':
                                tabuleiro_jogador1[linha][coluna] = 'X'
                                ataques_jogador2[linha][coluna] = 'X'
                                print(Fore.GREEN + f"IA acertou em {chr(65+coluna)}{linha+1}!" + Style.RESET_ALL)
                                registrar_jogada(arquivo_log, f"IA atacou {chr(65+coluna)}{linha+1}: ACERTOU")
                            else:
                                ataques_jogador2[linha][coluna] = 'O'
                                print(Fore.LIGHTBLACK_EX + f"IA errou em {chr(65+coluna)}{linha+1}." + Style.RESET_ALL)
                                registrar_jogada(arquivo_log, f"IA atacou {chr(65+coluna)}{linha+1}: ERROU")
                            break
                    mostrar_tabuleiro(tabuleiro_jogador1, ataques_jogador2)
                    if verificar_vitoria(tabuleiro_jogador1):
                        print(Fore.GREEN + "A IA venceu!" + Style.RESET_ALL)
                        registrar_jogada(arquivo_log, "A IA venceu!")
                        break
            turno += 1

        print("\nDeseja jogar novamente?")
        print("1 - Sim")
        print("2 - Não (Sair)")
        if input("Escolha: ") != '1':
            print("Obrigado por jogar Batalha Naval!")
            break
# Iniciar o jogo
if __name__ == "__main__":
    jogo()
# Fim do Jogo

    
    