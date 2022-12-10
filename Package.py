"""This is the Package class."""

__author__ = "Lydia Strough"


class Package:

    def __init__(self, package_id, address, city, state, zipcode, deadline, weight, status):
        """
        Package constructor.

        :param int package_id: package ID
        :param str address: delivery address
        :param str city: delivery city
        :param str state: delivery state
        :param str zipcode: delivery zipcode
        :param str deadline: delivery time deadline
        :param float weight: package weight
        :param str status: delivery status
        :returns None
        """
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.truck_start_time = None
        self.delivery_time = None

    def __str__(self):
        """
        Package string method.

        This method provides default syntax for package information (converts hashcode to string).

        :returns the package description
        :rtype str
        """
        return ('Package ID: %d Address: %s, %s, %s, %s Deadline: %s Delivery Time: %s %.2f Status: %s' %
                (self.package_id, self.address, self.city, self.state, self.zipcode, self.deadline, self.delivery_time,
                 self.weight, self.status))

    def print_status_for_time(self, requested_time):
        status = 'At the hub'
        if self.delivery_time > requested_time:
            status = 'Delivered'
        elif requested_time < self.truck_start_time:
            status = 'At the hub'
        else:
            status = 'En route'

        return ('Package ID: %d Address: %s, %s, %s, %s Deadline: %s Delivery Time: %s %.2f Status: %s' %
                (self.package_id, self.address, self.city, self.state, self.zipcode, self.deadline, self.delivery_time,
                 self.weight, status))
