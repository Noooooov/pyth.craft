class Machina(object):
    def __init__(self, mass, age, marka):
        self.mass = mass
        self.age = age
        self.name = marka
    
    def beep(self):
        print("бип-бип")
    
    def drive(self):
        print("'едет'")

    def showInfo(self):
        print("моя марка: " + self.name)
        print("мой возраст: " + str(self.age))
        print("моя масса: " + str(self.mass))

    def setOlder(self):
        print("мне " + str(self.age)  + " год/года/лет")
        print("через год...")
        self.age += 1
        print("мне теперь " + str(self.age))

machina1 = Machina(mass = 1650, age = 10, marka = "LADA")

machina1.showInfo()
machina1.drive()