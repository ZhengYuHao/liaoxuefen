# 知识点一：
# 当一个进程启动之后，会默认产生一个主线程，因为线程是程序执行流的最小单元，当设置多线程时，主线程会创建多个子线程，
# 在python中，默认情况下（其实就是setDaemon(False)），
# 主线程执行完自己的任务以后，就退出了，此时子线程会继续执行自己的任务，直到自己的任务结束，例子见下面一。
# import threading
# import time
# def run():
#     time.sleep(2)
#     print('当前线程的名字是： ', threading.current_thread().name)
#     time.sleep(2)
#
#
# if __name__ == '__main__':
#     start_time = time.time()
#     print('这是主线程：', threading.current_thread().name)
#     thread_list = []
#     for i in range(5):#这里定义5个线程
#         t = threading.Thread(target=run)
#         thread_list.append(t)
#     for t in thread_list:#这里分别启动这5个进程
#         t.start()
#
#     print('主线程结束！' , threading.current_thread().name)
#     print('一共用时：', time.time()-start_time)#当前时间-开始时间

# 知识点二：
# 当我们使用setDaemon(True)方法，设置子线程为守护线程时，主线程一旦执行结束，则全部线程全部被终止执行，
# 可能出现的情况就是，子线程的任务还没有完全执行结束，就被迫停止，例子见下面二。
# import threading
# import time
#
# def run():
#
#     time.sleep(2)
#     print('当前线程的名字是： ', threading.current_thread().name)
#     time.sleep(2)
#
#
# if __name__ == '__main__':
#
#     start_time = time.time()
#
#     print('这是主线程：', threading.current_thread().name)
#     thread_list = []
#     for i in range(5):
#         t = threading.Thread(target=run)
#         thread_list.append(t)
#
#     for t in thread_list:
#         t.setDaemon(True)
#         t.start()
#
#     print('主线程结束了！' , threading.current_thread().name)
#     print('一共用时：', time.time()-start_time)



# 知识点三：
# 此时join的作用就凸显出来了，join所完成的工作就是线程同步，即主线程任务结束之后，进入阻塞状态，
# 一直等待其他的子线程执行结束之后，主线程在终止，例子见下面三。
#join完成的任务就是线程同步

import threading
import time

def run():

    time.sleep(2)
    print('当前线程的名字是： ', threading.current_thread().name)
    time.sleep(2)


if __name__ == '__main__':

    start_time = time.time()

    print('这是主线程：', threading.current_thread().name)
    thread_list = []
    for i in range(5):
        t = threading.Thread(target=run)
        thread_list.append(t)

    for t in thread_list:
        t.setDaemon(True)
        t.start()
    thread_list[4].join()
    print('主线程结束了！' , threading.current_thread().name)
    print('一共用时：', time.time()-start_time)