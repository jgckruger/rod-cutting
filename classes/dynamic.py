from classes.strategy import Strategy

class Dynamic(Strategy):
    def __init__(self, rod_size, sizes, prices):
        self.rod_size = rod_size
        self.sizes = sizes
        self.prices = prices
        self.solutions = {}
    
    def solve(self, rod_size = None, sizes = None, prices = None):
        if rod_size is None:
            rod_size = self.rod_size
        if sizes is None:
            sizes = self.sizes
        if prices is None:
            prices = self.prices

        solution = (0, [])

        if (rod_size < 0) or (rod_size < sizes[0]):
            return solution

        if rod_size in self.solutions:
            return self.solutions[rod_size]
        
        solutions = []
        for idx, _ in enumerate(sizes):
            price, size = self.get_size_price(idx)
            if((rod_size-size) >=0):
                rec_solution = self.solve(rod_size-size)
                solutions.append((rec_solution[0] + price, rec_solution[1] + [size]))
    
        self.solutions[rod_size] = max(solutions, key=lambda x: x[0])
        return self.solutions[rod_size]
            

    def get_size_price(self, idx):
        return (self.prices[idx], self.sizes[idx])
        
        