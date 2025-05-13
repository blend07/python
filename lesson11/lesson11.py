import datetime
current_datetime = datetime.datetime.now()

print(current_datetime)

print("Year:", current_datetime.year)
print("Month:", current_datetime.month)
print("Day:", current_datetime.day)
print("Hour:", current_datetime.hour)
print("Minute:", current_datetime.minute)
print("Second:", current_datetime.second)
print("Microsecond:", current_datetime.microsecond)

current_datetime1 = datetime.datetime.now().date()
print(current_datetime1)
current_datetime2 = datetime.datetime.now().time()
print(current_datetime2)

time_object = datetime.date(2025, 5, 13)

print(time_object)

timedelta = datetime.timedelta(days=5, hours=5)
print(timedelta)

new_date = time_object + timedelta
print(new_date)