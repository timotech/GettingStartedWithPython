#Using lists
guests = ['Christopher', 'Bill', 'Sandra', 'Susan']
print(guests[0])

#empty list
#guest = []

#print backwards
print(guests[-2])

print('first value is ' + guests[0])
#update a value
guests[0] = 'Steve'
print('first value is now ' + guests[0])

#add new person
guests.append('Kola')
guests.append('Kunle')

#get last value
print(guests[-1])

guests.remove('Bill')
print(guests[0])

del guests[0]
print(guests[0])

#Search the list
print(guests.index('Kunle'))

#Print all guests
#items = len(guests)
#for x in range(items):
#    print(guests[x])

#Better way using for each way without the range
#for guest in guests:
#    print(guest)

#Sort
guests.sort()
for guest in guests: print(guest)