光控

	如果光线强度大于70则直线前进
	
	cs = ColorSensor(INPUT_1)
	ms = MoveSteering(OUTPUT_A, OUTPUT_B)
	test_speed = SpeedPercent(50)
	while True:
		if cs.reflected_light_intensity > 70:
			ms.on_for_degrees(0, test_speed, 90)
	
	
声控车

	A. 拍一次手机器人前进，拍第二次机器人后退，循环往复
	B. 拍手控制机器人前进，声音越大速度越快

A：
	ss = SoundSensor(INPUT_1)
	ms = MoveSteering(OUTPUT_A, OUTPUT_B)
	test_speed = SpeedPercent(50)
	degree = -90
	while True:
		ms.on_for_degrees(0, test_speed, degree)
		if ss.sound_pressure > 60:
			degree *= -1
			
B：
	while True:
		ms.on_for_degrees(0, SpeedPercent(ss.sound_pressure /10), 180)
	
		


	
