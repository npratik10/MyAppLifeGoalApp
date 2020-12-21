"""
Algorithm for Spending and database:
1) Initial Ideas
    Create a enum entries for spending :
    {necessity: {Grocery_Veggies, Grocery_meat, rent, bills},
     entertainment: {food, movies, party, others},
     vacation: {hotel, car_rent, gas, tickets, food},
     car: {maintainence, insurance, gas, registration},
     miscellaneous: {makeup, home_improvement, kitchen, black_friday, clothes, others}}

    Create the entries for every month
    Create the spending analysis report every month
    Set spend limits for the year on different categories
    Alert when approaching the limit
"""

class spending:
    
    def __init__(self, spending_profile_name):
        self.__spending_profile_name = spending_profile_name
        
    def add_entry(self, category, entry_name, value):
        self.category = category
        self.entry_name = entry_name
        self.entry_value = value

    def get_profile_name(self):
        print(self.__spending_profile_name)

    def get_value(self, category, entry_name):
        print("Category: ", category, ", EntryName: ", entry_name, ", EntryValue: ", self.entry_value)

    def create_monthly_report(self, year, month):
        print('Report')
        
'''
print("Hello! Spending profile")
acnt1 = spending('pratik_household')
acnt1.get_profile_name()
acnt1.add_entry("necessity", "rent", 1600)
acnt1.get_value("necessity", "rent")
'''
    
