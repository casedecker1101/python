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
