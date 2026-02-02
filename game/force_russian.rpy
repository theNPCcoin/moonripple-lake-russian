init python:
    config.default_language = "russian"

    if persistent.aname == "Anon" or persistent.aname is None:
        persistent.aname = "Анон"
    if persistent.sname == "Suzie" or persistent.sname is None:
        persistent.sname = "Сьюзи"

    def ru_location_name(name):
        ru_map = {"Attic": "Чердак", "Foyer": "Фойе"}
        if _preferences.language == "russian":
            return ru_map.get(name, name)
        return name

    _ru_quest_titles = {
        "Find alcohol": "Найти алкоголь",
        "Find alcohol (alternate path)": "Найти алкоголь (другой путь)",
        "Holy Spirit": "Святой Дух",
        "Quench the Thirst": "Утолить жажду",
        "In Queue": "В очереди",
        "Lake Tour": "Тур по озеру",
        "Park Rendezvous": "Встреча в парке",
    }

    _ru_quest_descs = {
        "Drago asked you to find some alcohol for the party. Have a look around town.":
            "Драго попросил найти алкоголь для вечеринки. Осмотрись в городе.",
        "It seems Skeeter is hoarding alcohol. He wants to have fun with [persistent.sname]. Maybe I should look elsewhere...":
            "Похоже, Скитер припрятал алкоголь. Он хочет развлечься с [persistent.sname]. Может, стоит поискать в другом месте...",
        "Got the alcohol! Bring it to the beach party.":
            "Алкоголь найден! Отнеси его на пляжную вечеринку.",
        "We already have the alcohol, we should go to the party at the beach!":
            "Алкоголь уже есть, пора идти на вечеринку на пляже!",
        "The bartender isn't allowed to sell you alcohol to go. Maybe he'll be more sympathetic if [persistent.sname] speaks to him?":
            "Бармен не может продать алкоголь на вынос. Может, он будет сговорчивее, если [persistent.sname] поговорит с ним?",
        "The bartender didn't want to budge. But [persistent.sname] has loosened up from the cocktail. Maybe I could try with Skeeter at the town square again?":
            "Бармен не уступил. Но [persistent.sname] расслабилась от коктейля. Может, снова попробовать со Скитером на площади?",
        "The bartender didn't want to budge. He pointed us in the direction of the town square, where Skeeter is supposed to be.":
            "Бармен не уступил. Он указал нам в сторону площади, где должен быть Скитер.",
        "Instead of dealing with Skeeter, we could just drive the 8 miles and get the drinks from the 24/7 gas station?":
            "Вместо того чтобы иметь дело со Скитером, можно просто проехать 8 миль и купить выпивку на круглосуточной заправке?",
        "You should go pay Father Clark a visit. He might be able to shine some light on your condition.":
            "Стоит навестить Отца Кларка. Возможно, он прольёт свет на твоё состояние.",
        "Go have a drink at the bar. You're killing time, anyway, right?":
            "Сходи выпить в бар. Всё равно убиваешь время, верно?",
        "Might as well go check if there's anything happening at the store.":
            "Можно заглянуть в магазин — вдруг там что-то происходит.",
        "You heard people talking about the ferry tours at the boardwalk. Could be fun.":
            "Ты слышал, что на набережной есть паромные экскурсии. Может быть весело.",
        "I should meet the girls at the park, near the town square and the beach.":
            "Надо встретиться с девушками в парке, рядом с площадью и пляжем.",
    }

    _ru_option_prompts = {
        "Did the ferryman catch": "Паромщик поймал",
        "Did {} give a blowjob to Drago in Episode 4?": "{} делала минет Драго в Эпизоде 4?",
        "Did you tell {} to be naughty?": "Ты сказал {} быть непослушной?",
        "Did you tell {} to kiss Drago?": "Ты сказал {} поцеловать Драго?",
    }

    def _ru_translate_prompt(prompt):
        if _preferences.language != "russian":
            return prompt
        for eng, rus in _ru_option_prompts.items():
            if eng in prompt:
                name = persistent.sname or ""
                return rus.format(name) if "{}" in rus else rus + " " + name + "?"
        return prompt

    def _ru_translate_quest(title, desc):
        if _preferences.language != "russian":
            return title, desc
        ru_t = _ru_quest_titles.get(title, title)
        ru_d = _ru_quest_descs.get(desc, desc)
        return ru_t, ru_d

    _ru_portal_hover = {
        "Home sweet home.": "Дом, милый дом.",
        "That's it I think!": "Кажется, это оно!",
        "I'm already here, at the bar.": "Я уже здесь, в баре.",
        "This place is my best bet.": "Это место — мой лучший вариант.",
        "I don't really need to go to the bar right now.": "Мне сейчас не нужно идти в бар.",
        "I was just there, I should go to the house.": "Я только что был там, надо идти к дому.",
        "That's the bar.": "Это бар.",
        "The grocery store.": "Продуктовый магазин.",
        "The beach.": "Пляж.",
        "The beach!": "Пляж!",
        "That's the town square.": "Это городская площадь.",
        "That's the boardwalk.": "Это набережная.",
        "That tunnel leads off the island.": "Этот тоннель ведёт с острова.",
        "The church.": "Церковь.",
        "That's the park.": "Это парк.",
    }

