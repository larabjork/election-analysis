# election-analysis
Data Bootcamp Module 3 - Python

## Overview of Election Audit
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Calculate the total number of votes cast in each county within the precinct.
3. Calculate which county reported the highest number of votes.
4. Get a complete list of candidates who received votes.
5. Calculate the total number of votes each candidate received. 
6. Calculate the percentage of votes each candidate received.
7. Calculate the winner of the election based on the popular vote,

## Resources
- Data source: election_results.csv
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
The script created for this task is highly reusable for future elections in this precinct because it can adjust to different number of candidates, or if redistricting occurs, a different number of counties (or even all counties in the state). 

EXPLAIN LOOPS USED THAT MAKE IT REUSABLE. EXPLAIN HOW CSV CHANGES WOULD HAVE TO BE INCORPORATED


The script can also be modified to report out county-level results by candidate.

The script can also be modified to report out ballot initiative results, where there is a yes/no option.

Could it handle write-in candidates?

It can be modified to include a check for duplicate ballot numbers
1.
2.
