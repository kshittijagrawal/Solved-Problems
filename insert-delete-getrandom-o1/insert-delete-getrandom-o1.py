class RandomizedSet:

	def __init__(self):
		self._val_to_ind = {}
		self._list = []

	def insert(self, val: int) -> bool:
		if val in self._val_to_ind:
			return False
		self._val_to_ind[val] = len(self._list)
		self._list.append(val)
		return True


	def remove(self, val: int) -> bool:
		if val in self._val_to_ind:
			if self._list[-1]!=val:
				ind = self._val_to_ind.pop(val)
				self._list[ind] = self._list.pop()
				self._val_to_ind[self._list[ind]] = ind
			else:
				del self._val_to_ind[val]
				self._list.pop()
			return True
		return False


	def getRandom(self) -> int:
		return random.choice(self._list)