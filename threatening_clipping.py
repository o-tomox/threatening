# -*- coding: utf-8 -*-

"""
脅迫状の一つ一つの文字
（新聞記事の切り抜き）
"""

class Clipping(object):
	""" 新聞記事の切り抜きのクラス """
	def __init__(self, character):
		pass


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
		