intervalo = list(range(0,2000001))
res = sorted(intervalo, key=lambda ele: len(
    [ele for idx in range(1, ele) if ele % idx == 0]))
casos = []
while True:
    caso = int(input())
    casos.append(caso)
    if caso == 0:
        break
for i in casos:
    print("Caso {}: {}".format(i, res.index(i)))
