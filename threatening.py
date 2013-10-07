# -*- coding: utf-8 -*-

"""
脅迫状を作成するプログラム
"""

from threatening_letter import Letter


# 脅迫状を作成する	
def makeletter(text, background, filename):
	# 文章を行毎，一文字に分ける
	characters = [[character for character in line.rstrip()] for line in text.split("\n")]

	# 脅迫状インスタンスを生成する
	letter = Letter(characters, background)

	print letter



if __name__ == '__main__':
	back_white = (255, 255, 255)
	text = u"これは脅迫状。\nここにいろいろな文章を入れる。\n改行もできる。"
	filename = "letter.png"
	makeletter(text, back_white, filename)