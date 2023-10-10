import string 
# 1.
print("please enter in your name")
name = input()
print("hello " + name)

#2.

print("please enter in two numbers ")
num1 = int(input())
num2 = int(input())

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1/num2)


#3.
print("please enter in the temperature in Celsius")
temp = int(input())
print(temp*9/5+32)

#4.
print("please enter in your name")
name = input()

print("please enter in your age")
age = input()

print("please enter in your city")
city = input()

print("name: " + name+ " age: " + age+ " city: " + city)


#5.
print("please enter in width and length")
w = int(input())
l = int(input())

print(w*l)

#6.
print("please enter in amount")
a = int(input())
print(a*0.74)

#7.
print("please enter in your first and last name")
first = input()
last = input()

print("Full Name: " + string.upper(first) + string.upper(last))


#8.
print("enter three prices of your purchased items ")
one = float(input())
two = float(input())
three = float(input())

total = one + two + three * 0.08
t = total + one + two + three
print(t)

#9.
print("please enter number of days")
day = int(input)
hour = day * 24 
print("days: " + day + " hours: " + hour)


#10.
print("enter distance and time")
d = float(input())
h = float(input())

speed = d / h
print("speed: " +speed )