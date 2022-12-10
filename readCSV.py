import csv

from Package import Package


def load_package_data(file_name, hash_table):
    with open(file_name) as package_file:
        package_data = csv.reader(package_file, delimiter=',')
        for package in package_data:
            p_id = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zipcode = package[4]
            deadline = package[5]
            weight = float(package[6])
            status = 'At hub'

            # Package object
            p = Package(p_id, address, city, state, zipcode, deadline, weight, status)

            # Insert object into hash table
            hash_table.insert(p_id, p)


def print_package_table(hash_table):
    for i in range(len(hash_table.table)):
        print("{}".format(hash_table.search(i + 1)))


def load_address_data(file_name, address_data):
    with open(file_name) as address_file:
        addresses = csv.reader(address_file, delimiter=",")
        for address in addresses:
            address_data.append(address[2])


def load_distance_data(file_name, distance_data):
    with open(file_name) as distance_file:
        distances = csv.reader(distance_file, delimiter=",")
        for distance in distances:
            distance_data.append(distance)
