name = input("Enter your name: ")

print("Game 1")
name1 = input("Opponent's Name: ")
points_y = input("Your score: ")
points_o = input("Opponents score: ")
box = (points_y + points_o) / points_y

print("Game 2")
name2 = input("Opponent's Name: ")
points_y2 = input("Your score: ")
points_o2 = input("Opponents score: ")
box2 = (points_y2 + points_o2) / points_y2

print("Game 3")
name3 = input("Opponent's Name: ")
points_y3 = input("Your score: ")
points_o3 = input("Opponents score: ")
box3 = (points_3 + points_3) / points_3

print("Game 4")
name4 = input("Opponent's Name: ")
points_y4 = input("Your score: ")
points_o4 = input("Opponents score: ")
box4 = (points_y4 + points_o4) / points_y4

print("Game 5")
name5 = input("Opponent's Name: ")
points_y5 = input("Your score: ")
points_o5 = input("Opponents score: ")
box5 = (points_y5 + points_o5) / points_y5

print(f"{'Opponents name':<20}{'Opponents score':>20}{'Yours score':>20}{'box':>20}")
print(f"{name1:<20}{points_o:>20}{points_y:>20}{box:>20}")
print(f"{name2:<20}{points_o2:>20}{points_y2:>20}{box2:>20}")
print(f"{name3:<20}{points_o3:>20}{points_y3:>20}{box3:>20}")
print(f"{name4:<20}{points_o4:>20}{points_y4:>20}{box4:>20}")
print(f"{name5:<20}{points_o5:>20}{points_y5:>20}{box5:>20}")
