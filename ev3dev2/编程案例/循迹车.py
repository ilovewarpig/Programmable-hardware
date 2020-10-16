单光感
	A. Z字形循迹法：检测到黑线右转，检测到白线左转
	B. 三段循迹法：在z字的基础上，增加检测黑白中间值，如果位于黑白之间则直行
	C. 比例循迹法：根据不同反射光决定转弯的程度


	A. 
while True:
	if cs.color == 1:
		ms.on_for_degrees(50, test_speed, 90)
	else:
		ms.on_for_degrees(-50, test_speed, 90)


	B. 
# 反射光在区间(12, 32)内走直线
while True:
	if cs.reflected_light_intensity < 12:
		ms.on_for_degrees(50, test_speed, 90)
	elif cs.reflected_light_intensity > 32:
		ms.on_for_degrees(-50, test_speed, 90)
	else:
		ms.on_for_degrees(0, test_speed, 90)
		
	C. 
while True:
	if cs.reflected_light_intensity <= 10:
		ms.on(-50, test_speed)
	elif cs.reflected_light_intensity > 10 and cs.reflected_light_intensity <= 20:
		ms.on(-30, test_speed)
	elif cs.reflected_light_intensity > 30 and cs.reflected_light_intensity <= 40:
		ms.on(30, test_speed)
	elif cs.reflected_light_intensity > 40:
		ms.on(50, test_speed)
	else:
		ms.on(0, test_speed）
