year = 2000 

if year % 4 == 0 and year % 100 != 0:
    print("The year is a Leap year")
elif year % 400 == 0:
    print("The year is a Leap year")
else:
    print("The year is not a Leap year")
    
