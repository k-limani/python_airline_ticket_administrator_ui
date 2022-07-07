BUSINESS_FARE = 1.5


class Ticket:
    """The ticket class cointains the ticket type (regular or business),
    price, and destination"""

    def __init__(self, destination, fare):
        """ constructor for Ticket """
        self._destination = destination
        self._fare = float(fare)
        self._type = "regular fare"

    def get_destination(self):
        """ getter for destination """
        return self._destination

    def get_fare(self):
        """ getter for fare """
        return self._fare

    def set_destination(self, destination):
        """ setter for destination """
        self._destination = destination

    def get_type(self):
        """ getter for ticket type """
        return self._type

    def set_fare(self, fare):
        """ setter for fare """
        self._fare = fare


class BusinessTicket(Ticket):

    def __init__(self, destination, fare):
        """ constructor for BusinessFare """
        super().__init__(destination, float(fare) * BUSINESS_FARE)
        self._type = "business class"

