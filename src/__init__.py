from gettext import GNUTranslations, NullTranslations, bindtextdomain, dgettext, find

from enigma import eTimer

from skin import loadSkin
from Components.Language import language
from Tools.Directories import SCOPE_PLUGINS, resolveFilename

loadSkin("/usr/lib/enigma2/python/Plugins/Extensions/EnhancedMovieCenter/CoolSkin/EMCMediaCenter_LCD.xml")

defaultlang = "en"


class InitTranslations:
	def __init__(self):
		self.active = True
		self.catalog = None
		self.timer = eTimer()
		self.timer.callback.append(self.finish)
		# Release the temporary catalog when the GUI enters its event loop.
		self.timer.start(0, True)

	def load(self, localePath):
		if self.active:
			catalog = NullTranslations()
			try:
				# Read directly so gettext's process-wide cache does not retain this catalog.
				for fileName in find("EnhancedMovieCenter", localePath, all=True):
					with open(fileName, "rb") as source:
						catalog.add_fallback(GNUTranslations(source))
			except OSError:
				catalog = NullTranslations()
			self.catalog = catalog

	def finish(self):
		self.active = False
		self.catalog = None
		if self.timer is not None:
			self.timer.stop()
			self.timer = None


initTranslations = InitTranslations()


def localeInit():
	global defaultlang
	defaultlang = language.getLanguage().split("_", 1)[0]
	if len(defaultlang) < 2:
		defaultlang = "en"
	localePath = resolveFilename(SCOPE_PLUGINS, "Extensions/EnhancedMovieCenter/locale")
	bindtextdomain("EnhancedMovieCenter", localePath)
	initTranslations.load(localePath)


def _(text):
	# Imported references keep working after the temporary startup catalog is released.
	catalog = initTranslations.catalog
	return (catalog.gettext(text) if catalog is not None else dgettext("EnhancedMovieCenter", text)) if text else ""


localeInit()
language.addCallback(localeInit)
