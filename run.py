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

def validate_option(selected_option):
    """
    Function validates the option the user entered is 
    one of the options suggested
    """
    try:
        if selected_option > 4:
            raise ValueError(
                f"Option {selected_option} invalid, please select a valid option."
            )
    except ValueError as e:
        print(f"Invalid character, {e}")
    
    return selected_option

def get_average_age():
    print("This function works 1")

def get_perc_male():
    print("This function works 2")

def get_perc_female():
    print("This function works 3")

def get_average_salary():
    print("This function works 4")

def main():
    """
    Main function that calls all other funtions based on option entered by user
    """
    while True:
        print("Please select the option you'd like displayed\n")
        print("Option 1:")
        print("Option 2:")
        print("Option 3:")
        print("Option 4:")
        user_option = int(input("Enter option here: \n"))
        option = validate_option(user_option)
    
        if option == 1:
            get_average_age()
        elif option == 2:
            get_perc_male()
        elif option == 3:
            get_perc_female()
        elif option == 4:
            get_average_salary()
        else:
            print("Please pick a valid option\n")


print("Welcome to the Survey Analysis App\n")
main()