
import inventory
import pitcher
import recipie

class lemonadestand:
    def __init__(self):
        self.inventory=None
        self.pitcher=None
        self.recipie=None
        self.getStandContents()
        
    def getStandContents(self):
        self.inventory=inventory.inventory()
        self.pitcher=pitcher.pitcher()
        self.recipie=recipie.recipie()
    
    def getPitcherLemonade(self):
        self.pitcher.volumeOz=128
        self.hasCup=True
        if self.inventory.lemons.qty<self.recipie.useQtyLemons:
            print('You ran out of lemons!')
            return False
        else:
            self.inventory.lemons.qty=(self.inventory.lemons.qty-self.recipie.useQtyLemons)
        if self.inventory.sugar.qty<self.recipie.useQtySugar:
            print('You ran out of sugar!')
            return False
        else:
            self.inventory.sugar.qty=(self.inventory.sugar.qty-self.recipie.useQtySugar)
    
    def getCupLemonade(self):
        startVolume=self.inventory.cups.volumeOz
        volumeIce=self.recipie.useQtyIce
        if self.inventory.cups.qty==0:
            print('You ran out of cups')
            return False
        if self.inventory.ice.qty<self.recipie.useQtyIce:
            print('You ran out of Ice')
            return False
        self.inventory.cups.qty=(self.inventory.cups.qty-1)
        self.inventory.ice.qty=(self.inventory.ice.qty-self.recipie.useQtyIce)
        remainingVolume=(startVolume-volumeIce)
        if self.pitcher.volumeOz<remainingVolume:
            self.getPitcherLemonade()        
            if self.pitcher.volumeOz == False:
                return False
            self.pitcher.volumeOz=(self.pitcher.volumeOz-remainingVolume)
        else:
            self.pitcher.volumeOz=(self.pitcher.volumeOz-remainingVolume)
        