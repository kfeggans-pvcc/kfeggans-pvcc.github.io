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
pizzasize = 'S'; 'M' ; 'L'; 'XL' #S Means Small M Means Medium L Means Large XL Means Xtra large
numpizzas = 0  #How many pizzas

    
def main():
    another_student = True
    while another_pizza:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to another pizza? (Y/N): ")
        if yesno == 'N' or yesno == 'n' or yesno == "no" or yesno =="No" :
            another_pizza= False

def get_user_data():
        global pizzasize, numpizzas
        pizzasize = int(input("Hey there! What size pizza whould you like today 'S,M,L'?: "))
        numpizzas = int(input("How many pizzas? : "))
       
def perform_calculations():
    global pizzacost, salestax, totaldue
    if  pizzasize == 'S':
        pizzacost = numpizzas * SM_PIZZAS
        
    if  pizzasize == 'M':
        pizzacost = numpizza * MED_PIZZAS
    
    if pizzasize == 'L'
        pizzacost = numpizza * LRG_PIZZAS
   
    if pizzasize == 'XL'
    pizzacost= numbpizza * XL_PIZZAS

        capitalfee = 0
    else:
        tuitionfee = numcredits * RATE_TUITION_OUT
        capitalfee = numcredits * RATE_CAPITAL

    institutionfee = numcredits * RATE_INSTITUTION
    activityfee = numcredits * RATE_ACTIVITY
    totalowed = tuitionfee + capitalfee + institutionfee + activityfee
    balance = totalowed - scholarshipamt

def display_results():
    print('\n****************************************')
    print('Number of pizzas ordered : ' + str(numpizzas))
    print('****************************************')
    print('Size         $ ' + format(pizzasize,'10,.2f'))
    print('     $ ' + format(capitalfee,'10,.2f'))
    print('Sales tax          $ '+ format(SALES_TAX_RATE,'10,.2f'))
    print('Scholarship     $ ' + format(scholarshipamt,'10,.2f'))
    print('****************************************')
    print('Balance Owed    $ ' + format(balance,'10,.2f'))
    print('****************************************')
    print(str(datetime.datetime.now()))
    print("NOTE: PVCC Fee Rates: https://www.pvcc.edu/tuition-and-fees")


# call on main program to execute
main()




import random
topics = []
TOTAL_TOPICS = 5 #test this program with 5 topics

def main():
    num_used_topics = 0
    for i in range(TOTAL_TOPICS): #fill the list with items with an "A" in each one
        topics.append("A")

    generate_another_randnunber = True #boolean variable to control the outer loop
    continue_search = True #boolean to control the inner loop

    while continue_search: #OUTER LOOP
        continue_search=True

        while continue_search: #INNERLOOP
            randnumber = random.randint(0, TOTAL_TOPICS-1) #items in list start with 0, not 1
            if topics[randnumber]== "A":
                topics[randnumber]= "U"
                num_used_topics += 1
                continue_search= False
        print("\nRandom Topic Number: " + str(randnumber+1)) #items in list start with 0, so add 1
        print("List of topic avalibility by number:")
        for i in range (TOTAL_TOPICS):
            print("\t"+ str(i+1) + ". " + topics[i])
        
        if num_used_topics == TOTAL_TOPICS:
            print("There are no more topics avaliable at this time.")
            return() #quite the main() function
        else:
            answer = input("Would you like another random number Y/N: ")
            if answer.upper() == "n" or answer.upper() == "N":
                generate_another_randnunber= False

main()
