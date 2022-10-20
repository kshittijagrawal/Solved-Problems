class Solution:
	def countTime(self, time: str) -> int:
		hh = 1
		mm = 1
		if time[0] == "?" and time[1] != "?":
			if time[1] <= "3":
				hh *= 3
			else:
				hh *= 2
		elif time[0] != "?" and time[1] == "?":
			if time[0] <= "1":
				hh *= 10
			else:
				hh *= 4
		elif time[0] == "?" and time[1] == "?":
			hh *= 24
		if time[3] == "?":
			mm *= 6
		if time[4] == "?":
			mm *= 10
		return hh * mm