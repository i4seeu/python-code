class Car:
    def __init__(self, engine, tires,year,color):
        self.engine = engine
        self.tires = tires
        self.year = year
        self.color = color
    def setEngine(self, engine):
        self.engine = engine
    def getEngine(self):
        return self.engine
    def setTires(self, tires):
        self.tires = tires
    def getTires(self):
        return self.tires
class Audi(Car):
    def __init__(self, engine, tires, year,color):
        Car.__init__(self,engine,tires,year,color)

r8 = Audi("beam 2000",4, "1994","Black")
engine = r8.getEngine()
print(engine)
r8.setEngine("AUdi Engine")
engine = r8.getEngine()
print(engine)