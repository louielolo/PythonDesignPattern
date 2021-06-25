'''
想必大家一定见过类似于麦当劳自助点餐台一类的点餐系统吧。
在一个大的触摸显示屏上，有三类可以选择的上餐品：汉堡等主餐、小食、饮料。
当我们选择好自己需要的食物，支付完成后，订单就生成了。
下面，我们用今天的主角--工厂模式--来生成这些食物的逻辑主体。
首先，来看主餐的生成（仅以两种汉堡为例）。
'''
class Burger(object):
    '''创建汉堡类及实例会用到的方法'''
    def __init__(self):
        self.name = None
        self.price = 0
    def getName(self):
        return self.name
    def getPrice(self):
        return self.price
    def setName(self,name):
        self.name = name
    def setPrice(self,price):
        self.price = price

class CheeseBurger(Burger):
    '''Burger实例化'''
    def __init__(self):
        self.name = "cheese burger"
        self.price = 10.0
class SpicyChickenBurger(Burger):
    '''Burger实例化'''
    def __init__(self):
        self.name = "spicy chicken burger"
        self.price = 15.0

class Snack(object):
    def __init__(self):
        self.name = None
        self.price = 0.0
    def getName(self):
        return self.name
    def getPrice(self):
        return self.price
    def setName(self,name):
        self.name = name
    def setPrice(self,price):
        self.price = price
class Chips(Snack):
    def __init__(self):
        self.name = "chips"
        self.price = 5.0
class ChickenWings(Snack):
    def __init__(self):
        self.name = "chicken wings"
        self.price = 2.0

class Beverage(object):
    def __init__(self):
        self.name = None
        self.price = 0.0
    def getName(self):
        return self.name
    def getPrice(self):
        return self.price
    def setName(self,name):
        self.name = name
    def setPrice(self,price):
        self.price = price

class Coke(Beverage):
    def __init__(self):
        self.name = "coke"
        self.price = 7.5
class Milk(Beverage):
    def __init__(self):
        self.name = "milk"
        self.price = 4.0

class FoodFactory():
    '''其产品类定义产品的公共属性和接口，工厂类定义产品实例化的“方式”。'''
    def __init__(self):
        self.type = None
    def createFood(self,foodClass):
        print(self.type," factory produce a instance.")
        foodIns = foodClass()
        return foodIns
class BurgerFactory(FoodFactory):
    def __init__(self):
        self.type = "BURGER"
class SnackFactory(FoodFactory):
    def __init__(self):
        self.type = "SNACK"
class BeverageFactory(FoodFactory):
    def __init__(self):
        self.type = "BEVERAGE"

class SimpleFoodFactory():
    '''使用@classmethod 可以使得类不需要实例化也能调用方法
    否则就像上面工厂模式那样，实例化各种factory，增加好多子类的生成'''
    @classmethod
    def createFood(cls,foodClass):
        print("Simple factory produce a instance.")
        foodIns = foodClass()
        return foodIns

if __name__ == "__main__":
    burger_factory = BurgerFactory()
    snack_factory = SnackFactory()
    beverage_factory = BeverageFactory()
    cheese_burger = burger_factory.createFood(CheeseBurger)
    print(cheese_burger.getName(),cheese_burger.getPrice()) 
    chicken_wings = snack_factory.createFood(ChickenWings)
    print(chicken_wings.getName(),chicken_wings.getPrice())
    coke_drink = beverage_factory.createFood(Coke)
    print(coke_drink.getName(),coke_drink.getPrice())
    print("---------------------------------------------------")
    cheese_burger2 = SimpleFoodFactory.createFood(CheeseBurger)
    chicken_wings2 = SimpleFoodFactory.createFood(ChickenWings)
    coke_drink2 = SimpleFoodFactory.createFood(Coke)
    print(cheese_burger2.getName(),cheese_burger.getPrice()) 
    print(chicken_wings2.getName(),chicken_wings.getPrice())
    print(coke_drink2.getName(),coke_drink.getPrice())

