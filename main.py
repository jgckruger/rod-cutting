from classes.recursive import Recursive
from classes.dynamic import Dynamic

rec = Recursive(8, [1, 2, 3, 4, 5, 6, 7, 8], [2, 4, 7, 9, 11, 16, 16, 21])
rec = Dynamic(8, [1, 2, 3, 4, 5, 6, 7, 8], [2, 4, 7, 9, 11, 16, 16, 21])
print(rec.solve())