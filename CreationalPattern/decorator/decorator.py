from functools import wraps
class addTagClass(object):
    def __init__(self,name):
        self.tagname = name

    def __call__(self,func):
        @wraps(func)
        def wrapped_function(*args,**kw):
            print(func.__name__,' was called')
            #self.printFoo()
            return '<{0}>{1}</{0}>'.format(self.tagname,func(*args,**kw))
        
        return wrapped_function
    
    def printFoo(self):
        '''用于被装饰器中调用，主题还是wrapped_function'''
        print('test if this method will run')

def addTagMethod(tagname):
    def decorator(func):
        def prt_func(*args):
            return '<{0}>{1}</{0}>'.format(tagname,func(*args))
        return prt_func
    return decorator

@addTagClass('vip')
def myfunc(name):
    return 'hello,'+name

@addTagMethod('ls')
def my_func(name):
    return 'hello,'+name
if __name__ == '__main__':
    print(myfunc('lyt'))
    print(my_func('lyt'))


