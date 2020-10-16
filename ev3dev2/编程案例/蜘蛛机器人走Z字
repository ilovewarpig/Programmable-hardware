def gyro_car():
	gs = GyroSensor(INPUT_4)
	ms = MoveSteering(OUTPUT_A, OUTPUT_D)
	lg1 = LargeMotor(OUTPUT_A)
	lg2 = LargeMotor(OUTPUT_D)
	# ir = InfraredSensor(INPUT_1)
	lg1.on_to_position(SpeedPercent(75),0)
	lg2.on_to_position(SpeedPercent(75), 0)
	time.sleep(1)
	while True:
		ms.on_for_seconds(0, SpeedPercent(50), 3)
		time.sleep(2)
		ms.on(60, SpeedPercent(50))
		gs.wait_until_angle_changed_by(delta=90)
		ms.stop()
		# 误差纠正
		lg1_correction = lg1.position
		lg2_correction = lg2.position
	while math.cos(lg1_correction / 360 * math.pi) != 1.0:
		lg1_correction += 1
		lg1.on_to_position(SpeedPercent(50), lg1_correction)
	time.sleep(1)
	while math.cos(lg2_correction / 360 * math.pi) != 1.0:
		lg2_correction += 1
		lg2.on_to_position(SpeedPercent(50), lg2_correction)
	time.sleep(1)
	ms.on_for_seconds(0, SpeedPercent(50), 3)
	time.sleep(2)
	ms.on(-60, SpeedPercent(50))
	gs.wait_until_angle_changed_by(delta=90)
	ms.stop()
	# 误差纠正
	lg1_correction = lg1.position
	lg2_correction = lg2.position
	while math.cos(lg1_correction / 360 * math.pi) != 1.0:
		lg1_correction += 1
		lg1.on_to_position(SpeedPercent(50), lg1_correction)
	time.sleep(1)
	while math.cos(lg2_correction / 360 * math.pi) != 1.0:
		lg2_correction -= 1
		lg2.on_to_position(SpeedPercent(50), lg2_correction)
	time.sleep(1)
