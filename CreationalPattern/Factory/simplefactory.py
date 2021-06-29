class ProductClass(object):
    '''抽象的产品层'''
    #工厂的产品都会有以下属性以及方法
    _param1 = "one"
    _param2 = "two"
    @property
    def param1(self):
        '''param1 只读属性'''
        return self._param1
    @property
    def param2(self):
        return self._param2
    @param2.setter
    def param2(self,val):
        '''param2 可读可写属性'''
        self._param2 = val
    def func1(self,*args,**kw):
        for elem in args:
            print(elem)
        for item in kw.items():
            print(item)
        print(self.param1)

    def func2(self,*args,**kw):
        for elem in args:
            print(elem)
        for key,value in kw.items():
            print(key,value)
        
        print(self.param2)        
        

class realProductClass1(ProductClass):
    '''产品品类1，或流水线1，抽象的产品具化一层，就是工厂生产的不同品类'''
    #新增自有的特殊属性和方法
    def __init__(self):
        super(realProductClass1,self).__init__()
        self.param3 = "three"
    def func1(self, *args, **kw):
        print(self.param3)
        return super().func1(*args, **kw)
class realProductClass2(ProductClass):
    '''产品品类2，或流水线2，抽象的产品具化一层，就是工厂生产的不同品类'''
    #新增自有的特殊属性和方法
    def __init__(self):
        super(realProductClass2,self).__init__()
        self.param2 = "TWO"
        self.param4 = "four"
    def func2(self, *args, **kw):
        print(self.param4)
        return super().func2(*args, **kw)

class simpleFactoryClass(object):
    '''简单工厂模式，定义抽象工厂后，不需要实例化工厂'''
    @classmethod
    def createProduct(cls,productClass):
        _instance = productClass()
        return _instance

if __name__ == '__main__':
    # 先生产出实例产品
    real_product1 = simpleFactoryClass.createProduct(realProductClass1)
    real_product2 = simpleFactoryClass.createProduct(realProductClass2)
    # 使用产品
    real_product1.func1(('a','b'),{'American':'New York','England':'London'})
    real_product2.func2(('A','B'),{'Malong':'Pingpang','Sunyang':'Swimming'})
    
