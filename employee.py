# Name: Kanesha Feggans
# Prog Purpose: Calculate pay with all deductions for employees
#
#Category Codes and Pay Rates
#C   Cashier:        $16.50
#S   Stocker:        $15.75
#J   Janitor:        $15.75
#M   Maintenance:    $19.50
#       
#Deduction Rates
#Federal Income Tax Rate:    12%   
#State Income Tax Rate:      3%    
#Social Security Tax Rate:   6.2%  
#Medicare Tax Rate:          1.45% 

import datetime

#use tuples to define pay and deduction rates
pay_rates = (16.50, 15.75, 15.75, 19.50)
deduction_rates = (.12, .03, .062, .0145)

#define global variables
pay_rate = 0
gross_pay = 0
fed_tax = 0
state_tax = 0
ss_tax = 0
med_tax = 0
total_deductions = 0
net_pay = 0
job_cat = ""
job_title = ""
hours_worked = 0

def main():
    another_employee = True
    while another_employee:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input('Would you like to calculate pay for another employee? (Y/N): ')
        if yesno.upper() != "Y":
            another_employee = False

def get_user_data():
    global job_cat, job_title, hours_worked, pay_rate
    
    print('\nJob Category Codes: ', 'C: Cashier', 'S: Stocker', 'J: Janitor', 'M: Maintenance\n')
    
    job_cat = input("What is thejob category coed you want to calculate? (C, S, J, M): ")
    hours_worked = int(input("How many hours did the employee work?: "))
    
    if job_cat.upper() == 'C':
        pay_rate = pay_rates[0]
        job_title = 'Cashier'
    if job_cat.upper() =='S':
        pay_rate = pay_rates[1]
        job_title = 'Stocker'
    if job_cat.upper() =='J':
        pay_rate = pay_rates[2]
        job_title = 'Janitor'
    if job_cat.upper() == 'M':
        pay_rate = pay_rates[3]
        job_title = 'Maintenance'


def perform_calculations():
    global gross_pay, pay_rate, fed_tax, state_tax, ss_tax, med_tax, total_deductions, net_pay
    gross_pay = pay_rate * hours_worked
    fed_tax = gross_pay * deduction_rates[0]
    state_tax = gross_pay * deduction_rates[1]
    ss_tax = gross_pay * deduction_rates[2]
    med_tax = gross_pay * deduction_rates[3]
    total_deductions = fed_tax + state_tax + ss_tax + med_tax
    net_pay = gross_pay - total_deductions

def display_results():
    print('\n--------------------------------------------------')
    print('----------------------------------------------------')
    print('          ***** MARKETPLACE *****')
    print('          ****** EMPLOYEE PAY *******')
    print('----------------------------------------------------')
    print('----------------------------------------------------')
    print('         Job:                 ', job_title)
    print('         Pay Rate:            $', format(pay_rate,'8,.2f'))
    print('         Hours Worked:        $', format(hours_worked, '8,.2f'))
    print('----------------------------------------------------')
    print('         Gross Pay:           $', format(gross_pay, '8,.2f'))
    print('         Federal Tax:         $', format(fed_tax, '8,.2f'))
    print('         State Tax:           $', format(state_tax, '8,.2f'))
    print('         Social Security Tax: $', format(ss_tax, '8,.2f'))
    print('         Medicare Tax:        $', format(med_tax, '8,.2f'))
    print('         Deducations:         $', format(total_deductions, '8,.2f'))
    print('----------------------------------------------------')
    print('----------------------------------------------------')
    print('----------------------------------------------------')
    print('         Pay:                 $', format(net_pay, '8,.2f'))
    print('----------------------------------------------------')
    print('            ' + str(datetime.datetime.now()) + '\n')
main()
