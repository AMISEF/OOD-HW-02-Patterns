

# I have used the state pattern in here which means the behaviour of handle class is different
#  based on the current state of the ticket .

from abc import ABC, abstractmethod


class TicketState(ABC):

#Each state is to implement the handle method

    name: str = "BASE"

    @abstractmethod
    def handle(self, ticket, service):
        pass


#state 1 : new
class NewState(TicketState):


    name = "NEW"

    def handle(self, ticket, service):
        print("ticket was created ")

        
        if ticket.channel == "WEB":
            print("The request was received through the web")
        elif ticket.channel == "EMAIL":
            print("The request was received through email")
        else:
            print(f"Unknown channel {ticket.channel}")

        ticket.set_state(AssignedState())


#state 2 : assigned
class AssignedState(TicketState):

    name = "ASSIGNED"

    def handle(self, ticket, service):
        service.assignment_strategy.assign(ticket)
        ticket.set_state(InProgressState())


#state 3 : in progress
class InProgressState(TicketState):


    name = "IN_PROGRESS"

    def handle(self, ticket, service):
        print("the ticket is being worked on")

        service.response_strategy.respond(ticket)

        ticket.set_state(ResolvedState())

#state 4 : resolved 
class ResolvedState(TicketState):


    name = "RESOLVED"

    def handle(self, ticket, service):
        print("ticket is resolved")
        ticket.set_state(ClosedState())


#state 5 : closed
class ClosedState(TicketState):


    name = "CLOSED"

    def handle(self, ticket, service):
        print("ticket is closed")
