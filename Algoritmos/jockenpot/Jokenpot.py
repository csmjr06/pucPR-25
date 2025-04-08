"""
Funcionalidades
✅ Solicite a entrada do nome dos jogadores.
✅ Permita dois modos de jogo:

Jogador vs Computador (IA) → O computador fará sua escolha de forma aleatória (random).

Jogador vs Jogador → Dois jogadores inserem suas escolhas manualmente.
✅ O jogo deve seguir as regras tradicionais:

Pedra vence Tesoura.

Tesoura vence Papel.

Papel vence Pedra.

✅ Deve exibir o vencedor da rodada ou indicar empate.
✅ Deve permitir múltiplas rodadas até que o jogador decida encerrar.
✅ O jogo deve armazenar e exibir o histórico de partidas, incluindo o número de vitórias de cada jogador e empates.
"""
def jokenpot():
    """
    User choose rock, paper or scissors. 
    """
    import random
    from time import sleep
    print("=-=" * 20)
    print("Bem-vindo ao Jokenpô!")

    game_mode = input("Escolha o modo de jogo (1 - Jogador vs Computador, 2 - Jogador vs Jogador): ")
    while game_mode not in ["1", "2"]:
        print("Modo de jogo inválido. Tente novamente.")
        game_mode = input("Escolha o modo de jogo (1 - Jogador vs Computador, 2 - Jogador vs Jogador): ")
    if game_mode == "1":
        player1 = input("Digite seu nome: ")
        player2 = "Computador"
        print(f"{player1} vs {player2}")
    else:
        player1 = input("Digite o nome do jogador 1: ") 
        player2 = input("Digite o nome do jogador 2: ")
        print(f"{player1} vs {player2}")
    history = []
    player1_wins = 0
    player2_wins = 0
    ties = 0
    
    while True:
        if game_mode == "1":
            player1_choice = input(f"{player1}, escolha (Pedra, Papel ou Tesoura): ").lower()
            player2_choice = random.choice(["pedra", "papel", "tesoura"])
            print(f"{player2} escolheu: {player2_choice}")
        else:
            player1_choice = input(f"{player1}, escolha (Pedra, Papel ou Tesoura): ").lower()
            player2_choice = input(f"{player2}, escolha (Pedra, Papel ou Tesoura): ").lower()

        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PÔ!!!')
        print('-=-' * 20)        
        if player1_choice == player2_choice:
            print("Empate!")
            ties += 1
        elif (player1_choice == "pedra" and player2_choice == "tesoura") or \
             (player1_choice == "tesoura" and player2_choice == "papel") or \
             (player1_choice == "papel" and player2_choice == "pedra"):
            print(f"{player1} venceu!")
            player1_wins += 1
        else:
            print(f"{player2} venceu!")
            player2_wins += 1

        history.append((player1_choice, player2_choice))
        
        play_again = input("Deseja jogar novamente? (s/n): ").lower()
        if play_again != 's':
            break
    print("\nHistórico de partidas:")
    for i, (p1, p2) in enumerate(history):
        print(f"Rodada {i + 1}: {player1} escolheu {p1}, {player2} escolheu {p2}") 
    print(f"\nResultados finais:")
    print(f"{player1}: {player1_wins} vitórias")
    print(f"{player2}: {player2_wins} vitórias")
    print(f"Empates: {ties}")
if __name__ == "__main__":
    while True:
        jokenpot()
        sair = input("Deseja sair do jogo? (s/n): ").lower()
        if sair == 's':
            print("Obrigado por jogar! Até a próxima.")
            break

