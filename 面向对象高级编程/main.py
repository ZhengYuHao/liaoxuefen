#使用__slots__
from types import MethodType
class Student(object):#声明一个类
    __slots__=("name","age")
    pass

def set_age(self,age):
    self.age=age

if __name__=="__main__":
    s=Student()
    s.name="yuhao"#为对象动态添加一个变量
    print(s.name)
    s.set_age=MethodType(set_age,s)
    s.set_age(34)
    print(s.age)
    #接下来的代码将会给所有的class绑定方法
    Student.set_age=set_age
    ss=Student()
    ss.set_age(90)
    print(ss.age)
    #动态绑定允许我们在程序运行的过程中动态给class添加功能,这在静态语言很难实现
#使用__slot__
#__slot__可以限制该class实例能添加的属性
#如果在子类中也定义了__slots__，这样，子类允许定义的属性就是自身的__slots__外加父类的__slots__


