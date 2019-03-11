from collections import namedtuple
from collections import deque
from collections import  OrderedDict
# if __name__=="__main__":

# namedtuple函数
    # Point=namedtuple("Point",['x','y'])#其实可以看成是定义了一个微型类
    # p=Point(3,4)
    # print(p.x,p.y)
#deque模块(这个模块具有巨大作用，在数据结构上面有巨大作用)
    # q=deque(['a','b','c'])
    # q.append('x')
    # q.appendleft("y")
    # print(q)
#defaultdict
#OrderedDict，使用orderDict时，key是无序的，在对dict做迭代的时候，我们无法确定key的顺序
    # d=dict([("a",1),("b",2),("c",3)])
    # print(d[1])
    # od=OrderedDict([("a",1),("b",2),("c",3)])
    # print(od)
#ChainMap
