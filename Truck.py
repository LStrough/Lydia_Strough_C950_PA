"""This is the Truck class."""

__author__ = "Lydia Strough"


class Truck:

    def __init__(self, location, time, time_left_hub, capacity, speed, load, packages):
        """
        Truck constructor.

        :param str location: current truck location
        :param str time: current time
        :param str time_left_hub: time that the truck left the hub
        :param int capacity: maximum number of packages that the truck can hold
        :param float speed: truck speed in miles per hour
        :param int load: current number of packages on truck
        :param Package packages: array of packages currently on truck
        :returns None
        """
        self.location = location
        self.time = time
        self.timeLeftHub = time_left_hub
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.packages = packages  # array of packages
