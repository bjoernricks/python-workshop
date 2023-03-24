def days_and_hours_in_minutes(hours, days=0):
    minutes_days = days * 24 * 60
    minutes_hours = hours * 60
    minutes = minutes_days + minutes_hours
    print("The result is", minutes, "minutes")
    # implicit return None


return_value = days_and_hours_in_minutes(32)
print(return_value)  # prints out None
