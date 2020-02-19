time_sec = int(input("Please enter time in seconds: "))
seconds = time_sec % 60
# print("seconds: ", seconds)
minutes1 = time_sec // 60
minutes = minutes1 % 60
# print("minutes: ", minutes)
hours = time_sec // 3600
# print("hours: ", hours)
print("Your time is {:0>2d}:{:0>2d}:{:0>2d}".format(hours, minutes, seconds))
