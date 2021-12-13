

class Backpack():
    def __init__(self):
        super().__init__()
        self.color = (0, 0, 0)
        self.size = "small"
        self.items = []
        self.open = False

    def openBag(self):
        self.open = True
        print("The bag is now open")

    def closeBag(self):
        self.open = False
        print("The bag is now closed")
    
    def putin(self, item):
        self.items.append(item)
        print(self.items[-1] + " was added to your bag")

    def takeout(self, item):
        found = 0
        for i in range(len(self.items)):
            if self.items[i] == item:
                print(item + " was removed from your bag")
                found = 1
        if found == 0:
            print(item + " was not found in your bag")


backpack1 = Backpack()
backpack2 = Backpack()
backpack3 = Backpack()

backpack1.color = (0, 0, 255)
backpack2.color = (255, 0, 0)
backpack2.size = "medium"
backpack3.color = (0, 255, 0)
backpack3.size = "large"

backpack1.openBag()
backpack1.putin("lunch")
backpack1.putin("jacket")
backpack1.closeBag()
backpack1.openBag()
backpack1.takeout("jacket")
backpack1.closeBag()
