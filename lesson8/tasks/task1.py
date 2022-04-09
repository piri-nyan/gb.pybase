print("Date class realisation")

class DayValidity(Exception):
    def __init__(self, *args):
        self.day, self.month = args

    def __str__(self):
        return f"There is no day number {self.day} in month number {self.month}"

class MonthValidity(Exception):
    def __init__(self, *args):
        self.month = args[0]

    def __str__(self):
        return f"There is no month number {self.month}"

class YearValidity(Exception):
    def __init__(self, *args):
        self.year = args[0]

    def __str__(self):
        return f"There is no day number {self.year}"

class Date():
    def __init__(self, date):
        self.date = date

    @classmethod
    def to_num(cls, date):
        return [int(x) for x in date.split("-")]

    @staticmethod
    def validate(self):
        day, month, year = Date.to_num(self.date)
        if month == 2:
            if day > 28:
                raise DayValidity(day, month)
            else:
                if day < 1 or day > 31:
                    raise DayValidity(day, month)
        elif month < 1 or month > 12:
            raise MonthValidity(month)
        if year < 1 or year > 2022: # <- this won't age well :)
            raise YearValidity(year)

dt = Date.to_num("22-02-2022")
print(dt)
dt = Date("22-02-2022")
dates = ["33-02-22", "22-13-2022", "22-02-0", "22-02-2022"]
for dt in [Date(date) for date in dates]:
    try:
        Date.validate(dt)
    except DayValidity as err:
        print(err)
    except MonthValidity as err:
        print(err)
    except YearValidity as err:
        print(err)
    else:
        print(f"Date {dt.date} is valid")