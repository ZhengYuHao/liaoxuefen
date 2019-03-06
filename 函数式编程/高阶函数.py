# 用于filter测试
# def not_empty(s):
#     return s and s.strip()
#
# if __name__=="__main__":
#     data=list(filter(not_empty,['a',' ','t']))
#     print(data)

#用于测试sorted函数
# def addNumbleOne(s):
#     s=s+1
#     return s
#
# if __name__=="__main__":
#     data=[34,56,-2,34,54]
#     data=sorted(data,key=abs,reverse=True)
#     print(data)

#返回函数(在python里面,函数是可以返回函数的)
# def lazy_num(*args):
#     def sum():
#         ax=0
#         for n in args:
#             ax=ax+n
#         return ax
#     return sum
#
# if __name__=="__main__":
#     li=[1,2,3,4,5]
#     f=lazy_num(*li)
#     print(f)
#     print(f())

#匿名函数

# if __name__=="__main__":
#     data=list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9]))
#     print(data)

#装饰器测试

# def log(func):
#     def wrapper(*args,**kw):
#         print("call %s():"%func.__name__)
#         return func(*args,**kw)
#     return wrapper
#
# @log
# def now():
#     print("2019-3-6")
# if __name__=="__main__":
#     now()

