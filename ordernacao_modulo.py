def is_odd(number):
    if number % 2 != 0:
      return True
    else:
      return False
def sort_dict(dict_elemento_mod):
  order_output = []
  sem_elemento = dict_elemento_mod.copy()
  menor_mod_anterior = 0
  elemento_menor_mod_anterior = 0
  while sem_elemento:
    menor_mod = list(sem_elemento.values())[0]
    elemento_menor_mod = list(sem_elemento)[0]
    for i, j in sem_elemento.items():
      if j < menor_mod:
        menor_mod = j
        elemento_menor_mod = i
    if menor_mod == menor_mod_anterior and len(order_output) != 0:
      if is_odd(elemento_menor_mod) == True and is_odd(elemento_menor_mod_anterior) == True:
        if elemento_menor_mod > elemento_menor_mod_anterior:
            order_output.insert(len(order_output)-1, elemento_menor_mod)
            sem_elemento.pop(elemento_menor_mod)
      elif is_odd(elemento_menor_mod) == True and is_odd(elemento_menor_mod_anterior) == False:
            order_output.insert(len(order_output)-1, elemento_menor_mod)
            sem_elemento.pop(elemento_menor_mod)
      else:
        if elemento_menor_mod < elemento_menor_mod_anterior:
          order_output.insert(len(order_output)-1, elemento_menor_mod)
          sem_elemento.pop(elemento_menor_mod)
    else:
      order_output.append(elemento_menor_mod)
      menor_mod_anterior = menor_mod
      elemento_menor_mod_anterior = elemento_menor_mod
      sem_elemento.pop(elemento_menor_mod)
  return order_output

while True:
  print(" TA AQUI")
  N, M = map(int, input().split())
  if N == 0 and M == 0:
    break
  elemento_mod = {}
  for i in range(N):
    print(f'input {i}')
    elemento = int(input())
    mod = abs(elemento) % M
    if elemento < 0:
      mod = - mod
    elemento_mod[elemento] = mod
  lista_ordenada = sort_dict(elemento_mod)
  print("passou aqui 1")
  print('{} {}'.format(N, M))
  for elemento in lista_ordenada:
    print(elemento)
print("0 0")

  
