import datetime 
while True:
    try:
        bday = input("Please enter your exact Date of Birth(eg. June 5 2001):")
        birthday = datetime.datetime.strptime(bday, '%B %d %Y')
        break
    except:  print("Please put in the Format 'Month Day Year' without any initial space")

tday = datetime.datetime.today()
timedelta = (tday - birthday).total_seconds()
print("You have been alive for:",timedelta,"seconds")
