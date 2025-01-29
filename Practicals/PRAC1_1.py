import datetime as dt
today = dt.datetime.today()
year = int(input("enter birth year: "))
month = int(input("enter birth month: "))
day = int(input("enter birth date: "))
birth_date = dt.datetime(year, month, day)
age = today.year - birth_date.year
print(f"Your age is: {age}")
