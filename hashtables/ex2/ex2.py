class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    # Create a dictionary (hash table) for all the tickets.
    tix = {ticket.source: ticket for ticket in tickets}

    # Instantiate a list of tickets to be added in order of route.
    trip = []

    # The ticket with "NONE" origin is the first ticket.
    curr_ticket = tix["NONE"]

    # The ticket with "NONE" destination is the last ticket.
    while curr_ticket.destination != "NONE":
        trip.append(curr_ticket.destination)
        curr_ticket = tix[curr_ticket.destination]
    trip.append(curr_ticket.destination)

    return trip
