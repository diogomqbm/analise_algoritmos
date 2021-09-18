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
                    #colocar isso como indexador ???
                    string[0:n]   
                    string = string[x:m] 
            else:
                resultados.append('n')

print("\n".join(resultados))       


## AABCD
# for i in range(m-n+1)
# string pegar n primeiros
# coloco do dicionario
# remover o primeiro caracter da string 
# 
