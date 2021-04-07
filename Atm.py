class Atm(object):
    def __init__(self,company,color):
        self.color=color
        self.company=company
        
    def withdraw100(self):
        print(" withdrew100 ")

    def deposit100(self):
        print(" deposited100 ")
    
    def deposit1000(self):
        print(" deposited1000 ")

    def withdraw1000(self):
        print(" withdrew1000 ")

Atm1 = Atm("triton","red")

Atm1.deposit100()

