""" 2. Cash Minimizer
Imagine that you are hired by a countrys mint, the entity which prints paper money and
coins. Your team studies the effectiveness and velocity of money (how quickly it changes
hands). Your initial task is to write a piece of software which gives a) a set of cash & coin
denominations, and b) an amount of money to be transferred between two parties, will
output both the payment & change which minimizes the number of bills & coins which
need to be exchanged. For example, lets take the US common cash denominations (i.e.,
[0.01, 0.05, 0.10, 0.25, 1, 5, 10, 20, 50, 100]) and an amount of $19.96. The payment &
change which minimizes the number of bills & coins for this exchange is a payment of 20 +
0.01 and a change of 0.05. """

# First commit for the this beeing at 14:40

def line(): return '-' * 40

from decimal import Decimal
#The reason for the use of "Decimal" it's because math operations with float dons't work well

currency = [0.01, 0.05, 0.10, 0.25, 1, 5, 10, 20, 50, 100]
#Converts currency list into a list of Decimal entitys
currency = sorted([Decimal(str(c)) for c in currency])

#I used AI for creating a algorithm for find where is the closest currency to the change
def find_closest(change):
    closest = min(currency, key=lambda x: abs(x - change))
    return closest

def change_optimized(product_price: str, payment: str):
    product_price_decimal = Decimal(product_price)
    payment_decimal = Decimal(payment)
    change = payment_decimal - product_price_decimal

    if (change < 0):
        return print("Insufficient payment")
    
    if (change in currency):
        return print(f"The best payment for this exchange is ${payment_decimal:.2f} and the change which minimizes is ${change:.2f}")
    
    if (change not in currency and change != Decimal('0.0')):
        add = find_closest(change) - change
        payment_decimal += add
        change = find_closest(change)
        return print(f"The best payment for this exchange is ${payment_decimal:.2f} and the change which minimizes is ${change:.2f}")

    return print("Your payment dosen't requires change")

print(line())
print("Cash Minimizer".center(40).upper())
print(line())

while True:
    product = input("Please inform the price of your product: $")
    try:
        product = float(product)
    except ValueError:
        print("Please insert a valid price format 00.00")
        continue
    #Validations for both prodcut and payment variables
    payment = input("Please inform your payment: $")
    try:
        payment = float(payment)
    except ValueError:
        print("Please insert a valid price format 00.00")
        continue
    break

change_optimized(str(product), str(payment))