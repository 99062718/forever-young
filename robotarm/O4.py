from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

for x in range(3, 0, -1):
    robotArm.grab()
    for y in range(x):
        robotArm.moveRight

robotArm.speed = 10

robotArm.wait()