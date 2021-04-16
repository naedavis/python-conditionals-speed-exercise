#Determining your points for driving over speed limit

current_speed = int(input("Enter your speed (km/h): "))
ave_speed = int(input("Enter Average speed of road: "))

if current_speed < ave_speed:
    print("okay")
else:
     diff = current_speed - ave_speed
     points = diff / 5
     print("Your points are: " + str(points))
if points >= 12:
     print("GO TO JAIL!")


