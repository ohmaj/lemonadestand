import random
import customer
import weather
class possiblecustomers:
    def __init__ (self):
        self.basePossibleCustomers=None
        self.adjustedPossibleCustomers=None
        self.weather=weather.weather()
        self.listCustomers=[]
        self.getBasePossibleCustomers()
        self.getAdjustedPossibleCustomers()
        self.createListCustomers()
    
    def getBasePossibleCustomers(self):
        self.basePossibleCustomers=random.randint(60,90)
        
    def getAdjustedPossibleCustomers(self):
        baseCustomers=self.basePossibleCustomers
        self.adjustedPossibleCustomers=(baseCustomers+(4*(self.weather.conditions.value)))
    
    def createListCustomers(self):
        id=0
        while id<self.adjustedPossibleCustomers:
            id=id+1
            actualCustomer=customer.customer(id)
            actualCustomer.maxPrice=(float(actualCustomer.maxPrice)+(float(self.weather.temprature)/200))
            self.listCustomers.append(actualCustomer)