init 999 python:
    _orig_showportalhovertext = Portal.showportalhovertext
    def _ru_showportalhovertext(self):
        if self.onhoveredtxt is not None and _preferences.language == "russian":
            txt = _ru_portal_hover.get(self.onhoveredtxt, self.onhoveredtxt)
            renpy.show_screen("anon_say", text=txt, xa=0.33, ya=0.85)
        else:
            _orig_showportalhovertext(self)
    Portal.showportalhovertext = _ru_showportalhovertext

translate russian style main_menu_button_text:
    font "fonts/FiraSansCondensed-Heavy.TTF"
    size 62

translate russian style translations_btn_text:
    font "fonts/FiraSansCondensed-Heavy.TTF"

translate russian style connect_button_text:
    font "fonts/FiraSansCondensed-Heavy.TTF"
    size 62

translate russian style news_frame_title:
    font "fonts/FiraSansCondensed-Heavy.TTF"

translate russian style news_text:
    font "fonts/FiraSansCondensed-Heavy.TTF"

translate russian style name_input_text:
    font "fonts/Roboto-Bold.TTF"

translate russian style name_input_text_1stline:
    font "fonts/Roboto-Bold.TTF"

translate russian style name_input_text_1stlinealt:
    font "fonts/Roboto-Bold.TTF"

translate russian style name_input_text_2ndline:
    font "fonts/Roboto-Bold.TTF"

translate russian style name_input_text_3rdline:
    font "fonts/Roboto-Bold.TTF"

translate russian style name_input_text_4thline:
    font "fonts/Roboto-Bold.TTF"

translate russian style name_input_input:
    font "fonts/Roboto-Bold.TTF"

translate russian style line1st_screentitle:
    font "fonts/FiraSansCondensed-Heavy.TTF"

translate russian style support_feedback_text:
    font "fonts/FiraSansCondensed-Heavy.TTF"

translate russian style support_feedback_text_accent:
    font "fonts/FiraSansCondensed-Heavy.TTF"

translate russian style continue_button_end_screen_text:
    font "fonts/FiraSansCondensed-Heavy.TTF"

translate russian style savefix_0:
    font "fonts/Roboto-Bold.TTF"

translate russian style savefix_1:
    font "fonts/Roboto-Bold.TTF"

translate russian style savefix_2:
    font "fonts/Roboto-Bold.TTF"

translate russian style option_prompt_text:
    font "fonts/Roboto-Bold.TTF"

translate russian style quest_title_text:
    font "fonts/Roboto-Bold.TTF"

translate russian style quest_description_text:
    font "fonts/Roboto-Bold.TTF"

translate russian style no_quests_text:
    font "fonts/Roboto-Bold.TTF"

translate russian style quickreact_button_text:
    font "fonts/FiraSansCondensed-Heavy.TTF"

translate russian style episode_text:
    font "fonts/FiraSansCondensed-Heavy.TTF"

translate russian style ver_text:
    font "fonts/FiraSansCondensed-Heavy.TTF"

