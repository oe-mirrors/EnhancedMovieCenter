from gettext import bindtextdomain, dgettext
from skin import loadSkin
from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS

loadSkin("/usr/lib/enigma2/python/Plugins/Extensions/EnhancedMovieCenter/CoolSkin/EMCMediaCenter_LCD.xml")

defaultlang = "en"


def localeInit():
	global defaultlang
	defaultlang = language.getLanguage().split("_", 1)[0]
	if len(defaultlang) < 2:
		defaultlang = "en"
	bindtextdomain("EnhancedMovieCenter", resolveFilename(SCOPE_PLUGINS, "Extensions/EnhancedMovieCenter/locale"))


_ = lambda txt: dgettext("EnhancedMovieCenter", txt) if txt else ""

localeInit()
language.addCallback(localeInit)
