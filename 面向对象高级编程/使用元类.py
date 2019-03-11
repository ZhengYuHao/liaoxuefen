#动态语言和静态语言的最大不同就是，函数和类的定义，不是在编译时候定义的，而是在运行时动态创建的
#type函数既可以返回一个对象的类型，又可以创建出新的类型
#通过type()函数创建的类和直接写class是完全一样的，因为python解释器遇到class定义时，仅仅是扫描一下class的定义语法，然后调用type()函数创建出class
# class Hello(object):
#     def hello(self,name="world"):
#         print("hello,%s."%name)
#
# if __name__=="__main__":
#     h=Hello()
#     h.hello()
#     print(type(h))

#metaclass，除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass
#可以这样看这个变量的作用，metaclass翻译成元类，它可以实例化出类，类再实例化出实例
