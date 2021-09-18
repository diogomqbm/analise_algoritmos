def calc_seq_sum(array):
    max_sum = 0
    max_of_round = 0
    for i in range(len(array)):
        max_of_round = max_of_round + array[i]
        if max_of_round < 0:
            max_sum = 0
        elif max_of_round > max_sum:
            max_sum = max_of_round
    return max_sum 

bets_max_sum = []

while True:
    num_bets_seq = int(input())
    if num_bets_seq == 0:
        break
    elif num_bets_seq <= 10000 :
        bets_seq = [0]*num_bets_seq
        i = 0
        for i in range(num_bets_seq):
             bets_seq[i] = float(input())
    print(bets_seq)
    bets_max_sum.append(calc_seq_sum(bets_seq))
    print(bets_max_sum)

for i in range(len(bets_max_sum)):
    if bets_max_sum[i] > 0:
        print('Maior sequência ganhadora é {}.'.format(bets_max_sum[i]))
    else:
        print('Sequência perdedora.')

        