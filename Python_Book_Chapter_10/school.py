"""
Design a class structure (incl. arguments and methods) for a primary school.
"""
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta


class Person:
    def __init__(self, first_name, last_name, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob

    def get_name(self):
        return self.first_name

    def get_surname(self):
        return self.last_name

    def get_age(self):
        today = date.today()
        age = relativedelta(today, datetime.strptime(self.dob, '%Y-%m-%d')).years
        return age







