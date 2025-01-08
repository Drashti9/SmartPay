'''
Assignment 1 - Boxmart Payroll

This script will on input of an employee name, number of hours worked, and a position code, compute and
print a pay stub and a pay check for the employee.  Rules for computation are as follows:

1. Hourly rate is determined by a position code where a cashier is paid $ 12.25/hr, clerk is paid $
   18.00/hr, and manager is paid $ 25.75/hour.
2. If the position code is not one of above, then print "Invalid code", and exit()
3. For everyone except for managers, the hours over 40 in a week are considered to be overtime hours
   (note normal hours of non-manager's can be at most 40).
4. Normal pay is normal hours times hourly rate.
5. Overtime pay is overtime hours times hourly rate times 1 1/2.
6. Gross pay is the sum of normal pay and overtime pay.
7. Federal tax is 10% of gross pay in excess of 500.
8. State tax is 3% of gross pay.
9. Net pay is gross pay less federal tax and less state tax.
10. Use start_date and end_date functions from the pay_period module to get the pay period dates. See module pay_period.py.
11. Use the pay_date function from the pay_period module to get the date of the check. See module pay_period.py.

Created on Oct 20, 2024

@author: Drashti Parimal Shah
'''
from pay_period import *

employees_dict = {
    "cashier": 12.25,
    "clerk": 18.00,
    "manager": 25.75
}

name = input("Enter employee name:\n")
hours = int(input("Enter hours worked:\n"))
code = input("Enter position code:\n")

get_code_verification(code)
print()
# TODO add calculations

print("            BoxMart Pay Stub")
print()
print(f"Employee Name: {name}")

# TODO complete print
print(f"Pay Period:    " + start_date() + " to " + end_date())
print()

normal_hours_worked = get_normal_hours_worked(hours, code)
if normal_hours_worked == 0:
    print(f"Normal Hours Worked:               {normal_hours_worked} hrs")
else:
    print(f"Normal Hours Worked:              {normal_hours_worked} hrs")

overtime_hours_worked = get_overtime_hours_worked(hours, code)
print(f"Overtime Hours Worked:             {overtime_hours_worked} hrs")

hourly_wage = get_hourly_wage(code, employees_dict)
print(f"Hourly Wage:               $   {hourly_wage:0.2f}/hr")
print()

normal_pay = get_normal_pay(normal_hours_worked, hourly_wage)
print(f"Normal Pay:                ${normal_pay:8.2f}")

overtime_pay = get_overtime_pay(overtime_hours_worked, hourly_wage)
print(f"Overtime Pay:              ${overtime_pay:8.2f}")

gross_pay = normal_pay + overtime_pay
print(f"Gross Pay:                 ${gross_pay:8.2f}")

federal_tax = get_federal_tax(gross_pay)
print(f"Federal Tax:               ${federal_tax:8.2f}")

state_tax = get_state_pay(gross_pay)
print(f"State Tax:                 ${state_tax:8.2f}")

net_pay = get_net_pay(gross_pay, federal_tax, state_tax)
print(f"Net Pay:                   ${net_pay:8.2f}\n")

print(f"Box Mart, Inc.                  {pay_date()}\n")

if normal_hours_worked == 0:
    print(f"Pay to: {name}                ${net_pay:8.2f}")
else:
    print(f"Pay to: {name}               ${net_pay:8.2f}")

print(f"{number_to_words(net_pay)}")
