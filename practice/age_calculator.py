import datetime

date = int (input("what is the date which you were born?:"))
month= int (input("what is the month which you were born?"))
year = int (input("what is the year which you were born?"))

def calculate_age(birth_date):
    today = datetime.date.today()
    age_years = today.year - birth_date.year
    age_month = today.month - birth_date.month
    age_date = today.day - birth_date.day

    #adjust if birth month/day hasn't occurred yet this year 
    if age_date < 0 :
        age_month -= 1
        age_date += (datetime.date(today.year, today.month, 1) - datetime.timedelta(days=1)).day

    if age_month < 0 :
        age_years -= 1
        age_month += 12

    return age_years, age_month, age_date

try:
    birth_date = datetime.date(year, month, date)
    age_years, age_months, age_days = calculate_age(birth_date)
    print(f"You are {age_years} years, {age_months} months, and {age_days} days old.")
except ValueError:
    print("Invalid input! Please enter valid numbers for year, month, and day.")
    