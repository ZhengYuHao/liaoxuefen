from enum import  Enum,unique


class Gender(Enum):
    Male=0
    Female=1

class Student(object):
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
if __name__=="__main__":
    bart=Student("Bart",Gender.Female)
    if bart.gender==Gender.Female:
        print("Yes")
    else:
        print("No")
    print(bart.name,bart.gender)