class Person:
    
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
        
    @tracer
    def giveRaise(self, percent): # giveRaise = tracer(giveRaise)
        self.pay *= (1.0 + percent)
        
    @tracer
    def lastName(self): # lastName = tracer(lastName)
        return self.name.split()[-1]
