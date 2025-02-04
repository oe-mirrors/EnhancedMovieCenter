from Components.Renderer.PositionGauge import PositionGauge


# DEPRECATED use core PositionGauge
class EMCPositionGauge(PositionGauge):
	def __init__(self):
		PositionGauge.__init__(self)
		self.__cutlist = []

	def getCutlist(self):
		return self.__cutlist

	def setCutlist(self, cutlist):
		if self.__cutlist != cutlist:
			# E2 Bug: Use a list copy instead of a reference
			self.__cutlist = cutlist[:]
			if self.instance is not None:
				try:
					self.instance.setInOutList(cutlist)
				except Exception as err:
					print(f"EMCPositionGauge error setInOutList value: {cutlist} / Error:{err}")

	cutlist = property(getCutlist, setCutlist)
