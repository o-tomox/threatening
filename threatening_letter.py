# -*- coding: utf-8 -*-

"""
脅迫状を作成するためのクラス
"""

class Letter(object):
	# 一つ一つの文字のサイズと文字間のマージン
	CHARA_WIDTH = 300
	CHARA_HEIGHT = 400
	HOR_MARGIN = 15
	VER_MARGIN = 30

	""" 脅迫状のクラス """
	def __init__(self, width_num, height_num):
		self.letter = None
		self._calculate_lettersize(width_num, height_num);

	""" 脅迫状のサイズ（仮）を計算する """
	def _calculate_lettersize(self, width_num, height_num):
		self.letterwidth = Letter.CHARA_WIDTH * width_num + Letter.HOR_MARGIN * (width_num + 1)
		self.letterheight = Letter.CHARA_HEIGHT * height_num + Letter.VER_MARGIN * (height_num + 1)

	def __str__(self):
		return "<Letter w:{0} h:{1}>".format(self.letterwidth, self.letterheight)


class ClippingStyle(object):
	""" 新聞記事の貼り付け位置などのクラス """
	def __init__(self):
		pass