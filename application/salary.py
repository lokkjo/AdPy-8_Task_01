import random


def calculate_salary(employees) -> list:
    checklist = {}
    for person in employees:
        checklist[person] = (random.randint(25, 50) * 1000)
    return checklist