translate russian strings:

    old "What will your name be?"
    new "Как тебя зовут?"

    old "What will your girl's name be?"
    new "Как зовут твою девушку?"

    old "You can disable potential femboy/futanari content here."
    new "Здесь можно отключить контент с фембоями/футанари."

    old "You will never see it if it is disabled :)"
    new "Если отключено — вы его никогда не увидите :)"

    old "Click on the blurred image here to see example."
    new "Нажмите на размытое изображение, чтобы увидеть пример."

    old "Hover over an option for more information."
    new "Наведите на вариант для подробностей."

    old "(you can change this at any time in the options menu)"
    new "(можно изменить в любое время в настройках)"

    old "You will ENABLE femboy/futanari content."
    new "Контент с фембоями/футанари будет ВКЛЮЧЁН."

    old "You will DISABLE femboy/futanari content."
    new "Контент с фембоями/футанари будет ОТКЛЮЧЁН."

    old "There are (not many) jumpscares in this game."
    new "В игре есть (немного) скримеров."

    old "I don't want to give anyone an unsolicited heart attack."
    new "Не хочу никому устраивать незваный сердечный приступ."

    old "Would you like to see a fluffy duck instead?"
    new "Хотите видеть пушистую уточку вместо скримеров?"

    old "You will see a fluffy duck instead of jumpscares."
    new "Вместо скримеров будет пушистая уточка."

    old "You will experience the jumpscares as intended."
    new "Скримеры будут показаны как задумано."

    old "Enter the password :)"
    new "Введите пароль :)"

    old "(Get it on Discord or the game's Steam forum)"
    new "(Найдите его в Discord или на форуме игры в Steam)"

    old "Do you want to start a new game, or jump to new content?"
    new "Начать новую игру или перейти к новому контенту?"

    old "New Game"
    new "Новая игра"

    old "Jump to episode 6"
    new "Перейти к эпизоду 6"

    old "Connect?"
    new "Подключить?"

    old "You'll get a feed of the latest posts here, \nand other features in the future!"
    new "Здесь будут последние новости\nи другие функции в будущем!"

    old "Fetching news..."
    new "Загрузка новостей..."

    old "Could not load news."
    new "Не удалось загрузить."

    old "Latest Posts"
    new "Последние записи"

    old "Please "
    new "Пожалуйста, "

    old "consider "
    new "оставьте "

    old "leaving "
    new ""

    old "a review!"
    new "отзыв!"

    old "Be sure to join "
    new "Присоединяйтесь "

    old "the community "
    new "к сообществу!"

    old "as well!"
    new ""

    old "Continue..."
    new "Продолжить..."

    old "A week"
    new "Неделю"

    old "later..."
    new "спустя..."

    old "Go to:"
    new "Идти:"

    old "EP1"
    new "ЭП1"

    old "EP2"
    new "ЭП2"

    old "EP3"
    new "ЭП3"

    old "EP4"
    new "ЭП4"

    old "EP5"
    new "ЭП5"

    old "EP6"
    new "ЭП6"

    old "EP1-3"
    new "ЭП1-3"

    old "Messages"
    new "Сообщения"

    old "Close"
    new "Закрыть"

    old "Messages Screen"
    new "Сообщения"

    old "All done!"
    new "Всё выполнено!"

    old "build:"
    new "сборка:"

    old "Catch [persistent.sname]!"
    new "Поймай [persistent.sname]!"

screen upstairs_hallway_stairs_menu(n0, n1, l0, l1):
    $ ru_n0 = ru_location_name(n0)
    $ ru_n1 = ru_location_name(n1)
    add "images/pngs/set_prefs_bg.png":
        alpha 0.75
    text _("Go to:") style "location_text" xalign 0.15 yalign 0.54
    textbutton "[ru_n0]":
        action Return(l0)
        text_size 77
        xsize 350
        ysize 100
        text_font "fonts/Myriad Pro Bold.TTF"
        text_color "#fff647"
        text_hover_color "#ff7575"
        xalign 0.35
        yalign 0.45
        mouse "hand"

    textbutton "[ru_n1]":
        action Return(l1)
        text_size 77
        xsize 350
        ysize 100
        text_font "fonts/Myriad Pro Bold.TTF"
        text_color "#fff647"
        text_hover_color "#ff7575"
        xalign 0.35
        yalign 0.65
        mouse "hand"

screen news_widget():
    if not persistent.steam_connectivity:
        frame:
            xalign 1.0
            yalign 0.62
            xmaximum 550
            background None
            padding (0, 0)
            vbox:
                textbutton _("Connect?") style "connect_button":
                    action [Function(refresh_news),SetField(persistent, "steam_connectivity", True)]
                    mouse "hand"
                    xalign 0.5
                    yalign 0.5
                text _("You'll get a feed of the latest posts here, \nand other features in the future!") style "connect_desc"
    else:
        imagebutton:
            idle "gui/no_btn_idle.png"
            hover "gui/no_btn_hover.png"
            mouse "hand"
            action [SetField(persistent, "steam_connectivity", False)]
            at transform:
                zoom 0.45
                pos(0.973,0.41)
                alpha 0.8
        frame:
            xalign 1.0
            yalign 0.62
            xmaximum 600
            background None
            padding (0, 0)

            vbox:
                spacing 5

                if news_data is None and not news_error:
                    text _("Fetching news...") xalign 0.5 size 88 color "#ffffff" ysize 300 font "fonts/FREESCPT.TTF"

                elif news_error:
                    text _("Could not load news.") xalign 0.5 size 88 color "#ff9999" ysize 300 font "fonts/FREESCPT.TTF"

                else:
                    text _("Latest Posts") xalign 0.75 style "news_frame_title"
                    for post in news_data:
                        button:
                            style "news_button"
                            action OpenURL(post['url'])
                            xfill True
                            mouse "hand"

                            hbox:
                                spacing 15
                                if post['image']:
                                    add post['image']:
                                        size (160, 90)
                                        fit "cover"
                                        yalign 0.5
                                else:
                                    add "cache/covers/no_img.png":
                                        size (160, 90)
                                        fit "cover"
                                        yalign 0.5
                                        alpha 0.8

                                vbox:
                                    yalign 0.5
                                    text post['title'] style "news_text" substitute False
                                    text post['date'] style "news_date"

