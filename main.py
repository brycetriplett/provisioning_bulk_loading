import pandas as pd
import requests

while True:
    user_input = input("Please enter the name of the file you want to load: ")

    if user_input.split('.')[-1] not in ('csv', 'xlsx'):
        print("Invalid file type. Please enter a valid file type. (csv or xlsx)")
        continue

    try:
        if user_input.split('.')[-1] == 'csv':
            df = pd.read_csv(user_input, dtype=str)
        else:
            df = pd.read_excel(user_input, dtype=str)

        break

    except FileNotFoundError:
        print("File not found. Please enter a valid file name.")

    except Exception as e:
        print("An error occurred. Please try again.")
        print(e)


df = df[['imsi', 'ki', 'op_opc', 'op_type', 'org']]
df = df.rename(columns={'op_opc': 'opc', 'op_type': 'op_code_type', 'org': 'organization'})

df_json = df.to_json(orient='records')
print(df_json)