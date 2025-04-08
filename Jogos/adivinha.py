import random

def jogo():
    numero_secreto = random.randint(1, 100)
    print("Escolha o nível de dificuldade:")
    print("1 - Fácil (20 tentativas)")
    print("2 - Médio (10 tentativas)")
    print("3 - Difícil (5 tentativas)")
    print("4 - Brutal (3 tentativas)")
    print("5 - Lucky (1 tentativa)")
    
    while True:
        try:
            nivel = int(input("Digite o número correspondente ao nível: "))
            if nivel not in [1, 2, 3, 4, 5]:
                raise ValueError
            break
        except ValueError:
            print("Nível inválido. Por favor, escolha um número de 1 a 5.")
    
    total_de_tentativas = {1: 20, 2: 10, 3: 5, 4: 3, 5: 1}[nivel]

    for rodada in range(1, total_de_tentativas + 1):
        print(f"Tentativa {rodada} de {total_de_tentativas}")
        try:
            valor_escolhido = int(input("Digite um número entre 1 e 100: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        if valor_escolhido < 1 or valor_escolhido > 100:
            print("Número inválido. O número deve estar entre 1 e 100.")
            continue

        if valor_escolhido == numero_secreto:
            print(f"Parabéns! Você acertou o número secreto ({numero_secreto}) em {rodada} tentativa(s)!")
            return True
        elif valor_escolhido > numero_secreto:
            print("Chute errado. Escolha um número MENOR que o número secreto.")
        else:
            print("Cute errado. Escolha um número MAIOR que o número secreto.")
    
    print(f"Você perdeu! O número secreto era {numero_secreto}.")
    return False

def main():
    print("Tente adivinhar o número secreto entre 1 e 100.")
    print("Você poderá escolher o nível de dificuldade para determinar o número de tentativas.")
    
    while True:
        _ = jogo()
        jogar_novamente = input("Deseja jogar novamente? (S/N): ").strip().lower()
        if jogar_novamente != 's':
            print("Obrigado por jogar! Até a próxima!")
            break

if __name__ == "__main__":
    main()
