# provisioning_bulk_loading

For adding sim cards in bulk to the provisioning system for Xtreme. <br><br>


Must install all packages in requirements.txt <br>

run `pip install -r requirements.txt` on windows <br>
run `pip3 install -r requirements.txt` on mac or linux <br><br>


Bulk sim cards must be a csv or xlsx file, existing in the same directory as main.py, containing the following string fields: <br>

`imsi`: 15 digit string <br>
`ki`: 32 digit string <br>
`op_opc`: 32 digit string <br>
`op_type`: either 0 for OPC or 1 for op, string <br>
`org`: 4 digit organization customer ID, string<br><br>


To run the script: <br>

run `python main.py` to execute on windows <br>
run `python3 main.py` to execute on mac or linux <br><br>


During the first time running the script, it will ask for an API key, which can be created in the admin panel under Tokens. if you need to change the token, it is saved in .env in the root directory <br>

## Each organization must exist, and must have a proper HNI assignment for the sim card already. Use admin panel for this.