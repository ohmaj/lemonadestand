import wallet
import store
import lemonadestand

class player:
    def __init__(self,name):
        self.name=name
        self.wallet=None
        self.devMart=None
        self.stand=None
        self.createPlayerAttributes()
    
    def createPlayerAttributes(self):
        self.wallet=wallet.wallet(20)
        self.devMart=store.store()
        self.stand=lemonadestand.lemonadestand()