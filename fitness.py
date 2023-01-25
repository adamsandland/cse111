import math
from datetime import datetime

def convert_to_metric(amt, units):
    if units=="lbs":
        return amt*0.45359237
    if units=="inches":
        return amt*2.54

def compute_BMI(w, h):
    return ((10000*w)/(h*h))

def compute_BMR(g, w, h, a):
    if g=="m":
        return (88.362+(13.397*w)+(4.799*h)-(5.677*a))
    if g=="f":
        return (447.593+(9.247*w)+(3.098*h)-(4.330*a))

def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years

def main():
    gender = input("Please Enter your Gender (m/f): ")
    birthDate = input("Please enter your Birth Date (YYYY-MM-DD): ")
    weight = int(input("Please enter your weight in lbs: "))
    height = int(input("Please enter your height in inches: "))
    age = compute_age(birthDate)
    bmi = compute_BMI(weight, height)
    bmr = compute_BMR(gender, weight, height, age)

    print(f"Results:\nAge: {age}\nWeight: {weight}kg\nHeight: {height}cm\nBMI: {bmi}\nBMR: {bmr}")

main()
