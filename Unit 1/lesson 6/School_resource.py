print("Welcome to the School Resource Assesment")
print("Location: BVG")
print("Data Collection ")

print("1. Restrroms: ")
water_fountains = int(input("Enter in # of water fountians: "))
location_fountains = input("Where are the fountains: ")
describe_fountains = input("How are the conditions of the fountains: ")

print("2. Restrooms")
restrooms = int(input("Enter in # of restrooms: "))
location_restrooms = input("where are the restrooms: ")
describe_restrooms = input("How are the restrooms: ")

print("3. classrooms")
classrooms = int(input("Enter in # of classrooms: "))
location_classrooms = input("Where are the classrooms: ")
describe_classrooms = input("Describe the condition of the classrooms: ")
print("The average is: "+ str(water_fountains / classrooms))
print("The average is: "+str(restrooms / classrooms))





