class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self._salary = salary  

    def get_salary(self) -> float:
        return self._salary

    def get_role(self) -> str:
        return "Employee"


class Manager(Employee):
    def __init__(self, name: str, salary: float, bonus_rate: float = 0.1) -> None:
        super().__init__(name, salary)
        self.bonus_rate = bonus_rate

    def get_role(self) -> str:
        return "Manager"

    def get_bonus(self) -> float:
        return self.get_salary() * self.bonus_rate


def print_employee_info(employees: list[Employee]) -> None:
    for e in employees:
        print(f"{e.name} | Role: {e.get_role()} | Salary: {e.get_salary()}")


def main() -> None:
    e1 = Employee("Aruzhan", 250000)
    m1 = Manager("Timur", 400000, bonus_rate=0.2)

    print_employee_info([e1, m1])
    print("Manager bonus:", m1.get_bonus())

if __name__ == "__main__":
    main()
