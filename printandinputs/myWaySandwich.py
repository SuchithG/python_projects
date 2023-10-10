print("Welcome to myWay Sandwich, Please Select your order")
menu = {1: 'Onions', 2: 'Lettuce', 3: 'Tomato', 4: 'Olives', 5: 'Peppers', 6: 'Tomatoes'}
price_per_item = 5

print("Select three items for your sandwich from the menu:")

for key, value in menu.items():
    print(f"{key}. {value}")

while True:
    selected_items = input("Enter the keys for your three choices separated by spaces (e.g., 1 3 5): ").split()
    
    # Ensure the user selected exactly 3 distinct items and that all are valid choices
    if len(set(selected_items)) == 3 and all(item in ['1', '2', '3', '4', '5', '6'] for item in selected_items):
        break
    else:
        print("Invalid choices. Please select exactly three different items.")

print("\nYou have selected:")
for item in selected_items:
    print(menu[int(item)])

# Calculate total
total_bill = len(selected_items) * price_per_item
print(f"\nYour total bill is: ${total_bill:.2f}")