import datetime
from application.db.people import get_employees as get_team
from application.salary import calculate_salary as salary


def salary_checkout():
    today = datetime.date.today()
    team = get_team()
    salary_sum = salary(team)
    print(f'\nЗарплатная смета от {today.day}.{today.month}.'
          f'{today.year}\n')
    for employee in salary_sum:
        print(f'{employee}: {salary_sum[employee]} рублей')
    print(f'\nИТОГО: {sum(salary_sum.values())} рублей')


if __name__ == '__main__':
    salary_checkout()
