from abc import ABC, abstractmethod

class Ticket:
    def __init__(self, ticket_type, message):
        self.type = ticket_type
        self.message = message

class SupportHandler(ABC):
    def __init__(self, successor=None):
        self.successor = successor

    def handle_ticket(self, ticket):
        if self.successor:
            self.successor.handle_ticket(ticket)
        else:
            print(f"Ticket cannot be handled: {ticket.message}")

    @abstractmethod
    def can_handle(self, ticket):
        pass

class BillingHandler(SupportHandler):
    def can_handle(self, ticket):
        return ticket.type == "billing"

    def handle_ticket(self, ticket):
        if self.can_handle(ticket):
            print(f"BillingHandler: Handling ticket about {ticket.message}")
        else:
            super().handle_ticket(ticket)

class TechnicalHandler(SupportHandler):
    def can_handle(self, ticket):
        keywords = ["crash", "bug", "error"]
        has_keyword
        return ticket.type == "technical"

    def handle_ticket(self, ticket):
        if self.can_handle(ticket):
            print(f"TechnicalHandler: Handling ticket about {ticket.message}")
        else:
            super().handle_ticket(ticket)

class GeneralHandler(SupportHandler):
    def can_handle(self, ticket):
        return isinstance(ticket, Ticket) and ticket.type == "general"

    def handle_ticket(self, ticket):
        if self.can_handle(ticket):
            print(f"GeneralHandler: Handling ticket about {ticket.message}")
        else:
            super().handle_ticket(ticket)

if __name__ == "__main__":
    general_h = GeneralHandler()
    technical_h = TechnicalHandler(general_h)
    support_chain = BillingHandler(technical_h) 

    ticket1 = Ticket("billing", "I want to dispute a charge.")
    ticket2 = Ticket("technical", "The application keeps crashing.")
    ticket3 = Ticket("general", "How to reset my password?")
    ticket4 = Ticket("others", "There is a bug in my form")

    support_chain.handle_ticket(ticket1)
    support_chain.handle_ticket(ticket2)
    support_chain.handle_ticket(ticket3)
    support_chain.handle_ticket(ticket3)