import datetime
subtotal = float(input("Please enter the subtotal: "))
data = datetime.datetime.now(tz=None)
current_day = data.weekday()

name_day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

name_day_current = name_day[current_day]
#print(name_day_current)
if (name_day_current == "Tuesday" or name_day_current == "Thursday") and subtotal < 50:
    while subtotal != 0:
        print(f"Increase  {50-subtotal}$ to access to the discount cupon")
        subtotal = float(input("Please enter the subtotal: "))
        if subtotal == 0:
            pass
        if subtotal>=50:
            pass
    

elif subtotal >= 50 and name_day_current =="Tuesday" or subtotal >= 50 and name_day_current =="Thursday":
    subtotal_desc = subtotal - (subtotal * 0.10)
    tax = subtotal_desc * 0.06
    print(f"Sales tax amount: {round(tax,2)}")
    print(f"Discount amount: {round(subtotal * 0.10,2)}")
    print(f"Total {round(tax+subtotal_desc,2)}")
""""
else:
    tax = (subtotal * 0.06)
    print(f"Sales tax amount: {round(tax,2)}")
    print(f"Total {round(tax+subtotal,2)}")
"""

