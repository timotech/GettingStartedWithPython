#if with strings

#favouriteTeam = input("What is your favourite hockey team? ")
#if favouriteTeam.upper() == "SENATORS" :
#    print("Yeah Go Sens Go") #Indentation matters when you are executing control structures
#    print("But I miss Alfredsson")
#print("it's okay if you prefer football/soccer")

#if with numbers
#deposit = int(input("how much do you want to deposit "))
#if deposit > 100 :
#    print("enjoy your toaster")
#print("Have a nice day")

#freeTotaster = False
#deposit = input("how much do you want to deposit ")
#if int(deposit) > 100 :
#    freeTotaster = True #boolean variable
#    print("enjoy your toaster")
#else :
#    print("enjoy your mug")
#print("Have a nice day")

#if freeTotaster :
#    print("enjoy your toaster")

#using elif for else if
#country = input("Where are you from? ").upper()
#if country == "CANADA" :
#    print("Hello")
#elif country == "GERMANY" :
#    print("Guten Tag")
#elif country == "FRANCE" :
#    print("Bonjour")
#else: print("You must be from Nigeria")

team = input('Enter your favourite hockey team: ').upper()
sport = input('Enter your favourite sport: ').upper()

#if sport == "HOCKEY" and team == 'RANGERS' :
#    print('I miss Messier')
#elif sport == 'LEAFS' or team == 'SENATORS' :
#    print('Good luck getting the cup this year')
#else : print('I don\'t know what you are saying')

#To break statements to multiple lines use the back slash
#if sport == "HOCKEY" or sport == "LEAFS" \
#    or team == "RANGERS" or team == "SENATORS" :
#    print("Team and sport found")

#Indenting if statements
if sport == 'HOCKEY' :
    print('Thats great')
    if team == 'SENATORS' :
        print('Go senators')