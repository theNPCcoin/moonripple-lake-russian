init python:
    config.default_language = "russian"

label after_load:
    $ renpy.change_language("russian")
    return

label splashscreen:
    $ renpy.change_language("russian")
    return
