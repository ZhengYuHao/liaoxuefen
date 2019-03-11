import os
#多进程的编程实践
# if __name__=="__main__":
#     print('Process (%s) start...' % os.getpid())
#     # Only works on Unix/Linux/Mac:
#     pid = os.fork()
#     if pid == 0:
#         print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
#     else:
#         print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

#windows环境下的多进程编程
# from multiprocessing import Process
# import os
#
# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')

#如果要调用大量的子进程，可以使用进程池的方式批量创建子进程
# from multiprocessing import Pool
# import os, time, random
#
#
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         print(i)
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')

#父进程和子进程之间的通信
if __name__=="__main__":
    import subprocess
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('Exit code:', r)