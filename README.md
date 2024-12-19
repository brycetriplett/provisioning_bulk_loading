# provisioning_bulk_loading

For adding sim cards in bulk to the provisioning system for Xtreme.

Must install all packages in requirements.txt
(run `pip install -r requirements.txt`)

During the first time running the script, it will ask for an API key, which can be created in the admin panel under Tokens. if you need to change the token, it is saved in .env in the root directory

Bulk sim cards must be a csv or xlsx file, containing the following string fields:

`imsi`: 15 digit string <br>
`ki`: 32 digit string <br>
`op_opc`: 32 digit string <br>
`op_type`: either 0 for OPC or 1 for op, string <br>
`org`: 4 digit organization customer ID, string <br>

## Each organization must exist, and must have a proper HNI assignment for the sim card already. Use admin panel for this.