# Author: Lydia Strough
# Student ID: 002452624
# Title: C950 WGUPS ROUTING PROGRAM
import HashTable
import Truck
import readCSV
import datetime


def distance_in_between(add1, add2, address_data, distance_data):
    distance = 0
    h = address_data.index(add1)
    j = address_data.index(add2)
    if distance_data[h][j] == '':
        distance = distance_data[j][h]
    else:
        distance = distance_data[h][j]
    return float(distance)


def min_distance_from(curr_address, pkg_list, hash_table, address_data, distance_data):
    min_distance = 1000
    next_address = ''
    next_id = 0
    print('Determining Closest Address!')
    for pkg_id in pkg_list:
        pkg = hash_table.search(pkg_id)
        address2 = pkg.address
        # Determine distance between addresses
        distance = distance_in_between(curr_address, address2, address_data, distance_data)
        print('Package ID: %d Distance: %.1f' % (pkg_id, distance))
        if distance == 0:
            min_distance = distance  # new min distance
            next_address = address2  # new min address
            next_id = pkg.package_id  # new package ID
            print('Closest Package Details: ID: %d Address: %s Distance: %.1f' % (next_id, next_address, min_distance))
            print()
            return next_address, next_id, min_distance
        elif distance < min_distance:
            min_distance = distance  # new min distance
            next_address = address2  # new min address
            next_id = pkg.package_id  # new package ID
    print('Closest Package Details: ID: %d Address: %s Distance: %.1f' % (next_id, next_address, min_distance))
    print()
    return next_address, next_id, min_distance


def load_truck_packages(truck1, truck2, truck3):
    # DELIVERY CONSTRAINTS
    # Can only be on truck 2: 3, 18, 36, 38
    # Must be on the SAME truck: 13, 14, 15, 16, 19, 20
    # Delayed on Flight (will not arrive to hub until 09:05:00): 6, 25, 28, 32
    # Wrong address listed (correct address arrives at 10:20:00): 9 (correct address: 410 S State St)
    # 10:30:00 Deadline: 1, 6, 13, 14, 16, 20, 25, 29, 30, 31, 34, 37, 40
    # 09:00:00 Deadline: 15

    # Manually Load Packages to Trucks
    list1 = [1, 2, 5, 7, 10, 13, 14, 15, 16, 19, 20, 29, 33, 34, 37, 39]
    list2 = [3, 6, 8, 11, 12, 18, 23, 25, 27, 30, 31, 35, 36, 38, 40]
    list3 = [4, 9, 17, 21, 22, 24, 26, 28, 32]
    truck1.packages = list1
    truck2.packages = list2
    truck3.packages = list3

    print('Truck 1 is Loaded:', list1)
    print('Truck 2 is Loaded:', list2)
    print('Truck 3 is Loaded:', list3)
    print()

    """
        print('10:30:00 Deadline:')
        print(p_hash_table.search(1))
        print(p_hash_table.search(6))
        print(p_hash_table.search(13))
        print(p_hash_table.search(14))
        print(p_hash_table.search(16))
        print(p_hash_table.search(20))
        print(p_hash_table.search(25))
        print(p_hash_table.search(29))
        print(p_hash_table.search(30))
        print(p_hash_table.search(31))
        print(p_hash_table.search(34))
        print(p_hash_table.search(37))
        print(p_hash_table.search(40))
        print()
        print('09:00:00 Deadline:')
        print(p_hash_table.search(15))
        """


