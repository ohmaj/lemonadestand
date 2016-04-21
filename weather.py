import random
import condition
class weather:
    def __init__(self):
        self.listConditions=None
        self.temprature=None
        self.conditions=None
        self.forecastTemprature=None
        self.forecastConditions=None
        self.createListConditions()
        self.getTemprature()
        self.getConditions()
        self.getForecastTemprature()
        self.getForecastConditions()
    
    def createListConditions(self):
        sunny=condition.condition('sunny',4)
        partlyCloudy=condition.condition('Partly Cloudy',3)
        overcast=condition.condition('Overcast',2)
        drizzle=condition.condition('Drizzly',1)
        rain=condition.condition('Rainy',0)
        self.listConditions=(sunny,partlyCloudy,overcast,drizzle,rain)
    
    def getTemprature(self):
        self.temprature=random.randint(60,100)
    
    def getConditions(self):
        randomCondition=random.choice(self.listConditions)
        self.conditions=randomCondition
    
    def getForecastTemprature(self):
        self.forecastTemprature=(self.temprature+(random.randint(-5,5)))
    
    def keepForcastWithinListConditions(self,forecastNumber):
        if forecastNumber not in [option.value for option in self.listConditions]:
            return(self.conditions.value)
        else:
            return(forecastNumber)
    
    def getForecastConditions(self):
        actualCondition=self.conditions.value
        randomNumber=random.randint(-1,1)
        forcastConditionValue=self.keepForcastWithinListConditions(actualCondition+randomNumber)
        self.forecastConditions=self.listConditions[forcastConditionValue]