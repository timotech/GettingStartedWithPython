#fileName = 'demo.txt'
#accessMode = 'w' #w to create a new file for written
#APPEND = 'a' #a to add to a file
#ReadWrite = 'w+'

#file = open(fileName, mode=APPEND)
#file.write('This first text\n')
#file.write('This is second text')
#file.close()

#print('File written successfully')

#Write to CSV file
#fileName = 'demo.csv'
#WRITE = 'w' #w to create a new file for written
#APPEND = 'a' #a to add to a file
#ReadWrite = 'w+'

#file = open(fileName, mode=WRITE)
#file.write('Susan, 29\n')
#file.write('Christopher, 20')
#file.close()

#print('File written successfully')

#Write from Console
#fileName = 'demo.txt'
#WRITE = 'w' #w to create a new file for written
#APPEND = 'a' #a to add to a file
#READWRITE = 'w+'

#data = input('Please enter file info')

#file = open(fileName, mode=WRITE)
#file.write(data)
#file.close()
#print('File written successfully')

#########
#Read from a file
#########

#myFile = open('demo.txt', 'r')
#Read all file contents
#fileContents = myFile.read()

#Read a single line, line by line
#fileContents = myFile.readline()
#print(fileContents)

#To close a file without using close() function use the format below
#Not nessarily with csv 
import csv
fileName = "demo.txt"

#with open(fileName, 'r') as myCsvFile:
#    allRowsList = csv.reader(myCsvFile)

#    for currentRow in allRowsList:
#        for currentWord in currentRow: #second loop to remove the brackets
#            print(currentWord)

#To remove the list brackets without a second loop use the join
with open(fileName, 'r') as myCsvFile:
    allRowsList = csv.reader(myCsvFile)
    for currentRow in allRowsList:
        print(','.join(currentRow))

