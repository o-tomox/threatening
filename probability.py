# -*- coding: utf-8 -*-

import random

def get_by_probability(probability):
	"""
		probabilityは辞書型
		キー：好きなオブジェクト
		値　：そのキーを得る確率（int型）
		値の総和に対するひとつの値が，そのキーを返す確率になる
	"""

	prob = []
	total = 0

	for k in probability:
		v = probability[k]
		total += v
		prob.append((k, total))

	# print total
	# print prob

	p = random.randint(0, total - 1)

	for (k, v) in prob:
		if p < v:
			return k

	return None


if __name__ == '__main__':
	prob = {"a": 10, "b": 60, "c": 10, "d": 20}
	# x = get_by_probability(prob)
	# print x

	result = {"a": 0, "b": 0, "c": 0, "d": 0}

	num = 10000

	for i in xrange(num):
		x = get_by_probability(prob)
		result[x] += 1

	for k in result:
		result[k] /= float(num)
		result[k] *= 100

	print result