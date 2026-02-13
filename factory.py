
# Factory pattern is used here
# Creating a Ticket object along with its appropriate strategies.
# Using this pattern, ticket creation is separated from the main code
# and new types of tickets can be easily added.

from ticket import Ticket
from states import NewState
from strategies import (
    BugAssignmentStrategy,
    SupportAssignmentStrategy,
    BugResponseStrategy,
    GenericResponseStrategy,
)


class TicketFactory:

    # factory of creating tickets
    # proper strategies are assigned to the ticket based on its type

    @staticmethod
    def create(ticket_id: int, channel: str, ticket_type: str) -> tuple:

        # it creates a ticket with its proper strategies
        ticket = Ticket(ticket_id, channel, ticket_type)

        ticket.set_state(NewState())

        if ticket_type == "BUG":
            assignment_strategy = BugAssignmentStrategy()
            response_strategy = BugResponseStrategy()
        else:
            assignment_strategy = SupportAssignmentStrategy()
            response_strategy = GenericResponseStrategy()

        print(
            f" [Factory] Ticket #{ticket_id} of type '{ticket_type}' "
            f"created from channel '{channel}'"
        )

        return ticket, assignment_strategy, response_strategy
