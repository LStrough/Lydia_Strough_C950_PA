import csv

import HashTable
from Package import Package


def load_package_data(fileName):
    with open(fileName) as packageFile:
        packageData = csv.reader(packageFile, delimiter=',')
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


def print_package_table(hashTable):
    for i in range(len(hashTable.table)):
        print("{}".format(hashTable.search(i + 1)))


def load_address_data(fileName):
    with open(fileName) as AddressFile:
        addresses = csv.reader(AddressFile, delimiter=",")

        for address in addresses:
            addressData.append(address[2])


def print_address_data(addresses):
    for i in range(len(addresses)):
        value = addresses[i]
        print('Address %d: %s' % (i, value))


# Hash table instance
pHashTable = HashTable.ChainingHashTable()

# Load packages to Hash Table
load_package_data('WGUPS Package File.csv')

# Print Hash Table
# print_formatted_table(pHashTable)

# Print Hash Table kv
# myPackage = pHashTable.search(2)
# print(myPackage)

# pHashTable.remove(2)
# print_formatted_table(pHashTable)

# Address List instance
addressData = []

# Load addresses to List
load_address_data('WGUPS Address File.csv')

# Print Address List
#print_address_data(addressData)
