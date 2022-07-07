"""
The program lets an airline administrator modify
the routes of an airline, and lets a customer buy tickets
for the available routes.
Both Routes and Tickets are store in a Dictionary type data structure.
For the Routes, the key is the destination and the value is the Route object.
For the Tickets the key is the Ticket object and the value is the number of tickets for that ticket.
"""

import csv
from ticket import Ticket, BusinessTicket
from route import Route


INPUT_FILE = "airfares.csv"


class AirlineTicketing:
    """ Read in each line of the file with the default filename constant and store it in a collection """

    def __init__(self, fname=INPUT_FILE):
        self._tickets = {}
        try:
            with open(fname) as infile:
                self._db = {elem[0]: Route(elem) for elem in csv.reader(infile)}
        except FileNotFoundError as e:
            raise SystemExit(str(e))

    def printRoutes(self):
        """ Print all the routes, with destination cities sorted in alphabetical order. """
        print("\n{:28s}{:16s}{:15s}".format("\tRoute", "Standard", "Business"))
        for dest in sorted(self._db.keys()):
            print(
                "San Jose - {:20s} {:10.2f} {:15.2f}".format(
                    dest,
                    self._db[dest].get_fare(),
                    self._db[dest].get_busFare(),
                )
            )

    def modifyRoutes(self):
        """Loop to ask the user to enter a new destination and fare or press the Enter key to end.
        Ask for the fare and check that the fare is a number.
        Add the new destination and fare to the database or change the existing destination with a new fare.
        Let the user know if you're modifying an existing city."""

        modified = False
        destination = (
            input('\nEnter a new destination city (press "Enter" to exit): ')
            .strip()
            .title()
        )
        while destination != "":
            # check whether the input for the fare is a number
            try:
                fare = float(input("Enter standard fare: "))
                if destination in self._db:
                    print(destination, "already exists, modifying", destination)
                modified = True
                self._db[destination] = Route([destination, fare])
            except ValueError:
                print("fare must be a number")
            destination = (
                input('\nEnter a new destination city (press "Enter" to exit): ')
                .strip()
                .title()
            )
        """
        When the user press the Enter key, if the database has been modified,
        call the printData function and printFile function. If the database has not
        been modified, don't print anything to screen or file.
        """
        if modified:
            self.printRoutes()

    def buyTickets(self):
        """User buys a ticket. Ask user for a destination. Ask for the type of fare.
        Print # of tickets, destination, total cost."""
        print("\n" + 12 * "=" + " Welcome to TechHub Airline " + 12 * "=" + "\n")
        moreTickets = True
        while moreTickets:
            destination = input("Destination? ").strip().title()
            while destination not in self._db:
                print(destination, "is not a destination. Choose from:")
                for city in sorted(self._db)[
                    :-1
                ]:  # for all items up to the last one print ',' after
                    print(city, end=", ")
                print(sorted(self._db)[-1])  # for the last item don't print ',' after
                destination = input("\nDestination? ").strip().title()

            # Ask the user for the number of tickets
            # Ask the user for 'r' for regular fare or 'b' for business class
            while True:
                numAndType = input(
                    "Number of tickets, then r (regular fare) or b (business class): "
                )
                try:
                    (ticNum, ticType) = numAndType.lower().strip().split()
                    ticNum = int(ticNum)
                    price = self._db[destination.title()].get_fare()
                    if ticType == "r":
                        ticType = "regular fare"
                        self._tickets[Ticket(destination, price)] = ticNum
                    elif ticType == "b":
                        ticType = "business class"
                        self._tickets[BusinessTicket(destination, price)] = ticNum
                    else:
                        print("Fare type is r or b")
                        continue
                    break
                except ValueError as e:
                    print(str(e))


            # Ask if the user wants to buy more tickets.
            choice = input("Buy more tickets? y/n: ")
            if choice.strip().lower() == "y":
                continue
            else:
                moreTickets = False
                if choice.strip().lower() != "n":
                    print("Invalid choice. Terminating.")
                print("\n" + 22 * "=" + "The End" + 22 * "=" + "\n")

            total = 0
            print("Receipt")
            for key in self._tickets:
                print(
                    "{:d} {:s} tickets to {:s}: ${:.2f} total".format(
                        self._tickets[key],
                        key.get_type(),
                        key.get_destination(),
                        key.get_fare() * self._tickets[key],
                    )
                )
                total += key.get_fare() * self._tickets[key]
            print(f"Grand total: ${total:.2f}")  # print receipt


    """
    Additional requirements:
        • For each module, add a beginning documentation block with your name and short description of the file
        • Docstring for every public method
        • There should be 3 modules, and each module should work as described.
    """


def main():
    print("\n" + 20 * "=" + " Welcome " + 20 * "=")
    # Airline administrator part:
    app = AirlineTicketing()
    app.printRoutes()
    app.modifyRoutes()
    # Customer part:
    app.buyTickets()


main()

