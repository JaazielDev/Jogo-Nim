# Definição das variavéis 
# Na variável " Pilhas " está usando a função Listas, tendo a sequência de [0,1,2]
pilhas = [3, 4, 5]
jogador = 1

# Aqui e um loop, enquanto pilhas for diferente de [0,0,0] continue o jogo, realizando assim a repetição para dar continuidade no jogo / O print (pilhas), mostra como as pilhas estão naqueles momentos / O print (Jogador) mostra de quem e a vez
while pilhas != [0, 0, 0]:
    print(pilhas)
    print("Jogador", jogador)
# Aqui o primeiro input e para digitar a pilha qe quer mexer, o segundo input digita a quantidade que quer tirar da pilha
    p = int(input())
    q = int(input())
# Aqui ele faz a retirada da quantidade escolhida pelo jogador
    pilhas[p] = pilhas[p] - q
# Aqui e a parte que entende quando e a vez de cada jogador, se o jogador 1 jogou, logo após vai ser a vez do jogador 2
    if jogador == 1:
        jogador = 2
    else:
        jogador = 1
# No fim, aqui e quando acaba o jogo, realizando o print final
print("Fim de jogo")
