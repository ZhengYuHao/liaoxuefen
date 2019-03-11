#一些特殊的命名的规则 __slots__  __XXX__

#next
#1
#__str__
# class Student(object):
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return ("Student object (name:%s)"%self.name)
# if __name__=="__main__":
#     print(Student("yuhao"))

#2
# __iter__ 如果一个类想被用于循环，就必须先实现一个__iter__(仅限于使用在for in 循环里面)
# class Fib(object):
#     def __init__(self):
#         self.a,self.b=0,1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.a,self.b=self.b,self.a+self.b
#         if self.a>1000:#循环退出条件
#             raise StopIteration()
#         return self.a
# if __name__=="__main__":
#     for i in Fib():
#         print(i)

#3 __getitem__模块(这个模块可以使用在list里面，当成list，下标访问形式的使用)
# class Fib(object):
#     def __getitem__(self, item):
#         a,b=1,1,
#         for x in range(item):
#             a,b=b,a+b
#         return a
# if __name__=="__main__":
#     f=Fib()
#     print(f[4])

# class Fib(object):
#     def __getitem__(self, n):
#         if isinstance(n,int):#是索引
#             a,b=1,1
#             for x in range(n):
#                 a,b=b,a+b
#             return a
#         if isinstance(n,slice):
#             start=n.start
#             stop=n.stop
#             if start is None:
#                 start=0
#             a,b=1,1
#             L=[]
#             for x in range(stop):
#                 if x>=start:
#                     L.append(a)
#                 a,b=b,a+b
#             return L
# if __name__=="__main__":
#     f=Fib()
#     print(f[4:90])

#4 __getattr__属性(当调用)
# class Student(object):
#     def __init__(self):
#         self.name="Michael"
#     def __getattr__(self, item):#如果类里面写了这个函数，读取数据失败的时候不会直接宕机
#         if item=="score":
#             return 99
# if __name__=="__main__":
#     s=Student()
#     print(s.name,)

#5  __call__函数
