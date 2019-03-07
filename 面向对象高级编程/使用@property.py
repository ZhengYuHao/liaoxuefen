#使用@property
class student(object):#这里的设置可以类比C#里面的get和set方法
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        self._score=value

if __name__=="__main__":
    yuhao=student()
    yuhao.score=78
    print(yuhao.score)