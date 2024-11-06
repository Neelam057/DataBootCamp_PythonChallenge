# Python-Challenge
In this challenge, we were given two CSV files as a resource. We were required to create Python scripts to analyze the data in these CSV files and export the outputs to text files in the respective folders.

## 1. PyBank Analysis

### Overview

The PyBank project performs an analysis of a dataset containing bank financial records (date and Profit/Loss). Using Python,I performed an analysis of data and provided a report of the bank's performance over a specific period.

### Project Description
The PyBank analysis is designed to examine a series of monthly financial records and derive meaningful insights, such as:

1. The total number of months included in the dataset
2. The net total amount of "Profit/Losses" over the entire period
3. The changes in "Profit/Losses" over the entire period, and then the average of those changes
4. The greatest increase in profits (date and amount) over the entire period
5. The greatest decrease in profits (date and amount) over the entire period

By conducting this analysis, the goal is to help the user understand its financial trends and make informed decisions based on historical data.

### Dataset
The dataset used in this project is a CSV file containing monthly financial records for the bank. Each record contains the following columns:

Date: The date of the record (in YYYY-MM format).
Profit/Losses: The profit or loss for that month.
https://github.com/Neelam057/DataBootCamp_VBA/blob/main/Submission/Screenshot_Q1.png

### Methodology

####Data Loading:
Load the dataset using csv reader.

#### Data Analysis and Calculation:
Performed the analysis and used list and dictionaries to fetch and store data. 

#### Results:
https://github.com/Neelam057/DataBootCamp_VBA/blob/main/Submission/Screenshot_Q1.png

#### Summary Report:
Output the key statistics in a text file.

## PyPoll Analysis

### Overview
The PyPoll project is a Python-based analysis of election polling data. The objective of the analysis is to determine key voting outcomes, including the total number of votes cast, the breakdown of votes for each candidate, and the identification of the winner of the election. This analysis was conducted using Python.

### Project Description
The PyPoll analysis focuses on processing a polling dataset to generate the following insights:

Total Votes: The total number of votes cast in the election.
Vote Distribution for candidates: The percentage of total votes received by each candidate.
Election Winner: The candidate with the highest number of votes.

### Dataset
The dataset used in this project contains voting records from a specific election. Each record includes:

Voter ID: A unique identifier for each voter.
County: The county or district where the vote was cast.
Candidate: The name of the candidate the voter voted for.

https://github.com/Neelam057/DataBootCamp_VBA/blob/main/Submission/Screenshot_Q1.png

### Methodology

####Data Loading:
Load the dataset using csv reader in python.

#### Data Analysis and Calculation:
Calculate the Total Number of Votes.
Calculate the Total Votes for Each Candidate.
Determine the Percentage of Votes for each candidate.
Identify the Winner (candidate with the highest vote count). 

#### Results:
https://github.com/Neelam057/DataBootCamp_VBA/blob/main/Submission/Screenshot_Q1.png

#### Summary Report:
Output a text summary showing the total votes, the percentage of votes for each candidate, and the election winner


