def ordena_vagoes(array_vagoes):
    num_inversoes = 0
    n = len(array_vagoes)
    for i in range(n):
        for j in range(i + 1, n):
            if (array_vagoes[i] > array_vagoes[j]):
                num_inversoes += 1
 
    return num_inversoes
 
num_casos_teste = int(input())
lista_ajeitamentos = []
for i in range(num_casos_teste):
    num_vagoes = int(input())
    if num_vagoes > 0:
        vagoes = list(map(int, input().split()))
        if len(vagoes) != num_vagoes:
            exit()
        num_ajeitamentos = ordena_vagoes(vagoes)
        lista_ajeitamentos.append(num_ajeitamentos)
for i in lista_ajeitamentos:
    print('A quantidade ajeitamentos deve ser {}.'.format(i))
