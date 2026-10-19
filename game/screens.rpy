################################################################################
## Inicialización
################################################################################

init offset = -1


################################################################################
## Estilos
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    left_bar Frame("gui/slider/horizontal_[prefix_]left.png", gui.slider_borders, tile=gui.slider_tile)
    right_bar Frame("gui/slider/horizontal_[prefix_]right.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"
    thumb_offset 17

style vslider:
    xsize gui.slider_size
    top_bar Frame("gui/slider/vertical_[prefix_]top.png", gui.vslider_borders, tile=gui.slider_tile)
    bottom_bar Frame("gui/slider/vertical_[prefix_]bottom.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"
    thumb_offset 17


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## Pantallas internas del juego
################################################################################


## Pantalla de diálogo #########################################################
##
## La pantalla de diálogo muestra el diálogo al jugador. Acepta dos parámetros,
## 'who' y 'what', es decir, el nombre del personaje que habla y el texto que ha
## de ser mostrado respectivamente. (El parámetro 'who' puede ser 'None' si no
## se da ningún nombre.)
##
## Esta pantalla debe crear un texto visualizable con id "what" que Ren'Py usa
## para gestionar la visualización del texto. Puede crear también visualizables
## con id "who" y id "window" para aplicar propiedades de estilo.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## Si hay una imagen lateral, la muestra encima del texto. No la muestra en
    ## la variante de teléfono - no hay lugar.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Permite que el 'namebox' pueda ser estilizado en el objeto 'Character'.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Pantalla de introducción de texto ###########################################
##
## Pantalla usada para visualizar 'renpy.input'. El parámetro 'prompt' se usa
## para pasar el texto presentado.
##
## Esta pantalla debe crear un displayable 'input' con id "input" para aceptar
## diversos parámetros de entrada.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Pantalla de menú ############################################################
##
## Esta pantallla presenta las opciones internas al juego de la sentencia
## 'menu'. El parámetro único, 'items', es una lista de objetos, cada uno los
## campos 'caption' y 'action'.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Pantalla de menú rápido #####################################################
##
## El menú rápido se presenta en el juego para ofrecer fácil acceso a los menus
## externos al juego.

screen quick_menu():

    ## Asegura que esto aparezca en la parte superior de otras pantallas.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"
            style "quick_menu"

            textbutton _("◀ Atrás") action Rollback()
            textbutton _("📜 Historial") action ShowMenu('history')
            textbutton _("⏩ Saltar") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("▶ Auto") action Preference("auto-forward", "toggle")
            textbutton _("💾 Guardar") action ShowMenu('save')
            textbutton _("⚡ Rápido") action QuickSave()
            textbutton _("📂 Cargar") action QuickLoad()
            textbutton _("⚙️ Opciones") action ShowMenu('preferences')


## Este código asegura que la pantalla 'quick_menu' se muestra en el juego,
## mientras el jugador no haya escondido explícitamente la interfaz.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.98
    yalign 0.99
    spacing 4

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Principal y Pantalla de menu del juego.
################################################################################

## Pantalla de navegación ######################################################
##
## Esta pantalla está incluída en el menú principal y los menús del juego y
## ofrece navegación a los otros menús y al inicio del juego.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("🌸 Comenzar") action Start()

        else:

            textbutton _("📜 Historial") action ShowMenu("history")

            textbutton _("💾 Guardar") action ShowMenu("save")

        textbutton _("📂 Cargar") action ShowMenu("load")

        textbutton _("🏆 Galería de Finales") action Show("endings_gallery_modal")

        textbutton _("⚙️ Opciones") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("Finaliza repetición") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("🏠 Menú principal") action MainMenu()

        textbutton _("📖 Acerca de") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## La ayuda no es necesaria ni relevante en dispositivos móviles.
            textbutton _("❓ Ayuda") action ShowMenu("help")

        if renpy.variant("pc"):

            ## El botón de salida está prohibido en iOS y no es necesario en
            ## Android y Web.
            textbutton _("🚪 Salir") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    xsize gui.navigation_button_width
    ysize 50
    padding (22, 10)
    background Frame("gui/button/navigation_idle_background.png", 16, 8, 16, 8)
    hover_background Frame("gui/button/navigation_hover_background.png", 16, 8, 16, 8)
    selected_background Frame("gui/button/navigation_selected_background.png", 16, 8, 16, 8)

style navigation_button_text:
    size 18
    bold True
    color "#ffffff"
    hover_color "#ffd13b"
    selected_color "#ffe680"
    outlines [(2, "#24031a", 0, 0)]
    yalign 0.5


## Pantalla del menú principal #################################################
##
## Usado para mostrar el menú principal cuando Ren'Py arranca.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
    tag menu

    # Fondo animado con suave movimiento cinemático
    add "images/bg_courtyard.png" at bg_menu_drift

    # Capa de partículas de pétalos de cerezo cayendo
    add "sakura_petals"

    # Gradiente sutil para legibilidad cinematográfica
    add "#1a031955"

    # Tarjeta de Título Anime Rom-Com (Lado Izquierdo Superior)
    frame:
        xpos 80
        ypos 60
        background None
        vbox:
            spacing 8

            frame:
                background Frame("images/ui/pill_stat_tlr.png", 24, 12, 24, 12)
                padding (18, 8)
                text "🌸 NOVELA VISUAL INTERACTIVA • ROM-COM & MISTERIO 🌸" size 16 bold True color "#ffd13b" outlines [(2, "#24031a", 0, 0)]

            text "CRÓNICAS DEL INSTITUTO SAKURA" at menu_title_pulse size 46 bold True color "#ff85c0" outlines [(4, "#24031a", 0, 0), (2, "#ff4d6d", 0, 0)]
            text "🏮 ¡Líos en el Festival Cultural! 🏮" size 26 bold True color "#ffe680" outlines [(3, "#190212", 0, 0)]
            text "«Entre 3 heroínas y 3 tentaciones prohibidas... ¿con quién compartirás el clímax?»" size 16 italic True color "#ffffff" outlines [(2, "#190212", 0, 0)]

            $ finales_desb = len(persistent.finales_desbloqueados or set())
            frame:
                background Frame("images/ui/panel_inner_tlr.png", 20, 10, 20, 10)
                padding (16, 7)
                hbox:
                    spacing 8
                    add "images/ui/icon_tlr_heart.png" zoom 0.65 yalign 0.5
                    text "🏆 Colección de Finales: [finales_desb] / 7 Desbloqueados" size 17 bold True color "#5dfdcb" outlines [(2, "#190212", 0, 0)] yalign 0.5

    # Panel de Botones de Navegación Estilizados (Lado Izquierdo Inferior)
    frame:
        xpos 80
        ypos 430
        background None
        vbox:
            spacing 13

            textbutton "🌸 Comenzar Historia":
                action Start()
                background Frame("images/ui/btn_pink_idle.png", 24, 14, 24, 14)
                hover_background Frame("images/ui/btn_pink_hover.png", 24, 14, 24, 14)
                padding (32, 13)
                text_size 21
                text_bold True
                text_color "#ffffff"
                text_outlines [(2, "#4a0528", 0, 0)]

            textbutton "📂 Cargar Partida":
                action ShowMenu("load")
                background Frame("images/ui/btn_cyan_idle.png", 24, 14, 24, 14)
                hover_background Frame("images/ui/btn_cyan_hover.png", 24, 14, 24, 14)
                padding (32, 13)
                text_size 21
                text_bold True
                text_color "#ffffff"
                text_outlines [(2, "#062b45", 0, 0)]

            textbutton "🏆 Galería de Finales & Jukebox":
                action Show("endings_gallery_modal")
                background Frame("images/ui/btn_gold_idle.png", 24, 14, 24, 14)
                hover_background Frame("images/ui/btn_gold_hover.png", 24, 14, 24, 14)
                padding (32, 13)
                text_size 21
                text_bold True
                text_color "#2b0318"
                text_hover_color "#000000"

            textbutton "⚙️ Opciones & Sonido":
                action ShowMenu("preferences")
                background Frame("images/ui/btn_purple_idle.png", 24, 14, 24, 14)
                hover_background Frame("images/ui/btn_purple_hover.png", 24, 14, 24, 14)
                padding (32, 13)
                text_size 21
                text_bold True
                text_color "#ffffff"
                text_outlines [(2, "#2d0645", 0, 0)]

            textbutton "📖 Acerca de":
                action ShowMenu("about")
                background Frame("images/ui/btn_dark_idle.png", 24, 14, 24, 14)
                hover_background Frame("images/ui/btn_dark_hover.png", 24, 14, 24, 14)
                padding (32, 11)
                text_size 19
                text_bold True
                text_color "#e0e0e0"

            if renpy.variant("pc"):
                textbutton "🚪 Salir":
                    action Quit(confirm=False)
                    background Frame("images/ui/btn_dark_idle.png", 24, 14, 24, 14)
                    hover_background Frame("images/ui/btn_pink_hover.png", 24, 14, 24, 14)
                    padding (32, 10)
                    text_size 18
                    text_color "#bbbbbb"

    # Tarjeta de Personajes en la esquina inferior derecha
    frame:
        xalign 0.95
        yalign 0.92
        background Frame("images/ui/panel_inner_tlr.png", 24, 18, 24, 18)
        padding (20, 14)
        vbox:
            spacing 6
            text "✨ Heroínas del Instituto Sakura ✨" size 15 bold True color "#ffe680" outlines [(2, "#24031a", 0, 0)] xalign 0.5
            hbox:
                spacing 8
                add "images/thumb_akane.png" zoom 0.85
                add "images/thumb_yuki.png" zoom 0.85
                add "images/thumb_hana.png" zoom 0.85
                add "images/thumb_kuroe.png" zoom 0.85
                add "images/thumb_mirei.png" zoom 0.85
                add "images/thumb_reina.png" zoom 0.85


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Pantalla del menú del juego #################################################
##
## Esto distribuye la estructura de base del menú del juego. Es llamado con el
## título de la pantalla y presenta el fondo, el título y la navegación.
##
## El parámetro 'scroll' puede ser 'None', "viewport" o "vpgrid". Se usa esta
## pantalla con uno o más elementos, que son transcluídos (situados) en su
## interior.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reservar espacio para la sección de navegación.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("◀ Volver"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 140

style game_menu_label_text:
    size 48
    bold True
    color "#ff85c0"
    outlines [(3, "#24031a", 0, 0)]
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -35
    xsize gui.navigation_button_width
    ysize 50
    padding (22, 10)
    background Frame("gui/button/navigation_idle_background.png", 16, 8, 16, 8)
    hover_background Frame("gui/button/navigation_hover_background.png", 16, 8, 16, 8)

style return_button_text:
    size 18
    bold True
    color "#5dfdcb"
    hover_color "#ffffff"
    outlines [(2, "#24031a", 0, 0)]
    yalign 0.5


## Pantalla 'acerca de' ########################################################
##
## Esta pantalla da información sobre los créditos y el copyright del juego y de
## Ren'Py.
##
## No hay nada especial en esta pantalla y por tanto sirve también como ejemplo
## de cómo hacer una pantalla personalizada.

screen about():

    tag menu

    use game_menu(_("Acerca de"), scroll="viewport"):

        vbox:
            spacing 20
            xsize 1320

            # Banner de Título
            frame:
                style "about_card_frame"
                vbox:
                    spacing 8
                    text "🌸 CRÓNICAS DEL INSTITUTO SAKURA: ¡LÍOS EN EL FESTIVAL CULTURAL! 🌸" size 24 bold True color "#ff85c0" outlines [(3, "#24031a", 0, 0)]
                    text "Edición Definitiva • Director's Cut v2.0" size 18 bold True color "#ffd13b" outlines [(2, "#24031a", 0, 0)]
                    text "«Un simulador interactivo de comedia romántica escolar con misterio, heroínas tsundere, kuudere, genki y la tentación del Darkness Club.»" size 16 italic True color "#e2e8f0"

            # Fila de 2 Tarjetas Informativas
            hbox:
                spacing 24

                frame:
                    style "about_card_frame"
                    xsize 648
                    vbox:
                        spacing 10
                        text "✨ Características Principales" size 20 bold True color "#5dfdcb" outlines [(2, "#190212", 0, 0)]
                        text "• 3 Heroínas Principales: Akane (Tsundere), Yuki (Kuudere), Hana (Genki)" size 16 color "#ffffff"
                        text "• 3 Heroínas Darkness Prohibidas: Kuroe (Gótica), Mirei (Enfermera), Reina (Gyaru)" size 16 color "#ffffff"
                        text "• 7 Finales Únicos y Desbloqueables con Pantalla de Trofeos" size 16 color "#ffffff"
                        text "• HUD en Vivo de Afinidad, Tentación, Ingenio, Reputación y Festival" size 16 color "#ffffff"
                        text "• Sistema de Elecciones Bajo Presión con Temporizador de Pánico" size 16 color "#ffffff"
                        text "• Transiciones de Ubicación Inmersivas y Reacciones Emocionales" size 16 color "#ffffff"

                frame:
                    style "about_card_frame"
                    xsize 648
                    vbox:
                        spacing 10
                        text "⚙️ Información Técnica & Créditos" size 20 bold True color "#ffd13b" outlines [(2, "#190212", 0, 0)]
                        text "• Motor: Ren'Py [renpy.version_only] (Python 3)" size 16 color "#ffffff"
                        text "• Interfaz: Glassmorphism Moderno con Acentos Neón" size 16 color "#ffffff"
                        text "• Audio: Banda sonora original y efectos remasterizados" size 16 color "#ffffff"
                        text "• Licencia: MIT / Ren'Py Engine Open Source" size 16 color "#ffffff"
                        null height 8
                        text _("Hecho con cariño para los amantes de las novelas visuales anime.") size 15 italic True color "#ffccf2"


style about_card_frame is empty:
    padding (24, 20)
    background Frame("gui/card_pref.png", 20, 20, 20, 20)

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Pantallas de carga y grabación ##############################################
##
## Estas pantallas permiten al jugador grabar el juego y cargarlo de nuevo. Como
## comparten casi todos los elementos, ambas están implementadas en una tercera
## pantalla: 'file_slots'.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Guardar"))


screen load():

    tag menu

    use file_slots(_("Cargar"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Página {}"), auto=_("Grabación automática"), quick=_("Grabación rápida"))

    use game_menu(title):

        fixed:

            ## Esto asegura que 'input' recibe el evento 'enter' antes que otros
            ## botones.
            order_reverse True

            ## El nombre de la pagina, se puede editar haciendo clic en el
            ## botón.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## La cuadrícula de huecos de guardado.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox:
                            spacing 4

                        # Cabecera de la ranura (Número y botón eliminar)
                        hbox:
                            xfill True
                            ysize 26
                            text _("✦ Ranura [slot:02d]"):
                                style "slot_header_text"
                                yalign 0.5

                            if FileLoadable(slot):
                                textbutton _("✕"):
                                    action FileDelete(slot, confirm=True)
                                    style "slot_delete_button"
                                    yalign 0.5
                                    tooltip _("Eliminar archivo guardado")

                        # Área de miniatura con indicador de vacío o captura
                        fixed:
                            xsize config.thumbnail_width
                            ysize config.thumbnail_height
                            xalign 0.5

                            if FileLoadable(slot):
                                add FileScreenshot(slot) xalign 0.5 yalign 0.5
                            else:
                                frame:
                                    xfill True
                                    yfill True
                                    background "#12031a99"
                                    vbox:
                                        align (0.5, 0.5)
                                        spacing 4
                                        text _("✦ VACÍO ✦"):
                                            size 18
                                            bold True
                                            color "#783b82"
                                            xalign 0.5
                                            outlines [(2, "#18021c", 0, 0)]
                                        text _("Clic para guardar"):
                                            size 13
                                            color "#b085bd"
                                            italic True
                                            xalign 0.5

                        # Fecha y nombre de la partida
                        hbox:
                            xfill True
                            text FileTime(slot, format=_("{#file_time}%d/%m/%Y • %H:%M"), empty=_("—")):
                                style "slot_time_text"
                                yalign 0.5

                            text FileSaveName(slot):
                                style "slot_name_text"
                                yalign 0.5

                        key "save_delete" action FileDelete(slot)

            ## Botones de acceso a otras páginas
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing 8

                    textbutton _("◀") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("Auto") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("Rápido") action FilePage("quick")

                    ## range(1, 10) da los números del 1 al 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _("▶") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Subir Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Descargar Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_header_text is gui_text
style slot_delete_button is gui_button
style slot_delete_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5
    xalign 0.5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color
    bold True
    color "#ffd13b"
    size 22
    outlines [(2, "#24031a", 0, 0)]

style page_button:
    xsize 54
    ysize 42
    background Frame("gui/button/page_idle_background.png", 10, 6, 10, 6)
    hover_background Frame("gui/button/page_hover_background.png", 10, 6, 10, 6)
    selected_background Frame("gui/button/page_selected_background.png", 10, 6, 10, 6)

style page_button_text:
    size 16
    bold True
    color "#ffffff"
    hover_color "#5dfdcb"
    selected_color "#ffd13b"
    align (0.5, 0.5)
    outlines [(2, "#24031a", 0, 0)]

style slot_button:
    properties gui.button_properties("slot_button")
    padding (15, 12, 15, 12)

style slot_header_text:
    size 14
    bold True
    color "#ffd13b"
    outlines [(2, "#24031a", 0, 0)]

style slot_delete_button is gui_button:
    xsize 26
    ysize 26
    background Frame("gui/button/delete_idle_background.png", 6, 6, 6, 6)
    hover_background Frame("gui/button/delete_hover_background.png", 6, 6, 6, 6)

style slot_delete_button_text is gui_button_text:
    size 13
    bold True
    color "#ff85a2"
    hover_color "#ffffff"
    align (0.5, 0.5)

style slot_button_text:
    properties gui.text_properties("slot_button")

style slot_time_text:
    size 13
    bold True
    color "#5dfdcb"
    outlines [(2, "#190212", 0, 0)]

style slot_name_text:
    size 13
    color "#ffe680"
    outlines [(2, "#190212", 0, 0)]
    xalign 1.0


## Pantalla de preferencias ####################################################
##
## La pantalla de preferencias permite al jugador configurar el juego a su
## gusto.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Opciones"), scroll="viewport"):

        vbox:
            spacing 24
            xsize 1320

            hbox:
                spacing 28

                # Tarjeta 1: Pantalla y Velocidad de Lectura
                frame:
                    style "pref_glass_card"
                    vbox:
                        spacing 14
                        xfill True

                        text _("🖥️ Pantalla y Visualización"):
                            style "pref_section_title"

                        if renpy.variant("pc") or renpy.variant("web"):
                            hbox:
                                style_prefix "radio"
                                spacing 24
                                textbutton _("Ventana") action Preference("display", "window")
                                textbutton _("Pantalla completa") action Preference("display", "fullscreen")

                        null height 4

                        text _("⏩ Opciones de Salto"):
                            style "pref_section_title"

                        vbox:
                            style_prefix "check"
                            spacing 6
                            textbutton _("Saltar texto no visto") action Preference("skip", "toggle")
                            textbutton _("Continuar salto tras elecciones") action Preference("after choices", "toggle")
                            textbutton _("Omitir transiciones lentas") action InvertSelected(Preference("transitions", "toggle"))

                        null height 4

                        text _("⚡ Velocidad de Lectura"):
                            style "pref_section_title"

                        vbox:
                            style_prefix "slider"
                            spacing 8
                            label _("Velocidad de aparición del texto"):
                                style "slider_sub_label"
                            bar value Preference("text speed") style "pref_slider"

                            label _("Tiempo de autoavance"):
                                style "slider_sub_label"
                            bar value Preference("auto-forward time") style "pref_slider"

                # Tarjeta 2: Mezclador de Audio & Sonido
                frame:
                    style "pref_glass_card"
                    vbox:
                        spacing 14
                        xfill True

                        text _("🔊 Mezclador de Audio & Sonido"):
                            style "pref_section_title"

                        vbox:
                            style_prefix "slider"
                            spacing 10

                            label _("🎵 Volumen de Música"):
                                style "slider_sub_label"
                            bar value Preference("music volume") style "pref_slider"

                            label _("💥 Efectos de Sonido"):
                                style "slider_sub_label"
                            hbox:
                                spacing 12
                                bar value Preference("sound volume") style "pref_slider"
                                if config.sample_sound:
                                    textbutton _("▶ Probar"):
                                        action Play("sound", config.sample_sound)
                                        style "slider_test_button"

                            label _("🎙️ Voces de Personajes"):
                                style "slider_sub_label"
                            hbox:
                                spacing 12
                                bar value Preference("voice volume") style "pref_slider"
                                if config.sample_voice:
                                    textbutton _("▶ Probar"):
                                        action Play("voice", config.sample_voice)
                                        style "slider_test_button"

                        null height 8

                        frame:
                            background "#1f042ecc"
                            padding (14, 10)
                            xfill True
                            hbox:
                                align (0.5, 0.5)
                                spacing 14
                                textbutton _("🔇 Silenciar Todo el Audio"):
                                    action Preference("all mute", "toggle")
                                    style "mute_all_button"


style pref_glass_card is empty:
    xsize 640
    padding (26, 22)
    background Frame("gui/card_pref.png", 20, 20, 20, 20)

style pref_section_title is gui_text:
    color "#ffd13b"
    bold True
    size 20
    outlines [(2, "#24031a", 0, 0)]

style slider_sub_label is gui_text:
    color "#ffccf2"
    bold True
    size 16
    outlines [(1, "#190212", 0, 0)]

style pref_slider is slider:
    xsize 480
    ysize gui.slider_size

style slider_test_button is gui_button:
    xsize 96
    ysize 32
    background Frame("gui/button/quick_idle_background.png", 14, 6, 14, 6)
    hover_background Frame("gui/button/quick_hover_background.png", 14, 6, 14, 6)

style slider_test_button_text is gui_button_text:
    size 14
    bold True
    color "#5dfdcb"
    hover_color "#ffffff"
    align (0.5, 0.5)

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text:
    color "#ff9ebb"
    hover_color "#ffffff"

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    color "#ffd13b"
    bold True
    size 20
    outlines [(2, "#24031a", 0, 0)]
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")
    size 17
    bold True
    color "#e2e8f0"
    hover_color "#ffd13b"
    selected_color "#5dfdcb"
    outlines [(2, "#24031a", 0, 0)]

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")
    size 17
    bold True
    color "#e2e8f0"
    hover_color "#ffd13b"
    selected_color "#ff85c0"
    outlines [(2, "#24031a", 0, 0)]

style slider_slider:
    xsize 480

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 600


## Pantalla de historial #######################################################
##
## Esta pantalla presenta el historial de diálogo al jugador, almacenado en
## '_history_list'.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    predict False

    use game_menu(_("Historial"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            frame:
                style "history_card_frame"

                vbox:
                    spacing 6
                    xfill True

                    if h.who:
                        hbox:
                            spacing 8
                            yalign 0.5
                            text "✦" size 16 bold True color "#ffd13b" yalign 0.5
                            label h.who:
                                style "history_name"
                                substitute False
                                if "color" in h.who_args:
                                    text_color h.who_args["color"]

                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what:
                        style "history_text"
                        substitute False

                    if h.voice:
                        textbutton _("🔊 Reproducir Voz"):
                            action VoiceReplay(h.voice)
                            style "history_voice_button"

        if not _history_list:
            frame:
                style "history_card_frame"
                xalign 0.5
                text _("✦ El registro de diálogo está vacío por el momento. ¡Comienza a leer la historia! ✦"):
                    size 18
                    color "#ffd13b"
                    xalign 0.5


## Esto determina qué etiquetas se permiten en la pantalla de historial.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_card_frame is empty:
    xsize 1320
    xalign 0.5
    padding (24, 16, 24, 16)
    background Frame("gui/history_card.png", 16, 16, 16, 16)

style history_name is gui_label:
    left_padding 0
    top_padding 0

style history_name_text is gui_label_text:
    size 20
    bold True
    outlines [(2, "#24031a", 0, 0)]

style history_text is gui_text:
    size 18
    color "#f8fafc"
    outlines [(1, "#18021c", 0, 0)]
    line_spacing 4

style history_voice_button is gui_button:
    xsize 180
    ysize 32
    background Frame("gui/button/quick_idle_background.png", 14, 6, 14, 6)
    hover_background Frame("gui/button/quick_hover_background.png", 14, 6, 14, 6)

style history_voice_button_text is gui_button_text:
    size 14
    bold True
    color "#5dfdcb"
    hover_color "#ffffff"
    align (0.5, 0.5)

style history_window is empty
style history_label is gui_label
style history_label_text is gui_label_text:
    xalign 0.5


## Pantalla de ayuda ###########################################################
##
## Una pantalla que da información sobre el uso del teclado y el ratón. Usa
## otras pantallas con el contenido de la ayuda ('keyboard_help', 'mouse_help',
## y 'gamepad_help').

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Ayuda"), scroll="viewport"):

        vbox:
            spacing 24
            xsize 1320

            # Selector de Pestañas
            hbox:
                spacing 16
                textbutton _("⌨️ Teclado"):
                    action SetScreenVariable("device", "keyboard")
                    style "help_tab_button"
                    selected (device == "keyboard")

                textbutton _("🖱️ Ratón"):
                    action SetScreenVariable("device", "mouse")
                    style "help_tab_button"
                    selected (device == "mouse")

                if GamepadExists():
                    textbutton _("🎮 Mando"):
                        action SetScreenVariable("device", "gamepad")
                        style "help_tab_button"
                        selected (device == "gamepad")

            # Contenido según dispositivo en tarjeta de cristal
            frame:
                style "about_card_frame"
                xfill True
                vbox:
                    spacing 16
                    if device == "keyboard":
                        use keyboard_help
                    elif device == "mouse":
                        use mouse_help
                    elif device == "gamepad":
                        use gamepad_help


screen keyboard_help():

    vbox:
        spacing 14
        grid 2 6:
            spacing 18
            xfill True

            hbox:
                spacing 14
                yalign 0.5
                frame:
                    style "keycap_frame"
                    text "Intro / Espacio" style "keycap_text"
                text _("Avanza el diálogo y activa opciones.") color "#ffffff" size 16 yalign 0.5

            hbox:
                spacing 14
                yalign 0.5
                frame:
                    style "keycap_frame"
                    text "S" style "keycap_text"
                text _("Captura de pantalla instantánea.") color "#ffffff" size 16 yalign 0.5

            hbox:
                spacing 14
                yalign 0.5
                frame:
                    style "keycap_frame"
                    text "Tabulador" style "keycap_text"
                text _("Activa o desactiva el salto continuo.") color "#ffffff" size 16 yalign 0.5

            hbox:
                spacing 14
                yalign 0.5
                frame:
                    style "keycap_frame"
                    text "V" style "keycap_text"
                text _("Asistente accesible por voz.") color "#ffffff" size 16 yalign 0.5

            hbox:
                spacing 14
                yalign 0.5
                frame:
                    style "keycap_frame"
                    text "Ctrl" style "keycap_text"
                text _("Salto rápido mientras se mantenga presionado.") color "#ffffff" size 16 yalign 0.5

            hbox:
                spacing 14
                yalign 0.5
                frame:
                    style "keycap_frame"
                    text "Shift + A" style "keycap_text"
                text _("Menú de accesibilidad.") color "#ffffff" size 16 yalign 0.5

            hbox:
                spacing 14
                yalign 0.5
                frame:
                    style "keycap_frame"
                    text "Escape" style "keycap_text"
                text _("Abre o cierra el menú del juego.") color "#ffffff" size 16 yalign 0.5

            hbox:
                spacing 14
                yalign 0.5
                frame:
                    style "keycap_frame"
                    text "Av. Pág / Re. Pág" style "keycap_text"
                text _("Retrocede o avanza diálogos.") color "#ffffff" size 16 yalign 0.5

            hbox:
                spacing 14
                yalign 0.5
                frame:
                    style "keycap_frame"
                    text "Flechas" style "keycap_text"
                text _("Navega por la interfaz y opciones.") color "#ffffff" size 16 yalign 0.5

            hbox:
                spacing 14
                yalign 0.5
                frame:
                    style "keycap_frame"
                    text "Supr" style "keycap_text"
                text _("Elimina la partida guardada elegida.") color "#ffffff" size 16 yalign 0.5

            hbox:
                spacing 14
                yalign 0.5
                frame:
                    style "keycap_frame"
                    text "H" style "keycap_text"
                text _("Oculta la interfaz para ver el arte.") color "#ffffff" size 16 yalign 0.5

            hbox:
                spacing 14
                yalign 0.5
                frame:
                    style "keycap_frame"
                    text "F" style "keycap_text"
                text _("Alternar pantalla completa.") color "#ffffff" size 16 yalign 0.5


screen mouse_help():

    vbox:
        spacing 16
        hbox:
            spacing 16
            yalign 0.5
            frame:
                style "keycap_frame"
                text "Clic Izquierdo" style "keycap_text"
            text _("Avanza el diálogo y activa elecciones.") color "#ffffff" size 17 yalign 0.5

        hbox:
            spacing 16
            yalign 0.5
            frame:
                style "keycap_frame"
                text "Clic Derecho" style "keycap_text"
            text _("Abre o cierra el menú de pausa / opciones.") color "#ffffff" size 17 yalign 0.5

        hbox:
            spacing 16
            yalign 0.5
            frame:
                style "keycap_frame"
                text "Clic Medio" style "keycap_text"
            text _("Oculta la interfaz para contemplar la ilustración.") color "#ffffff" size 17 yalign 0.5

        hbox:
            spacing 16
            yalign 0.5
            frame:
                style "keycap_frame"
                text "Rueda Arriba" style "keycap_text"
            text _("Abre el historial de diálogo hacia atrás.") color "#ffffff" size 17 yalign 0.5

        hbox:
            spacing 16
            yalign 0.5
            frame:
                style "keycap_frame"
                text "Rueda Abajo" style "keycap_text"
            text _("Avanza hacia el diálogo siguiente.") color "#ffffff" size 17 yalign 0.5


screen gamepad_help():

    vbox:
        spacing 16
        hbox:
            spacing 16
            yalign 0.5
            frame:
                style "keycap_frame"
                text "Gatillo R / Botón A" style "keycap_text"
            text _("Avanza el diálogo y activa elecciones.") color "#ffffff" size 17 yalign 0.5

        hbox:
            spacing 16
            yalign 0.5
            frame:
                style "keycap_frame"
                text "Gatillo L / Botón LB" style "keycap_text"
            text _("Retrocede al diálogo anterior.") color "#ffffff" size 17 yalign 0.5

        hbox:
            spacing 16
            yalign 0.5
            frame:
                style "keycap_frame"
                text "D-Pad / Sticks" style "keycap_text"
            text _("Navega por la interfaz y opciones.") color "#ffffff" size 17 yalign 0.5

        hbox:
            spacing 16
            yalign 0.5
            frame:
                style "keycap_frame"
                text "Start / Botón B" style "keycap_text"
            text _("Accede al menú del juego.") color "#ffffff" size 17 yalign 0.5

        hbox:
            spacing 16
            yalign 0.5
            frame:
                style "keycap_frame"
                text "Botón Y" style "keycap_text"
            text _("Oculta la interfaz.") color "#ffffff" size 17 yalign 0.5

        null height 10

        textbutton _("⚙️ Calibrar Mando"):
            action GamepadCalibrate()
            style "help_tab_button"


style keycap_frame is empty:
    background Frame("gui/keycap.png", 10, 10, 10, 10)
    padding (12, 6)
    yminimum 38

style keycap_text:
    size 15
    bold True
    color "#ffd13b"
    outlines [(2, "#24031a", 0, 0)]
    align (0.5, 0.5)

style help_tab_button is gui_button:
    xsize 210
    ysize 44
    background Frame("gui/button/navigation_idle_background.png", 16, 8, 16, 8)
    hover_background Frame("gui/button/navigation_hover_background.png", 16, 8, 16, 8)
    selected_background Frame("gui/button/navigation_selected_background.png", 16, 8, 16, 8)

style help_tab_button_text is gui_button_text:
    size 17
    bold True
    color "#ffffff"
    hover_color "#5dfdcb"
    selected_color "#ffd13b"
    align (0.5, 0.5)



################################################################################
## Pantallas adicionales
################################################################################


## Pantalla de confirmación ####################################################
##
## Ren'Py llama la pantalla de confirmación para presentar al jugador preguntas
## de sí o no.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    modal True
    zorder 200
    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:
        xalign 0.5
        yalign 0.5
        background Frame("gui/frame.png", 28, 28, 28, 28)
        padding (50, 36)

        vbox:
            xalign 0.5
            spacing 22

            hbox:
                xalign 0.5
                spacing 10
                add "images/ui/icon_tlr_heart.png" zoom 0.85 yalign 0.5
                text "✦ AVISO DEL INSTITUTO SAKURA ✦" size 16 bold True color "#ffd13b" outlines [(2, "#24031a", 0, 0)] yalign 0.5

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            null height 4

            hbox:
                xalign 0.5
                spacing 36

                textbutton _("✓ Sí, continuar"):
                    action yes_action
                    background Frame("images/ui/btn_pink_idle.png", 24, 14, 24, 14)
                    hover_background Frame("images/ui/btn_pink_hover.png", 24, 14, 24, 14)
                    padding (28, 12)
                    text_size 20
                    text_bold True
                    text_color "#ffffff"
                    text_outlines [(2, "#4a0528", 0, 0)]

                textbutton _("✕ Cancelar"):
                    action no_action
                    background Frame("images/ui/btn_dark_idle.png", 24, 14, 24, 14)
                    hover_background Frame("images/ui/btn_cyan_hover.png", 24, 14, 24, 14)
                    padding (28, 12)
                    text_size 20
                    text_bold True
                    text_color "#e0e0e0"

    ## Clic derecho o escape responden "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Pantalla del indicador de salto #############################################
##
## La pantalla de indicador de salto se muestra para indicar que se está
## realizando el salto.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Saltando")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## Esta transformación provoca el parpadeo de las flechas una tras otra.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## Es necesario usar un tipo de letra que contenga el glifo BLACK RIGHT-
    ## POINTING SMALL TRIANGLE.
    font "DejaVuSans.ttf"


## Pantalla de notificación ####################################################
##
## La pantalla de notificación muestra al jugador un mensaje. (Por ejemplo, con
## un guardado rápido o una captura de pantalla.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## Pantalla NVL ################################################################
##
## Esta pantalla se usa para el diálogo y los menús en modo NVL.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Presenta el diálogo en una 'vpgrid' o una 'vbox'.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Presenta el menú, si lo hay. El menú puede ser presentado
        ## incorrectamente si 'config.narrator_menu' está ajustado a 'True'.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## Esto controla el número máximo de entradas en modo NVL que pueden ser
## mostradas de una vez.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Pantalla de globos ##########################################################
##
## La pantalla de burbujas se utiliza para mostrar el diálogo al jugador cuando
## se utilizan burbujas de diálogo. La pantalla de burbujas toma los mismos
## parámetros que la pantalla "say", debe crear un visualizable con el id de
## "what", y puede crear visualizables con los ids "namebox", "who", y "window".
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Variantes móviles
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Ya que puede carecer de ratón, se reempleza el menú rápido con una versión
## con menos botones y más grandes, más fáciles de tocar.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style "quick_menu"
            style_prefix "quick"

            textbutton _("◀ Atrás") action Rollback()
            textbutton _("⏩ Saltar") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("▶ Auto") action Preference("auto-forward", "toggle")
            textbutton _("⚙️ Menú") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 1305

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    left_bar Frame("gui/phone/slider/horizontal_[prefix_]left.png", gui.slider_borders, tile=gui.slider_tile)
    right_bar Frame("gui/phone/slider/horizontal_[prefix_]right.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"
    thumb_offset 17

style vslider:
    variant "small"
    xsize gui.slider_size
    top_bar Frame("gui/phone/slider/vertical_[prefix_]top.png", gui.vslider_borders, tile=gui.slider_tile)
    bottom_bar Frame("gui/phone/slider/vertical_[prefix_]bottom.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"
    thumb_offset 17

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
