def check_if_substring_3(string, substring):
    set_ = set()
    slice_size = len(substring)
    for idx, char in enumerate(string):
        cut_to = idx + slice_size
        if substring == string[idx:cut_to]:
            return 's'  
    return 'n'

# def check_if_substring(string, substring):
#     mapper = create_mapper(string, substring)
#     try:
#         return mapper[substring]
#     except:
#         return 'n'

# def check_if_substring_2(string, substring):
#     if substring in string:
#         return 's'
#     else:
#         return 'n'

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
            resultados.append(check_if_substring_3(string, padrao))

print("\n".join(resultados))       
