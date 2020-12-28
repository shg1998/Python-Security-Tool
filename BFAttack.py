from os import system
from itertools import product
from string import ascii_lowercase
from csv import reader
import csv
import time
import whois

# Author : Shg
# in the next Release I will Store the information in DB
# in this Release , Results have been shown in Console and and last of them stores in .csv file(need to become efficient!)


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


def FindBruteForceAvailableWebsites():
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


def DictionaryCheckAvailabilityOfWebsites():
    ActiveSubDomains = []
    WhoisInformations = []
    Domain = str(
        input('and please enter TLD: '))
    with open('Dictionary.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        if header != None:
            print('SubDomains:')
            for row in csv_reader:
                row[0] = row[0]+Domain
                res = system("ping -n 1 "+row[0])
                if res == 0:
                    ActiveSubDomains.append(row[0])
                    print(f'____________________________{row[0]}________________________________')
                    domain = whois.whois(row[0])
                    print(domain)
                    WhoisInformations.append(domain)
        resu=int(input('Do You want to store this result in .csv File(negative number for No and positive number for Yes)'))
        if resu >=0:
            i=0
            for var in WhoisInformations:
                        with open('ValidUrlLogger.csv', 'w') as f:
                            for key in var.keys():
                                    f.write("%s,%s\n"%(key,var[key]))
        elif resu<0:
            exit()       
      

if __name__ == "__main__":

    print("Welcome To Shg Attacker Tool!!")
    print("Choose Your Tool!")
    print("1) Find Available websites With Your own Words and TLD!")
    print("2) Dictionary Check availability of Websites!")
    print("3) Comming Soon!")
    Choice = int(input())
    if Choice == 1:
        FindBruteForceAvailableWebsites()
    elif Choice == 2:
        DictionaryCheckAvailabilityOfWebsites()
    elif Choice == 3:
        print("See You soon!")
        exit()