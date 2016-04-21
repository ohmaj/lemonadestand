import products

class store:
    def __init__(self):
        self.listProducts=self.createListProducts()
    
    def createListProducts(self):
        lemons30=products.products('Tray(30) Lemons',1,1,30,2)
        lemons50=products.products('Box(50) Lemons',2,1,50,3)
        lemons80=products.products('Case(80) Lemons',3,1,80,4.50)
        sugar25=products.products('Small Bag(25) Sugar',4,2,25,3)
        sugar40=products.products('Large Bag(40) Sugar',5,2,40,5)
        sugar75=products.products('Sack(75) Sugar',6,2,75,8.50)
        ice125=products.products('Small Bag(125) Ice',7,3,125,1.50)
        ice300=products.products('Large Bag(300) Ice',8,3,300,3)
        ice500=products.products('Case(500) Ice',9,3,500,4.50)
        cups20=products.products('Sleeve(20) Cups',10,4,20,1)
        cups180=products.products('Pack(180) Cups',11,4,180,6)
        cups720=products.products('Case(720) Cups',12,4,720,15)
        createList=(lemons30,lemons50,lemons80,sugar25,sugar40,sugar75,ice125,ice300,ice500,cups20,cups180,cups720)
        return (createList)