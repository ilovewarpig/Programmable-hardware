有人靠近检测器时播放门铃音乐一次，离开后停止

'''
靠近检测器时播放门铃音乐一次，离开后停止
'''
sd = Sound()
ir = InfraredSensor(INPUT_1)
not_played = True
# 周杰伦 《超人不会飞》副歌部分
song = (('C4', 'e'), ('D4', 'e'), ('E4', 's'), ('D4', 's'), ('C4', 's'),
('E4', 'e'), ('E4', 's'), ('E4', 's'), ('E4', 's'), ('E4', 's'), ('E4', 's'), ('F4', 's'), ('E4', 's'), ('D4', 'e'),
('C4', 's'), ('B3', 's'), ('C4', 'e'))
while True:
	if ir.proximity < 30 and not_played:
		sd.play_song(song=song)
		not_played = False
	elif ir.proximity > 30 and not not_played:
		not_played = True



