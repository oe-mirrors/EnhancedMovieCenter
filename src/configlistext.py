from Components.ConfigList import ConfigList, ConfigListScreen
from Components.config import ConfigElement


class ConfigListExt(ConfigList):

	def __init__(self, list, session=None):
		ConfigList.__init__(self, list, session)
		try:
			from skin import componentSizes
			sizes = componentSizes[componentSizes.CONFIG_LIST]
			self.l.setSeperation(sizes.get("seperation", 400))
			self.l.setDividerHeight(sizes.get("dividerHeight", 2))
		except:
			self.l.setSeperation(400)
		self._headers = []

	def setList(self, newList):
		self.timer.stop()
		self.__list = newList
		self.l.setList(self.__list)
		self._headers = []
		self._fake = []
		if newList is not None:
			for index, x in enumerate(newList):
				if len(x) < 2:
					self._headers.append(index)
				elif len(x[0]) < 1:
					self._fake.append(index)
				else:
					assert isinstance(x[1], ConfigElement), "entry in ConfigList " + str(x[1]) + " must be a ConfigElement"
		print("setList")
		print("headers: %s" % self._headers)
		print("fake: %s" % self._fake)

	def jumpToNextSection(self):
		index = self.getCurrentIndex()
		maxlen = len(self.__list)
		while index < maxlen - 1:
			index += 1
			if index in self._headers:
				if index + 1 < maxlen:
					self.setCurrentIndex(index + 1)
					return
				else:
					self.setCurrentIndex(index - 1)
					return
		self.goPageDown()

	def jumpToPreviousSection(self):
		index = self.getCurrentIndex() - 3
		maxlen = len(self.__list)
		while index >= 0 and maxlen > 0:
			index -= 1
			if index in self._headers:
				if index + 1 < maxlen:
					self.setCurrentIndex(index + 1)
					return
				else:
					self.setCurrentIndex(index - 1)
					return
		self.goPageUp()

#	def up(self):
#		self.instance.moveSelection(eListbox.moveUp)
#		index = self.getCurrentIndex()
#		if index in self._fake:
#			self.instance.moveSelection(eListbox.moveUp)

#	def down(self):
#		self.instance.moveSelection(eListbox.moveDown)
#		index = self.getCurrentIndex()
#		if index in self._fake:
#			self.instance.moveSelection(eListbox.moveDown)


class ConfigListScreenExt(ConfigListScreen):
	def __init__(self, list, session=None, on_change=None):
		ConfigListScreen.__init__(self, list, session, on_change)
		self["config"] = ConfigListExt(list, session=session)
		self["config"].onSelectionChanged.append(self.handleInputHelpers)

	def keyPageUp(self):
		self["config"].jumpToPreviousSection()

	def keyPageDown(self):
		self["config"].jumpToNextSection()
