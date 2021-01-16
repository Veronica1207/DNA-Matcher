from sys import argv, exit
import csv
import collections
import itertools
from copy import deepcopy

# define location of a string in a list


def find_location(list, string, start, end):
    if string in list:
        return list.find(string, start, end)
    else:
        return -1

# define comparison function


def compare(OrderedDict, list):
    copy = deepcopy(OrderedDict)
    copy.popitem(last=False)
    temp = []
    for value in copy.values():
        temp.append(value)
    if list == temp:
        return True
    else:
        return False


# check the number of arguments
if len(argv) != 3:
    print("Missing command-line argument")
    exit(1)

# open the sequence file
file_s = open(argv[2], "r")
sequence = file_s.read()

# open the database file
with open(argv[1], 'r') as file_d:
    csv_reader = csv.DictReader(file_d)

    # convert orderedDict into list
    data = list(csv_reader)

    # remove the 'name' field
    fields = csv_reader.fieldnames
    fields.remove('name')

    # create list to store sequences
    list = []

    # start iterating through names
    for name in fields:

        # create variables to iterate through
        count = 1
        temp = 1
        ind = 0
        copy = 0

        # find the longest sequence
        while ind != -1:
            copy = ind
            ind = find_location(sequence, name, ind+1, len(sequence))
            if (ind - copy) == len(name):
                temp += 1
                if count < temp:
                    count = temp
            else:
                temp = 1

        # convert int to string
        count_string = str(count)

        # add strings to a new list
        list.append(count_string)

    # boolean switch
    matched = False

    # iterate through rows
    for row in data:
        if compare(row, list) == True:
            print(row['name'])
            matched = True
            break

# print 'no match'
if matched == False:
    print("No match")

file_s.close()
