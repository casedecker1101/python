# 201 and 202
import json
from pprint import pprint

dict_bank = {
    "Account Number":"092848",
    "Customer_ID":"9332",
    "first_name": "john",
    "last_name": "smith"
}

with open("data/json_bank.json",'w') as outfile:
    json.dump(dict_bank, outfile, indent=4)
json_bank = json.dumps(dict_bank,indent=4)
print(json_bank)