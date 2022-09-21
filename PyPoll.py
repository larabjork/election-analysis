# The data we need to retrieve:
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on the popular vote

# Add dependencies
import csv
import os

# We want to be able to read from a csv file that's loaded in our Resources folder.
# Assign a variable for the file to load and the path.
# This is a direct path
# file_to_load = 'Resources/election_results.csv'
# This is an indirect path
file_to_load = os.path.join("Resources", "election_results.csv")

# We want to write the results of our analysis to a text file. 
# Create a filename varialbe to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

# Read the file object with csv's reader function
# 
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)
    
    # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)

# close the file
# election_data.close()



# Using the open() function with the "w" mode we will write data to the file.
# outfile = open(file_to_save, "w")
# Write some data to the file
# outfile.write("Hello World")
# Close the file
# outfile.close()

# Using the with statement open the file as a text file 
# with open(file_to_save, "w") as txt_file:

#     # Write some data to the file, with all counties on one line
#     # txt_file.write("Arapahoe, Denver, Jefferson")

#     # Write some data to the file, with all counties on separate lines
#     txt_file.write("Counties in the Election\n--------------------------\nArapahoe\nDenver\nJefferson")