screen set_name():
    modal True
    add "images/BGs/maintitlebg.jpg" at mm_bg_anim
    add "images/pngs/set_prefs_bg.png"
    text _("What will your name be?") style "name_input_text" xalign 0.15 yalign 0.3
    hbox:
        xalign 0.2
        yalign 0.4
        input value VariableInputValue("persistent.aname") length 20 style "name_input_input"
        imagebutton:
            at custom_zoom(0.6)
            anchor(0.5,0.5)
            pos(0.2,0.5)
            xoffset 80
            yoffset -10
            idle "gui/yes_btn_idle.png"
            hover "gui/yes_btn_hover.png"
            action [SetField(persistent, "aname", persistent.aname.strip()), Return()]
            mouse "hand"
    if any_polaroids_unlocked():
        imagebutton:
            pos(0.7,0.3)
            idle "gui/reset_roids_btn_idle.png"
            hover "gui/reset_roids_btn_hover.png"
            action Function(reset_polaroids)
            mouse "hand"
    key "K_RETURN" action [SetField(persistent, "aname", persistent.aname.strip()), Return()]
    timer 1.5 repeat True action SetField(persistent, "aname", persistent.aname.strip())

screen set_sname():
    modal True
    add "images/BGs/maintitlebg.jpg" at mm_bg_anim
    add "images/pngs/set_prefs_bg.png"
    text _("What will your girl's name be?") style "name_input_text" xalign 0.15 yalign 0.3
    hbox:
        xalign 0.2
        yalign 0.4
        input value VariableInputValue("persistent.sname") length 20 style "name_input_input"
        imagebutton:
            at custom_zoom(0.6)
            anchor(0.5,0.5)
            pos(0.2,0.5)
            xoffset 80
            yoffset -10
            idle "gui/yes_btn_idle.png"
            hover "gui/yes_btn_hover.png"
            action [SetField(persistent, "sname", persistent.sname.strip()), Return()]
            mouse "hand"
    key "K_RETURN" action [SetField(persistent, "sname", persistent.sname.strip()), Return()]
    timer 1.5 repeat True action SetField(persistent, "sname", persistent.sname.strip())

screen set_femboys():
    default femboy_explainer = __("Hover over an option for more information.")
    default blur_femboy = True
    default first_screen_open = True
    default border_color = "#ffffff30"

    modal True
    add "images/BGs/maintitlebg.jpg" at mm_bg_anim
    add "images/pngs/set_prefs_bg.png"
    text _("You can disable potential femboy/futanari content here.") style "name_input_text" xalign 0.15 yalign 0.3
    text _("You will never see it if it is disabled :)") style "name_input_text_2ndline" xalign 0.15 yalign 0.35
    text _("Click on the blurred image here to see example.") style "name_input_text_4thline" xalign 0.93 yalign 0.278
    text "[femboy_explainer!t]" style "name_input_text_3rdline" xalign 0.185 yalign 0.55
    text _("(you can change this at any time in the options menu)") style "name_input_text_4thline" xalign 0.21 yalign 0.58

    frame:
        background border_color
        padding (10, 10, 10, 10)
        ypos 0.45 yanchor 0.5
        xpos 0.83 xanchor 0.5
        imagebutton:
            if first_screen_open:
                at femboy_base_transform
            else:
                if blur_femboy:
                    at femboy_blur
                else:
                    at femboy_noblur
            at custom_zoom(0.2)
            pos(0.5, 1.0)
            anchor(0.5,1.0)
            idle "images/example_femboy.jpg"
            hover "images/example_femboy.jpg"
            hovered SetScreenVariable("border_color", "#ffffff74")
            unhovered SetScreenVariable("border_color", border_color)
            action [ToggleScreenVariable("blur_femboy"), SetScreenVariable("first_screen_open", False)]
            mouse "hand"

    hbox:
        spacing(60)
        xalign 0.17
        yalign 0.36
        hbox:
            xalign 0.2
            yalign 0.4
            imagebutton:
                at custom_zoom(0.6)
                anchor(0.5,0.5)
                pos(0.2,0.5)
                xoffset 100
                yoffset 100
                idle "gui/yes_btn_idle.png"
                hover "gui/yes_btn_hover.png"
                action [SetField(persistent, "femboys", True), Return()]
                hovered SetScreenVariable("femboy_explainer", __("You will ENABLE femboy/futanari content."))
                unhovered SetScreenVariable("femboy_explainer", __("Hover over an option for more information."))
                mouse "hand"
            imagebutton:
                at custom_zoom(0.6)
                anchor(0.5,0.5)
                pos(0.2,0.5)
                xoffset 300
                yoffset 100
                idle "gui/no_btn_idle.png"
                hover "gui/no_btn_hover.png"
                action [SetField(persistent, "femboys", False), Return()]
                hovered SetScreenVariable("femboy_explainer", __("You will DISABLE femboy/futanari content."))
                unhovered SetScreenVariable("femboy_explainer", __("Hover over an option for more information."))
                mouse "hand"
    key "K_RETURN" action [SetField(persistent, "femboys", True), Return()]

