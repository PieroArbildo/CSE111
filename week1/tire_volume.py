import math
from datetime import datetime, timedelta

width = (float(input("Enter the width of the tire in mm (ex 205):")))
ratio = (float(input("Enter the aspect ratio of the tire (ex 60):")))
diameter = (float(input("Enter the diameter of the wheel in inches (ex 15):")))

volumen = (((math.pi*width**2)*ratio*(width*ratio+2540*diameter))/10000000000)
print(f"The approximate volume is {round(volumen,2)} liters")

#Exceeding the Requirements (information at the end of the program)
if width == 195 and ratio == 65 and diameter == 14:
    print("The price is 68.09$")
elif width == 195 and ratio == 65 and diameter == 15:
    print("The price is 94.26$")
elif width == 235 and ratio == 65 and diameter == 17:
    print("The price is 231.78$")
elif width == 245 and ratio == 60 and diameter == 18:
    print("The price is 258.21$")

#If the customer agrees to buy, they will be asked for their phone number.
asking = input("Do you want to buy the tire yes/no: ")  
if asking.lower() == "yes":
    phone = input("Enter your phone number: ")
    print("The purchase was completed successfully")

current_date_and_time = datetime.now(tz=None)
# Open a text file named volumes.txt in append mode.
with open("volumes.txt", "at") as volumes_file:
    # Print information to the file.
    #If the customer agreed to purchase, their number will be saved in the file.
    if asking == "yes":
        print(f"{current_date_and_time:%Y-%m-%d},{int(width)},{int(ratio)},{int(diameter)},{round(volumen,2)},{phone}", file=volumes_file)
    else:
        print(f"{current_date_and_time:%Y-%m-%d},{int(width)},{int(ratio)},{int(diameter)},{round(volumen,2)}", file=volumes_file)

"""
If you use these measurements you will get the price of the tire
195/65 R14 68.09$
195/65 R15 94.26$
235/65 R17 231.78$
245/60 R18 258.21$
"""