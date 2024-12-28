# set the API URL. Change this as necessary
api_url = "https://provisioning.xtremeenterprises.com/api/v1/bulk-load-sim-cards/"


# Import the required packages and modules
try: 
    from dotenv import load_dotenv
    import pandas as pd
    import requests
    import os

except ImportError as e:
    print(f"An error occurred: {e}")
    print("Please run the install.py script to install the required packages.")
    exit(1)


# load or create the API key
load_dotenv()
api_key = os.getenv('API_KEY')

if not api_key:
    with open('.env', 'w') as env_file:
        api_key = input("API_KEY not found. Please enter your API_KEY: ")
        env_file.write(f"API_KEY={api_key}\n")

    load_dotenv()
    api_key = os.getenv('API_KEY')


# load the sim card data file
while True:
    user_input = input("Please enter the name of the file you want to load: ")

    if user_input.split('.')[-1] not in ('csv', 'tab', 'xlsx'):
        print("Invalid file type. Please enter a valid file type. (.csv, .tab, or .xlsx)")
        continue

    try:
        if user_input.split('.')[-1] == 'xlsx':
            df = pd.read_excel(user_input, dtype=str)
        else:
            df = pd.read_csv(user_input, dtype=str)

        break

    except FileNotFoundError:
        print("File not found. Please enter a valid file name.")

    except Exception as e:
        print("An error occurred. Please try again.")
        print(e)


# transform the file
df = df[['imsi', 'ki', 'op_opc', 'op_type', 'org']]
df = df.rename(columns={'op_opc': 'opc', 'op_type': 'op_code_type', 'org': 'organization'})

df_json = df.to_json(orient='records')


# send the transformed file to the API
result = requests.post(
    api_url,
    headers = {
    "Authorization": f"Token {api_key}",
    "Content-Type": "application/json"
    },
    data=df_json
)

# display the result
print(f"{result}\n{result.text}")