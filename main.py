import HashTable
import Truck
import readCSV
import datetime


def distance_in_between(add1, add2, addressData, distanceData):  # str values
    distance = 0
    h = addressData.index(add1)  # gets index from str address
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
        if distance < minDistance:
            minDistance = distance  # new min distance
            nextAddress = address2  # new min address
            nextId = pkg.package_id  # new package ID
    print('Closest package details:')
    print('Package ID: %d Address: %s Distance: %.1f' % (nextId, nextAddress, minDistance))
    return nextAddress, nextId, minDistance


def main():
    """
        # time object
        startTime = '08:00:05'
        h,m,s = startTime.split(':')
        timeObject = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        print(timeObject)

        list1 = [1, 2, 3]  # truck package list (pass into truck instantiation)
    """

    # Hash table instance
    pHashTable = HashTable.ChainingHashTable()
    # Distance List instance
    distanceData = []
    # Address List instance
    addressData = []

    # insert time object

    # Truck 1 instance
    truck1 = Truck.Truck('4001 South 700 East', '', '', 16, 18, 0, [])
    # Truck 2 instance
    truck2 = Truck.Truck('4001 South 700 East', '', '', 16, 18, 0, [])
    # Truck 3 instance
    truck3 = Truck.Truck('4001 South 700 East', '', '', 16, 18, 0, [])

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

    hub = '4001 South 700 East'  # hub should be replaced with truck location
    min_distance_from(hub, truck1.packages, pHashTable, addressData, distanceData)


if __name__ == '__main__':
    main()
