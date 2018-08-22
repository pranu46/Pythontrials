#  If the program meant to add any 12 elements to the list and pop them out using LIFO concept then below is the solution

class SClass2:
    myList = []

    def sadd(self):
        for i in range(0, 12):
            SClass2.myList.append(i)
        print(SClass2.myList)

    def sretrieve(self):
        for j in range(len(SClass2.myList)):
            SClass2.myList.pop(-1)
            print(SClass2.myList)

lifo = SClass2()
print('Elements getting added to the list:')
lifo.sadd()
print('\n Elements getting popped using LIFO from:', SClass2.myList)
lifo.sretrieve()
