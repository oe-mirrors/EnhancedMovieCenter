from gettext import bindtextdomain, dgettext
from skin import loadSkin
from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS

loadSkin("/usr/lib/enigma2/python/Plugins/Extensions/EnhancedMovieCenter/CoolSkin/EMCMediaCenter_LCD.xml")


def localeInit():
	bindtextdomain("EnhancedMovieCenter", resolveFilename(SCOPE_PLUGINS, "Extensions/EnhancedMovieCenter/locale"))


_ = lambda txt: dgettext("EnhancedMovieCenter", txt) if txt else ""

localeInit()
language.addCallback(localeInit)
