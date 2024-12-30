# provisioning_bulk_loading

For adding or deleting sim cards in bulk to the provisioning system for Xtreme. <br><br>


Must first run the install script <br>

run `python install.py` on windows <br>
run `python3 install.py` on mac or linux <br>

When running the install script, it will ask for an API key, which can be created in the admin panel under Tokens. This token must be created for a superuser account to work. if you need to change the token, it is saved in .env in the root directory, or just re-run the install script. <br>

Additionally, it will ask you for the column names that the file you load will be using. This can also be changed by editing the .env file, or running the install script again. Make this something that you use every time to avoid having to constantly edit the configuration. <br><br>


Bulk sim cards must be a csv, tab, or xlsx file, existing in this same directory, containing the following string fields: <br>

`imsi`: 15 digit string <br>
`ki`: 32 digit string <br>
`op_opc`: 32 digit string <br><br>


To run the script on windows: <br>
execute `.\run.bat` <br><br>


for linux and mac, the script needs to be made executable first. This only needs to be done once. <br>
execute `chmod +x run.sh` <br>

Now you can run the script. <br>
execute `./run.sh` <br><br>


## Each organization must exist, and must have a proper HNI assignment for the sim card already. Use admin panel for this.