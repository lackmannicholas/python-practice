name = input('Enter your name: ')
print(name)


size_input = input("How big is your house (SQFT): ")
square_feet = int(size_input)
square_metters = square_feet / 10.8
print(f"{square_feet} square feet is equals to {square_metters:.2f} square meters")