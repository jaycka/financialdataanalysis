# Write a Python program to:
# (1) read from a text file (FileToRead.txt)
# (2) count the number of characters (including “invisible” control characters)
# (3) count the number of lines
# (4) count the number of mentions of “finance”
# (5) extract email address with the following pattern using regular expressions:
#    (a) start with: a letter
#    (b) include only: letters or digits or underlines
#    (c) end with: .com
# (6) write the above statistics to a csv file (FileToWrite.csv) with the following format:
# FileToWrite.csv
# Item	Value
# charCount	a
# lineCount	b
# financeCount	c
# matchedEmail	email address

import os
import csv
import re

file_address = "C:\\Users\\Day19\\Dropbox\\Notability\\金融数据分析方法与应用-林志杰\\金融数据分析方法与应用\\Week 2\\02-DataProcessingUsingPython2\\Exercise\\FileToRead.txt"
output_address = "C:\\Users\\Day19\\Dropbox\\Notability\\金融数据分析方法与应用-林志杰\\金融数据分析方法与应用\\Week 2\\02-DataProcessingUsingPython2\\Exercise\\FileToWrite.csv"

if os.path.exists(file_address):
    # (1) read from a text file (FileToRead.txt)
    with open(file_address,'r') as f:
        file = f.read()

        # (2) count the number of characters (including “invisible” control characters)
        char_count = len(file)

        # (3) count the number of lines
        line_count = len(file.split("\n"))

        # (4) count the number of mentions of “finance”
        finance_count = file.count("finance")

        # (5) extract email address with the following pattern using regular expressions:
        #     (a) start with: a letter
        #     (b) include only: letters or digits or underlines
        #     (c) end with: .com
        email = (re.search("[a-zA-Z][a-zA-Z0-9_]*@[a-zA-Z0-9-_]*.com",file)).group()

        # (6) write the above statistics to a csv file (FileToWrite.csv) with the following format:
        # FileToWrite.csv
        # Item	Value
        # charCount	a
        # lineCount	b
        # financeCount	c
        # matchedEmail	email address
        with open(output_address,"w",newline="") as output:
            Headers = ["Item","Value"]
            Rows = [
                ["charCount",char_count],
                ["lineCount",line_count],
                ["financeCount",finance_count],
                ["matchedEamil",email]
            ]
            writer = csv.writer(output)
            writer.writerow(Headers)
            writer.writerows(Rows)
else:
    print ("File FileToReat.txt not exist")


