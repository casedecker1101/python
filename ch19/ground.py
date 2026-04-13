import os, csv

dataset = []
cinWriter = ""

while True:
    if os.path.exists("data/company-stoncks.csv"):
        if cinWriter == 'quit':
            break
    else:
        cinWriter = input("Testing data input [quit to exit]: ")
        with open("data/company-stoncks.csv","a") as stocks:
            csv_writer = csv.writer(stocks,delimiter=",")
            csv_writer.writerow(cinWriter)
            for stock in stocks:
                csv_writer.writerow(cinWriter)
                print(cinWriter)