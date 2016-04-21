
class products:
    def __init__(self,name,id,inventoryId,qty,price):
        self.name=name
        self.id=id
        self.inventoryId=inventoryId
        self.qty=qty
        self.price='%.2f'%(float(price))