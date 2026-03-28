from datetime import datetime, timedelta

now = datetime.now()
print("Сейчас:", now)

print("Через 7 дней:", now + timedelta(days=7))
print("7 дней назад:", now - timedelta(days=7))

birth_date = datetime(2005, 5, 15)
days_passed = (now - birth_date).days
print("Дней с рождения:", days_passed)