screen set_jumpscares():
    default jumpscares_explainer = __("Hover over an option for more information.")

    modal True
    add "images/BGs/maintitlebg.jpg" at mm_bg_anim
    add "images/pngs/set_prefs_bg.png"
    text _("There are (not many) jumpscares in this game.") style "name_input_text_1stline" xalign 0.15 yalign 0.2
    text _("I don't want to give anyone an unsolicited heart attack.") style "name_input_text_1stlinealt" xalign 0.17 yalign 0.25
    text _("Would you like to see a fluffy duck instead?") style "name_input_text_2ndline" xalign 0.19 yalign 0.35

    text "[jumpscares_explainer!t]":
        style "name_input_text_3rdline"
        xalign 0.21
        yalign 0.57
    text _("(you can change this at any time in the options menu)") style "name_input_text_4thline" xalign 0.23 yalign 0.6

    hbox:
        xalign 0.2
        yalign 0.4
        imagebutton:
            at custom_zoom(0.6)
            anchor(0.5,0.5)
            pos(0.2,0.5)
            xoffset 100
            yoffset 100
            idle "gui/yes_btn_idle.png"
            hover "gui/yes_btn_hover.png"
            action [SetField(persistent, "jumpscares", False), Return()]
            hovered SetScreenVariable("jumpscares_explainer", __("You will see a fluffy duck instead of jumpscares."))
            unhovered SetScreenVariable("jumpscares_explainer", __("Hover over an option for more information."))
            mouse "hand"
        imagebutton:
            at custom_zoom(0.6)
            anchor(0.5,0.5)
            pos(0.2,0.5)
            xoffset 300
            yoffset 100
            idle "gui/no_btn_idle.png"
            hover "gui/no_btn_hover.png"
            action [SetField(persistent, "jumpscares", True), Return()]
            hovered SetScreenVariable("jumpscares_explainer", __("You will experience the jumpscares as intended."))
            unhovered SetScreenVariable("jumpscares_explainer", __("Hover over an option for more information."))
            mouse "hand"

    key "K_RETURN" action [SetField(persistent, "jumpscares", True), Return()]

screen gallery_unlock_screen():
    modal True
    default focus = "input_pass"
    add "images/pngs/set_prefs_bg.png"
    text _("Enter the password :)") style "name_input_text" xalign 0.15 yalign 0.3
    text _("(Get it on Discord or the game's Steam forum)") style "name_input_text" xalign 0.12 yalign 0.35 size 27 color "#b8b8b8"
    hbox:
        xalign 0.2
        yalign 0.4
        input id "input_pass" value VariableInputValue("persistent.pp") length 20 style "name_input_input"
        imagebutton:
            at custom_zoom(0.6)
            anchor(0.5,0.5)
            pos(0.2,0.5)
            xoffset 80
            yoffset -10
            idle "gui/yes_btn_idle.png"
            hover "gui/yes_btn_hover.png"
            action [Function(unlock_gallery_wpass), Hide("gallery_unlock_screen")]
            mouse "hand"
        imagebutton:
            at custom_zoom(0.6)
            anchor(0.5,0.5)
            pos(0.2,0.5)
            xoffset 80
            yoffset -10
            idle "gui/no_btn_idle.png"
            hover "gui/no_btn_hover.png"
            action Hide("gallery_unlock_screen")
            mouse "hand"
    key "K_RETURN" action [Function(unlock_gallery_wpass), Hide("gallery_unlock_screen")]

screen jump_to_content:
    modal True
    add "images/BGs/maintitlebg.jpg" at mm_bg_anim
    add "images/pngs/set_prefs_bg.png"
    text _("Do you want to start a new game, or jump to new content?") style "name_input_text" xalign 0.5 yalign 0.3
    hbox:
        xalign 0.5
        yalign 0.2
        textbutton _("New Game"):
            action [Return()]
        textbutton _("Jump to episode 6"):
            action [Return()]

