class Product(object):
    _param1 = ""
    _param2 = ""
    @property
    def param1(self):
        return self._param1
    @property
    def param2(self):
        return self.param2
    @param2.setter
    def param2(self,val):
        self._param2 = val

class realProduct(Product):
    def __init__(self):
        self.param1 = ""
        self.param2 = ""
        

class simpleFactoryClass(object):
    def createProduct(self,productClass):
        _instance = productClass()
        return _instance