import random
class customer:
    def __init__(self,id):
        self.id=id
        self.isBuying=None
        self.basePurchaseThreshold=None
        self.maxPrice=None
        self.getBasePurchaseThreshold()
        self.getBaseMaxPrice()
        
    def getBasePurchaseThreshold(self):
        self.basePurchaseThreshold=random.randint(0,100)
    
    def getBaseMaxPrice(self):
        self.maxPrice='%.2f'%(random.uniform(.01,.2))