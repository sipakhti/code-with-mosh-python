import math

rocket_speed = 1320
bs_speed = 600
distance = int(input("Enter the distance: ")) - 120

rocket_eta = (distance/rocket_speed) * 60

bs_eta = (distance/bs_speed) * 60


print(bs_eta - rocket_eta)
human_error = 1
firing_solution = (bs_eta - (bs_eta-rocket_eta)) - human_error

if firing_solution >= 60:
    minutes = (firing_solution) // 60
    seconds = (firing_solution) % 60
    print(f"Fire when the battleship is at {minutes}m {seconds}s mark!!!")
else:
    print(f"Fire when the battleship is at {firing_solution}s mark!!!")

