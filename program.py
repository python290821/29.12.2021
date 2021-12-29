
# input salary
# check if salary 5000, 15,000

# custom exception
class SalaryNotInRangeError(Exception):
    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.message = message
        self.salary = salary
        super().__init__(self.message)

    def __str__(self):
        return f'SalaryNotInRangeError: {self.message}'

def get_salary():
    salary = int(input("Enter salary: "))
    if not 5000 < salary < 15000:
        raise SalaryNotInRangeError(salary)
    return salary

try:
    salary = get_salary()
except SalaryNotInRangeError as e:
    print(e)
    print(f'you entered {e.salary} which is illegal')











