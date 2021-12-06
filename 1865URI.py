c = int(input())                            # Pega a quantidade de casos de Teste
z = 0
while z < c:                                # Repete o programa de acordo com a quantidade de casos de Teste
    nome, forca = input().split(" ")        # Recebe o primeiro nome e a força aplicada

    if nome != 'Thor':                      #|
        print('N')                          #|
    else:                                   #| → # Uma condição pra ver se a pessoa conseguiu ou não levantar o martelo
        print('Y')                          #|
    z += 1
