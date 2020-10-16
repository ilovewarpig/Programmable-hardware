直角绕圈
def gyro_car():
'''
直角转弯
ms = MoveSteering(OUTPUT_A, OUTPUT_B)
speed = SpeedPercent(50)
while True:
ms.on_for_seconds(0, speed, 5)
turn_right_g(50, 90)
'''
gs = GyroSensor(INPUT_3)
ms = MoveSteering(OUTPUT_A, OUTPUT_B)
ir = InfraredSensor(INPUT_1)
while True:
	if ir.proximity < 50:
		ms.on(60, SpeedPercent(50))
		gs.wait_until_angle_changed_by(delta=90)
	# ms.stop()
	else:
		ms.on(0, SpeedPercent(50))
