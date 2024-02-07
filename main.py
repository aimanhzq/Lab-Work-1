print("Currency Convertion Program")

print("Exchange Rates:")
print("USD - US Dolar: 0.25")
print("EUR - Euro: 0.21")
print("GBP - British Pound: 0.18")

print("Choose the target currency:")
print("1. USD - US Dollar")
print("2. EUR - Euro")
print("3. GBP - British Pound")

USD = 0.25
Euro = 0.21
GBP = 0.18

choice = int(input("Enter your choice1 (1 - 3): "))

if choice == 1:
    value = float(input("Enter the amount in Ringgit (MYR): "))
    total = value*USD
    print("Equivalent Amount in USD: ", total)

elif choice == 2:
    value = float(input("Enter the amount in Ringgit (MYR): "))
    total = value*Euro
    print("Equivalent Amount in USD: ", total)

elif choice == 3:
    value = float(input("How many ticket ? : "))
    total = value*GBP
    print("Equivalent Amount in GBP: ", total)

else:
    print("Invalid option! Please re-enter number 1 - 3")
