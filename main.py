# set the API URL. Change this as necessary
api_url = "https://provisioning.xtremeenterprises.com/api/v1/bulk-load-sim-cards/"


# Disable certificate warnings. Remove when not using self-signed certificates
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


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
api_key = os.getenv('PROVISIONING_API_KEY')
imsi_field = os.getenv('PROVISIONING_IMSI')
ki_field = os.getenv('PROVISIONING_KI')
op_opc_field = os.getenv('PROVISIONING_OP_OPC')

if not api_key:
    print("Initial configuration not found. Please run the install.py script to create the .env file.")
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


# gather the op type
while True:
    op_type = input("Are you using OP or OPC? type 0 for OPC or 1 for OP (type q to quit): ")

    if op_type not in ['0', '1']:
        print("Invalid input. Please enter 0 or 1.")

    elif op_type == 'q':
        exit(0)
    
    else:
        df['op_code_type'] = op_type
        break


# gather the organization ID
while True:
    org_id = input("Please enter the ID of the organization you want to assign the SIM cards to (type q to quit): ")

    if org_id == 'q':
        exit(0)

    elif len(org_id) == 4 and org_id.isdigit():
        df['organization'] = org_id
        break
        
    else:
        print("Invalid input. Please enter a 4-digit integer.")


# transform the file and check for correct column names
try:
    df = df[[imsi_field, ki_field, op_opc_field, 'op_code_type', 'organization']]

except KeyError:
    print("One or more of the fields you entered are not present in the file. \
          Please either adjust the column names in the .env file or change the column names in the data.")
    exit(1)


# transform the data
df = df.rename(columns={imsi_field: 'imsi', ki_field: 'ki', op_opc_field: 'opc'})
df_json = df.to_json(orient='records')


# send the transformed file to the API
result = requests.post(
    api_url,
    headers = {
    "Authorization": f"Token {api_key}",
    "Content-Type": "application/json"
    },
    data=df_json,
    verify=False
)

# display the result
print(f"{result}\n{result.text}")