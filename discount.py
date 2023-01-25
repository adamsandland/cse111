from datetime import datetime

#find the day of the week
day_of_week = datetime.now().weekday()

# get the subtotal from the user
subtotal = float(input("Please enter the subtotal: "))
discount = 0
tax = 0
total = 0

# Determine if Discounted By day of Week, calculate in discount
if subtotal >= 50 and (day_of_week==1 or day_of_week==2):
    discount=subtotal*0.1
    total = subtotal-discount
elif subtotal < 50 and (day_of_week==1 or day_of_week==2):
    total = subtotal
    dif = 50-subtotal
    print(f"If you spend at least ${dif:.2f} more dollars, you may qualify for a 10% discount.\n")
else:
    total = subtotal

#calculate tax and determine true total
tax = (subtotal-discount)*.06
total = total+tax

#Print out to the user the summary screen
print(f"Subtotal: ${subtotal:.2f}")
if discount > 0:
    print(f"Discount: -${discount:.2f}")
print(f"Tax: ${tax:.2f}\nTotal: ${total:.2f}")