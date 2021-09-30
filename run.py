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
        if int(selected_option) <= 4:
            raise ValueError(
                f"Option {selected_option} invalid, please select a valid option."
            )
    except ValueError as e:
        print(f"Invalid character, {e}")
    
    return selected_option

def main():
    """
    Main function that calls all other funtions based on option entered by user
    """
    print("Please select the option you'd like displayed\n")
    print("Option 1:")
    print("Option 2:")
    print("Option 3:")
    print("Option 4:")
    user_option = input("Enter option here: \n")
    option = validate_option(user_option)
    
    if option == 1:
        get_average_age()
    elif option == 2:
        get_perc_male()
    elif option == 3:
        get_perc_female()
    elif option == 4:
        get_survey_data()
    else:
        print("Please pick a valid option\n")


print("Welcome to the Survey Analysis App\n")
main()