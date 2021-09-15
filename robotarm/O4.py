from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

robotArm.speed = 2

for x in range(3, 0, -1):
    robotArm.grab()
    for y in range(x):
        robotArm.moveRight()
    robotArm.drop()
    if x == 1:
        break
    for y in range(x):
        robotArm.moveLeft()
    
for x in range(1, 3):
    for y in range(x):
        robotArm.moveRight()
    robotArm.grab()
    for y in range(x):
        robotArm.moveLeft()
    robotArm.drop()

robotArm.wait()