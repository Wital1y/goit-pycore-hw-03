import datetime

def get_days_from_today(date):
    try:
        target_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        current_date = datetime.date.today()
        difference = target_date - current_date
        return difference.days
    except ValueError:
        return "Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'."
    
print(get_days_from_today("2021-10-09"))
print(get_days_from_today("2024-12-31"))
print(get_days_from_today("2024/12/31"))
