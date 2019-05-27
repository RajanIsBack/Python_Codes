import math

origin_position = [0, 0]
while True:
    start_position = eval(input())
    if not start_postion:
        break
start_position.split(" ")
direction = start_position[0]
steps = start_positions[1]

if direction == "UP":
    origin_position[0] +=steps
elif direction == "DOWN":
    origin_position[0] -=steps
elif direction == "LEFT":
    origin_position[-1] -=steps
elif direction=="RIGHT":
    origin_position[1] +=steps
else:
    pass
print(int(round(math.sqrt(pos[0]**2+pos[1]**2))))


