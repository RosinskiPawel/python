class Apiary:
    number_of_hives = 0
    
    def __init__(self, beekeeper):
        self.beekeeper = beekeeper
    def __str__(self) -> str:
        return f"My name is {self.beekeeper} and I have actually {self.number_of_hives} hives in my apiary."
           
        
class Hive(Apiary):
    
    queen_name = None #during the Hive creation the name of the queen is unknown
    
    def __init__(self, beekeeper, id, size, color, population, location, efficiency):
        super().__init__(beekeeper)
        self.id = id
        self.size = size
        self.color = color
        self.population = population
        self.location = location
        self.efficiency = efficiency
        Apiary.number_of_hives +=1
        
    
    def change_of_population(self, value):
        self.population = self.population + value
        return
    
    def name_of_queen(self, name):
        #this function has to be called after the queen has been created        
        Hive.queen_name = name
        return
    def __str__(self):
        return f"The Queen's name is: {self.queen_name}"

class Bee:
    def __init__(self, art, resident):        
        self.art = art
        self.resident = resident
        
                
class TheQueen(Bee):
    def __init__(self, art, resident, name, age, function, eggs_week):
        super().__init__(art, resident)
        self.name = name
        self.age = age
        self.function = function
        self.eggs_week = eggs_week
    
    def __str__(self):
        return f"I am the Queen {self.name}, I am {self.age} years old. I live in hive {self.resident} and I lay {self.eggs_week} eggs per week."
                

class Worker(Bee):
    def __init__(self, art, resident, name, age, function, strenght, speed, efficiency):
        super().__init__(art, resident)
        self.name = name 
        self.age = age     
        self.function = function
        self.strenght = strenght
        self.speed = speed
        self.efficiency = efficiency
    def __str__(self):
        return f"I am just a bee {self.art}, my name is {self.name} and I am {self.age} weeks old. My function is {self.function}, my fly speed is {self.speed} km/h. "


        
class Drone(Bee):
    def __init__(self, art, resident, name, age, function):
        super().__init__(art, resident)
        self.name = name 
        self.age = age       
        self.function = function
    def __str__(self):
        return f"my name is {self.name}, I am {self.age} weeks old, I live in hive number {self.resident} and my function is {self.function}.\n"
        
    
            
ul_1 = Hive('Goodman', '001', 'small', 'white', 10000, 'vanilla fields', 15)

xantor = Drone('beeEU', ul_1.id, "Xantor", 2,"drone")
print(xantor)

ul_21 = Hive('Goldfish', '002', 'medium', 'white', 15000, 'forrest', 13)

print(ul_21.queen_name)

xenia = TheQueen('beeEU', ul_21.id, "Xenia", 2, "The Queen", 2000)
print(xenia)
ul_21.name_of_queen(xenia.name)
print(ul_21.queen_name)
print(ul_21)
print(Apiary.number_of_hives)






