"""
Short program that calculates the age of a person given their birthday (user input).

Issues:
- calculator does not acknowledge leap years in calculating i.e. it assumes every year is 365 days long
- no error handling

For a basic test of running a program in terminal, fixes for these are irrelevant
"""

from datetime import datetime, date

def get_date() -> date:
    # Get the given date from the user
    day = int(input("Please enter the day e.g. 3, 21: "))
    month = int(input("Please enter the month e.g. 5, 11: "))
    year = int(input("Please enter the year e.g. 2026: "))
    birthday = date(year,month,day)
    return birthday

def date_difference(given_date: date) -> int:
    # A function that calculates the age between the current date and a given date
    age = date.today() - given_date
    age_in_seconds = age.total_seconds()
    age_in_days = age_in_seconds/(3600*24)
    age_in_years = int(age_in_days//365)
    return age_in_years

print("---Welcome to the age calculator. Please enter a birthday to calculate from.---")
print("")

birthday = get_date()
age = date_difference(birthday)
print(f"\nThey are {age} years old.")
print("")
print("Thanks for using the calculator. Bye.")