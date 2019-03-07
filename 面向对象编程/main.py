#面向对象编程第一例子
# class Student(object):#object的位置是用来写继承类的地方
#     def __init__(self,name,score):
#         self._name=name#变量名前面加—，被看做是python方面的私有变量，习惯上是私有变量不可访问，但是实际上python并没有强制的私有变量概念
#         self.score=score
#
#     def print_student_score(self):
#         print("%s  %s"%(self._name,self.score))
#
# if __name__=="__main__":
#     yuhao=Student("caigentan","90")
#     yuhao.print_student_score()

#访问限制
# class Student(object):
#     def __init__(self,name,score):
#         self.__name=name
#         self.__score=score
#     def print_score(self):
#         print("name:%s  score:%s"%(self.__name,self.__score))
#
# if __name__=="__main__":
#     yuhao=Student("yuhao",89)
#     yuhao.print_score()
#     print(yuhao.print_score())

#继承和多态
# class Animal(object):
#     def run(self):
#         self.wangcai="woman"
#         print("Animal is running...")
#
# class Dog(Animal):#可以实现继承和多态
#     def run(self):
#         print("dog is wunning...")
#
# def run_mutil(Animal):#这里体现了多态和开闭原则(对扩展开放，对修改闭合),简称开闭原则
#     Animal.run()
# if __name__=="__main__":
#     run_mutil(Animal())

#获取对象信息
#判断对象类型-----使用type(),基本类型都可以用type()判断,返回对应的class类型

#使用isinstance()
#isinstance判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上面,isinstance有一种语法，可以判断某类型是否是一些类型中的一种

#使用dir()
#dir()函数可以获得一个对象的所有属性和方法


#实例属性和类属性

class Student(object):
    def __init__(self,name):
        self.name=name
if __name__=="__main__":
    s=Student("yuhao")
    print(s.name)
    s.age=0
    print(s.age)
#在python编程里面,不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽类属性，但是当你删除实例属性之后，再使用相同的属性的名称，访问的将是类属性
