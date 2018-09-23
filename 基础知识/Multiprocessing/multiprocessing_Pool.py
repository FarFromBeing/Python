from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    start = time.time()
    print('于 %s 开始执行子进程 %s (%s)...' % (start,name, os.getpid()))
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))
    print('task  %s (%s)finished'%(name, os.getpid()))
    print('************************************')    
if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    '''Pool的设置试一次性启动多少进程
        e.g Pool(20) ，一次可以创建20个子进程，如图结果
    '''
    p = Pool(20)
    for i in range(30):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done')
    p.close()
    p.join()
    print('All subprocesses done.')