planetas_mins = []
while True:
    num_mensagens = int(input())
    if num_mensagens == 0:
        break
    elif (num_mensagens >= 1) and (num_mensagens <= 100):
        i = 0
        planeta_min = {
          "nome": "",
          "ano": 0,
          "decorridos": 0,  
          "envio": 0
        }
        for i in range(num_mensagens):
          nome, ano, decorridos  = str(input()).split()
          ano = int(ano)
          decorridos = int(decorridos)
          ## se o planeta_min ja existe
          if (planeta_min["nome"] == ""):
            planeta_min["nome"] = nome
            planeta_min["ano"] = ano
            planeta_min["decorridos"] = decorridos
            planeta_min["envio"] = ano - decorridos
          ## atribui para o atual
          else:
            if (planeta_min["envio"] > (ano - decorridos)):
              planeta_min["nome"] = nome
              planeta_min["ano"] = ano
              planeta_min["decorridos"] = decorridos
              planeta_min["envio"] = ano - decorridos
        planetas_mins.append(planeta_min)

if len(planetas_mins) == 0:
  exit()
else:
  for planeta in planetas_mins:
    print(planeta["nome"]) 
