import math

#1.
print(f"{math.pi:.3f}")

#2.
price = 29.999999
print(f"${price:.2f}")

#3.
city = "New York"
print(f"{city:^15}")

#4.
temp = 62.5
print(f"{temp:^10}")

#5.
tax = 0.075
print(f"{tax:.2%}")

#6.
discount = 0.25
print(f"{discount:.1%}")


#7.

item = "Product"
price = 25.99
quantity = 3
total = price * quantity 


print(f"{'Item':<10}{'price':<10}{'quantity':<10}{'total':<10}")
print(f"{item:<10}{price:<10}{quantity:<10}{total:<10}")


city = "new york"
population = 3000000
area = 226.63


print(f"{'city':<10}{'population':>10}{'Area (sq km)':>10}")
print(f"{city:<10}{population:>12}{area:>10}")


  
