import datetime
from application import *
from application.db import *


def salary_checkout():
    today = datetime.date.today()
    team = people.get_employees()
    salary_sum = salary.calculate_salary(team)
    print(f'\nЗарплатная смета от {today.day}.{today.month}.'
          f'{today.year}\n')
    for employee in salary_sum:
        print(f'{employee}: {salary_sum[employee]} рублей')
    print(f'\nИТОГО: {sum(salary_sum.values())} рублей')


if __name__ == '__main__':
    salary_checkout()