'''
This module provides functions to access dates used for a printing a pay stub and
pay check of the BoxMart Payroll program. Functions are:

start_date() - return the start date of the current pay period.
end_date()   - return the end date of the current pay period.
pay_date()   - return the pay check date of the current pay period.

This version of the module is provided for testing purposes as dates returned are
hard coded stubs.

Created on Oct 20, 2024

@author: Drashti Parimal Shah
'''

def start_date():
    return '01/14/2020'


def end_date():
    return '01/20/2020'


def pay_date():
    return '01/27/2020'


def get_code_verification(code):
    valid_codes = {"manager", "clerk", "cashier"}

    if code.lower() in valid_codes:
        return
    else:
        print("\nInvalid position code")
        exit()


def get_hourly_wage(code, employees_dict):
    return employees_dict[code]


def get_normal_pay(normal_hours_worked, hourly_wage):
    return normal_hours_worked * hourly_wage


def get_overtime_pay(overtime_hours_worked, hourly_wage):
    return overtime_hours_worked * hourly_wage * 1.5


def get_federal_tax(gross_pay):
    if (gross_pay >= 500):
        new_gross_pay = gross_pay - 500
        federal_tax = new_gross_pay * 0.1

        return federal_tax

    else:
        return 0


def get_state_pay(gross_pay):
    return gross_pay * 0.03


def get_net_pay(gross_pay, federal_tax, state_tax):
    total_tax = federal_tax + state_tax
    net_pay = gross_pay - total_tax
    return net_pay


def get_normal_hours_worked(hours, code):
    if code == "manager":
        return hours
    elif hours > 40:
        return 40
    else:
        return hours


def get_overtime_hours_worked(hours, code):
    if code == "manager":
        return 0
    elif hours > 40:
        return hours - 40
    else:
        return 0


def number_to_words(amount):
    if amount == 0:
        return "Zero and 0.00"

    else:
        dollars, cents = divmod(amount, 1)
        dollars = int(dollars)
        cents = int(round(cents * 100))

        digit_into_words = [
            "Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
            "Eighteen", "Nineteen", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy",
            "Eighty", "Ninety"
        ]
        dollar_part = ""

        if dollars >= 1000:
            thousands = dollars // 1000
            dollar_part += digit_into_words[thousands] + " Thousand "
            dollars %= 1000

        if dollars >= 100:
            hundreds = dollars // 100
            dollar_part += digit_into_words[hundreds] + " Hundred "
            dollars %= 100

        if dollars >= 20:
            tens = dollars // 10
            dollar_part += digit_into_words[20 + tens - 2] + " "
            dollars %= 10

        if dollars > 0:
            dollar_part += digit_into_words[dollars] + " "

        dollar_part = dollar_part.strip()

        if cents == 0:
            return f"{dollar_part}"

        cents_part = f"{cents:02d}"
        return f"{dollar_part} and 0.{cents_part}"
