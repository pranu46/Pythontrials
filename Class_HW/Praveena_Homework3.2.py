'''
Write a program that will read the file, 'red-headed-league.txt', count the frequency of the words and store it as a csv file.
Create a class called WordCounter with the following methods.
def __init__(self,filename) where filename is the name of the text file, 'red-headed-league.txt'. This function should read the text file
def removepunctuation(self) must remove all the punctuations and leave only alphabets and numbers in each word
def findcount(self) must count the frequency of each word and store it in a instance variable called countdict
def writecountfile(self,csvfilename) writes the content of the countdict variable to a csv file with two columns. The first column is the word and second column is the count.
Create an instance of the class and call appropriate method and store the result in a csv file. Printout the five most popular words.
'''

import heapq
class WordCounter:

    def __init__(self, filename):
        self.filename = filename
        self.CountDict = {}
        self.file = open(self.filename, "r+")

    def removepunctuation(self):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        no_punct = ""
        for char in self.file.read():
            if char not in punctuations:
                no_punct = no_punct + char
        self.file.seek(0, 0)
        self.file.truncate()
        self.file.writelines(no_punct)
        self.file.close()

    def findcount(self):
        self.file = open(self.filename, "r+")
        for word in self.file.read().split():
            if word not in self.CountDict:
                self.CountDict[word] = 1
            else:
                self.CountDict[word] += 1
        print('Most popular words from the text file :', heapq.nlargest(5, self.CountDict, key=self.CountDict.get))
        return self.CountDict

    def writecountfile(self,cw):
        csv = open(cw, "w")
        columnTitleRow = "Word, Count\n"
        csv.write(columnTitleRow)

        for key in self.CountDict.keys():
            Word = key
            Count = str(self.CountDict[key])
            row = Word + "," + Count + "\n"
            csv.write(row)


wc = WordCounter('red-headed-league.txt')
wc.removepunctuation()
wc.findcount()
wc.writecountfile('CountOfWords.csv')




