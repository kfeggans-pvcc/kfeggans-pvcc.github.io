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
#define pizza sizes and tax
SALES_TAX_RATE = .055
SM_PIZZA = 9.99
MED_PIZZA = 12.99
LRG_PIZZA = 14.99
XL_PIZZA = 17.99

#define global variables
pizzasize = "" #S Means Small M Means Medium L Means Large XL Means Extra large
numpizzas = 0  #How many pizzas

    
def main():
    another_pizza = True
    while another_pizza:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to another pizza? (Y/N): ")
        if yesno == 'N' or yesno == 'n' or yesno == "no" or yesno =="No" :
            another_pizza = False

def get_user_data():
        global pizzasize, numpizzas
        pizzasize = input("Hey there! What size pizza whould you like today: \n S for Small \n M for Medium \n L for Large \n X Extra Large'?: ")
        numpizzas = int(input("How many pizzas? : "))
       
def perform_calculations():
    global pizzacost, salestax, totaldue
    if  pizzasize.upper() == 'S':
        pizzacost = numpizzas * SM_PIZZA
        
    if  pizzasize.upper() == 'M':
        pizzacost = numpizzas * MED_PIZZA
    
    if pizzasize.upper() == 'L':
        pizzacost = numpizzas * LRG_PIZZA
   
    if pizzasize.upper() == 'X':
        pizzacost = numpizzas * XL_PIZZA
   
    salestax = pizzacost * SALES_TAX_RATE
    totaldue =  pizzacost + salestax 
    

def display_results():
    print('\n****************************************')
    print('             Palermo Pizza')
    print('****************************************')
    print('Number of pizzas ordered : ' + str(numpizzas))
    print('Size          ' + pizzasize)
    print('****************************************')
    print('Pizza cost      $ '+ format(pizzacost,'10,.2f'))
    print('Sales tax       $ '+ format(salestax,'10,.2f'))
    print('****************************************')
    print('Total Due       $ ' + format(totaldue,'10,.2f'))
    print('****************************************')
    print(str(datetime.datetime.now()))
    print("NOTE: ")


# call on main program to execute
main()