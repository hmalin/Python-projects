print('''
 _____________________
|  _________________  |
| | JO  3.141592654 | |
| |_________________| |
|  __ __ __ __ __ __  |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

Monthly Bill calculator.....by Lloyd Malin\n
''')
rent=float(input("Please enter the rent/house payment "))
electric=float(input("Please enter the energy bill "))
waste=float(input("Please enter the waste bill "))
water=float(input("Please enter the water bill "))
internet=float(input("Please enter the internet bill "))
mobile=float(input("Please enter the cell phone bill "))
misc=float(input("Please enter any misc ammount to add "))

billTotal= rent + electric + waste + water + internet + mobile + misc

split_bills = input(" Are you splitting the bills with others ? Y or N ")

if split_bills== "Y" or "y":
    numOfPeople= int(input("How many people are splitting the bills? "))
    print(f"The amount each pearson should pay is ${round(billTotal/numOfPeople, 2)}")

else:
    print(f"Total bills is ${billTotal}")
