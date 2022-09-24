# Election Analysis Challenge
Data Bootcamp Module 3 - Python

## Overview of Election Audit
A Colorado Board of Elections employee has assigned the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Calculate the total number of votes cast in each county within the precinct.
3. Calculate which county reported the highest number of votes.
4. Get a complete list of candidates who received votes.
5. Calculate the total number of votes each candidate received. 
6. Calculate the percentage of votes each candidate received.
7. Calculate the winner of the election based on the popular vote,

## Resources
- Data source: [election_results.csv](https://github.com/larabjork/election-analysis/blob/main/Resources/election_results.csv)
- Software: Python 3.9.12, Visual Studio Code 1.71.2

## Election-Audit Results
The analysis of the election data shows that:
- There were 369,711 votes cast in the election.
- The breakdown of votes by county was:
    - Jefferson County reported 38,855 votes, or 10.5% of the total votes in the precinct.
    - Denver County reported 306,055 votes, or 82.8% of the total votes in the precinct.
    - Arapahoe County reported 24,801 votes, or 6.7% of the total votes in the precinct.
- The county with the largest number of votes was Denver County, at 82.8% of the total votes in the precinct (306,055 votes out of a precinct total of 369,711).  
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidates' results were:
    - Charles Casper Stockham received 85,213 votes, which equals 23.0% of the total votes cast.
    - Diana DeGette received 272,892 votes, which equals 73.8% of the votes cast.
    - Raymon Anthony Doane received 11,606 votes, which equals 3.1% of the votes cast.
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote (272,892 votes out of a precinct total of 369,711).

## Election-Audit Summary
The script created for this task is highly reusable for future elections in this precinct because it can accommodate different number of candidates, or if redistricting occurs, a different number of counties (or even all counties in the state). As long as the election data to be analyzed continues to consists of ballot number, county, and candidate name, this script can be reused, with any needed modifications taking only a few simple steps.

### What Makes This Script Highly Reusable
This script is highly reusable because it does not have built-in assumptions about how many candidates or counties are included. This flexibility is possible for many reasons.

Instead of hard-coding names for candidates or counties, this script stores these names in two lists (candidate_options and county_list), as shown in lines 18 and 22. In Python, lists are a mutable data type, meaning that they can be changed (so list items can be added as the code runs). To keep track of how many votes cast per candidate and per county, this script uses another mutable data type, the dictionary. In lines 19 and 23, this script sets up two dictionaries (candidate_votes and county_votes) so that paired information can be stored. For example, in the candidate_votes dictionary, the pairs are made up of a name (stored as candidate_name) and the associated vote count (stored as an integer). 

![code snippet of lines 17-23, with initialization of lists and dictionaries](https://github.com/larabjork/election-analysis/blob/main/Resources/initialize-candidate-county.png)

The _for_ loop, which begins on line 43, is written so that the data is analyzed row by row. As we pass through the loop, each time:
* One vote is added to the total and stored in the variable total_votes (line 46), which will conitnue to increase each time we iterate over the loop. 
* The candidate receiving the vote is stored as candidate_name (line 49), but only for the current iteration of the loop; if that name is not already part of the list of candidates (candidate_options), it is added to the list (line 56) and a vote is added to that candidate's total (line 65).
* The county in which the vote was cast is stored as county_name(line 52), but only for the current iteration of the loop. As with the candidate information, a similar evaluation of the list of counties and the increase county vote total is made (lines 69 and 79).
* This loop continues for as long as there is data in the .csv file. 

Lines 83 through 159 cover the process of taking the output of this _for_ loop and presenting the output on screen (i.e., "in the terminal") and in a text file. This process takes advantage of the same features as in the analysis process, namely the use of:
* automated ability to open files, and in this section of code, write directly to them)
* dynamic variables to store information, so that it can be efficiently retrieved
* _for_ loops, to systematically evaluate all data
* logical operators in _if_ statements to evaluate data and determine largest number of votes by candidate and by county


### Steps to Reuse This Script
For convenience, line numbers are referenced below, reflecting the current status of the code, but with insertions and/or deletions, line numbers could shift. To run this script against a different data set, we would need to:

1. Confirm that the election data is once again stored in .csv format. If it is in a different format that is still based on a table structure of rows and columns (e.g., an Excel or .xls file), the simplest fix is to convert that file to .csv format. Otherwise, additional modifications to the code would be necessary.

2. Confirm that the .csv data is organized in the same way, especially:
    * A header row is used; as shown in line 40 below, the code is written so that this line of data is skipped and not analyzed. If no header row is present, comment out line 40, so that the first row of data is included.
    
    ![code snippet of lines 39-40, which use the next method to skip the header row in our loop](https://github.com/larabjork/election-analysis/blob/main/Resources/header-row.png)
    * The second column has the county name and the third column has candidate name. If the election data presents information in a different order, the index numbers (in brackets) for affected columns would need to be adjusted using zero-based indexing, in lines 49 and/or 52, as appropriate.
    
    ![code snippet of lines 48-52, showing where to check and, if necessary, adjust index](https://github.com/larabjork/election-analysis/blob/main/Resources/candidate-county-row-index.png)

3. Save the .csv file with election data in the [Resources](https://github.com/larabjork/election-analysis/tree/main/Resources) folder of this Github repository or correct that portion of the file path, which is shown in line 10 of the following code. If the new file was also named "election_results.csv", we would not have to change line 10, but if any other file name is used, we would have to replace "election_analysis.csv" with the new file name.

    ![code snippet of lines 8-10, which establish a variable to store the data source's file path](https://github.com/larabjork/election-analysis/blob/main/Resources/candidate-county-row-index.png)

4. Follow a similar process as in step 3 for the output file, election_analysis.txt. If the results are to be stored in a text file with the same name and stored in the same folder ("analysis"), then no changes need to be made to line 12, shown below. But if either the file location or the file name changes, that information must be updated in this line of code so that the correct file path is available.

    ![code snippet of lines 11-12, which establish a variable to store the analysis's file path](https://github.com/larabjork/election-analysis/blob/main/Resources/initialize-output-file.png)

### Additional Possible Modifications 
* The script could be modified to report out county-level results by candidate.

* The script could also be modified to report out ballot initiative results, where there is a yes/no option instead of candidates.

* In the case of write-in candidates, this script could also be modified to check for misspellings.

* This script could be modified to include a check for duplicate ballot numbers and/or to check against a separate list of eligible ballot numbers.

