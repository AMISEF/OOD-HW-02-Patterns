#The strategy pattern is used here  
#Behaviors that can be implemented in multiple ways:
#1. Assignment Strategy: Which department should the ticket go to?
#2. Response Strategy: What response should be sent?

from abc import ABC, abstractmethod

#First part :
#we have assignment strategy here 

class AssignmentStrategy(ABC):

#every strategy has to implement the assign method

    @abstractmethod
    def assign(self, ticket) -> None:
        pass


class BugAssignmentStrategy(AssignmentStrategy):

#bug tickets should be given to the engineering team

    def assign(self, ticket) -> None:
        print("ticket was assigned to the engineering team")


class SupportAssignmentStrategy(AssignmentStrategy):

#public tickets

    def assign(self, ticket) -> None:
        print("ticket was assigned to the support team")


#Second part : Response strategy

class ResponseStrategy(ABC):

#every strategy has to implement the respond method

    @abstractmethod
    def respond(self, ticket) -> None:
        pass


class BugResponseStrategy(ResponseStrategy):

#bug tickets

    def respond(self, ticket) -> None:
        response_text = (
            "report received. "
            "the team is working on it and will update you soon."
        )
        ticket.response = response_text
        print(f"Response was sent: {response_text}")


class GenericResponseStrategy(ResponseStrategy):

#other types of tickets

    def respond(self, ticket) -> None:
        response_text = (
            "your request has been received. "
            "we will get back to you shortly."
        )
        ticket.response = response_text
        print(f"public response has been sent : {response_text}")
