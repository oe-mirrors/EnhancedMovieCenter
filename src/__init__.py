from gettext import GNUTranslations, NullTranslations, bindtextdomain, dgettext, find

from skin import loadSkin
from Components.Language import language
from Tools.Directories import SCOPE_PLUGINS, resolveFilename

loadSkin("/usr/lib/enigma2/python/Plugins/Extensions/EnhancedMovieCenter/CoolSkin/EMCMediaCenter_LCD.xml")

defaultlang = "en"


class InitTranslations(NullTranslations):
	def __init__(self):
		NullTranslations.__init__(self)
		localePath = resolveFilename(SCOPE_PLUGINS, "Extensions/EnhancedMovieCenter/locale")
		try:
			# Do not retain the temporary catalog in gettext's process-wide cache.
			for fileName in find("EnhancedMovieCenter", localePath, all=True):
				with open(fileName, "rb") as source:
					self.add_fallback(GNUTranslations(source))
		except OSError:
			NullTranslations.__init__(self)

	def __call__(self, text):
		return self.gettext(text) if text else ""


def localeInit():
	global defaultlang
	defaultlang = language.getLanguage().split("_", 1)[0]
	if len(defaultlang) < 2:
		defaultlang = "en"
	bindtextdomain("EnhancedMovieCenter", resolveFilename(SCOPE_PLUGINS, "Extensions/EnhancedMovieCenter/locale"))


def _(text):
	return dgettext("EnhancedMovieCenter", text) if text else ""


localeInit()
language.addCallback(localeInit)