def deliver_truck_packages(truck, time, hash_table, address_data, distance_data):
    # Delivered packages list instance
    delivered = []
    # Not delivered packages list instance
    not_delivered = truck.packages.copy()
    # Set current address to truck location (hub)
    curr_address = truck.location
    # Total distance traveled
    distance_traveled = 0
    # Time Object
    start_time = time
    h, m, s = start_time.split(':')
    time_object = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    while len(not_delivered) > 0:
        for pkg in not_delivered:
            # update package status
            curr_pkg = hash_table.search(pkg)
            curr_pkg.status = 'En route'
            print('Package ID:', curr_pkg.package_id, 'Status:', curr_pkg.status)
        print()
        for pkg in not_delivered:
            print('Delivered:', delivered)
            print('Not Delivered:', not_delivered)
            print()
            # Determine closest address
            address, pkg_id, miles = min_distance_from(curr_address, not_delivered, hash_table, address_data,
                                                       distance_data)
            curr_address = address
            # Update distance traveled
            distance_traveled += miles
            print('Total Distance traveled:', distance_traveled)
            if miles == 0:
                print('Current time:', time_object)
                # update package status
                curr_pkg = hash_table.search(pkg_id)
                curr_pkg.status = 'Delivered at ' + str(time_object)
            else:
                # update time
                time_passed = (miles / 18) * 60 * 60
                dts = datetime.timedelta(seconds=int(time_passed))
                time_object += dts
                print('Current time:', time_object)
                # update package status
                curr_pkg = hash_table.search(pkg_id)
                curr_pkg.status = 'Delivered at ' + str(time_object)
            # add package to delivered list
            delivered.append(pkg_id)
            # update package start and delivery time
            curr_pkg = hash_table.search(pkg_id)
            curr_pkg.truck_start_time = truck.time_left_hub
            curr_pkg.delivery_time = time_object
            # remove package from not delivered list
            not_delivered.remove(pkg_id)
            # print delivered package
            print('Package', curr_pkg.package_id, 'Delivered!')
            # update truck
            truck.location = curr_address
            truck.time = time_object
            truck.mileage = distance_traveled
            print(truck)
            print()
    # Final stop
    print('Last stop: The hub!')
    hub = '4001 South 700 East'
    # Calculate distance between current truck location and the hub
    miles = distance_in_between(truck.location, hub, address_data, distance_data)
    print('Distance to hub:', miles)
    print('Distance traveled thus far:', distance_traveled)
    # Update distance traveled
    distance_traveled += miles
    print('Final truck mileage:', distance_traveled)
    # Update truck miles
    truck.mileage = distance_traveled
    time_passed = (miles / 18) * 60 * 60
    dts = datetime.timedelta(seconds=int(time_passed))
    time_object += dts
    # Update truck time
    truck.time = time_object
    # Update truck location
    truck.location = hub
    print('Delivery Completed!')
    print('Delivered:', delivered)
    print('Not Delivered:', not_delivered)
    print(truck)
    print()
    return truck.mileage


def command_user_interface(truck1, truck2, truck3, hash_table, address_data, distance_data):
    try:
        # Command UI Main Menu
        print('What information would you like to see? ')
        print('1) Package information')
        print('2) Exit the Program \n')
        user_input = int(input())
        if user_input == 1:
            # Package information
            print('Option 1 was selected!')
            print('What information would you like to see?')
            print('1) All Package information')
            print('2) All Package information (by Time)')
            print('3) Specific Package information (by Package ID)')
            print('4) Exit the Program \n')
            user_input = int(input())
            if user_input == 1:
                # All Package Information
                print('Option 1 was selected!')
                print('All Package information:')
                readCSV.print_package_table(hash_table)
                print()
                # Return to Main Menu
                command_user_interface(truck1, truck2, truck3, hash_table, address_data, distance_data)
            elif user_input == 2:
                # Specific Package Information (by Time)
                print('Option 2 was selected!')
                print('Enter a time in the HH:MM:SS format')
                user_input = input()
                (h, m, s) = user_input.split(':')
                convert_user_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                print('All Package information at time:', convert_user_time)
                for p_id in range(1, 41):
                    pkg = hash_table.search(p_id)
                    print(pkg.print_status_for_time(convert_user_time))
                print()
                # Return to Main Menu
                command_user_interface(truck1, truck2, truck3, hash_table, address_data, distance_data)
            elif user_input == 3:
                # Specific Package Information (by Package ID)
                print('Option 3 was selected!')
                print('Enter a Package ID number 1-40')
                user_input = int(input())
                print('Package ID chosen:', user_input)
                print(hash_table.search(user_input))
                print()
                # Return to Main Menu
                command_user_interface(truck1, truck2, truck3, hash_table, address_data, distance_data)
            elif user_input == 4:
                # Exit Program
                print('You have chosen to \'exit\' the program.')
                print('Goodbye.')
                exit()
        elif user_input == 2:
            # Exit Program
            print('You have chosen to \'exit\' the program.')
            print('Goodbye.')
            exit()
        else:
            print('Invalid Entry! \n')
            command_user_interface(truck1, truck2, truck3, hash_table, address_data, distance_data)
    except ValueError:
        print('Invalid Entry: Incorrect data type! \n')
        command_user_interface(truck1, truck2, truck3, hash_table, address_data, distance_data)


