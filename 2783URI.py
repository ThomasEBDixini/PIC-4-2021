n, c, m = input().split(" ")                    # Recebe o total de Espaços no Album, Total de Figurinhas Carimbadas e o Total de Figurinhas Compradas
carimbadas = input().split(" ")                 # Diz quais são as Figurinhas Carimbadas
compradas = input().split(" ")                  # Diz quais são as Figurinhas Compradas
tenho = 0
aux = 0
for i in range(len(carimbadas)):                #|
    for k in range(len(compradas)):             #| > Compara uma lista com a outra
        if carimbadas[i] == compradas[k]:       #|
            aux += 1
    if aux >= 1:                                #|
        tenho +=1                               #| > Adicionas as figurinhas carimbadas já compradas a uma variavel
        aux = 0                                 #|
print(int(c) - tenho)              # → Imprimi a quantidade de Carimbadas que faltam.
