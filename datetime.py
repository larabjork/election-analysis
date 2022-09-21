import datetime as dt
# Use the now() attribute on the datetime class to get the present time. The first datetime is abbreviated to dt and is the datetime module that we imported; the second datetime is the datetime class within that module; the final now() is an attribute of the datetime class.
now = dt.datetime.now()

# Print the present time.
print("The time right now is ", now)


# Print the total votes.
# print(total_votes)
# # Print the candidate list.
# print(candidate_options)
# # Print the candidate's vote dictionary.
# print(candidate_votes)

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