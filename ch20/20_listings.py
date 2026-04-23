# normalizing integers
# Normalize whole numbers

value = "0.0"

int(value.strip())

# normalize decimals
float(value.strip())

# Removing separators
int(value.replace(",","").strip())
float(value.replace("$","").replace(",","").strip())


# 20.1 Creating a JSON file from python dictionaries
import json

# create a list of dictionaries
data = []
data.append({"name":"Andre Richards","DOB":"10/10/1979"})
data.append({"name":"Melinda Jefferson","DOB":"12/31/1979"})

with open('data/person.json','w') as outfile:
    json.dump(data,outfile)
    
# print the file's contents
f = open('data/person.json', 'r')
print(f.read())
f.close()

# 20.2/20.3 Creating a json file with unstructured data
json_dict = {
    "first_name": "Robert",
    "last_name": "Balti",
    "role":  ["Manager","Lead Developer"],
    "age": 34
}

json_data = json.dumps(json_dict,indent = 4)
print(json_data)
print(type(json_data))

# 20.4 serialize and deserialize objects
python_dict = json.loads(json_data)
print(python_dict)
print(type(python_dict))

# 20.5 converting from json to a dictionary
x = """{
    "Name": "Cheyanne Kemp",
    "Contact Number": 7867567898,
    "Email": "ckemp@gmail.com",
    "Services": ["Checking", "Savings", "Auto Loan"]
    }"""
user_data = json.loads(x)
print(user_data['Email'])

# 20.6 Iterating through a json file
with open('data/prize.json','r') as jsonfile:
    # use the json module with the load function
    # to read the entire content of the json file
    data = json.load(jsonfile)
    
# iterate through the file and display each json object separately
for k in data['prizes']:
    print(k)
    
# 20.7 iterating through a json file of bank transactions
filename = 'data/bank_transactions.json'

with open(filename,'r') as jsonfile:
    data = json.load(jsonfile)
    
for each in data:
    if each['WITHDRAWAL AMT'] != '':
        val = float(each['WITHDRAWAL AMT'])
        if val > 650000:
            print(each['Account No'], "===>",val)

# 20.8 iterating for totals
filename = 'data/bank_transactions.json'
with open(filename,'r') as jsonfile:
    data = json.load(jsonfile)
    
total = 0
total_balance = 0

for each in data:
    if each['WITHDRAWAL AMT'] != '':
        total += float(each['WITHDRAWAL AMT'])
    if each['BALANCE AMT'] != '':
        total_balance += float(float(each['BALANCE AMT']))
print("Total Withdrawals: ", total)
print("Total of Balances: ", total_balance)

# 20.9 using pprint
from pprint import pprint
with open('data/prize.json','r') as jsonfile:
    data = json.load(jsonfile)
print(data)
    