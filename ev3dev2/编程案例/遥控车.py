def turn_left(state):
	ir = InfraredSensor(INPUT_1)
	ms = MoveSteering(OUTPUT_A, OUTPUT_B)
	speed = 80
	steering = -80
	if ir.bottom_right():
		ms.on(steering, SpeedPercent(speed))
	else:
		ms.stop()

def turn_right(state):
	ir = InfraredSensor(INPUT_1)
	ms = MoveSteering(OUTPUT_A, OUTPUT_B)
	speed = 80
	steering = 80
	if ir.top_right():
		ms.on(steering, SpeedPercent(speed))
	else:
		ms.stop()

def go_straight(state):
	ir = InfraredSensor(INPUT_1)
	ms = MoveSteering(OUTPUT_A, OUTPUT_B)
	speed = 50
	if ir.top_left():
		ms.on(0, SpeedPercent(speed))
	else:
		ms.stop()


def reverse_car(state):
	ir = InfraredSensor(INPUT_1)
	ms = MoveSteering(OUTPUT_A, OUTPUT_B)
	speed = -50
	if ir.bottom_left():
		ms.on(0, SpeedPercent(speed))
	else:
		ms.stop()
	

def remote_control():
'''
左上：前进
左下：后退
右上：右转
右下：左转
'''
	ir = InfraredSensor(INPUT_1)
	ir.on_channel1_top_left = go_straight
	ir.on_channel1_bottom_left = reverse_car
	ir.on_channel1_top_right = turn_right
	ir.on_channel1_bottom_right = turn_left
	print('start!')
	while True:
		print(ir.proximity)   
		ir.process()
		time.sleep(0.01)
