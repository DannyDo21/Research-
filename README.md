# Research-
a research repo for demo
Instructions for Software Project for Help Desk Ticketing System

The code is an implementation of a Help Desk Ticketing System using the Python programming language. The system keeps track of tickets created, resolved, and open tickets to solve. 
The program has a class called Ticket represents a ticket object that has various attributes such as ticket number, creator name, staff ID, contact email, description, response, and status. The class also has several methods that define the behavior of a ticket object such as resolving a password change request, responding to a ticket, reopening a ticket, and printing ticket statistics and information.
1.	_init__ - This method initializes a ticket object with the provided information such as staff ID, creator name, contact email, and description.

2.	resolve_password_change_request - This method checks if the ticket is for a password change request and generates a new password. The new password is a combination of the first two characters of the staff ID and the first three characters of the creator's name.

3.	respond_to_ticket - This method allows the IT department to provide a response to a ticket and close it.

4.	reopen_ticket - This method allows the IT department to reopen a ticket that was previously closed.

5.	print_ticket_stats - This method prints the statistics of the tickets such as the number of tickets created, resolved, and open tickets to solve.

6.	print_ticket_info - This method prints the information about a ticket such as ticket number, creator name, staff ID, contact email, description, response, and status.
The code also creates three ticket objects as an example, resolves one ticket for a password change request, and prints the ticket statistics and information.

