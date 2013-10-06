# -*- coding: utf-8 -*-

"""
脅迫状を作成するためのクラス
"""

from threatening_clipping import Clipping

from probability import get_by_probability


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
		clipping_styles = []
		for h, lines in enumerate(characters):
			for w, character in enumerate(lines):
				clipping = Clipping(character)
				clipping_style = ClippingStyle(clipping, w == len(lines) - 1)
				clipping_styles.append(clipping_style)
				print clipping_style

	def __str__(self):
		return "<Letter w:{0} h:{1}>".format(self.letterwidth, self.letterheight)


class ClippingStyle(object):
	# 座標
	total_x = Letter.HOR_MARGIN + 30
	total_y = Letter.VER_MARGIN
	# 幅の最大値
	max_width = 0
	# ずらす量の候補
	slip_probability = None

	""" 新聞記事の貼り付け位置などのクラス """
	def __init__(self, clipping, next_is_newline):
		self.clipping = clipping

		# 切り抜きの回転率を決める
		rotate_probability = {-3: 7, -2: 9, -1: 10, 0: 10, 1: 10, 2: 9, 3: 7}
		self.rotate = get_by_probability(rotate_probability)

		# 切り抜きをxy方向にずらす量を決める
		slip = self._calculate_slip()

		# 貼り付ける座標を決める
		self.x = ClippingStyle.total_x + slip[0]
		self.y = ClippingStyle.total_y + slip[1]

		# xとyを更新する
		# ただし，次が行始めの場合にxを0，yを加算する
		# そうでなければ，xを加算する
		if next_is_newline:
			# まず，最大幅の確認をする
			self._calculate_max_width(ClippingStyle.total_x)
			ClippingStyle.total_x = Letter.HOR_MARGIN + 30
			ClippingStyle.total_y += Clipping.CLIPPING_HEIGHT + Letter.VER_MARGIN
		else:
			ClippingStyle.total_x += clipping.width + Letter.HOR_MARGIN


	""" 切り抜きをxy方向にずらす量を計算する """
	def _calculate_slip(self):
		# ずれ候補を計算する（一回だけ）
		self._set_slip_probability()
		# 各方向への貼り付けのずれ
		slip_x = get_by_probability(ClippingStyle.slip_probability[0])
		slip_y = get_by_probability(ClippingStyle.slip_probability[1])

		# x方向へは左にずらすだけ
		slip_x = - slip_x

		# y方向へは上下のどちらかにずらす
		minus = get_by_probability({True: 10, False: 10})
		if minus:
			slip_y = - slip_y

		return (slip_x, slip_y)

	""" ずらす量の候補を設定する """
	def _set_slip_probability(self):
		if ClippingStyle.slip_probability is None:
			slip_x = self._calculate_slip_probability(Letter.HOR_MARGIN, 5, 5)
			slip_y = self._calculate_slip_probability(Letter.VER_MARGIN, 10, 10)
			ClippingStyle.slip_probability = (slip_x, slip_y)

	""" ずらす量の候補を計算する """
	def _calculate_slip_probability(self, margin, margin_probability, step):
		slip_prob = {}
		prob = (margin / step + 1) * margin_probability
		for i in xrange(0, margin - 1, step):
			slip_prob[i] = prob
			prob -= margin_probability
		return slip_prob

	""" 切り抜きの一列の最大幅を求める """
	def _calculate_max_width(self, width):
		if ClippingStyle.max_width < width:
			ClippingStyle.max_width = width

	def __str__(self):
		return "<ClippingStyle clip:{0} rotate:{1} x:{2} y:{3}".format(self.clipping, self.rotate, self.x, self.y)




