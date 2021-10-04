![Main Image](https://github.com/Gh0ul5lay3r-91/survey-data-analysis/blob/main/assets/readme%20images/Header%20Image.png)

# Survey Data Analysis


## Introduction

The Survey Data analysis app in brief gets the survey data from a google sheet using an API, then based off the option a user selects calculates the data. The app calculates data for average age, percentage of males, percentage of females and average salary. The app also will allow the user to input survey data manually if more survey data needs to be added. This data calculation allows insight into the survey results and will help the user understand the statistics. 

Live link can be found here - https://survey-data-analysis.herokuapp.com/

Opportunities where listed out to decided what features to build

| Opportunity                          | Importance | Viability/Feasability |
| ------------------------------------ | ---------- | --------------------- | 
| Options List                         | 5          | 5                     | 
| Add data to survey                   | 2          | 2                     |
| Most popular Industry                | 2          | 1                     |
| Average Salary                       | 3          | 3                     |
| Percentage of M,F                    | 4          | 4                     | 
| Average Age                          | 4          | 4                     |

With this table done it was decided that the features to include would be
* Options List
* Average age
* Percentage of Males
* Percentage of Females
* Average Salary

The order you see is the order of precedence, the other features can be considered for later implementation. Work then began on user stories and flow charts.

User stories consisted of me placing myself in the shoes of a user who wanted to get some insight into statistical data of a survey.
* User
    * As a user, I want to be able to choose between options for data to be displayed to me.
    * As a user, I want to be able to know the average age of all entries.
    * As a user, I want to be able to know the percentages of Males and Females in the survey.
    * As a user, I want to be able to know what the average salary of the entries is.

Flow charts where drawn up to aid with decision of how the app would function
* 

## Features
The Survey Data Analysis app has a few features to help the user both navigate the app, and be able to read the data coming from the survey.

### Options List
The options list is provide to allow the user to select which way they would like the data presented to them.
* Average Age
* Percentage of Males
* Percentage of Females
* Average Salary
The app will ask the user to input their option then check to see if its valid and matches the list of options.

![Options List](https://github.com/Gh0ul5lay3r-91/survey-data-analysis/blob/main/assets/readme%20images/Options%20List.png)

### Average Age
This feuture gets the column of ages from the sheet and then calculates the average age. It then displays this to the user.

![Average Age](https://github.com/Gh0ul5lay3r-91/survey-data-analysis/blob/main/assets/readme%20images/Option%201:Option%202.png)

### Percentage of Males
This feature takes the gender column in the survey and calculates the percentage of males in the survey.

![Percentage Male](https://github.com/Gh0ul5lay3r-91/survey-data-analysis/blob/main/assets/readme%20images/Option%201:Option%202.png)

### Percentage of Females
This feature is the exact same as the previous but just it calculates the percentage of females in the survey.

![Percentage Female](https://github.com/Gh0ul5lay3r-91/survey-data-analysis/blob/main/assets/readme%20images/Option%203.png)

### Average Salary
This feuture gets all the data from the salarys column and calculates the average salary and displays it to the user.

![Average Salary](https://github.com/Gh0ul5lay3r-91/survey-data-analysis/blob/main/assets/readme%20images/Option%204.png)

## Testing
As with my previous project, testing was done on a continuous basis, as I built the functions I used print statements to check the data being handled was correct. I then deployed the app as soon as it was in a workable state on Heroku. 

### Bugs
There where a few bugs in the code along the way, but these where dealt with as they where identified. At this time the only bugs that remain are the ability to handle letters, specials characters and whitespace when the user enters the option. I didnt have time to complete this. Also the program does not exit properly, again I didnt have time to implement this. 

## Validating
I used the PEP8 website to check the code. Initially there where many warnings in relation to indentation and whitespace, but I cleaned these up, re ran the code and it passed through successfully. 

![PEP8](https://github.com/Gh0ul5lay3r-91/survey-data-analysis/blob/main/assets/readme%20images/PEP8.png)

## Deployment
To deploy this project I used Heroku, I followed the walk through videos to set all my settings and deploy the app.

To deploy I went through the following steps
* Set up my account on Heroku.
* Ensured requirements.txt was correct.
* Added the correct config vars.
* Added the correct build packs.
* Ensured automatic deployment was turned on.
* Deployed.

Live link can be found here - https://survey-data-analysis.herokuapp.com/

## Credits
During the build I only came across one issue and that was getting the data from one column rather than a row, I did some research and found a solution on StackOverflow.
[Here](https://stackoverflow.com/questions/36235559/how-to-use-python-to-read-one-column-from-excel-file)
Another credit goes to the love sandwiches app with the data input validation. I used a similar method. 
Credit again goes to tutoring for helping me with an issue at the start of the project where i didnt capitalize the name in sheet which caused the program not to be able to find the sheet.

Over all look and feel came from the love sandwiches walk though, as this was only a data manipulation app I felt I didnt need to break too much from that layout. 