# Write a function called greet that prints 'Habari! Welcome to Python class.' Then call it.

def greet():
    print("Habari! Welcome to Python class")
greet()

# Write a function called show_line that prints a line of 30 dashes. Call it three times in a row

def show_line():
    print("-" * 30)
show_line()
show_line()
show_line()

# Write a function called mpesa_menu that prints a simple M-Pesa menu (Send Money, Withdraw, Check Balance, Exit). Call it once.

def mpesa_menu():
    print("Send Money")
    print("Withdraw")
    print("Check Balance")
    print("Exit")
mpesa_menu()

# Write a function called greet_student that takes a name parameter and prints 'Habari, [name]! Ready to code?'

def greet_student(name):
    print(f"Habari! {name}! Ready to code?")
greet_student("John Doe")
greet_student("Jane Doe")

 # Write a function called print_times_table that takes a number parameter and prints its times table from 1 to 10.

def print_times_table(number):
    for x in range (1, 11):
        multiplication = x * number
        print(f"Number {number} multiplied by number {x} is {multiplication} ")
print_times_table(1)
print_times_table(2)
print_times_table(3)
print_times_table(4)
print_times_table(5)
print_times_table(6)
print_times_table(7)
print_times_table(8)
print_times_table(9)
print_times_table(10)


# Write a function called add_mpesa that takes two parameters (sender and amount) and prints a transfer message. E.g. 'Amina sent Ksh 500 via M-Pesa

def add_mpesa(sender, amount):
    print(f"{sender} sent {amount} via Mpesa")
add_mpesa ("Amina", 600)
add_mpesa ("Bobu", 1000)


# Write a function called add that takes two numbers and returns their sum. Store the result in a variable and print it.

def add (number1, number2):
    summation = number1 + number2
    return summation
result = add(100, 200)
print(result)
result = add(300, 200)
print(result)

# Write a function called vat_price that takes an original price and returns the price after adding 16% VAT (Kenya's standard VAT rate).

def vat_price(price):
    vat = price * 0.16
    new_price = price + vat
    print(f"Price is {price} with a VAT price of {vat} that amounts to {new_price} ")
vat_price(500)
vat_price(800)
vat_price(1000)

# Write a function called is_pass that takes a score and returns True if the score is 50 or above, and False otherwise. Test it with several scores

def is_pass(score):
    if score >= 50:
        return True
    else:
        return False
result = is_pass(70)
print(result)
result = is_pass(90)
print(result)
result = is_pass(40)
print(result)
print(is_pass(70))

# Write a function called average that takes a list of numbers and returns the average. Test it with exam scores.

scores = [89, 76, 44, 89]
numbers = [70, 89, 67, 54]
def average (numbers):
    global marks
    average_scores = sum(numbers) / len(numbers)
    return average_scores
result = average(numbers)
print(result)
    
result = average(scores)
print(result)

# Q11. Write a function called make_tea that takes cups and an optional sugar parameter (default 1). Print a message like 'Making 2 cups of tea with 1 spoon of sugar.'

def make_tea(cups, sugar=1):
    print(f"Making {cups} cups of tea with {sugar} spoon of sugar")
make_tea(20)
make_tea(5)
make_tea(10)
make_tea(6)
make_tea(50)
make_tea(100)

# Q12. Write a function called send_message that takes recipient, message, and an optional channel parameter (default 'SMS'). Print: 'Sending to [recipient] via [channel]: [message]'

def send_message (recipient, message, channel="SMS"):
    print(f"Sending to {recipient} via {channel}: {message}")
send_message("Eugine", "Invoice created")
send_message("Quinter", "Approved")


# # Q13. Receipt Generator: Write a program that uses functions to calculate and print a shop receipt. Use separate functions for: calculating the subtotal, applying a discount, adding VAT, and printing the receipt.

def calculate_subtotal(items):
    """Calculates the sum of (price * quantity) for all items."""
    subtotal = 0.0
    for item in items:
        # item format: {"name": str, "price": float, "qty": int}
        subtotal += item["price"] * item["qty"]
    return subtotal


def apply_discount(subtotal, discount_rate):
    """Calculates the discount amount based on a percentage rate."""
    return subtotal * (discount_rate / 100)


def calculate_vat(amount, vat_rate):
    """Calculates the VAT amount on a given taxable amount."""
    return amount * (vat_rate / 100)


def print_receipt(items, subtotal, discount_amount, vat_amount, total):
    """Formats and prints the final shop receipt."""
    print("\n" + "=" * 40)
    print(f"{'MY RETAIL SHOP':^40}")
    print("=" * 40)
    print(f"{'Item Name':<18}{'Qty':<6}{'Price':<8}{'Total':<8}")
    print("-" * 40)

    # Print each line item
    for item in items:
        item_total = item["price"] * item["qty"]
        print(f"{item['name']:<18}{item['qty']:<6}{item['price']:<8.2f}{item_total:<8.2f}")
    
    print("-" * 40)
    # Print calculated summaries
    print(f"{'Subtotal:':<30}${subtotal:.2f}")
    if discount_amount > 0:
        print(f"{'Discount:':<30}-${discount_amount:.2f}")
    print(f"{'VAT:':<30}${vat_amount:.2f}")
    print("=" * 40)
    print(f"{'TOTAL PAYABLE:':<30}${total:.2f}")
    print("=" * 40)
    print(f"{'Thank you for shopping with us!':^40}\n")


def main():
    # 1. Define the items purchased
    cart = [
        {"name": "Wireless Mouse", "price": 25.00, "qty": 2},
        {"name": "Mechanical Keyboard", "price": 75.50, "qty": 1},
        {"name": "HDMI Cable", "price": 12.00, "qty": 3},
    ]
    
    # 2. Set configuration rates
    DISCOUNT_RATE = 10  # 10% discount
    VAT_RATE = 16       # 16% VAT
    
    # 3. Perform calculations using separate functions
    subtotal = calculate_subtotal(cart)
    discount_amt = apply_discount(subtotal, DISCOUNT_RATE)
    
    # Calculate VAT on the amount after the discount has been deducted
    taxable_amount = subtotal - discount_amt
    vat_amt = calculate_vat(taxable_amount, VAT_RATE)
    
    # Final total calculation
    grand_total = taxable_amount + vat_amt
    
    # 4. Print the final receipt
    print_receipt(cart, subtotal, discount_amt, vat_amt, grand_total)


if __name__ == "__main__":
    main()
