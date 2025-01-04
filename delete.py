# Import the required packages and modules
try: 
    from dotenv import load_dotenv
    import pandas as pd
    import requests
    import urllib3
    import os

except ImportError as e:
    print(f"An error occurred: {e}")
    print("Please run the install.py script to install the required packages.")
    exit(1)


# Disable certificate warnings. Remove when not using self-signed certificates
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Attempt to load required environment variables
load_dotenv()
api_url = os.getenv('PROVISIONING_API_URL')
api_key = os.getenv('PROVISIONING_API_KEY')

if not all([api_url, api_key]):
    print("Initial configuration not found or incomplete. \
          Please run the install.py script to create the .env file with all required variables.")
    exit(1)


# load the sim card data file
while True:
    user_input = input("Please enter the name of the file you want to load (type q to quit): ")

    try:
        if user_input.split('.')[-1] == 'xlsx':
            df = pd.read_excel(user_input, dtype=str)

        elif user_input.split('.')[-1] == 'tab':
            df = pd.read_csv(user_input, sep='\t', dtype=str)
            
        elif user_input.split('.')[-1] == 'csv':
            df = pd.read_csv(user_input, dtype=str)

        elif user_input == 'q':
            exit(0)

        else:
            print("Invalid file type. Please enter a valid file type. (.csv, .tab, or .xlsx)")
            continue

        break

    except FileNotFoundError:
        print("File not found. Please enter a valid file name.")

    except Exception as e:
        print("An error occurred. Please try again.")
        print(e)


# make all column names lowercase
df.columns = df.columns.str.lower()


# extract the IMSI column from the dataframe
try:
    df = df[['imsi']]

except KeyError:
    print("The IMSI column cannot be found in the file. Please ensure that the column is named 'imsi'.")
    exit(1)


# convert to JSON
imsi_list = df['imsi'].tolist()
imsi_json = {"imsi_list": imsi_list}


# confirm the deletion
finalchance = input("Are you sure you want to delete these records? (Y): ")
if finalchance.lower() != 'y':
    print("Exiting...")
    exit(0)


# send the transformed file to the API
result = requests.delete(
    api_url,
    headers = {
    "Authorization": f"Token {api_key}",
    "Content-Type": "application/json"
    },
    json=imsi_json,
    verify=False
)


# display the result
print(f"{result}\n{result.text}")