
import numpy as np

matrix = np.array([[9, 6, 0, 11, 12], [8, 5, 6, 7, 11], [2, 11, 5, 1, 11], [8, 5, 12, 3, 2], [4, 8, 12, 8, 12]])
p = [0.36, 0.0, 0.12, 0.29, 0.22]
q = [0.4, 0.5, 0.09, 0.02, 0.0]

answer = {}

lower_price = max([min(x) for x in matrix])
upper_price = min([max(x) for x in np.rot90(matrix)])  

if lower_price == upper_price:
    print("седловая точка есть", f"ответ v = {lower_price}")
else:
    buff = 0
    for i, pin in zip(matrix, p):
        buff += pin * sum([x * y for x, y in zip(i, q)])
    answer["H(P,Q)"] = buff
    for k, i in enumerate(np.rot90(matrix), 1):   # enumerate нумерует, то есть мы получает сразу индекс элемента и его значение.
        answer["H(P,B{})".format(k)] = sum([x * y for x, y in zip(i, p)])
for i in [(x, y) for x, y in answer.items()]:
    print("Ответ выйгрыш игрока А в ситуации {0[0]} = {0[1]}".format(i))
