import queue

if __name__ == '__main__':
    q = queue.Queue(10)
    for i in range(10):
        q.put('{0}号厨师制作,还有{1}多个包子'.format(i,q.qsize())) 

    while q.qsize():
        ret = q.get()
        print(ret)
