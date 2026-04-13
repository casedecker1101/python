# 18.13 writing a list to a file
customers = []

class WriteList():
    def write_file_list(self, input_list, input_filepath):
        f = open(input_filepath, "a")
        for name in input_list:
            name = "\n" + name
            f.write(name)
        f.close()

input_file = ""
cinMain = ""
write = WriteList()

input_file = input("Please enter the input file location: ")
while cinMain != 'quit':
    customer = input("Please enter client list, enter quit when finished: ")
    customers.append(customer)
    cinMain = input("Continue typing client list or quit to exit. ")
    if cinMain == 'quit':
        break
    else:
        continue
WriteList().write_file_list(customers,input_file)