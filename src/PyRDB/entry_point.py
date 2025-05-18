from PyRDB.db import DBQuerier

employers = [
    {"id": 1, "name": "Employer 1"},
    {"id": 2, "name": "Employer 2"},
]

employees = [
    {"id": 1, "name": "employee 1", "employer_id": 1},
    {"id": 2, "name": "employee 2", "employer_id": 2},
    {"id": 3, "name": "employee 3", "employer_id": 1},
]

def fill_db_with_dummy_data():
    DBQuerier.insert_into("employers", employers)
    # DBQuerier.insert_into("employees", employees)

def read_employers_table():
    data = DBQuerier.select_from("employers")
    print(data)

if __name__ == '__main__':
    fill_db_with_dummy_data()
    read_employers_table()