BUSINESS_FARE = 1.5


class Route:
    """The Route class contains information
    for one route from San Jose to a destination city"""


    def __init__(self, line):
        """ Constructor for Route """
        self._destination = line[0]
        self._fare = float(line[1])
        self._busFare = self._fare * BUSINESS_FARE

    # print("self._destination=", self._destination, ",", "self._fare=", self._fare)  # DEBUG

    def get_destination(self):
        """ Getter for destination """
        return self._destination

    def get_fare(self):
        """ Getter for fare """
        return self._fare

    def get_busFare(self):
        """ Getter for business fare """
        return self._busFare

    def set_destination(self, destination):
        """ Setter for destination """
        self._destination = destination

    def set_fare(self, fare):
        """ Setter for fare """
        self._fare = float(fare)
        self._busFare = float(fare) * BUSINESS_FARE
