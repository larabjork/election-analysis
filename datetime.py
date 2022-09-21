import datetime as dt
# Use the now() attribute on the datetime class to get the present time. The first datetime is abbreviated to dt and is the datetime module that we imported; the second datetime is the datetime class within that module; the final now() is an attribute of the datetime class.
now = dt.datetime.now()

# Print the present time.
print("The time right now is ", now)