# encoding=utf-8
class Person(object):
    name = '' #姓名
    province = '' #省份
    age = 0 #年龄
    height = 0 #身高
    weight = 0 #体重
    appearance = 0 #颜值

    def __init__(self, name, province, age, height, weight, appearance):
        self.name = name
        self.province = province
        self.age = age
        self.height = height
        self.weight = weight
        self.appearance = appearance

    def printAllAttribute(self):
        print self.name, self.province, self.age, self.height, self.weight, self.appearance

    def grow(self):
        self.age += 1
        self.height += 3
        self.weight += 1
        self.printAllAttribute()



# ===============================
XieYingying = Person('谢莹莹', '广东', 21, 160, 46, 100)
GuYueyang = Person('顾悦阳', '江苏', 20, 182, 78, 50)

XieYingying.printAllAttribute()
GuYueyang.printAllAttribute()

XieYingying.grow()
GuYueyang.grow()