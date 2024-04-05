class Kot(object):
    def __init__(self, mass, age, name, poroda):
        self.mass = mass
        self.age = age
        self.name = name

        self.poroda = poroda
    def meow(self):
        print("мяу")
    
    def hurt(self):
        print("'царапаю'")
    
    def getName(self):
        print("май неэм из " + self.name)

    def showInfo(self):
        print("меня зовут:" + self.name)
        print("мой возраст: " + str(self.age))
        print("моя порода: " + self.poroda)
        print("моя масса: " + str(self.mass))

    def grow(self):
        print("мне " + str(self.age)  + " год/года/лет")
        print("через год...")
        self.age += 1
        print("мне теперь " + str(self.age))

cat1 = Kot(mass = 3, age = 5, name = "Vasya", poroda = "Egipet")

cat1.meow()
cat1.grow()