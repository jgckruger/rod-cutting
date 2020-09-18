from classes.recursive import Recursive
from classes.dynamic import Dynamic

rec_calls = []
dyn_calls = []
N = 20
x = list(range(2, N))

for i in x:
    sizes = list(range(1,i))
    prices = list(range(1,i))

    rec = Recursive(i, sizes, prices)
    dyn = Dynamic(i, sizes, prices)

    rec.solve()
    rec_calls.append(sum(rec.calls))
    dyn.solve()
    dyn_calls.append(sum(dyn.calls))

import matplotlib.pyplot as plt
plt.plot(x, rec_calls)
plt.plot(x, dyn_calls)
plt.ylabel('log(Number of calls)')
plt.xlabel('N')
plt.yscale('log')
plt.legend(('Recursive - $\\theta(2^n)$', 'Dynamic Programming (Memoization) - $\\theta(n^2)$'),
           loc='upper left')
plt.show()