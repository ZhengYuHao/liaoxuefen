
# 方法是启动一个子线程，线程名就是我们定义的name
# run()
# 方法并不启动一个新线程，就是在主线程中调用了一个普通函数而已。
# 因此，如果你想启动多线程，就必须使用start()
# 方法。

import threading
import time


def worker():
    count = 1
    while True:
        if count >= 6:
            break
        time.sleep(1)
        count += 1
        print("thread name = {}".format(threading.current_thread().name))  # 当前线程名

if __name__=="__main__":

    t = threading.Thread(target=worker)
    t.start()

    print("===end===")
