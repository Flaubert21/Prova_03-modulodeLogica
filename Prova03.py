n = 8
chances = 2
N_de_tentativas = 0

while N_de_tentativas <= chances:
    tentativa = int(input("Tente adivinhar qual o número certo de 1 a 10. (Você tem 3 chances):"))
    N_de_tentativas +=1

    if tentativa == n:
        print("Parabéns, você acertou.")
        break
    elif tentativa < n:
        print("O número é maior, tente novamente")
    elif tentativa > n:
        print("O número é menor, tente novamente")
else:
    print(f"Você perdeu, o número era {n}.")        


