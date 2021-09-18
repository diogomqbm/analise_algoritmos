def insertion_sort(arr):
    count = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                count += 1
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

    return count
 

num_casos_teste = int(input())
for i in range(num_casos_teste):
    lista_ajeitamentos = []
    num_vagoes = int(input())
    vagoes = list(map(int, input().split()))
    if len(vagoes) != num_vagoes:
        exit()
    num_ajeitamentos = insertion_sort(vagoes)
    lista_ajeitamentos.append(num_ajeitamentos)
    print('A quantidade ajeitamentos deve ser ' + str(num_ajeitamentos) + '.')