贴墙行走
红外线 + 碰触传感器
当红外线传感器小于20时向左调整方向，大于20时向右调整方向
当碰触传感器被按下时左转

ts = TouchSensor(INPUT_1)
ins = InfraredSensor(INPUT_2)
ms = MoveSteering(OUTPUT_A, OUTPUT_B)
test_speed = SpeedPercent(50)

while True:
	# 离墙太近
	if ins.proximity < 20:
		ms.on_for_degrees(-30, test_speed, 90)
	# 离墙太远
	elif ins.proximity >= 20 and ins.proximity < 30:
		ms.on_for_degrees(30, test_speed, 90)
	# 右侧有路口
	elif ins.proximity > 60:
		ms.on_for_rotations(0, test_speed, 3) # 让整个机器人侧对路口
		ms.on_for_degrees(80, test_speed, 360) # 面朝路口
		ms.on_for_rotations(0, test_speed, 3) # 进入路口
	# 正面有障碍物
	if ts.is_pressed:
		ms.on_for_rotations(0, test_speed, -3) # 留出转弯空间
		ms.on_for_degrees(-80, test_speed, 360) # 左转90度
		ms.on_for_rotations(0, test_speed, 1) 
