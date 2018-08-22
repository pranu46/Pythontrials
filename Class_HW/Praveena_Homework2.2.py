# Program to add to a given list and pop out all elements using LIFO concept

class SClass:
    def __init__(self, mylist):
        self.mylist = mylist

    def sadd(self, num):
        print('Elements in list before append',self.mylist)
        self.mylist.append(num)
        print('Elements in list after append',self.mylist)

    def sretrieve(self):
        for j in range(len(self.mylist)):
            self.mylist.pop()
            print('Elements getting popped:',self.mylist)


lifo = SClass([4, 6, 9])
lifo.sadd(12)
lifo.sretrieve()














