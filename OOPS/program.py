class calculator:

    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b
    
    def subtraction(self):
        return self.a - self.b
    
    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b
    
c = calculator(20,10)
print(c.addition())
print(c.subtraction())
print(c.multiplication())
print(c.division())