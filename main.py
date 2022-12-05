import csv

import HashTable
from Package import Package


def load_package_data(fileName):
    with open(fileName) as packages:
        packageData = csv.reader(packages, delimiter=',')
        for package in packageData:
            pID = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zipcode = package[4]
            deadline = package[5]
            weight = float(package[6])
            status = 'At hub'

            # package object
            p = Package(pID, address, city, state, zipcode, deadline, weight, status)

            # insert it into the hash table
            pHashTable.insert(pID, p)


# Hash table instance
pHashTable = HashTable.ChainingHashTable()

# Load packages to Hash Table
load_package_data('WGUPS Package File.csv')

# Print Hash Table
# print(pHashTable.table)  # format print function for Hash Table

# Print Hash Table kv
myPackage = pHashTable.search(2)
print(myPackage)