screen end_screen():
    on "show" action renpy.transition(dissolve)

    add "black"
    add "suzie_fireplace_playful":
        xalign 0.5
        yalign 0.5
        zoom 0.6
    add "images/pngs/radial_fade_to_black.png":
        alpha 0.5
    button:
        anchor (0, 0)
        pos (0, 0)
        xysize (1.0, 1.0)
        action Return()

    imagebutton:
        at smaller_logo
        at transform:
            zoom 0.5
        anchor (0.5, 0.5)
        pos(0.08,0.1)
        idle "images/pngs/bcglogo.png"
        hover "images/pngs/bcglogo.png"
        action OpenURL("https://store.steampowered.com/publisher/bcg")
        hovered SetLocalVariable("logo_hover", True)
        unhovered SetLocalVariable("logo_hover", False)
        mouse "hand"
        if logo_hover:
            at pulse_logo

    hbox:
        xalign 0.6
        yalign 0.25
        imagebutton:
            at custom_zoom(1)
            yalign 0.5
            xalign 1.0
            idle "gui/steam_logo_idle.png"
            hover "gui/steam_logo_hover.png"
            action OpenURL("https://store.steampowered.com/app/2857910/Moonripple_Lake/")
            mouse "hand"
    add "gui/arrow_bent.png":
        zoom 0.3
        rotate 230
        yzoom -1
        xzoom -1

    hbox:
        xalign 0.5
        yalign 0.15
        text _("Please ") style "support_feedback_text"
        text _("consider ") style "support_feedback_text_accent"
        text _("leaving ") style "support_feedback_text"
        text _("a review!") style "support_feedback_text_accent"

    hbox:
        xalign 0.35
        yalign 1.0
        vbox:
            text _("Be sure to join ") style "support_feedback_text"
            text _("the community ") style "support_feedback_text_accent" yoffset -50
            text _("as well!") style "support_feedback_text" yoffset -100 xoffset -40
        add "gui/arrow.png":
            yalign 0.3
            zoom 0.6
            rotate(42)

    imagebutton:
        anchor(0.5,0.5)
        pos(0.7,0.79)
        at custom_zoom(1.1)
        idle "gui/discord_logo_full_btn.png"
        hover "gui/discord_logo_full_btn_hover.png"
        action OpenURL("https://discord.gg/xSgTSJ3tA9")
        mouse "hand"

    textbutton _("Continue...") style "continue_button_end_screen":
        xalign 1.0
        yalign 0.5
        mouse "hand"
        action Return()

screen show_text_title(textinput, fadeoutafter=2):
    modal True
    default time_left = fadeoutafter

    timer fadeoutafter action [Return()]

    add "images/pngs/radial_fade_to_black.png" at fade_to_nothing():
        xalign 1.0
        zoom 1.2
        yalign 0.5
        alpha 1.0
    text _("A week") style "line1st_screentitle" xpos 0.05 ypos 0.15
    text _("later...") style "line1st_screentitle" xpos 0.05 ypos 0.4
    button:
        anchor (0, 0)
        pos (0, 0)
        xysize (1.0, 1.0)
        action Return()

screen gallery_navigation:
    imagebutton:
        at custom_zoom(0.8)
        xoffset 1100
        yoffset 150
        idle "images/freeroam_images/patron_unlock_idle.png"
        hover "images/freeroam_images/patron_unlock_hover.png"
        action Show("gallery_unlock_screen",transition=dissolve)
        mouse "hand"

    vbox:
        yoffset 30
        hbox:
            style_prefix "gallery"
            spacing 50
            textbutton _("EP1") action ShowMenu("gallery_ep1") mouse "hand"
            textbutton _("EP2") action ShowMenu("gallery_ep2") mouse "hand"
            textbutton _("EP3") action ShowMenu("gallery_ep3") mouse "hand"
            textbutton _("EP4") action ShowMenu("gallery_ep4") mouse "hand"
            textbutton _("EP5") action ShowMenu("gallery_ep5") mouse "hand"
            textbutton _("EP6") action ShowMenu("gallery_ep6") mouse "hand"

        hbox:
            xalign 0.5
            style_prefix "gallery"
            textbutton _("Return"):
                action ShowMenu("gallery_mode_select")
                mouse "hand"

screen scenes_navigation:
    vbox:
        yoffset 30
        hbox:
            style_prefix "gallery"
            spacing 50
            textbutton _("EP1-3") action ShowMenu("scenes_0") mouse "hand"
            textbutton _("EP4") action ShowMenu("scenes_1") mouse "hand"
            textbutton _("EP5") action ShowMenu("scenes_2") mouse "hand"
            textbutton _("EP6") action ShowMenu("scenes_3") mouse "hand"

        hbox:
            xalign 0.5
            style_prefix "gallery"
            textbutton _("Return"):
                action ShowMenu("gallery_mode_select")
                mouse "hand"

