resultado_rodadas = []
while True:
    num_mensagens = int(input())
    if num_mensagens == 0:
        break
    elif (num_mensagens >= 1) and (num_mensagens <= 100):
        planeta_arr, ano_recebido_arr, anos_decorr_arr, ano_enviado_arr = ([] for i in range(4))
        i = 0
        for i in range(num_mensagens):
            nome_planeta, ano_recebido, anos_decorridos  = str(input()).split()
            if (nome_planeta.isalpha()) and (len(nome_planeta)>=1 and len(nome_planeta) <= 50):
                planeta_arr.append(nome_planeta)
                if (int(ano_recebido)>= 2021) and (int(ano_recebido) <= 3210):
                    ano_recebido_arr.append(int(ano_recebido))
                    if(int(anos_decorridos)>= 1) and (int(anos_decorridos)<= 1000):
                        anos_decorr_arr.append(int(anos_decorridos))
                        ano_enviado_arr.append(ano_recebido_arr[i] - anos_decorr_arr[i])
                    else:
                        exit()
                else:
                    exit()
            else:
                exit()

        min_ano = min(ano_enviado_arr)
        min_index = ano_enviado_arr.index(min_ano)
        print(min_ano)
        print(min_index)
        resultado_rodadas.append(planeta_arr[min_index])
    else:
        exit()

if len(resultado_rodadas) == 0: 
    exit()
else: 
    print('\n'.join(resultado_rodadas))
    exit()
    
        

    


