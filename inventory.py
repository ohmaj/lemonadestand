import cup
import lemons
import sugar
import ice
class inventory:
    def __init__(self):
        self.cups=None
        self.lemons=None
        self.sugar=None
        self.ice=None
        self.listInventory=[]
        self.getInventory()
        
    def getInventory(self):
        self.cups=cup.cup(4,'Cups',0,12)
        self.lemons=lemons.lemons(1,'Lemons',0)
        self.sugar=sugar.sugar(2,'sugar',0)
        self.ice=ice.ice(3,'ice',0)
        self.listInventory=(self.cups,self.lemons,self.sugar,self.ice)