screen specials_navigation:
    vbox:
        yoffset 30
        hbox:
            style_prefix "gallery"
            spacing 50

        hbox:
            xalign 0.5
            style_prefix "gallery"
            textbutton _("Return"):
                action ShowMenu("gallery_mode_select")
                mouse "hand"

screen fan_art_navigation:
    vbox:
        yoffset 30
        hbox:
            style_prefix "gallery"
            spacing 40

        hbox:
            xalign 0.5
            style_prefix "gallery"
            textbutton _("Return"):
                action ShowMenu("gallery_mode_select")
                mouse "hand"

screen gallery_mode_select:
    tag menu
    add "pinboard_gallery_bg"
    add "gui/gm_specials.png" xpos 400 ypos 760
    add "gui/gm_polaroids.png" xpos 260 ypos 180
    add "gui/gm_scenes.png" xpos 1180 ypos 180

    imagebutton:
        at custom_zoom(0.5)
        anchor(0.5,0.5)
        pos(0.35,0.35)
        idle "gui/polaroid_arrangement_idle.png"
        hover "gui/polaroid_arrangement_hover.png"
        action ShowMenu("gallery_ep1")
        mouse "hand"

    imagebutton:
        at custom_zoom(0.45)
        anchor(0.5,0.5)
        pos(0.62,0.37)
        idle "gui/scene_cut_idle.png"
        hover "gui/scene_cut_hover.png"
        action ShowMenu("scenes_0")
        mouse "hand"

    imagebutton:
        at custom_zoom(0.4)
        anchor(0.5,0.5)
        pos(0.5,0.7)
        idle "gui/specials_idle.png"
        hover "gui/specials_hover.png"
        action ShowMenu("specials_0")
        mouse "hand"

    style_prefix "gallery"
    textbutton _("Return"):
        xalign 0.5
        ypos 980
        action Return()
        mouse "hand"

screen phone_screen():
    modal True

    frame:
        style "phone_frame"
        at transform:
            on show:
                yoffset 1080
                easein_back 0.5 yoffset 90
            on hide:
                yoffset 120
                easeout_back 0.5 yoffset 1440
        vbox:
            if player_phone.current_screen == "apps":
                xoffset 220
                yoffset 300
                spacing 10

                textbutton _("Messages") action [SetField(player_phone, "current_screen", "sms"), Return()]
                textbutton _("Close") action Hide("phone_screen")

            elif player_phone.current_screen == "sms":
                xoffset 220
                yoffset 300
                spacing 10

                text _("Messages Screen")
                textbutton _("Back") action [SetField(player_phone, "current_screen", "apps"), Return()]

screen conversation_screen(sender):
    viewport:
        draggable True
        mousewheel True
        scrollbars "vertical"

        vbox:
            for message in player_phone.conversations[sender]:
                text "[message['content']]":
                    xalign (1.0 if message["is_player"] else 0.0)
                    color ("#00ff00" if message["is_player"] else "#ffffff")

    textbutton _("Back"):
        action SetField(player_phone, "current_conversation", None)

screen quickreact_prompt(label_name):
    modal True
    default time_left = 1.0

    timer 1.25 action Return()

    add "gui/button_bg_idle.png":
        xalign 0.5
        yalign 0.5
        zoom 0.6
        yoffset 10
        alpha 0.9
        xzoom 0.6
    textbutton _("Catch [persistent.sname]!") style "quickreact_button":
        action Jump(label_name)
        mouse "hand"
        xalign 0.5
        yalign 0.5

screen quests_screen():
    modal True

    add "gui/quests_pad.png" at transform:
        xalign 0.0
        yalign 0.5
        zoom 1.2
        on show:
            yoffset 500
            alpha 0
            parallel:
                easeout_back 0.1 alpha 1
            parallel:
                easein_back 0.35 yoffset 80
        on hide:
            yoffset 80
            alpha 1
            parallel:
                easeout_back 0.35 yoffset 500
            parallel:
                easeout_back 0.1 alpha 0

    frame:
        background None
        xalign 0.33
        yalign 0.45
        xysize (500, 600)
        at transform:
            on show:
                yoffset 500
                alpha 0
                parallel:
                    easeout_back 0.1 alpha 1
                parallel:
                    easein_back 0.35 yoffset 80
            on hide:
                yoffset 80
                alpha 1
                parallel:
                    easeout_back 0.35 yoffset 500
                parallel:
                    easeout_back 0.1 alpha 0

        if current_quests:
            vbox:
                yalign 0.0
                spacing 20
                for quest_title, quest_description in current_quests.items():
                    $ _ru_qt, _ru_qd = _ru_translate_quest(quest_title, quest_description)
                    text "• " + _ru_qt style "quest_title_text"
                    text _ru_qd style "quest_description_text"

        else:
            text _("All done!") style "no_quests_text"

    imagebutton:
        at transform:
            zoom 1
            xzoom -1
            matrixcolor TintMatrix("#00000010")
            on show:
                alpha 0
                yoffset 500
                parallel:
                    ease 0.2 alpha 1
                parallel:
                    easein_back 0.35 yoffset 80
            on hide:
                alpha 1
                parallel:
                    easeout_back 0.35 yoffset 500
        anchor (0.5, 0.5)
        pos(0.55, 0.5)
        idle "gui/no_btn_idle.png"
        hover "gui/no_btn_hover.png"
        action Hide("quests_screen")
        mouse "hand"

