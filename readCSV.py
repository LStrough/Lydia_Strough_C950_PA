import csv

from Package import Package


def load_package_data(fileName, hashTable):
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
            hashTable.insert(pID, p)


def print_package_table(hashTable):
    for i in range(len(hashTable.table)):
        print("{}".format(hashTable.search(i + 1)))


def load_address_data(fileName, addressData):
    with open(fileName) as AddressFile:
        addresses = csv.reader(AddressFile, delimiter=",")
        for address in addresses:
            addressData.append(address[2])


def print_address_data(addresses):
    for i in range(len(addresses)):
        value = addresses[i]
        print('Address %d: %s' % (i, value))


def load_distance_data(fileName, distanceData):
    with open(fileName) as DistanceFile:
        distances = csv.reader(DistanceFile, delimiter=",")
        for distance in distances:
            distanceData.append(distance)


def print_distance_data(distances):
    for distance in distances:
        print(distance)
