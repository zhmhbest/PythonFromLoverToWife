"""
    多任务
"""

import threading
import time

"""
    多任务即操作系统可以同时运行多个任务。
    
    即使过去的单核CPU，也可以执行多任务。
    由于CPU执行代码都是顺序执行的，那么，单核CPU是怎么执行多任务的呢？
    答案就是操作系统轮流让各个任务交替执行，
    任务1执行0.01秒，切换到任务2，
    任务2执行0.01秒，再切换到任务3，执行0.01秒……这样反复执行下去。
    
    表面上看，每个任务都是交替执行的，
    但是，由于CPU的执行速度实在是太快了，我们感觉就像所有任务都在同时执行一样。
    真正的并行执行多任务只能在多核CPU上实现。
    
    一般情况下由于任务数量远远多于CPU的核心数量，
    所以，操作系统也会自动把很多任务轮流调度到每个核心上执行。
    对于操作系统来说，一个任务就是一个进程（Process），
    进程是系统进行资源分配和调度的一个独立单位，
        比如打开一个浏览器就是启动一个浏览器进程，
        打开一个记事本就启动了一个记事本进程，
        打开两个记事本就启动了两个记事本进程，
        打开一个Word就启动了一个Word进程。
    有些进程还不止同时干一件事，比如Word，它可以同时进行打字、拼写检查、打印等事情。
    在一个进程内部，要同时干多件事，就需要同时运行多个“子任务”，
    我们把进程内的这些“子任务”称为线程（Thread）。
    
    由于每个进程至少要干一件事，所以，一个进程至少有一个线程。
    即线程是进程的一个实体。
    此外，线程还是CPU调度的最小可执行单元。
    线程自己基本上不拥有系统资源，它可与同属一个进程的其他的线程共享进程所拥有的全部资源。
    当然，像Word这种复杂的进程可以有多个线程，多个线程可以同时执行，
    多线程的执行方式和多进程是一样的，也是由操作系统在多个线程之间快速切换，
    让每个线程都短暂地交替运行，看起来就像同时执行一样。
    当然，真正地同时执行多线程需要多核CPU才可能实现。
    
    线程是系统级别的，它们由操作系统调度，
    而协程则是程序级别的由程序根据需要自己调度。
    在一个线程中会有很多函数，我们把这些函数称为子程序，
    在子程序执行过程中可以中断去执行别的子程序，
    而别的子程序也可以中断回来继续执行之前的子程序，
    这个过程就称为协程。

    # 关系图
    System {
        Process(1) {
            Memory          shared by all threads.
            Thread(1)       the basic unit of CPU scheduling.
            Thread(2)       (If exist) parallel running
            Thread(...)     (If exist) parallel running
        }
        
        Process(2) {
            ...
        }
        
        Process(...)
    }

"""


class MyThread (threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.is_run = True
        self.name = name

    def stop(self):
        self.is_run = False

    def run(self):
        for _i_ in range(10):
            if not self.is_run:
                return
            # end if
            print(self.name, _i_)
            time.sleep(1)
        # end for


if __name__ == '__main__':
    # 创建线程
    thread1 = MyThread("Thread-1")
    thread2 = MyThread("Thread-2")

    # 开启线程
    thread1.start()  # 循环10次
    thread2.start()  # 循环10次

    for i in range(3):  # 循环3次
        print('Main', i)
        time.sleep(1)
    # end for

    thread2.stop()  # 停止线程2
    print("Exiting Main Thread")
