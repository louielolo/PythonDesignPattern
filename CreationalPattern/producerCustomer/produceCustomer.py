import queue,threading     #导入队列、线程模块
import time  
import random
q=queue.Queue(10)
 
def pro(i):
    while 1:
        q.put('{}号厨师制作'.format(i))        #往队列中放入内容
        print('{}号厨师制作'.format(i))
        time.sleep(3)          #这里可以使用time模块的sleep函数，使运行速度变慢，便于观察
 
def cus(i):
    while 1:
        ret=q.get()         #取出
        print('顾客{}正在吃{}的包子'.format(i,ret))  
        time.sleep(random.randint(6,30))

def check():
    while 1:
        print('流水线上还有{}个包子'.format(q.qsize()))
        time.sleep(0.5)
 
if __name__ == '__main__':
    for i in range(1,4):       #创建3个厨师
        p1=threading.Thread(target=pro,args=str(i))
        p1.start()
 
    for i in range(1,11):       #创建10个顾客
        p2=threading.Thread(target=cus,args=str(i))
        p2.start()
    p3 = threading.Thread(target=check)
    p3.start()
