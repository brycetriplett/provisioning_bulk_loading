# provisioning_bulk_loading

For adding sim cards in bulk to the provisioning system for Xtreme.

Must install all packages in requirements.txt
(run `pip install -r requirements.txt`)

Must create a .env file in the same directory as main.py containing the following:

`API_KEY = ""`
`API_URL = ""`

Bulk sim cards must be a csv or xlsx file, containing the following string fields:

`imsi`: 15 digit string
`ki`: 32 digit string
`op_opc`: 32 digit string
`op_type`: either 0 for OPC or 1 for op, string
`org`: 4 digit organization customer ID, string

## Each organization must exist, and must have a proper HNI assignment for the sim card already. Use admin panel for this.