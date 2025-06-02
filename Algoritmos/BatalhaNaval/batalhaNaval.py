# configurações

TamanhoBarco = 1  # tamanho do barco
TamanhoMinimo = 10 # tamanho mínimo do tabuleiro
TamanhoMaximo = 26 # tamanho máximo do tabuleiro (de preferência no MÁXIMO 26 pra não passar as letras do alfabeto)

# código

import random
import os
import platform

from colorama import Fore, Style, init
init(autoreset=True)  # Inicializa o colorama para resetar cores automaticamente
import datetime
arquivo_log = f"batalha_naval_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log"


def clear():
    '''
    Limpa o console dependendo do sistema operacional.'''
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
clear()

def logger(arquivo, mensagem, level=1):
    '''
    Registra mensagens em um arquivo de log.
    Args:
        arquivo (str): Caminho do arquivo de log.
        mensagem (str): Mensagem a ser registrada.
        level (str): Nível de log (padrão é 'INFO').
    '''
    levels = [[1, "[INFO]"], [2, "[WARNING]"], [3, "[ERROR]"], [4, "[DEBUG]"]]

    with open(arquivo, "a") as f:
        f.write(f"{datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')} {levels[level-1][1]} {mensagem}\n")

def menu():
    '''
    Exibe o menu inicial do jogo e solicita as configurações do tabuleiro e modo de jogo.
    Parametros: None
    Retornos: Tamanho do tabuleiro e modo de jogo (1 para jogador vs jogador, 2 para jogador vs máquina).
    '''
    print(Fore.MAGENTA + Style.BRIGHT + "batalha naval\n")
    tamanho = int(input(Fore.CYAN + Style.BRIGHT + f"tamanho do tabuleiro ({TamanhoMinimo}-{TamanhoMaximo}): "))
    while tamanho < TamanhoMinimo or tamanho > TamanhoMaximo:
        clear()
        print(Fore.RED + "tamanho inválido\n")
        tamanho = int(input(Fore.CYAN + Style.BRIGHT + f"tamanho do tabuleiro ({TamanhoMinimo}-{TamanhoMaximo}): "))
    clear()
    modo = input("modo de jogo (1 = jogador vs jogador | 2 = jogador vs maquina): ")
    while modo not in ['1', '2']:
        clear()
        print(Fore.RED + "modo inválido\n")
        modo = input(Fore.CYAN + Style.BRIGHT + "modo de jogo (1 = jogador vs jogador | 2 = jogador vs maquina): ")

    return tamanho, int(modo)

def CriarBoard(tamanho):
    '''
    Cria um tabuleiro vazio com o tamanho especificado.
    Parametros: tamanho (int) - Tamanho do tabuleiro.
    Retornos: (list) - Tabuleiro vazio.
    '''
    return [[Fore.BLUE + '~' for _ in range(tamanho)] for _ in range(tamanho)]

def PrintBoard(tabuleiro):
    '''
    Exibe o tabuleiro formatado com letras para colunas e números para linhas.
    Parametros: tabuleiro (list) - Tabuleiro a ser exibido.
    Retornos: None
    '''
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print("  ", end="")
    for i in range(len(tabuleiro[0])):
        print(letras[i], end=" ")
    print()
    for i in range(len(tabuleiro)):
        print(str(i+1).rjust(2), end=" ")
        for j in range(len(tabuleiro[i])):
            print(tabuleiro[i][j], end=" ")
        print()

def LetraPNumero(letra):
    '''
    Converte uma letra (A-Z) para um número correspondente (0-25).
    Parametros: letra (str) - Letra a ser convertida.
    Retornos: (int) - Número correspondente (0-25).
    '''
    return ord(letra.upper()) - ord('A')

def NumeroPLetra(numero):
    '''
    Converte um número (0-25) para uma letra correspondente (A-Z).
    Parametros: numero (int) - Número a ser convertido.
    Retornos: (str) - Letra correspondente (A-Z).
    '''
    return chr(ord('A') + numero)

def vitoria(tabuleiro):
    '''
    Verifica se todos os barcos foram afundados no tabuleiro.
    Parametros: tabuleiro (list) - Tabuleiro a ser verificado.
    Retornos: (bool) - True se todos os barcos foram afundados, False caso contrário.
    '''
    for linha in tabuleiro:
        if 'n' in linha:
            return False
    return True

