# -*- coding: utf-8 -*-

"""
脅迫状を作成するためのクラス
"""

from threatening_clipping import Clipping


class Letter(object):
	# 文字間のマージン
	HOR_MARGIN = 15
	VER_MARGIN = 30

	""" 脅迫状のクラス """
	def __init__(self, characters):
		width_num = max([len(line) for line in characters])
		height_num = len(characters)

		self._calculate_lettersize(width_num, height_num)
		self._make_clippings(characters)

	""" 脅迫状のサイズ（仮）を計算する """
	def _calculate_lettersize(self, width_num, height_num):
		self.letterwidth = Clipping.CLIPPING_WIDTH * width_num + Letter.HOR_MARGIN * (width_num + 1)
		self.letterheight = Clipping.CLIPPING_HEIGHT * height_num + Letter.VER_MARGIN * (height_num + 1)

	""" 各文字用の切り抜きを作る """
	def _make_clippings(self, characters):
		clippings = []
		for h, lines in enumerate(characters):
			for w, character in enumerate(lines):
				clipping = Clipping(character)
				clippings.append(clipping)
				print clipping

	def __str__(self):
		return "<Letter w:{0} h:{1}>".format(self.letterwidth, self.letterheight)


class ClippingStyle(object):
	""" 新聞記事の貼り付け位置などのクラス """
	def __init__(self):
		pass