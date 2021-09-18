# recebo o numero de casos de teste (string)
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
            n = len(padrao)
            if m >= n:
                #checa todas as posicoes onde o padrao pode ocorrer
                for x in range(m - n + 1):
                    y = 0
                    #comparo cada caracter do padrao com do texto
                    while(y < n):
                        if(string[x + y] != padrao[y]):
                            break
                        y+= 1
                    if(y == n):
                        resultados.append('s')
                        break
                    elif (x == (m-n) and y < n): 
                        resultados.append('n')        
            else:
                resultados.append('n')

print("\n".join(resultados))       
