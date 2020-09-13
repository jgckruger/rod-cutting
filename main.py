from classes.recursive import Recursive
from classes.dynamic import Dynamic

rec = Recursive(8, [1, 2, 3, 4, 5, 6, 7, 8], [2, 4, 7, 9, 11, 16, 19, 21])
dyn = Dynamic(8, [1, 2, 3, 4, 5, 6, 7, 8], [2, 4, 7, 9, 11, 16, 19, 21])
print(rec.solve())
print(dyn.solve())