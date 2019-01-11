class ElectronicProduct(object):
    def electronic(self):
        print 'it is an electronic product'

class Watch(ElectronicProduct):
    def time(self):
        print 'check time'

class Telephone(ElectronicProduct):
    def makeAcall(self):
        print 'telephone'

class MobilePhone(Watch, Telephone):
    def move(self):
        print ''