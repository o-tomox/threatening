# -*- coding: utf-8 -*-

"""
脅迫状の一つ一つの文字
（新聞記事の切り抜き）
"""

from probability import get_by_probability


class Clipping(object):
	# 一つ一つの文字のサイズ
	CLIPPING_WIDTH = 300
	CLIPPING_HEIGHT = 400

	""" 新聞記事の切り抜きのクラス """
	def __init__(self, character):
		self.character = character
		self.clippingsize = self._calculate_clippingsize()

	""" 切り抜きの実際のサイズを計算する """
	def _calculate_clippingsize(self):
		# 新聞の基準サイズとの差を求める
		gap_min = 0
		gap_max = 61
		step = 15
		width_gap = get_by_probability(dict([(i, 10) for i in xrange(gap_min, gap_max, step)]))
		height_gap = get_by_probability(dict([(i, 10) for i in xrange(gap_min, gap_max, step)]))
		# 実際のサイズ
		self.width = Clipping.CLIPPING_WIDTH - width_gap
		self.height = Clipping.CLIPPING_HEIGHT - height_gap

	def __str__(self):
		return "<Clipping chara:{0} w:{1} h:{2}>".format(self.character.encode("utf-8"), self.width, self.height)


class Background(object):
	""" 新聞記事の背景のクラス """
	def __init__(self):
		self.backcolor = None
		self.stripe = None


class CharacterStyle(object):
	""" 文字スタイルのクラス """
	def __init__(self, character, background):
		self.size = None
		self.font = None
		self.color = None
		