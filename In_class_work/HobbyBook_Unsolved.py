# * Create a dictionary to store the following:
#   * Your pet's name
#   * Your pet's age
#   * A list of a few of your pet's hobbies
#   * A dictionary of a few times you wake up during the week

# * Print out the following:
#   * Your pet's name and age.
#   * How many hobbies your pet has.
#   * What your pet's favorite hobby is.
#   * What time your pet wakes on one of the days of the week.
# 
# @TODO: Your code here

linus_info = {"Name":"Linus",
             "Age": 7, 
             "Hobbies": ["snoozing", "napping", "resting", "finding sunny spots"],
             "Wakeup Times": {"Sunday":"4:45 am","Monday":"4:45 am","Tuesday":"4:45 am","Wednesday":"4:45 am", "Thursday":"4:45 am","Friday":"4:45 am","Saturday":"4:45 am"}
             }


print(f"My pet's name is {linus_info['Name']}")
print(f"He is {linus_info['Age']} years old.")
print(f"He has {len(linus_info['Hobbies'])} hobbies.")
print(f"On Mondays, he wakes up at {linus_info['Wakeup Times']['Monday']}.")
