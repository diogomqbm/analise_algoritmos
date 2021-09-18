intervalo = list(range(0,200))
res = sorted(intervalo, key=lambda ele: len(
    [ele for idx in range(1, ele) if ele % idx == 0]))
casos = []
while True:
    caso = int(input())
    if caso == 0:
        break
    casos.append(caso)
for i in casos:
    print("Caso {}: {}".format(i, res.index(i)))
