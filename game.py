import day
import player
import random
import time
import os


class game:
    def __init__(self):
        self.player=None
        self.dayVal=1
        self.createPlayer()
        self.today=None
    
    def userInterface(self):
        self.clear()
        print('Day ',self.dayVal)
        print('You have '+'%.2f'%(float(self.player.wallet.money))+' Dollars')
        for stock in self.player.stand.inventory.listInventory:
            print('You have '+str(stock.qty)+' '+stock.name)
        print('Forecast for today is '+str(self.today.possibleCustomers.weather.forecastTemprature)+' and '+self.today.possibleCustomers.weather.forecastConditions.name)
        action=(input('What would you like to do [1]Store [2]Change Recipie [3]Start the Day: '))
        if action==str(1):
            self.store()
        elif action==str(2):
            self.recipie()
        elif action==str(3):
            self.runDay()
        else:
            print('not a valid action')
            time.sleep(2)
            return(self.userInterface())
    
    def store(self):
        print('Store')
        print('Money:'+str(self.player.wallet.money))
        for product in self.player.devMart.listProducts:
            print('['+str(product.id)+']'+product.name+' '+str(product.price))
        print('[13] Nothing, Go Back')
        action=self.convertToInt(input('What would you like to buy: '),self.store)
        if action == 13:
            self.userInterface()
        elif action in range(1,13):
            self.makeStorePurchase(action,self.store)
        else:
            print('not a valid selection')
            return(self.store())
    
    def makeStorePurchase(self,action,returnFunction):
        for product in self.player.devMart.listProducts:
            if action == product.id:
                if float(self.player.wallet.money)<float(product.price):
                    print("You can't afford that!")
                    return returnFunction()
                self.player.wallet.money=(float(self.player.wallet.money)-float(product.price))
                for stock in self.player.stand.inventory.listInventory:
                    if stock.id==product.inventoryId:
                        stock.qty=(stock.qty+product.qty)
                        print(stock.qty)
                        print ('You bought '+product.name)
                        return returnFunction()
    
    def recipie(self):
        print('Current Recipie is '+str(self.player.stand.recipie.useQtyLemons)+' Lemons, '+str(self.player.stand.recipie.useQtySugar)+' Sugar, '+str(self.player.stand.recipie.useQtyIce)+' Ice and you are selling it for '+('%.2f'%(self.player.stand.recipie.price)))
        action=(input('What would you like to change [1]Sugar [2]Lemons [3]Ice [4]Price [5]Nothing, Go Back: '))
        action=self.convertToInt(action,self.recipie)
        if action==1:
            self.player.stand.recipie.useQtySugar=int(input('how many to use?: '))
            return(self.recipie())
        elif action==2:
            self.player.stand.recipie.useQtyLemons=int(input('how many to use?: '))
            return(self.recipie())
        elif action==3:
            self.player.stand.recipie.useQtyIce=int(input('how many to use?: '))
            return(self.recipie())
        elif action==4:
            self.player.stand.recipie.price=float(input('sell for?: '))
            return(self.recipie())
        elif action==5:
            self.userInterface()
        else:
            print ('Not a valid choice')
            return (self.recipie())
               
               
        print('not a valid action')
        return(self.recipie())
        
    def runDay(self):
        print('Weather today was '+str(self.today.possibleCustomers.weather.temprature)+' and '+self.today.possibleCustomers.weather.conditions.name)
        for customer in self.today.possibleCustomers.listCustomers:
            checkBuy=(random.randint(1,100))
            chanceBuy=(customer.basePurchaseThreshold)
            self.checkBuying(customer,chanceBuy,checkBuy)
            self.buy(customer)
        self.endDay()
    
    def buy(self,customer):
        if customer.isBuying==True:
            time.sleep(.5)
            if self.player.stand.getCupLemonade()==False:
                self.endDay()
            else:
                self.takeMoney()
                print('Customer '+str(customer.id)+' bought a lemonade')
    
    def checkBuying(self,customer,chanceBuy,checkBuy):
        if chanceBuy < checkBuy:
            customer.isBuying = True
            if self.player.stand.recipie.price>customer.maxPrice:
                customer.isBuying = False
        else:
            customer.isBuying = False
    
    def createNewDay(self):    
        self.today=day.day(('Day '+str(self.dayVal)),self.dayVal)
        
    def createPlayer(self):
        self.player=player.player(input('What is your name: '))
    
    def convertToInt(self,value,originalFunction):
        try:
            return(int(value))
        except:
            print('not a valid selection')
            return originalFunction()
    
    def takeMoney(self):
        self.player.wallet.money=(float(self.player.wallet.money)+float(self.player.stand.recipie.price))
                    
    def endDay(self):
        if self.dayVal==7:
            time.sleep(5)
            return(self.endGame())
        else:
            print('End of day')
            time.sleep(5)
            self.dayVal=(self.dayVal+1)    
            self.createNewDay()
            return(self.userInterface())
        
    def endGame(self):
        self.clear()
        print(self.player.name+' You finished with '+str(self.player.wallet.money)+' dollars!')
        print('Game Over')
        os.system('exit')
    
    def clear(self):
        return os.system('cls')
        
    
begin=game()
begin.createNewDay()
begin.userInterface()