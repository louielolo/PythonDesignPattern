#encoding=utf8
"""
现假设有如下场景：某中央处理器（CPU）通过某种协议总线与一个信号灯相连，
信号灯有64种颜色可以设置，中央处理器上运行着三个线程，都可以对这个信号灯进行控制，
并且可以独立设置该信号灯的颜色。抽象掉协议细节（用打印表示），如何实现线程对信号等的控制逻辑。
"""

'''
什么是单例模式？单例模式是指：保证一个类仅有一个实例，并提供一个访问它的全局访问点。具体到此例中，
总线对象，就是一个单例，它仅有一个实例，各个线程对总线的访问只有一个全局访问点，即惟一的实例。
'''

import threading
import time
#使用__new__实现单例模式
class Singleton(object):#抽象单类
    def __new__(cls,*args,**kw):
        if not hasattr(cls,'_instance'):
            orig = super(Singleton,cls)
            cls._instance = orig.__new__(cls,*args,**kw)
        return cls._instance

class Bus(Singleton):
    lock = threading.RLock()
    def sendData(self,data: str):
        self.lock.acquire()
        time.sleep(3)
        print("Sending Signal Data ",data)
        self.lock.release()

class VisitEntity(threading.Thread):
    my_bus = ""
    name = ""
    def getName(self) -> str:
        return self.name
    def setName(self,name):
        self.name = name
    def run(self):
        self.my_bus = Bus()
        self.my_bus.sendData(self.name)

if __name__ == '__main__':
    for i in range(3):
        print ("Entity %d begin to run ... "%i)
        my_entivity = VisitEntity()
        my_entivity.setName("Entivity_"+str(i))
        # start是使用多线程的办法，这里表示循环可以开三个线程，如果不是单例模式的话，打印将会接近同时进行
        #单例模式使得bus实例使得所有线程只能用同一个实例。
        my_entivity.start()




