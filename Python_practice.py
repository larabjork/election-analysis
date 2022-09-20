
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


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
            {"county":"Denver", "registered_voters": 463353},
            {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    # print(county_dict)
    for value in county_dict.values():
        print(value)

# for num in range(5):
#     print(num)
