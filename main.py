import HashTable
import readCSV


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
    # print(pHashTable.search(40))

    # Load Distances to 2-D List
    readCSV.load_distance_data('WGUPS Distance Table.csv', distanceData)
    # readCSV.print_distance_data(distanceData)
    # print('Distance:', distanceData[0][0], 'miles.')

    # Load Addresses to List
    readCSV.load_address_data('WGUPS Address File.csv', addressData)
    # readCSV.print_address_data(addressData)
    # print(addressData[21])


if __name__ == '__main__':
    main()




