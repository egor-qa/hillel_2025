class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size

def test_team_lead():
    lead = TeamLead('Taras', 50000, 'Backend', 'Python', 4)

    assert lead.name == 'Taras'
    assert lead.salary == 50000
    assert lead.department == 'Backend'
    assert lead.programming_language == 'Python'
    assert lead.team_size == 4

    print("All tests passed successfully!")