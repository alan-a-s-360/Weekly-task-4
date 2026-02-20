class Employee:
    def __init__(self, employee_name, employee_id, salary):
        self.employee_name = employee_name
        self.employee_id = employee_id
        self.salary = salary
    def increase_salary(self, amount):
        if amount > 0:
            self.salary += amount
            print(f"Salary increased by ${amount}")
        else:
            print("Increase amount must be positive.")
    def display_details(self):
        print("----- Employee Details -----")
        print(f"Name: {self.employee_name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary}")
        print("-----------------------------")
employee1 = Employee("Alice Smith", "EMP001", 50000)
employee1.display_details()
employee1.increase_salary(5000)
employee1.display_details()                                                                                                                                                                                                                 Q2
