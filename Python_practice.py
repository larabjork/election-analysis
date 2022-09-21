
#counties = ["Arapahoe", "Denver", "Jefferson"]

# if counties[1] == "Denver" :
#     print(counties[1])
# if counties[3] != "Jefferson" :
#     print(counties[2])

# temperature = int(input("What is the temperature outside?"))

# if temperature > 80:
#     print("Turn on the AC.")
# else:
#     print("Open the windows.")

#What is the score?
# score = int(input("What is your test score? "))

# #Determine the grade
# if score >= 90:
#     print("Your grade is an A.")
# elif score >= 80:
#     print("Your grade is a B.")
# elif score >= 70:
#     print("Your grade is a C.")
# elif score >= 60:
#     print("Your grade is a D.")
# else:
#     print("Your grade is an F.")

# counties = ["Arapahoe", "Denver", "Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not in the list of counties.")

# x = 0
# while x <= 5:
#     print(x)
#     x = x + 1

# counties = ["Arapahoe", "Denver", "Jefferson"]
# # for county in counties:
# #     print(county)

# for i in range(len(counties)):
#     print(counties[i])


# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county in counties_dict:
#     print(counties_dict.get(county))


# for i, j in counties_dict.items():
#     print(i + " county has " + str(j) + " registered voters.")

# print(counties_dict)
# print(counties_dict.items())
# print(counties_dict.keys())
# print(counties_dict.values())


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
            {"county":"Denver", "registered_voters": 463353},
            {"county":"Jefferson", "registered_voters": 432438}]



            
for i in voting_data:
    for county, registered_voters in i.items():
        print(f"{county}: {registered_voters}")
        # print(f"{county} county has {registered_voters} registered voters.")


# for county_dict in voting_data:
#     #prints k-v pairs for eact dict
#     print(county_dict)
#     #prints k only
#     print(county_dict['county'])
    # for value in county_dict.values():
    #     print(value)


# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total of votes in the election? "))
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")
# percentage_votes = (my_votes / total_votes) * 100
# print(f"I received {my_votes / total_votes * 100}% of the total votes.")
# for num in range(5):
#     print(num)

# for county, voters in counties_dict.items():
#     print(county + " county has " + str(voters) + " registered voters.")

# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")

# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters:,} registered voters.")
