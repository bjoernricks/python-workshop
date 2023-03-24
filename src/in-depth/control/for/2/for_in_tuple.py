def hours_in_minutes(hours):
    minutes = hours * 60
    return minutes


hours_list = (10, 5, 22, 32, 9)
for hours in hours_list:
    print(hours, "hours are", hours_in_minutes(hours), "minutes")
