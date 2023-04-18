"""Software Project for Help Desk Ticketing System
Author: Danny Do"""

class Ticket:
    counter = 1
    open_tickets = 0
    closed_tickets = 0

    def __init__(self, staff_id, creator_name, contact_email, description):
        self.ticket_number = Ticket.counter + 2000
        Ticket.counter += 1
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"
        Ticket.open_tickets += 1
    
    # this is the rule for password change ticket
    def resolve_password_change_request(self):
        if "Password Change" in self.description:
            new_password = self.staff_id[:2] + self.creator_name[:3]
            self.response = f"New password generated: {new_password}"
            self.status = "Closed"
            Ticket.open_tickets -= 1
            Ticket.closed_tickets += 1

    def respond_to_ticket(self, response):
        self.response = response
        self.status = "Closed"
        Ticket.open_tickets -= 1
        Ticket.closed_tickets += 1

    def reopen_ticket(self):
        self.status = "Reopened"
        Ticket.open_tickets += 1
        Ticket.closed_tickets -= 1

    @staticmethod
    def print_ticket_stats():
        print("Tickets Created:", Ticket.counter - 1)
        # -1 because ticket counter starts at 1, we want the total number of tickets created, not the current value of the counter
        print("Tickets Resolved:", Ticket.closed_tickets)
        print("Tickets To Solve:", Ticket.open_tickets)
       

    def print_ticket_info(self):
        print("Ticket Number:", self.ticket_number)
        print("Ticket Creator:", self.creator_name)
        print("Staff ID:", self.staff_id)
        print("Email Address:", self.contact_email)
        print("Description:", self.description)
        print("Response:", self.response)
        print("Ticket Status:", self.status)


if __name__ == "__main__":
    # Creating 3 tickets for example
    ticket1 = Ticket("INNAM", "Inna", "inna@whitecliffe.co.nz", "My monitor stopped working")
    ticket2 = Ticket("MARIAH", "Maria", "maria@whitecliffe.co.nz", "Request for a videocamera to conduct webinars")
    ticket3 = Ticket("JOHNS", "John", "john@whitecliffe.co.nz", "Password Change")

  

    # Resolving tickets

    # An option for IT department provides the response to a ticket-------
    # ticket1.respond_to_ticket("Replaced monitor")

    ticket3.resolve_password_change_request()


    # An option for the IT department to reopen the ticket---------
    # ticket1.reopen_ticket()


    # Displaying ticket statistics and ticket information 
    print("\nTicket Statistics:")
    Ticket.print_ticket_stats()
    print("\nPrinting Tickets:")
    ticket1.print_ticket_info()
    print()
    ticket2.print_ticket_info()
    print()
    ticket3.print_ticket_info()

  
  

   
