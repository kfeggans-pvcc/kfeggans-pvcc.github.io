# Name:Kanesha Feggans
# Prog Purpose: This program computes the sum based on the total amount of pizzas placed with and ordered at Palermo Pizza
#  
 # Note: Pizza Sizes are   
#       Small pizza :      $ 9.99
#       Medium d Pizza:    $ 12. 99
#       Large pizza:       $ 14.99
#       Xrta Large pizza : $ 2.90
#       Sales Tax on every total : .005

import datetime
from functools import update_wrapper
#define tax rate and prices
SALES_TAX_RATE = .055
PR_TICKET = 10.99


#define global variables
num_tickets = 0
subtotal = 0
sales_tax = 0
total = 0  

    
def main():
    another_ticket = True
    while another_ticket:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to purchase another ticket?? (Y/N): ")
        if yesno == 'N' or yesno == 'n' or yesno == "no" or yesno =="No" :
            another_ticket = False

def get_user_data():
        global num_tickets
        num_tickets= int(input("Number of movies tickets: "))
       
def perform_calculations():
    global subtotal, sales_tax, total
    subtotal = num_tickets * PR_TICKET 
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax
    

def display_results():
    print('\n*********************************')
    print('     CINEMA MOVIE HOUSE     ')
    print('Your neighborhood movie house')
    print('*****************************')
    print('Tickets         $ '+ format(subtotal,'8,.2f'))
    print('Sales tax       $ '+ str(sales_tax))
    print('****************************')
    print('Total           $ ' + str(total))
    print('********************************')
    print(str(datetime.datetime.now()))
    print("NOTE: Tickets can only be refunded as  movie(s) credit at: \n CINEMA MOVIE HOUSE.\n Tickets are non-refundable for for cash/credit back. ")


# call on main program to execute
main()