# Import the required packages and modules
try: 
    from dotenv import load_dotenv
    from pprint import pprint
    import pandas as pd
    import requests
    import urllib3
    import sys
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


# process the file name provided by the user
if len(sys.argv) > 2:
    print("Error: Too many arguments provided. Please provide only the filename as an argument.")
    exit(1)
elif len(sys.argv) == 2:
    user_input = sys.argv[1]
else:
    user_input = input("Please enter the name of the file you want to load (type q to quit): ")


# load the sim card data file
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
        exit(1)

except FileNotFoundError:
    print("File not found. Please enter a valid file name.")
    exit(1)

except Exception as e:
    print("An error occurred. Please try again.")
    print(e)
    exit(1)


# Convert all column names in the dataframe to lowercase
df.columns = df.columns.str.lower()


# gather the op_code_type
if 'op' not in df.columns and 'opc' not in df.columns:
    print("Error: Either 'op' or 'opc' column is required.")
    exit(1)

def determine_op_code_type(row):
    op = row.get('op')
    opc = row.get('opc')
    
    if pd.notna(op) and pd.notna(opc):
        print("Error: Both 'op' and 'opc' have data for one row.")
        exit(1)
    elif pd.notna(op):
        return "1"
    elif pd.notna(opc):
        return "0"
    else:
        print("Error: Either 'op' or 'opc' column must have data.")
        exit(1)

df['op_code_type'] = df.apply(determine_op_code_type, axis=1)


# combine op and opc into one column
df['opc'] = df.apply(
    lambda row: row['op'] 
    if 'op' in row 
    and pd.notna(row['op']) 
    else row['opc'], axis=1
)


# check for the presence of the required fields, and ensure they are the correct format
required_fields = {
    'imsi': lambda x: x.isdigit() and len(x) == 15,
    'ki': lambda x: len(x) == 32,
    'opc': lambda x: len(x) == 32,
    'customerid': lambda x: x.isdigit() and len(x) == 4
}

for field, check in required_fields.items():
    if field not in df.columns:
        print(f"Error: Required field '{field}' is missing.")
        exit(1)
    if not df[field].apply(check).all():
        print(f"Error: Field '{field}' has invalid data.")
        exit(1)


# Convert the dataframe to JSON
df = df[['imsi', 'ki', 'opc', 'op_code_type', 'customerid']]
df.rename(columns={'customerid': 'organization'}, inplace=True)
df_json = df.to_json(orient='records')


# send the JSON to the API
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
print(result)
pprint(result.json())