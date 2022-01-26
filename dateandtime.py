from datetime import *

today = datetime.now()

print(type(today))
print(type(today.date()))
print(type(today.time()))

# timedelta - used to do some date or time based calculations

one_week_after = today + timedelta(days=7)
print(one_week_after)

one_week_before = today - timedelta(days=7)
print(one_week_before)

one_hour_after = today + timedelta(hours=1)
print(one_hour_after)

# strftime() - changing datetime to string

print(today.strftime('%a, %d-%b-%Y %I:%M %p'))

# strptime() - converting string to datetime

string_date = "26 Sep 2022 1:54 PM"

print(datetime.strptime(string_date, "%d %b %Y %I:%M %p"))