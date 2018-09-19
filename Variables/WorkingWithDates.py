import datetime
currentDate = datetime.date.today()
#print(currentDate)
#print(currentDate.year)
#print(currentDate.month)
#print(currentDate.day)

#print(currentDate.strftime('%d %b, %Y'))
#print(currentDate.strftime('%d %b, %y')) #Two digit year

#print(currentDate.strftime('Please attend our event %A, %B %d in the year %Y'))

#userInput = input("Please enter your birthday (mm/dd/yyyy) ")
#birthday = datetime.datetime.strptime(userInput, '%m/%d/%Y').date()
#print(birthday)

#days = birthday - currentDate
#print(days.days)

currentTime = datetime.datetime.now()
print(currentTime.minute)