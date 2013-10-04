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
		self.background = Background()

	""" 切り抜きの実際のサイズを計算する """
	def _calculate_clippingsize(self):
		# 新聞の基準サイズとの差を求める
		gap_min = 0
		gap_max = 61
		step = 15
		gap_probability = dict([(i, 10) for i in xrange(gap_min, gap_max, step)])
		width_gap = get_by_probability(gap_probability)
		height_gap = get_by_probability(gap_probability)
		# 実際のサイズ
		self.width = Clipping.CLIPPING_WIDTH - width_gap
		self.height = Clipping.CLIPPING_HEIGHT - height_gap

	def __str__(self):
		return "<Clipping chara:{0} w:{1} h:{2} back:{3}>".format(self.character.encode("utf-8"), self.width, self.height, self.background)


class Background(object):
	""" 新聞記事の背景のクラス """
	def __init__(self):
		# 背景色
		backcolor_probability = {(105, 105, 105): 10, (137, 137, 137): 10, (169, 169, 169): 10, (201, 201, 201): 10}
		self.backcolor = get_by_probability(backcolor_probability)
		
		# 背景が単色かストライプか
		is_solid = get_by_probability({True: 100, False: 50})

		# 背景が単色なら何もしない，ストライプ柄なら設定
		if is_solid:
			self.stripelinecolor = None
			self.stripelinewidth = None
		else:
			linecolor_probability = {(87,87,87): 10, (128,128,128): 10, (169,169,169): 10, (210, 210, 210): 10}
			linewidth_probability = {2: 10, 5: 10, 8: 10}
			self.stripelinecolor = get_by_probability(linecolor_probability)
			self.stripelinewidth = get_by_probability(linewidth_probability)

	def __str__(self):
		return "<Background color:{0} linecolor:{1} linewidth:{2}>".format(self.backcolor, self.stripelinecolor, self.stripelinewidth)



class CharacterStyle(object):
	""" 文字スタイルのクラス """
	def __init__(self, character, background):
		self.size = None
		self.font = None
		self.color = None
		





