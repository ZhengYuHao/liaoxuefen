
from datetime import datetime

if __name__=="__main__":
    #获取当期日期和时间
    now=datetime.now()
    print(now)
    print(type(now))
    #获取指定日期和时间
    dt=datetime(2019,3,11,16,9)
    print(dt)