# prompts user for n integer 
# reads the first n lines of stocks.csv
# if n > number of lines
# create handler

import os,csv

cinMain = ""

while cinMain.lower()!= 'quit':
    if os.path.exists('data/stocks_short.csv'):
        with open('data/stocks_short.csv') as stocks:
            userInput = input("File Exists. Current Options [print, append, create & quit]: ")
            cinMain = userInput
            if userInput.lower() == 'quit':
                break
            elif userInput.lower() =='print':
                print(stocks.read())
            elif userInput.lower() == 'append':
                with open('data/stocks_short.csv','a') as new_stocks:
                    userWrite = input("Enter data for the new file: ")
                    writer = csv.writer(new_stocks,delimiter=',')
                    writer.writerows(userWrite)    
            elif userInput.lower() == 'create':
                with open('data/stocks_short.csv','w') as new_stocks:
                    userWrite = input("Enter data for the new file: ")
                    writer = csv.writer(new_stocks,delimiter=',')
                    writer.writerows(userWrite)
