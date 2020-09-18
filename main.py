from classes.recursive import Recursive
from classes.dynamic import Dynamic

rec = Recursive(4, [1, 2, 3, 4, 5, 6, 7, 8], [1, 5, 8, 9, 10, 17, 17, 20])
dyn = Dynamic(4, [1, 2, 3, 4, 5, 6, 7, 8], [2, 4, 7, 9, 11, 16, 19, 21])

print("Recursive Solution")
print(rec.solve())
print("Total Calls: ", sum(rec.calls))
print("Calls: ", rec.calls)
print("")

print("Dynamic Solution")
print(dyn.solve())
print("Total Calls: ", sum(dyn.calls))
print("Calls: ", dyn.calls)
print("")