def barco_valido(tabuleiro, linha, coluna, orientacao, tamanho_barco):
    '''
    Verifica se a posição e orientação do barco são válidas.
    Parametros:
        tabuleiro (list) - Tabuleiro onde o barco será colocado.
        linha (int) - Linha inicial do barco.
        coluna (int) - Coluna inicial do barco.
        orientacao (str) - Orientação do barco ('h' para horizontal, 'v' para vertical).
        tamanho_barco (int) - Tamanho do barco.
    Retornos: (bool) - True se a posição é válida, False caso contrário.
    '''
    if orientacao == 'h':
        if coluna + tamanho_barco > len(tabuleiro[0]) or linha < 0 or linha >= len(tabuleiro):
            return False
        for i in range(tamanho_barco):
            if tabuleiro[linha][coluna + i] != '~':
                return False
    elif orientacao == 'v':
        if linha + tamanho_barco > len(tabuleiro) or coluna < 0 or coluna >= len(tabuleiro[0]):
            return False
        for i in range(tamanho_barco):
            if tabuleiro[linha + i][coluna] != '~':
                return False
    else:
        return False
    return True

def ColocarBarco(tabuleiro, tipo_barco='generico', tamanho_barco=TamanhoBarco):
    '''
    Solicita ao usuário a posição e orientação do barco e o coloca no tabuleiro.
    verifica se a posição é válida.
    Parametros: tabuleiro (list) - Tabuleiro onde o barco será colocado.
    Retorno: tabuleiro atualizado
    '''
    print(f"coloque seu navio (tamanho: {TamanhoBarco})\n")
    while True:
        linha_input = input("linha inicial do navio: ")
        if linha_input.isdigit():
            linha = int(linha_input) - 1
            if 0 <= linha < len(tabuleiro):
                break
            else:
                print("Linha fora do intervalo do tabuleiro.")
        else:
            print("Por favor, digite um número válido para a linha.")
    while True:
        coluna_letra = input("coluna inicial do navio (letra): ").upper()
        if coluna_letra.isalpha() and 0 <= LetraPNumero(coluna_letra) < len(tabuleiro[0]):
            coluna = LetraPNumero(coluna_letra)
            break
        else:
            print("Por favor, digite uma letra válida para a coluna.")
    orientacao = input("horizontal (h) ou vertical (v): ").lower()
    clear()

    if linha < 0 or linha >= len(tabuleiro) or coluna < 0 or coluna >= len(tabuleiro):
        print("posição inválida!")
        return ColocarBarco(tabuleiro, tipo_barco, tamanho_barco)
    if orientacao not in ['h', 'v']:
        print("orientação inválida!")
        return ColocarBarco(tabuleiro, tipo_barco, tamanho_barco)
    if not barco_valido(tabuleiro, linha, coluna, orientacao, tamanho_barco):
        print("posição inválida!")
        return ColocarBarco(tabuleiro, tipo_barco, tamanho_barco)

    for i in range(tamanho_barco):
        if orientacao == 'h':
            tabuleiro[linha][coluna + i] = 'n'
        elif orientacao == 'v':
            tabuleiro[linha + i][coluna] = 'n'
    
    return tabuleiro

