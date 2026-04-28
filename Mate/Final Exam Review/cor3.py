'''
Design a customer support ticketing system that routes tickets to the correct department. 

Tickets have a type:
'technical', 'billing', 'general'
'''

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
    # cor ends here
    # ??? TODO
    def can_handle(self, ticket):
        return ticket.type == 'billing'
    
    def handle_ticket(self, ticket):
        if self.can_handle(ticket):
            print(f"BillingHandler: Handling {ticket} ticket about {ticket.message}")
        else:
            super().handle_ticket(ticket)

class TechnicalHandler(SupportHandler):
    # should forward to BillingHandler
    # ??? TODO
    def can_handle(self, ticket): # pyright: ignore[reportIncompatibleMethodOverride]
        keywords = ["crash", "bug", "error"]
        has_keyword = any(keyword in ticket.message.lower() for keyword in keywords)
        return ticket.type == 'technical' or has_keyword
    
    def handle_ticket(self, ticket):
        if self.can_handle(ticket):
            print(f"TechnicalHandler: Handling ticket about {ticket.message}")
        else:
            super().handle_ticket(ticket)

class GeneralHandler(SupportHandler):
    # should forward to TechnicalHandler
    # ??? TODO
    def can_handle(self, ticket):
        return ticket.type == 'general'
    
    def handle_ticket(self, ticket):
        if self.can_handle(ticket):
            print(f"GeneralHandler: Handling ticket about {ticket.message}")

if __name__ == "__main__":
    general_h = GeneralHandler()
    technical_h = TechnicalHandler(general_h)
    support_chain = BillingHandler(technical_h) 

    # ??? TODO
    ticket1 = Ticket("billing", "I want to dispute a charge.")
    ticket2 = Ticket("technical", "The application keeps crashing on startup.")
    ticket3 = Ticket("general", "How do I reset my password?")
    ticket4 = Ticket("other", "There is a bug in the payment form.") 

    print("--- Processing Tickets ---")
    support_chain.handle_ticket(ticket1)
    support_chain.handle_ticket(ticket2)
    support_chain.handle_ticket(ticket3)
    support_chain.handle_ticket(ticket4)
    print("\n--- Processing Complete ---")