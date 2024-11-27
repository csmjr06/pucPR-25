import random

numero_secreto = random.randrange(1,101)
total_de_tentativas = 0

print("qual o nivel de dificuldade")
print("1 - facil, 2 - medio, 3 - dificil, 4 - brutal, 5 - lucky")
nivel = int(input("digite o nivel: "))

if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
    total_de_tentativas = 5
elif nivel == 4:
    total_de_tentativas = 3
elif nivel == 5:
    total_de_tentativas = 1
elif nivel < 1 or nivel > 5:
    print("numero invalido, tente novamente")

for rodada in range(1, total_de_tentativas + 1):
    print(f"tentativas {rodada} de {total_de_tentativas}")
    valor_escolhido_str = input("digite um numero entre 1 a 100: ")
    print("voce digitou ", valor_escolhido_str)
    valor_escolhido = int(valor_escolhido_str)

    if valor_escolhido < 1 or valor_escolhido > 100:
        print("numero invalido. o numero deve ser entre 1 a 100")
        continue
    acertou = valor_escolhido == numero_secreto
    maior = valor_escolhido > numero_secreto
    menor = valor_escolhido < numero_secreto

    if acertou:
        print(f"you won in {rodada} rounds")
        print("do you want to play again?")
        play_again = "null"
        while play_again != "n" or play_again != "N" or play_again != "y" or play_again != "Y":
            play_again = int(input("Y/N:"))
            continue
        if play_again = "y" or play_again ="Y":
        
    else:
        if maior :
            print("muito grande")
        elif menor :
            print("muito pequeno")

print("game over")