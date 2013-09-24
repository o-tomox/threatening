# -*- coding: utf-8 -*-

"""
脅迫状を作成するプログラム
"""


# 脅迫状を作成する	
def makeletter(text, background, filename):
	pass



if __name__ == '__main__':
	back_white(255, 255, 255)
	text = "これは脅迫状。\nここにいろいろな文章を入れる。\n改行もできる。"
	filename = "letter.png"
	makeletter(text, back_white, filename)