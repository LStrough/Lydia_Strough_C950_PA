import HashTable
import Truck
import readCSV

# Hash table instance
pHashTable = HashTable.ChainingHashTable()
# Distance List instance
distanceData = []
# Address List instance
addressData = []

# Truck 1 instance
truck1 = Truck.Truck('At the hub', '', '', 16, 18, 0, [4, 11])
# Truck 2 instance
truck2 = Truck.Truck('At the hub', '', '', 16, 18, 0, [3, 8])
# Truck 3 instance
truck3 = Truck.Truck('At the hub', '', '', 16, 18, 0, [1, 2])


def distance_in_between(add1, add2):  # str values
    distance = 0
    h = addressData.index(add1)  # gets index from str address
    j = addressData.index(add2)
    if distanceData[h][j] == '':
        distance = distanceData[j][h]
    else:
        distance = distanceData[h][j]
    return float(distance)


"""
def min_distance_from(currAddress, packageList):
    minDistance = 1000
    nextAddress = ''
    nextId = 0
    for package in packageList:

        distance = distance_in_between(currAddress, nextAddress)
        if distance < minDistance:
            minDistance = distance

    print('Minimum distance address:', nextAddress, '(', minDistance, ')', 'Package:', nextId)
    return nextAddress, nextId, minDistance
"""


def main():
    # Load Packages to Hash Table
    readCSV.load_package_data('WGUPS Package File.csv', pHashTable)
    # readCSV.print_package_table(pHashTable)
    # print(pHashTable.search(1))

    # Load Distances to 2-D List
    readCSV.load_distance_data('WGUPS Distance Table.csv', distanceData)
    # readCSV.print_distance_data(distanceData)
    # print(distanceData)

    # Load Addresses to List
    readCSV.load_address_data('WGUPS Address File.csv', addressData)
    # readCSV.print_address_data(addressData)
    # print(addressData)


if __name__ == '__main__':
    main()




