class Cashier:
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.products, self.nr_customer = {}, 0
        self.discount, self.discount_at_n = discount, n
        
        for product in products:
            self.products[product] = prices.pop(0)
                
    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.nr_customer += 1
        
        total = 0.0
        for p in product:
            total += self.products[p] * amount.pop(0)
        
        if self.nr_customer == self.discount_at_n:
            self.nr_customer = 0
            total -= (self.discount * total) / 100
        
        return total