class Solution(object):
	def abbreviateProduct(self, left, right):
		product, suffix, zeros, org_digits = 1.0, 1, 0, 0
		for n in range(left, right + 1):
			product *= n
			while product >= 1:  # keep 0.1 <= prod < 1.0, so len(str(int(prod * 100000))) == 5
				product /= 10
				org_digits += 1  # add 1 while remove 1 digit
			suffix *= n
			while suffix % 10 == 0:  # count and remove the trailing zeros
				zeros += 1
				suffix //= 10
			if suffix > 10 ** 14:
				suffix %= 10 ** 14
		if org_digits - zeros <= 10:
			return str(int(product * (10 ** (org_digits - zeros)) + 0.5)) + 'e' + str(zeros)
		else:
			return str(int(product * 100000)) + '...' + ('0000' + str(suffix))[-5:] + 'e' + str(zeros)