def my_abs(num):
	if not isinstance(num,(int,float)):
		raise TypeError('bad operand type')
	if num >= 0:
		return num
	else:
		return -num