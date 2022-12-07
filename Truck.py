"""This is the Truck class."""

__author__ = "Lydia Strough"


class Truck:

    def __init__(self, location, time, time_left_hub, capacity, speed, load, packages):
        """
        Truck constructor.

        :param str location: current truck location
        :param timedelta time: current time
        :param timedelta time_left_hub: time that the truck left the hub
        :param int capacity: maximum number of packages that the truck can hold
        :param int speed: truck speed in miles per hour
        :param int load: current number of packages on truck
        :param list packages: array of packages (package ID's) currently on truck
        :returns None
        """
        self.location = location
        self.time = time
        self.timeLeftHub = time_left_hub
        self.capacity = capacity
        self.speed = speed
        self.load = len(packages)
        self.packages = packages
