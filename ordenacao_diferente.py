intervalo = list(range(0,300))
res = sorted(intervalo, key=lambda ele: len(
    [ele for idx in range(1, ele) if ele % idx == 0]))
print(res)
