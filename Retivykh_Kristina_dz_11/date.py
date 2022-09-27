class Date:
    
    def __init__(self, param):
        self.str_date = param
        
    @classmethod
    def extract_and_modify(cls, str_date):
        return tuple([int(x) for x in str_date.split('-')])
    
    @staticmethod
    def validate(date):
        try:
            day, month, year = [int(x) for x in date.split('-')]
        except TypeError:
            return False
        
        if (not (0 < month < 13)) or (not (0 < day < 31)) or (not (0 < year)):
            return False
        
        if (month == 2) and (day == 29):
            return ((not (year % 4)) or ((not (year % 100)) and (not (year % 400))))
        
        if month == 2:
            return (day < 29)
        
        if day == 31:
            return (month in (1,3,5,7,8,10,12))
        
        return True
        


if __name__ == '__main__':
    for date in ('03-11-2011', '25-12-1969', '29-02-2020', '29-02-2022', '31-09-1961', '32-01-2023'):
        try:
            print(Date(date))
            print(Date.extract_and_modify(date))
            print(Date.validate(date))
        except ValueError as e:
            print(e)