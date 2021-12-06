n = int(input())             # Quantidade de números que serão ordenados
z = 0                        # Variável acumuladora
par = []                     # Lista de números pares a serem ordenados
impar = []                   # Lista de números ímpares a serem ordenados
while z < n:                 # Enquanto o acumulador z for menor que a quantidade de números a serem ordenados
    x = int(input())         # Variável x recebendo um valor
    if x % 2 == 0:           # Se o valor que está em x for par
        par.append(x)        # Será adicionado a lista par
    else:                    # Se for ímpar
        impar.append(x)      # Será adicionado a lista ímpar
    z += 1                   # Variável acumulando 1 a cada volta no while
par.sort()                   # Colocando a lista par em ordem crescente
impar.sort(reverse=True)     # Colocando a lista ímpar em ordem decrescente
for i in range(len(par)):    # "i" indo da primeira posição da lista até a última
    print(par[i])            # Printando cada posição da lista par
for i in range(len(impar)):  # "i" indo da primeira posição da lista até a última
    print(impar[i])          # Printando cada posição da lista ímpar
