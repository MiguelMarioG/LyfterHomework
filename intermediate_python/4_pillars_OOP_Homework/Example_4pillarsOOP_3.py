class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def clock_in(self):
        print(f"{self.name} has checked in")


class ProgrammerSkill:
    def write_code(self):
        print(f"{self.name} is writing Python code...")

    def debug_errors(self):
        print(f"{self.name} is fixing a bug in the system")


class LeadershipSkill:
    def organize_meeting(self):
        print(f"{self.name} has called a meeting with the team")

    def approve_vacation(self, employee_name: str):
        print(f"{self.name} approved the vacation for {employee_name}.")


class Developer(Employee, ProgrammerSkill):
    def __init__(self, name: str, salary: float, primary_language: str):
        super().__init__(name, salary)
        self.primary_language = primary_language


class TechLead(Employee, ProgrammerSkill, LeadershipSkill):
    def __init__(self, name: str, salary: float, equipment: str):
        super().__init__(name, salary)
        self.equipment = equipment


def main():
    print("=== Demonstration of Multiple Inheritance ===\n")
    tech_lead = TechLead("Miguel Mario", 85000, equipment="Backend Python")
    tech_lead.clock_in()
    tech_lead.write_code()
    tech_lead.organize_meeting()
    tech_lead.approve_vacation("Maribel")
    print()
    dev = Developer("Maribel", 94200, primary_language="Python, Java, C#, C++")
    dev.clock_in()
    dev.debug_errors()


if __name__ == "__main__":
    main()