class pair_iterator():
	def __init__(self, i, buff, flag_curr, flag_my):
		self._i    = iter(i)
		self._buff = buff
		self._flag = flag_curr
		self._my   = flag_my

	def __iter__(self):
		return self

	def __next__(self):
		if   0 == len(self._buff):
			ret = next(self._i)
			self._buff.append(ret)
			self._flag[0] = not self._my
		elif self._flag[0] == self._my:
			ret = self._buff.pop(0)
		else:
			ret = next(self._i)
			self._buff.append(ret)
		return ret
	#def __next__(self):
#class pair_iterator():

def pair_iter(iterable):
	i    = iterable
	buff = []
	flag = [None]
	return (pair_iterator(i, buff, flag, True ),
	        pair_iterator(i, buff, flag, False))

def pair(x):
	ret = pair_iter(x)
	next(ret[1])
	return zip(ret[0], ret[1])
