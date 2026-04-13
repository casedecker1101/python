class ReverseOrder():
    def __init__(self, input_filepath,output_filepath,num_lines):
        self.input_filepath = input_filepath
        self.output_filepath = output_filepath
        self.num_lines = num_lines
        
    def tail_reverse(self,input_filepath,output_filepath,num_lines):
        num_lines = int(num_lines)
        with open(input_filepath, "r") as file:
            lines = file.readlines()
            if num_lines == 0:
                reversed_lines = lines[::-1]
            else:
                reversed_lines = lines[-num_lines:][::-1]
            with open(output_filepath, "w") as ofile:
                content = "".join(reversed_lines)
                ofile.write(content)
                return content
                
    
# return the last 300 lines in reverse order
input_file_path = input("Enter the input file path: ")
output_file_path = input("Enter the output file path: ")
num_lines = input("Please enter the order: 0 = reverse. ")
text = ReverseOrder(input_file_path, output_file_path, num_lines).tail_reverse(input_file_path, output_file_path, num_lines)
print(text)