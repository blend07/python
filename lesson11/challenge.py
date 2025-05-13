import datetime
filepath = "C:/Users/Student/Desktop/New folder/python/lesson11/file.txt"


futuredelta = datetime.timedelta(days=100)

pastdelta = datetime.timedelta(days=-100)

currentdate = datetime.date(2025, 5, 13)

future = currentdate + futuredelta
print(future)
past = currentdate + pastdelta
print(past)


with open(filepath, "w") as file:
    file.write(f"Future Delta: {future}, Past Delta: {past}")

