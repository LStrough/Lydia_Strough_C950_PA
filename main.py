import HashTable
import Truck
import readCSV
import datetime


def distance_in_between(add1, add2, addressData, distanceData):
    distance = 0
    h = addressData.index(add1)
    j = addressData.index(add2)
    if distanceData[h][j] == '':
        distance = distanceData[j][h]
    else:
        distance = distanceData[h][j]
    return float(distance)


def min_distance_from(currAddress, packageList, pHashTable, addressData, distanceData):
    minDistance = 1000
    nextAddress = ''
    nextId = 0
    for pkgId in packageList:
        pkg = pHashTable.search(pkgId)
        address2 = pkg.address
        distance = distance_in_between(currAddress, address2, addressData, distanceData)
        print('Package ID: %d Distance: %.1f' % (pkgId, distance))
        if distance < minDistance:
            minDistance = distance  # new min distance
            nextAddress = address2  # new min address
            nextId = pkg.package_id  # new package ID
    print('Closest Package Details: ID: %d Address: %s Distance: %.1f' % (nextId, nextAddress, minDistance))
    return nextAddress, nextId, minDistance


def main():
    # Hash table instance
    pHashTable = HashTable.ChainingHashTable()
    # Distance List instance
    distanceData = []
    # Address List instance
    addressData = []

    # Load Packages to Hash Table
    readCSV.load_package_data('WGUPS Package File.csv', pHashTable)
    # readCSV.print_package_table(pHashTable)
    # print(pHashTable.search(1))

    # Load Distances to 2-D List
    readCSV.load_distance_data('WGUPS Distance Table.csv', distanceData)
    # print(distanceData)

    # Load Addresses to List
    readCSV.load_address_data('WGUPS Address File.csv', addressData)
    # print(addressData)

    # time object
    startTime = '08:00:00'
    h, m, s = startTime.split(':')
    timeObject = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

    # Instantiate Truck Objects
    hub = '4001 South 700 East'
    list1 = [1, 2, 3]
    list2 = []
    list3 = []
    truck1 = Truck.Truck(hub, timeObject, '', 16, 18, len(list1), list1)
    truck2 = Truck.Truck(hub, timeObject, '', 16, 18, len(list2), list2)
    truck3 = Truck.Truck(hub, timeObject, '', 16, 18, len(list3), list3)

    min_distance_from(truck1.location, truck1.packages, pHashTable, addressData, distanceData)


if __name__ == '__main__':
    main()
