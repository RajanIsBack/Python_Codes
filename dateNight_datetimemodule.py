import datetime

current_time=datetime.datetime.now()
print(current_time)
hour=(current_time.hour)
min=(current_time.minute)

if (hour >18 and min >30) and (hour <5  and min <30):
    print("It's DARK - NIGHT TIME")
else:
    print("It's not DARK - DAY TIME")

