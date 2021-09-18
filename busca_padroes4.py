def check_if_substring_2(string, substring):
    if substring in string:
        return 's'
    else:
        return 'n'

casos = int(input())
resultados = []
if casos == 0:
    exit()
else:
    for i in range(casos): 
        # recebo a primeira string referente ao numero de casos de teste
        string = str(input())
        m = len(string)
        # recebo o numero de consultas (padroes)
        consultas = int(input())
        for k in range(consultas):
            padrao = str(input())
            resultados.append(check_if_substring_2(string, padrao))

print("\n".join(resultados))    