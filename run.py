#Importing gspread API and credentials to be able to open and read from the google sheet
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Survey Data')

# Both this function adn the next where inspired buy the Love Sandwiches validation system
def get_option():
    """
    Function asks user for their option 1-4, then checks to see if it is valid, 
    returns option to main
    """
    #These prints, print the options to the user, then asks for the input
    print("Please select the option you'd like displayed\n")
    print("Option 1: Average Age")
    print("Option 2: Percentage of Males")
    print("Option 3: Percentage of Females")
    print("Option 4: Average Salary")
    user_option = int(input("Enter option here: \n"))

    #This if calls the function to check the option the user 
    # entered is correct, option is passed to the function
    #If the function returns as true, then it prints the line below
    if validate_option(user_option):
        print(f"Option is valid, your selected option {user_option} \n")
    
    return user_option


def validate_option(selected_option):
    """
    Function validates the option the user entered is 
    one of the options suggested
    """
    #Code below error handles the users input, if the input is wrong it prints the lines below
    try:
        if selected_option > 4:
            raise ValueError(
                f"Option {selected_option} invalid, please select a valid option."
            )
    except ValueError as e:
        print(f"Invalid character, {e}")
    
    return True

def get_average_age():
    """
    Function gets the average age of all the persons inouted into google sheet
    """
    #This piece was found after some research on StackOverflow
    #https://stackoverflow.com/questions/36235559/how-to-use-python-to-read-one-column-from-excel-file
    #Code ads the values of the column into the ages list
    ages = []
    for value in SHEET.worksheet("Sheet1").col_values(2):
        ages.append(value)
    
    #Removes the first entry of the list as it is the Heading of the column
    ages.pop(0)

    #This code gets the sum of the ages list and puts them into the total_age variable, then calculates the average age.
    total_age = sum([int(age) for age in ages])
    average = total_age / len(ages)
    
    return average

def get_perc_male():
    """
    Function gets the gender column and checks to see if male, adds to a list, then calculates the percentage
    """
    males = []
    #Gets column of genders from sheet
    genders = SHEET.worksheet("Sheet1").col_values(3)
    #Removes the heading from the list
    genders.pop(0)
    
    #Checks the see if the values in the list are M(male), if there are it adds them to the males list
    for value in SHEET.worksheet("Sheet1").col_values(3):
        if value == "M":
            males.append(value)
    
    #Calculates percentage of males
    average_age_male = len(males) / len(genders) * 100
    return average_age_male

def get_perc_female():
    """
    Function gets the gender column and checks to see if female, adds to a list, then calculates the percentage
    """
    #Exact copy for previous function code
    females = []
    genders = SHEET.worksheet("Sheet1").col_values(3)
    genders.pop(0)

    for value in SHEET.worksheet("Sheet1").col_values(3):
        if value == "F":
            females.append(value)
    
    average_age_female = len(females) / len(genders) * 100
    return average_age_female

def get_average_salary():
    """
    This function gets and calculates the total sum of all the salaries,
    Then calculates the average and returns it to main
    """
    #Writes column to variable
    worksheet_salarys = []
    for value in SHEET.worksheet("Sheet1").col_values(5):
        worksheet_salarys.append(value)
    
    #Removes Heading in list
    worksheet_salarys.pop(0)
    
    #Writes a new list with out the comma in the numbers
    salarys = []
    for salary in worksheet_salarys:
        salarys.append(salary.replace(",",""))
    
    #Calculates average Salary
    total_salary = sum([int(salary) for salary in salarys])
    average_salary = total_salary / len(salarys)
    
    return average_salary

def main():
    """
    Main function that calls all other funtions based on option entered by user, then prints result of the function
    """
    option = get_option()
    if option == 1:
        average_age = get_average_age()
        print(f"The average age of the Survey is {average_age}\n")
    elif option == 2:
        male_percentage = get_perc_male()
        print(f"The percentage of males in the survey is {male_percentage}%\n")
    elif option == 3:
        female_percentage = get_perc_female()
        print(f"The percentage of females in the survey is {female_percentage}%\n")
    elif option == 4:
        average_salary = get_average_salary()
        print(f"The average salary of the survey is {average_salary}\n")
    else:
        return False

#While loop keeps the program running to allow the user to select another option
while True:
    print("Welcome to the Survey Analysis App\n")
    main()