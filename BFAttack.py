from os import system
from itertools import product
from string import ascii_lowercase
import csv
import time


def Listappender(Inputlist, num):
    Dictionary = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                  'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in range(num):
        Inputlist.append(Dictionary[i])


def CsvWriter(params):
    for item in params:
        with open('ValidUrlLogger.csv', mode='w') as ValidUrlLogger:
            ValidUrlWriter = csv.writer(ValidUrlLogger)
            ValidUrlWriter.writerows(params)


def GenerateWords(myList, digit):
    urls = [''.join(i) for i in product(myList, repeat=digit)]
    return urls


if __name__ == "__main__":

    print("Shg Attacker!!")
    wordNumber = int(
        input('please enter number of word do you want for test : '))
    Domain = str(
        input('and please enter Domain of Url that you want to test : '))
    concreteList = []
    urls = []
    ActiveURLs = []

    Listappender(concreteList, wordNumber)

    urls = GenerateWords(concreteList, wordNumber)

    for item in urls:
        item = item+Domain
        res = system("ping -n 1 "+item)
        if res == 0:
            ActiveURLs.append(item)

    CsvWriter(ActiveURLs)
