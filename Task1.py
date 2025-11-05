from datetime import datetime

def get_days_from_today(date):
    try:
        date_object = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print ("Invalid date format, please use YYYY-MM-DD")
        return None 

    today = datetime.today().date()
    delta = today - date_object.date()
    return delta.days

print(get_days_from_today("2026-10-01"))