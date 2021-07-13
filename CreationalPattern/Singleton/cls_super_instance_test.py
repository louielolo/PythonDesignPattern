import threading
import time

class demosingletonClass(object):
    instance_created = 0
    def __new__(cls,*args,**kw):
        if not hasattr(cls,'_instance'):
            cls._instance = super().__new__(cls,*args,**kw)
            cls.instance_created += 1
            cls._instance.number = cls.instance_created
            print('success instance point',cls._instance)
        else:
            print('failed instance point',cls._instance)
        return cls._instance
class taskClass(object):
    lock = threading.RLock()
    instance_created = 0
    def __init__(self):
        self.threadname = "thread"
        self.instancename = "instance"
        self.instance_created += 1
        self.number = self.instance_created
        print('success instance point',self)
    def show(self,threadnum):
        self.lock.acquire()
        print(self.threadname,' is ',threadnum,' and ',self.instancename,' is ',self.number)
        self.lock.release()
    
class visitThread(threading.Thread):
    my_instance_thread = ""
    thread_name = ""
    def getName(self) -> str:
        return self.thread_name
    def setName(self, name: str) -> None:
        self.thread_name = name
    def run(self) -> None:
        self.my_instance_thread = taskClass()
        self.my_instance_thread.show(self.thread_name)



if __name__ == '__main__':
    for i in range(2):
        print('thread %d is going to run'%i)
        t = visitThread()
        t.setName(str(i))
        t.start()

    