import string
import random
from typing import List
from abc import ABC, abstractmethod


def generate_id(length = 8):
    return "".join(random.choices(string.ascii_uppercase, k=length))

class SupportTicket:
    id: str
    customer: str
    issue: str

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue

class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        pass

class FIFOStrategy(TicketOrderingStrategy):

    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        return list.copy()

class FILOStrategy(TicketOrderingStrategy):

    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        list_copy.reverse()
        return list_copy

class RandomStrategy(TicketOrderingStrategy):

    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        random.shuffle(list_copy)
        return list_copy

class BlackHoleStrategy(TicketOrderingStrategy):

    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        return []

class CustomerSupport:

    tickets: List[SupportTicket] = []

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self, processing_strategy: TicketOrderingStrategy):

        ticket_list = processing_strategy.create_ordering(self.tickets)

        if len(ticket_list) == 0:
            print("Currently there are no tickets in queue.")
            return


        for ticket in ticket_list:
            self.process_ticket(ticket)


    def process_ticket(self, ticket: SupportTicket):
        print("===================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("===================================")

if __name__ == "__main__":
    app = CustomerSupport()

    app.create_ticket("John Schnee", "Weird noises. Something like beeeeeep booo booo baaaaaaaaa.")
    app.create_ticket("Robert Baratheon", "Am i drunk, or is this resolution too low?")
    app.create_ticket("David Kasdorf", "I always write bug-free code. This is just a ticket for proving it.")

    app.process_tickets(BlackHoleStrategy())





