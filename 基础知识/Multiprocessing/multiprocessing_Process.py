from multiprocessing import Process
import os
'''
不知道为啥，其他的IDE都没有在multiprocessing显示Process这个类...
ST3，Jupyter相应代码都没有执行，或者就是has no attribute...
'''
# 子进程要执行的代码
def run_proc(name):
    print('Run child process: %s pid:(%s)...' % (name, os.getpid()))
    print("-------------hello,world!-----------------")

if __name__=='__main__':
    print('Parent process pid:%s.' % os.getpid())
    # 创建Process对象，target设置需要子进程执行的代码，args设置子进程名称
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    #启动subProcess
    p.start()
    print('Child process has started.')
    #进程开始切换执行。如果没有这句，则会先把父进程执行完，而后子进程。
    p.join()
    print('Child process has joined.')
    print('Child process end.')