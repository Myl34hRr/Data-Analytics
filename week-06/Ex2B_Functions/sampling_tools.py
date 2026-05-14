import random

# List of products
products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse','Webcam', 'Headset', 'Docking station', 'USB Hub', 'Desk Lamp', 'Surge Proctecor']

# Random choose 
product_of_the_day = random.choice(products)

# Results
print("Product_of_the_Day:", product_of_the_day)
# Product of the day: USB Hub

# Random shuffle product List
random.shuffle(products)
print("shuffled products:", products)
# Randomized: webcam, surge proctecor, docking station, headset, keyboard, laptop, monitor, desk lamp, mouse, USB hub

# Random transaction count between 50 and 300
transaction_count = random.randint(50, 300)

# results
print("daily transaction count:", transaction_count)
#Daily Transaction count: 263