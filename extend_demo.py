class Animal(object):
    def eat(self):
        print 'I am eating'

    def drink(self):
        print 'I am drinking'

    def sleep(self):
        print 'I am sleeping'



class Bird(Animal):
    def fly(self):
        print 'bird can fly!!!'


class Person(Animal):
    def __init__(self):
        self.head = Head()
    def speak(self):
        print 'person can speak!!!'
    def kantou(self):
        print '我的头被砍了'



class Head(object):
    def head(self):
        print 'has a head'

# ===================================
sparrow = Person()
sparrow.speak()
head = Head()