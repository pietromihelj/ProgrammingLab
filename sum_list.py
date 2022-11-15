
def sum_list(my_list):
    somma = 0
    for item in my_list:
        somma = somma + item
    return somma

lista_numeri = [1,4,7,-8,12]

print('{}'.format(sum_list(lista_numeri)))

