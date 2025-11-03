class Employee:
    def __init__(self, employee_id, name, position):
        self.employee_id = employee_id
        self.name = name
        self.position = position

    def __str__(self):
        return f'ID: {self.employee_id}, Name: {self.name}, Position: {self.position}'


class EmployeeManager:
    def __init__(self):
        self.employees = {}

    def create_employee(self, employee_id, name, position):
        if employee_id in self.employees:
            print("Employee already exists.")
            return False
        self.employees[employee_id] = Employee(employee_id, name, position)
        print(f"Employee '{name}' added successfully.")
        return True

    def update_employee(self, current_id, new_id=None, name=None, position=None):
        if current_id not in self.employees:
            print("Cannot find the employee to be updated in the database.")
            return False

        emp = self.employees[current_id]

        if new_id and new_id != current_id:
            if new_id in self.employees:
                print(f"Cannot change ID: new ID '{new_id}' is already in use.")
                return False
            emp.employee_id = new_id
            self.employees[new_id] = emp
            del self.employees[current_id]
            current_id = new_id

        if name:
            emp.name = name
        if position:
            emp.position = position

        print(f"Employee (ID: {emp.employee_id}) updated successfully: {emp}")
        return True

    def delete_employee(self, employee_id):
        if employee_id in self.employees:
            del self.employees[employee_id]
            print("Employee deleted successfully.")
            return True
        else:
            print("Employee not found in the database.")
            return False

    def list_emp(self):
        if not self.employees:
            print("Database is empty.")
            return
        for emp in self.employees.values():
            print(emp)


manager = EmployeeManager()


def main():
    while True:
        print("\n=== Employee Manager ===")
        print("1 -> Create an employee")
        print("2 -> Update an employee")
        print("3 -> Delete an employee")
        print("4 -> List employees")
        print("5 -> Exit")

        try:
            user_input = int(input("Choose an option (1-5): ").strip())
        except ValueError:
            print("Please enter a valid number (1-5).")
            continue

        if user_input == 1:
            user_id = input("Enter employee id: ").strip()
            user_name = input("Enter employee name: ").strip()
            user_position = input("Enter employee position: ").strip()
            manager.create_employee(user_id, user_name, user_position)

        elif user_input == 2:
            target_id = input("Enter the ID of the employee you want to update: ").strip()
            if target_id not in manager.employees:
                print("Employee not found.")
                continue

            while True:
                print("\nWhat would you like to update?")
                print("1 -> Change ID")
                print("2 -> Change name")
                print("3 -> Change position")
                print("4 -> Change multiple fields")
                print("5 -> Back to main menu")

                try:
                    opt = int(input("Choose an option (1-5): ").strip())
                except ValueError:
                    print("Please enter a valid number (1-5).")
                    continue

                if opt == 1:
                    new_id = input("Enter the new ID: ").strip()
                    manager.update_employee(current_id=target_id, new_id=new_id)
                    if new_id in manager.employees:
                        target_id = new_id
                elif opt == 2:
                    new_name = input("Enter the new name: ").strip()
                    manager.update_employee(current_id=target_id, name=new_name)
                elif opt == 3:
                    new_position = input("Enter the new position: ").strip()
                    manager.update_employee(current_id=target_id, position=new_position)
                elif opt == 4:
                    new_id = input("Enter the new ID (leave blank to keep current): ").strip() or None
                    new_name = input("Enter the new name (leave blank to keep current): ").strip() or None
                    new_position = input("Enter the new position (leave blank to keep current): ").strip() or None
                    manager.update_employee(current_id=target_id, new_id=new_id, name=new_name, position=new_position)
                    if new_id:
                        target_id = new_id
                elif opt == 5:
                    break
                else:
                    print("Unknown input. Please choose a valid option.")

        elif user_input == 3:
            delete_emp_id = input("Enter the ID of the employee to be deleted: ").strip()
            manager.delete_employee(delete_emp_id)

        elif user_input == 4:
            manager.list_emp()

        elif user_input == 5:
            print("Exiting. Goodbye!")
            break
        else:
            print("Unknown option. Choose between 1 and 5.")


if __name__ == "__main__":
    main()