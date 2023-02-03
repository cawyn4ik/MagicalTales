define config.name = _("MagicalTales")

define gui.show_name = False

define config.version = "2.5"
define gui.about = _("Это игра рассчитывается как проект, но в будущем может использовать как коммерческий продукт")
define build.name = "MagicalTales"

define config.has_sound = False
define config.has_music = True
define config.has_voice = False
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = Dissolve(1.0)
define config.end_splash_transition = Dissolve(1.0)
define config.end_game_transition = None
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)
default preferences.text_cps = 25
default preferences.afm_time = 15
define config.save_directory = "save"
define config.window_icon = "gui/window_icon.png"

init python:

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)


    build.documentation('*.html')
    build.documentation('*.txt')


