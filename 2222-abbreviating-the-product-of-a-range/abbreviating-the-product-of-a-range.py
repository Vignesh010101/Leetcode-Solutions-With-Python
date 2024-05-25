class Solution(object):
	def abbreviateProduct(self, left, right):
		prod, suf, zeros, org_digits = 1.0, 1, 0, 0
		for n in range(left, right + 1):
			prod *= n
			while prod >= 1:  # keep 0.1 <= prod < 1.0, so len(str(int(prod * 100000))) == 5
				prod /= 10
				org_digits += 1  # add 1 while remove 1 digit
			suf *= n
			while suf % 10 == 0:  # count and remove the trailing zeros
				zeros += 1
				suf //= 10
			if suf > 10 ** 14:
				suf %= 10 ** 14
		if org_digits - zeros <= 10:
			return str(int(prod * (10 ** (org_digits - zeros)) + 0.5)) + 'e' + str(zeros)
		else:
			return str(int(prod * 100000)) + '...' + ('0000' + str(suf))[-5:] + 'e' + str(zeros)