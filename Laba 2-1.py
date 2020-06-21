from math import floor
def calculate_percentage(num, percent):
    return floor((num/100) * percent)
salarys = []
amount_payables = []
with open('input.txt', 'r') as file:
    for line in file:
        salary = int(line)
        MINIMUM_WAGE = 12_130
        if salary > MINIMUM_WAGE:
            PENSION_TAX = calculate_percentage(salary, 6)
            tax = calculate_percentage((salary - MINIMUM_WAGE - PENSION_TAX), 13) + calculate_percentage(salary, 1)
            award_percent = int(input(f'Введите процент вознаграждения за {salary} зарплату: '))
            award = calculate_percentage(salary, award_percent)
            amount_payable = salary - tax + award
            salarys.append(salary)
            amount_payables.append(amount_payable)
            print(f'Сумма к оплате {amount_payable} руб\n')
        else:
            print(f'Ошибка зарплаты {salary} < МОРТа {MINIMUM_WAGE}\n')

with open('output.txt', 'w') as file:
    for s, a in zip(salarys, amount_payables):
        file.write(f'Зарплата {s} Подлежащая уплате сумма {a}\n')