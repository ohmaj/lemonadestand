import possiblecustomers

class day:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.possibleCustomers=None
        self.getListCustomers()    
     
    def getListCustomers(self):
        self.possibleCustomers=possiblecustomers.possiblecustomers()