screen option_prompt(prompt="Placeholder prompt",x=0.1,y=0.6):
    modal False
    $ _ru_prompt = _ru_translate_prompt(prompt)
    text "[_ru_prompt]" style "option_prompt_text":
        xalign x
        yalign y

screen nvl_phonetext(dialogue):
    style_prefix None

    $ previous_d_who = None
    for id_d, d in enumerate(dialogue):
        if d.who == None:
            text d.what:
                    xpos -335
                    ypos 0.0
                    xsize 350
                    text_align 0.5
                    italic True
                    size 5
                    slow_cps False
                    id d.what_id
                    if d.current:
                        at message_narrator
        else:
            if d.who and phone_mode == "default":
                $ message_frame = "phone_send_frame.png"
            elif d.who == MC_GF and phone_mode == "gf":
                $ message_frame = "phone_send_frame.png"
            else:
                $ message_frame = "phone_received_frame.png"

            hbox:
                spacing 20
                xfill True
                if d.who == MC and phone_mode == "default":
                    xalign 1.0
                    xoffset 10
                    box_reverse True
                elif d.who == MC_GF and phone_mode == "gf":
                    xalign 1.0
                    box_reverse True
                else:
                    xalign 0.0

                if previous_d_who != d.who:
                    if d.who == MC:
                        $ message_icon = "images/phone/anon_profile_pic_alt.png"
                    elif d.who == MC_GF:
                        $ message_icon = "images/phone/suzie_profile_pic.png"
                    elif d.who in ("Cee", "Си"):
                        $ message_icon = "images/phone/cee_profile_pic.png"
                    elif d.who in ("Madelynn", "Мэделин"):
                        $ message_icon = "images/phone/madelynn_profile_pic.png"
                    elif d.who in ("Trevor", "Тревор"):
                        $ message_icon = "images/phone/trevor_profile_pic.png"
                    elif d.who in ("Drago", "Драго"):
                        $ message_icon = "images/phone/drago_profile_pic.png"
                    else:
                        $ message_icon = "phone_received_icon.png"
                    add message_icon:
                        if d.current:
                            at message_appear_icon()
                        if d.who == MC and phone_mode == "default":
                            at transform:
                                xoffset -10
                        elif d.who == [persistent.sname] and phone_mode == "gf":
                            at transform:
                                xoffset -10

                else:
                    null width 80

                vbox:
                    yalign 1.0
                    if d.who == [persistent.aname]:
                        xalign 1.0
                    else:
                        xalign 0
                    if d.who != [persistent.aname] and previous_d_who != d.who:
                        text d.who:
                            font "fonts/Roboto-Bold.TTF"

                    frame:
                        padding (10, 15)
                        background Frame(message_frame, 30,30,30,30)
                        xmaximum 300

                        text d.what:
                            pos (0,0)
                            xsize 310
                            slow_cps False
                            font "fonts/Roboto-Bold.TTF"
                            size 24

                            if d.who == MC:
                                color "#FFF"
                                text_align 0.0
                                xpos 10
                                outlines([ (1, "#ea840000", 0, 0) ])
                                if id_d == len(dialogue) - 1:
                                    slow_cps True
                                else:
                                    slow_cps False
                            elif d.who == MC_GF and phone_mode == "default":
                                color "#000"
                                text_align 0.0
                                xpos 10
                                outlines([ (1, "#ea840000", 0, 0) ])
                            elif d.who == MC_GF and phone_mode == "gf":
                                color "#fff"
                                text_align 0.0
                                xpos 10
                                outlines([ (1, "#ea840000", 0, 0) ])
                                if anon_sending_messages_from_gf_phone:
                                    if id_d == len(dialogue) - 1:
                                        slow_cps True
                                    else:
                                        slow_cps False
                            elif d.who in ("Cee", "Си"):
                                color "#000"
                                text_align 0.0
                                xpos 10
                                outlines([ (1, "#ea840000", 0, 0) ])
                            else:
                                outlines([ (1, "#ea840000", 0, 0) ])
                                color "#000"
                                xpos 10
                                text_align 0.0


                            id d.what_id
        $ previous_d_who = d.who

label after_load:
    $ renpy.change_language("russian")
    return

label splashscreen:
    $ renpy.change_language("russian")
    return