def realizar_ataque(tabuleiro_alvo, tabuleiro_tiros):
    '''
    Solicita ao usuário a posição do ataque e atualiza os tabuleiros de acordo com o resultado.
    Parametros:
        tabuleiro_alvo (list) - Tabuleiro do adversário onde o ataque será realizado.
        tabuleiro_tiros (list) - Tabuleiro do jogador onde os tiros são registrados.
    Retornos:
        tabuleiro_alvo (list) - Tabuleiro atualizado com o resultado do ataque.
        tabuleiro_tiros (list) - Tabuleiro atualizado com o resultado do ataque.
        True se o ataque acertou, False se errou.
    '''
    while True:
        linha_input = input("\nlinha do ataque: ")
        if linha_input.isdigit():
            linha = int(linha_input) - 1
            if 0 <= linha < len(tabuleiro_alvo):
                break
            else:
                print("Linha fora do intervalo do tabuleiro.")
        else:
            print("Por favor, digite um número válido para a linha.")
    while True:
        coluna_letra = input("coluna do ataque (letra): ").upper()
        if coluna_letra.isalpha() and 0 <= LetraPNumero(coluna_letra) < len(tabuleiro_alvo[0]):
            coluna = LetraPNumero(coluna_letra)
            break
        else:
            print("Por favor, digite uma letra válida para a coluna.")
    clear()
    if tabuleiro_alvo[linha][coluna] == 'n':
        print(Fore.GREEN + "acertou!\n")
        tabuleiro_alvo[linha][coluna] = Fore.RED + 'X' 
        tabuleiro_tiros[linha][coluna] = Fore.RED + 'X'
        return tabuleiro_alvo, tabuleiro_tiros, True
    elif tabuleiro_alvo[linha][coluna] == 'X':
        print(Fore.YELLOW + "ja acertou nessa posicao!\n")
        tabuleiro_tiros[linha][coluna] = Fore.RED + 'X'
    else:
        print(Fore.RED + "errou!\n")
        tabuleiro_tiros[linha][coluna] = Fore.YELLOW + 'O'
    return tabuleiro_alvo, tabuleiro_tiros, False

def ataque_ia(tabuleiro_alvo, tabuleiro_tiros):
    '''
    Realiza um ataque da máquina em uma posição aleatória do tabuleiro.
    Parametros:
        tabuleiro_alvo (list) - Tabuleiro do adversário onde o ataque será realizado.
        tabuleiro_tiros (list) - Tabuleiro da máquina onde os tiros são registrados.
    Retornos: True se o ataque acertou, False se errou.
    '''
    while True:
        linha = random.randint(0, len(tabuleiro_alvo) - 1)
        coluna = random.randint(0, len(tabuleiro_alvo) - 1)
        if tabuleiro_tiros[linha][coluna] == '~':
            break
    clear()
    print("maquina atacou na posição:", linha + 1, NumeroPLetra(coluna))
    if tabuleiro_alvo[linha][coluna] == 'n':
        print("maquina acertou!\n")
        tabuleiro_alvo[linha][coluna] = Fore.RED + 'X'
        tabuleiro_tiros[linha][coluna] = Fore.RED + 'X'
        return True
    elif tabuleiro_alvo[linha][coluna] == 'X':
        print("maquina ja acertou nessa posicao!\n")
        tabuleiro_tiros[linha][coluna] = Fore.RED + 'X'
    else:
        print("maquina errou!\n")
        tabuleiro_tiros[linha][coluna] = Fore.YELLOW + 'O'
    return False

