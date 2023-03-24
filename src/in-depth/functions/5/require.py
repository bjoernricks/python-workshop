def days_and_hours_in_minutes(hours, *, days=0):
    minutes_days = days * 24 * 60
    minutes_hours = hours * 60
    minutes = minutes_days + minutes_hours
    return minutes


return_value = days_and_hours_in_minutes(32)
print("The result is", return_value, "minutes")

# this will fail
# return_value = days_and_hours_in_minutes(32, 14)

return_value = days_and_hours_in_minutes(6, days=15)
print("The result is", return_value, "minutes")
