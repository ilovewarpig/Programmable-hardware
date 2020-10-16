单触碰传感器

	A. 小车向前移动，碰触障碍物时停止
	B. 碰触手指后停止，等手指移开后播放警报并后退三圈
	C. 小车向前移动，碰撞障碍后逆时针旋转90度后再次前进

A
	ts = TouchSensor(INPUT_1)
	ms = MoveSteering(OUTPUT_A, OUTPUT_B)
	while(ts.is_released):
		debug_print('running')
		ms.on_for_degrees(0, SpeedPercent(50), 90)
	
B
	while True:
		ms.on_for_degrees(0, SpeedPercent(50), 90)
		if ts.is_pressed:
			ms.stop()
			ts.wait_for_released()
			for i in range(3):
				sound.speak('warning...')
			ms.on_for_rotations(0, SpeedPercent(50), -3)
			break
	
C
	while True:
		ms.on_for_degrees(0, SpeedPercent(50), 180)
		if ts.is_pressed:
			ms.on_for_rotations(-80, SpeedPercent(50), 2)
	