def main():
    '''
    Função principal do jogo Batalha Naval.
    Parametros: None
    Retornos: Estatísticas do jogo.
    '''
    
    # Variáveis globais
    
    global TamanhoBarco, TamanhoMinimo, TamanhoMaximo
    global arquivo_log
    
    # Estatísticas do jogo
    
    turno = 1
    quantidade_tiros_j1 = 0
    acertos_j1 = 0
    quantidade_tiros_j2 = 0
    acertos_j2 = 0
    clear()
    
    # Configurações do jogo
    
    #barcos: [tipo, tamanho, quantidade]
    barcos = [["Encouraçado", 5, 1], ["Porta-avião", 4, 1], ["Contratorpedeiro", 3, 2], ["Submarino", 2, 2]]

    tamanho, modo = menu()
    logger(arquivo_log, f"Jogo iniciado: Tamanho do tabuleiro: {tamanho} x {tamanho}, Modo: {'Jogador vs Jogador' if modo == 1 else 'Jogador vs Máquina'}")

    # Criação dos tabuleiros
    tabuleiro_j1 = CriarBoard(tamanho)
    tiros_j1 = CriarBoard(tamanho)

    tabuleiro_j2 = CriarBoard(tamanho)
    tiros_j2 = CriarBoard(tamanho)

    clear()
    
    # Colocação dos barcos
    print(Fore.BLUE + "navio do jogador 1\n")
    for barco in barcos:
        for _ in range(barco[2]):
            tabuleiro_j1 = ColocarBarco(tabuleiro_j1, barco[0], barco[1])
    logger(arquivo_log, "Barcos do jogador 1 colocados no tabuleiro.")

    if modo == 1:
        print(Fore.GREEN + "navio do jogador 2\n")
        for barco in barcos:
            for _ in range(barco[2]):
                tabuleiro_j2 = ColocarBarco(tabuleiro_j2, barco[0], barco[1])
        logger(arquivo_log, "Barcos do jogador 2 colocados no tabuleiro.")
    else:
        print(Fore.YELLOW + "navio da maquina colocado")
        for barco in barcos:
            for _ in range(barco[2]):
                linha = random.randint(0, tamanho - 1)
                coluna = random.randint(0, tamanho - barco[1])
                orientacao = random.choice(['h', 'v'])
                while not barco_valido(tabuleiro_j2, linha, coluna, orientacao, barco[1]):
                    linha = random.randint(0, tamanho - 1)
                    coluna = random.randint(0, tamanho - barco[1])
                    orientacao = random.choice(['h', 'v'])
                for i in range(barco[1]):
                    if orientacao == 'h':
                        tabuleiro_j2[linha][coluna + i] = 'n'
                    elif orientacao == 'v':
                        tabuleiro_j2[linha + i][coluna] = 'n'
        logger(arquivo_log, "Barcos da máquina colocados no tabuleiro.")
        
    clear()

    # Início de ataques
    while True:
        print(Fore.YELLOW + "turno do jogador 1:\n")
        PrintBoard(tiros_j1)
        tabuleiro_j2, tiros_j1, acertou = realizar_ataque(tabuleiro_j2, tiros_j1)
        if acertou:
            acertos_j1 += 1
        quantidade_tiros_j1 += 1
        if vitoria(tabuleiro_j2):
            print(Fore.GREEN + "jogador 1 venceu!")
            break

        print(Fore.YELLOW + "turno do jogador 2:\n")
        if modo == 1:
            PrintBoard(tiros_j2)
            tabuleiro_j1, tiros_j2, acertou = realizar_ataque(tabuleiro_j1, tiros_j2)
            if acertou:
                acertos_j2 += 1
            quantidade_tiros_j2 += 1
            if vitoria(tabuleiro_j1):
                print(Fore.GREEN + "jogador 2 venceu!")
                break
        else:
            tabuleiro_j1, tiros_j2, acertou = ataque_ia(tabuleiro_j1, tiros_j2)
            if acertou:
                acertos_j2 += 1
            quantidade_tiros_j2 += 1
        turno += 1
        logger(arquivo_log, f"Turno {turno}: Jogador 1 - Tiros: {quantidade_tiros_j1}, Acertos: {acertos_j1}; Jogador 2 - Tiros: {quantidade_tiros_j2}, Acertos: {acertos_j2}")
        clear()
      
    #Mostra es estatísticas do jogo
    print(Fore.MAGENTA + Style.BRIGHT + f"\nEstatísticas do jogo:")
    print(Fore.CYAN + Style.BRIGHT + f"Jogador 1 - Tiros: {quantidade_tiros_j1}, Acertos: {acertos_j1}")
    print(Fore.CYAN + Style.BRIGHT + f"Jogador 2 - Tiros: {quantidade_tiros_j2}, Acertos: {acertos_j2}")
    logger(arquivo_log, f"Estatísticas do jogo: Jogador 1 - Tiros: {quantidade_tiros_j1}, Acertos: {acertos_j1}; Jogador 2 - Tiros: {quantidade_tiros_j2}, Acertos: {acertos_j2}")

    #Verifica se quer continuar jogando
    continuar = input(Fore.CYAN + Style.BRIGHT + "Deseja jogar novamente? (s/n): ").lower()
    while continuar not in ['s', 'n']:
        print(Fore.RED + "Opção inválida. Tente novamente.")
        continuar = input(Fore.CYAN + Style.BRIGHT + "Deseja jogar novamente? (s/n): ").lower()
    if continuar == 's':
        main()
    else:
        print(Fore.GREEN + Style.BRIGHT + "Obrigado por jogar Batalha Naval!")
        logger(arquivo_log, "Jogo encerrado pelo usuário.")  

if __name__ == "__main__":
    main()