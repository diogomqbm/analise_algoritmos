num = int(input())
arr_k = [0]*num
i=0 
for i in range(len(arr_k)):
    if i == 0:
        arr_k[i] = 'K'
    else:
        arr_k[i] = 'k'
print('{}!'.format(''.join(arr_k)))
