drink = int(input("Enter in your drink "))
a = int(input("enter in your appatizer "))
d = int(input("enter in your desert "))
tip = int(input("enter in your tip rate "))

subtotal = drink + a + d

tip = subtotal * (tip / 100)

total = subtotal + tip

print(f"{subtotal }{tip}{total }")



l = float(input("length "))
w = float(input("Width "))
h = float(input("Height "))
c = float(input("cost"))
d1 = float(input("Dimensions"))
d2 = float(input("Dimensions"))
d3 = float(input("Dimensions"))

sa = l * w * 2 + w * h * 2 + h * l * 2
print(sa)

bricks = sa / (d1 * d2 * d3) 
print(bricks)

cost = bricks * c
print(cost)




d = float(input("distance"))
f = float(input("fuel efficiency "))
pr = float(input("price "))
p = float(input("passengers "))

fuel = d / f
cost = fuel * pr
passenger = cost / p 
print(fuel)
print(cost)
print(passenger)