def main():
    # Hash table instance
    p_hash_table = HashTable.ChainingHashTable()
    # Distance List instance
    distance_data = []
    # Address List instance
    address_data = []

    # Load Packages to Hash Table
    readCSV.load_package_data('WGUPS Package File.csv', p_hash_table)
    # Load Distances to 2-D List
    readCSV.load_distance_data('WGUPS Distance Table.csv', distance_data)
    # Load Addresses to List
    readCSV.load_address_data('WGUPS Address File.csv', address_data)

    # Instantiate Truck Objects
    hub = '4001 South 700 East'
    list1 = []
    list2 = []
    list3 = []
    truck1 = Truck.Truck(hub, '08:00:00', '08:00:00', 16, 18, 0, list1)
    truck2 = Truck.Truck(hub, '09:05:00', '09:05:00', 16, 18, 0, list2)
    truck3 = Truck.Truck(hub, '10:20:00', '10:20:00', 16, 18, 0, list3)

    # Load Packages to Trucks
    print('Loading Packages!')
    load_truck_packages(truck1, truck2, truck3)

    # Deliver Truck Packages
    print('Truck 1 Delivery Started!')
    print('Truck 1 total miles:', deliver_truck_packages(truck1, truck1.time_left_hub, p_hash_table, address_data,
                                                         distance_data))
    print('Truck 2 Delivery Started!')
    print('Truck 2 total miles:', deliver_truck_packages(truck2, truck2.time_left_hub, p_hash_table, address_data,
                                                         distance_data))
    print('Truck 3 Delivery Started!')
    print('Truck 3 total miles:', deliver_truck_packages(truck3, truck3.time_left_hub, p_hash_table, address_data,
                                                         distance_data))
    print()

    # ALL Truck Information
    # Truck Packages (at start)
    print('Truck Packages (at start):')
    print('Truck 1 Packages:', truck1.packages)
    print('Truck 2 Packages:', truck2.packages)
    print('Truck 3 Packages:', truck3.packages)
    print()
    # Truck Times
    print('Truck Delivery Times:')
    print('Truck 1 start time:', truck1.time_left_hub)
    print('Truck 1 completion time:', truck1.time)
    print('Truck 2 start time:', truck2.time_left_hub)
    print('Truck 2 completion time:', truck2.time)
    print('Truck 3 start time:', truck3.time_left_hub)
    print('Truck 3 completion time:', truck3.time)
    print()
    # Total miles traveled
    print('Truck Miles:')
    t1_miles = '%.1f' % truck1.mileage
    print('Truck 1 Miles:', t1_miles)
    print('Truck 2 Miles:', truck2.mileage)
    print('Truck 3 Miles:', truck3.mileage)
    total_miles = '%.1f' % (truck1.mileage + truck2.mileage + truck3.mileage)
    print('Total Miles:', total_miles)
    print()

    # Command UI
    command_user_interface(truck1, truck2, truck3, p_hash_table, address_data, distance_data)


if __name__ == '__main__':
    main()
