################################################################################
## INTERFAZ PERSONALIZADA ESTILO ANIME ROM-COM «TO LOVE-RU» (HUD, MODALES Y MAPA)
################################################################################

## 1. HUD Superior Permanente estilo To Love-Ru (zorder 110 para funcionar sobre el mapa)
screen stats_hud():
    zorder 110
    if mostrar_hud:
        $ porc_partida = calcular_progreso_total()
        frame:
            xalign 0.5
            yalign 0.0
            xfill True
            ysize 82
            background "images/ui/hud_bar_tlr.png"
            padding (16, 10)

            hbox:
                xfill True
                yalign 0.5

                # Emblema To Love-Ru + Estadísticas en cápsulas brillantes (0% a 100%)
                hbox:
                    spacing 8
                    yalign 0.5

                    add "images/ui/icon_tlr_heart.png" zoom 0.78 yalign 0.5

                    frame:
                        background Frame("images/ui/pill_stat_tlr.png", 24, 12, 24, 12)
                        padding (13, 6)
                        yalign 0.5
                        hbox:
                            spacing 5
                            text "★ Reputación:" size 16 bold True color "#ffccf2" outlines [(2, "#24031a", 0, 0)] yalign 0.5
                            text "[reputacion]%%" size 18 bold True color "#5dfdcb" outlines [(2, "#190212", 0, 0)] yalign 0.5

                    frame:
                        background Frame("images/ui/pill_stat_tlr.png", 24, 12, 24, 12)
                        padding (13, 6)
                        yalign 0.5
                        hbox:
                            spacing 5
                            text "⚡ Ingenio:" size 16 bold True color "#90e0ef" outlines [(2, "#24031a", 0, 0)] yalign 0.5
                            text "[ingenio]%%" size 18 bold True color "#ffffff" outlines [(2, "#190212", 0, 0)] yalign 0.5

                    frame:
                        background Frame("images/ui/pill_stat_tlr.png", 24, 12, 24, 12)
                        padding (13, 6)
                        yalign 0.5
                        hbox:
                            spacing 5
                            text "✨ Carisma:" size 16 bold True color "#ffe680" outlines [(2, "#24031a", 0, 0)] yalign 0.5
                            text "[carisma]%%" size 18 bold True color "#ffffff" outlines [(2, "#190212", 0, 0)] yalign 0.5

                    frame:
                        background Frame("images/ui/pill_stat_tlr.png", 24, 12, 24, 12)
                        padding (13, 6)
                        yalign 0.5
                        hbox:
                            spacing 5
                            text "🏮 Festival:" size 16 bold True color "#ffb703" outlines [(2, "#24031a", 0, 0)] yalign 0.5
                            text "[presupuesto_festival]%%" size 18 bold True color "#fff0f6" outlines [(2, "#190212", 0, 0)] yalign 0.5

                # Botones de acceso a Modales estilo To Love-Ru + Progreso Total 0-100%
                hbox:
                    xalign 1.0
                    spacing 8
                    yalign 0.5

                    textbutton "🏆 Progreso: [porc_partida]%%":
                        action Show("game_progress_modal")
                        background Frame("images/ui/btn_gold_idle.png", 24, 14, 24, 14)
                        hover_background Frame("images/ui/btn_gold_hover.png", 24, 14, 24, 14)
                        padding (18, 8)
                        text_size 17
                        text_bold True
                        text_color "#2b0318"
                        text_hover_color "#000000"

                    textbutton "💖 Chicas ([afinidad_akane]%%/[afinidad_yuki]%%/[afinidad_hana]%%)":
                        action Show("girls_status_modal")
                        background Frame("images/ui/btn_pink_idle.png", 24, 14, 24, 14)
                        hover_background Frame("images/ui/btn_pink_hover.png", 24, 14, 24, 14)
                        padding (18, 8)
                        text_size 17
                        text_bold True
                        text_color "#fff0f6"
                        text_hover_color "#ffffff"
                        text_outlines [(2, "#4a0528", 0, 0)]

                    textbutton "😈 Darkness ([tentacion_kuroe]%%/[tentacion_mirei]%%/[tentacion_reina]%%)":
                        action Show("sub_girls_modal")
                        background Frame("images/ui/btn_purple_idle.png", 24, 14, 24, 14)
                        hover_background Frame("images/ui/btn_purple_hover.png", 24, 14, 24, 14)
                        padding (18, 8)
                        text_size 17
                        text_bold True
                        text_color "#f3d5ff"
                        text_hover_color "#ffffff"
                        text_outlines [(2, "#2d0645", 0, 0)]

                    textbutton "🔀 Ramas ([len(registro_consecuencias)])":
                        action Show("consequences_log_modal")
                        background Frame("images/ui/btn_cyan_idle.png", 24, 14, 24, 14)
                        hover_background Frame("images/ui/btn_cyan_hover.png", 24, 14, 24, 14)
                        padding (16, 8)
                        text_size 17
                        text_bold True
                        text_color "#e8fbff"
                        text_hover_color "#ffffff"
                        text_outlines [(2, "#062b45", 0, 0)]


## 2. Notificaciones Flotantes Apiladas de Puntos / Afinidad / Objetos
screen point_popup():
    zorder 160
    if len(cola_popups) > 0:
        vbox:
            at popup_float
            xalign 0.98
            ypos 88
            spacing 8
            for msg_txt, msg_col in cola_popups:
                frame:
                    xalign 1.0
                    background Frame("images/ui/popup_toast_tlr.png", 28, 16, 28, 16)
                    padding (26, 12)
                    hbox:
                        spacing 8
                        text "✦" size 22 bold True color "#ffd13b" outlines [(2, "#320520", 0, 0)] yalign 0.5
                        text "[msg_txt]" size 22 bold True color msg_col outlines [(2, "#220318", 0, 0)] yalign 0.5

        timer 2.6 action Function(limpiar_popups)


## 2B. Overlay de Reacciones Anime en Vivo (Emotes 💕💢❗💧✨🔥 + Brillo Ambiental)
screen reaction_overlay():
    zorder 105
    if reaccion_actual_ambiente == "romance":
        add "#ff4d94" at mood_glow_fade
    elif reaccion_actual_ambiente == "darkness":
        add "#c724b1" at mood_glow_fade
    elif reaccion_actual_ambiente == "shock":
        add "#ffd13b" at mood_glow_fade

    if reaccion_actual_icono:
        $ x_emote = 0.58
        if reaccion_actual_pos == "left":
            $ x_emote = 0.30
        elif reaccion_actual_pos == "right":
            $ x_emote = 0.85

        add reaccion_actual_icono:
            at emote_pop_anim
            xalign x_emote
            ypos 155

        timer 2.35 action Function(limpiar_reaccion)



## 3. Panel Modal de las 3 HEROÍNAS PRINCIPALES (Estilo To Love-Ru Romance & Comedia)
screen girls_status_modal():
    modal True
    zorder 200

    add "#180212e6"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1700
        ysize 935
        background Frame("images/ui/modal_romance_tlr.png", 44, 44, 44, 44)
        padding (44, 34)

        vbox:
            spacing 16
            xfill True

            hbox:
                xfill True
                hbox:
                    spacing 12
                    yalign 0.5
                    add "images/ui/icon_tlr_heart.png" yalign 0.5
                    vbox:
                        text "💖 HEROÍNAS PRINCIPALES — TROUBLE ROMANCE!" size 32 bold True color "#ff85c0" outlines [(3, "#2b031a", 0, 0)]
                        text "✦ Desarrolla tu vínculo romántico con ellas para desbloquear el clímax del Festival ✦" size 17 italic True color "#ffe680" outlines [(2, "#240316", 0, 0)]

                hbox:
                    xalign 1.0
                    spacing 14
                    yalign 0.5
                    textbutton "😈 Modo Darkness (Sub-Chicas) ➔":
                        action [Hide("girls_status_modal"), Show("sub_girls_modal")]
                        background Frame("images/ui/btn_purple_idle.png", 24, 14, 24, 14)
                        hover_background Frame("images/ui/btn_purple_hover.png", 24, 14, 24, 14)
                        padding (24, 10)
                        text_size 20
                        text_bold True
                        text_color "#ffffff"
                        text_outlines [(2, "#2d0645", 0, 0)]
                    textbutton "✖ Cerrar":
                        action Hide("girls_status_modal")
                        background Frame("images/ui/btn_pink_idle.png", 24, 14, 24, 14)
                        hover_background Frame("images/ui/btn_pink_hover.png", 24, 14, 24, 14)
                        padding (24, 10)
                        text_size 20
                        text_bold True
                        text_color "#ffffff"
                        text_outlines [(2, "#4a0528", 0, 0)]

            hbox:
                spacing 28
                xalign 0.5

                # --- TARJETA AKANE ---
                $ rango_akane, col_akane = obtener_rango_relacion(afinidad_akane)
                frame:
                    xsize 515
                    ysize 770
                    background Frame("images/ui/card_akane_tlr.png", 40, 40, 40, 40)
                    padding (28, 22)
                    vbox:
                        spacing 10
                        xfill True
                        text "♥ Akane Tachibana ♥" size 28 bold True color "#ff5ca8" outlines [(2, "#280316", 0, 0)] xalign 0.5
                        text "«La Presidenta Tsundere del Consejo»" size 18 italic True color "#ffe680" outlines [(1, "#280316", 0, 0)] xalign 0.5

                        add "images/thumb_akane.png" xalign 0.5

                        text "Estricta, orgullosa y explosiva por fuera, pero se derrite de amor cuando la ayudas en secreto." size 17 color "#fff0f6"

                        frame:
                            xfill True
                            background Frame("images/ui/panel_inner_tlr.png", 24, 18, 24, 18)
                            padding (16, 10)
                            vbox:
                                spacing 6
                                hbox:
                                    xfill True
                                    text "💖 Amor Romántico:" size 18 bold True color "#ffb3d9"
                                    text "[afinidad_akane] / 100 ♥" size 19 bold True color "#ffd13b" outlines [(2, "#280316", 0, 0)] xalign 1.0
                                bar:
                                    value StaticValue(afinidad_akane, 100)
                                    xfill True
                                    ysize 20
                                    left_bar Frame("images/ui/bar_full_pink.png", 10, 4)
                                    right_bar Frame("images/ui/bar_empty_tlr.png", 10, 4)

                                hbox:
                                    spacing 8
                                    text "✦ Rango:" size 17 color "#ffd6eb"
                                    text "[rango_akane]" size 17 bold True color col_akane
                                hbox:
                                    spacing 8
                                    text "✦ Misión:" size 17 color "#ffd6eb"
                                    text "[estado_mision_akane]" size 17 bold True color ("#5dfdcb" if estado_mision_akane == "Resuelto con Éxito" else "#ffd13b")
                                hbox:
                                    spacing 8
                                    text "😈 Rival Darkness:" size 17 color "#e0aaff"
                                    text "Kuroe ([estado_sub_kuroe])" size 17 bold True color ("#ff4d6d" if estado_sub_kuroe == "Enredado" else "#5dfdcb")

                # --- TARJETA YUKI ---
                $ rango_yuki, col_yuki = obtener_rango_relacion(afinidad_yuki)
                frame:
                    xsize 515
                    ysize 770
                    background Frame("images/ui/card_yuki_tlr.png", 40, 40, 40, 40)
                    padding (28, 22)
                    vbox:
                        spacing 10
                        xfill True
                        text "✦ Yuki Shirogane ✦" size 28 bold True color "#70e4ff" outlines [(2, "#071c36", 0, 0)] xalign 0.5
                        text "«La Genio Kuudere del Laboratorio»" size 18 italic True color "#ffe680" outlines [(1, "#071c36", 0, 0)] xalign 0.5

                        add "images/thumb_yuki.png" xalign 0.5

                        text "Serena, misteriosa y brillante. Calcula el amor con fórmulas hasta que haces latir su corazón." size 17 color "#eefaff"

                        frame:
                            xfill True
                            background Frame("images/ui/panel_inner_tlr.png", 24, 18, 24, 18)
                            padding (16, 10)
                            vbox:
                                spacing 6
                                hbox:
                                    xfill True
                                    text "💙 Amor Romántico:" size 18 bold True color "#90e0ef"
                                    text "[afinidad_yuki] / 100 ♥" size 19 bold True color "#ffd13b" outlines [(2, "#071c36", 0, 0)] xalign 1.0
                                bar:
                                    value StaticValue(afinidad_yuki, 100)
                                    xfill True
                                    ysize 20
                                    left_bar Frame("images/ui/bar_full_cyan.png", 10, 4)
                                    right_bar Frame("images/ui/bar_empty_tlr.png", 10, 4)

                                hbox:
                                    spacing 8
                                    text "✦ Rango:" size 17 color "#d8f3ff"
                                    text "[rango_yuki]" size 17 bold True color col_yuki
                                hbox:
                                    spacing 8
                                    text "✦ Misión:" size 17 color "#d8f3ff"
                                    text "[estado_mision_yuki]" size 17 bold True color ("#5dfdcb" if estado_mision_yuki == "Resuelto con Éxito" else "#ffd13b")
                                hbox:
                                    spacing 8
                                    text "😈 Rival Darkness:" size 17 color "#e0aaff"
                                    text "Mirei ([estado_sub_mirei])" size 17 bold True color ("#ff4d6d" if estado_sub_mirei == "Enredado" else "#5dfdcb")

                # --- TARJETA HANA ---
                $ rango_hana, col_hana = obtener_rango_relacion(afinidad_hana)
                frame:
                    xsize 515
                    ysize 770
                    background Frame("images/ui/card_hana_tlr.png", 40, 40, 40, 40)
                    padding (28, 22)
                    vbox:
                        spacing 10
                        xfill True
                        text "🌸 Hana Sakuragi 🌸" size 28 bold True color "#ff85c0" outlines [(2, "#2b0518", 0, 0)] xalign 0.5
                        text "«La Estrella Genki de Atletismo»" size 18 italic True color "#ffe680" outlines [(1, "#2b0518", 0, 0)] xalign 0.5

                        add "images/thumb_hana.png" xalign 0.5

                        text "Alegre, cariñosa y llena de energía, aunque esconde sus problemas tras una sonrisa radiante." size 17 color "#fff0f6"

                        frame:
                            xfill True
                            background Frame("images/ui/panel_inner_tlr.png", 24, 18, 24, 18)
                            padding (16, 10)
                            vbox:
                                spacing 6
                                hbox:
                                    xfill True
                                    text "🌸 Amor Romántico:" size 18 bold True color "#ffc2e2"
                                    text "[afinidad_hana] / 100 ♥" size 19 bold True color "#ffd13b" outlines [(2, "#2b0518", 0, 0)] xalign 1.0
                                bar:
                                    value StaticValue(afinidad_hana, 100)
                                    xfill True
                                    ysize 20
                                    left_bar Frame("images/ui/bar_full_pink.png", 10, 4)
                                    right_bar Frame("images/ui/bar_empty_tlr.png", 10, 4)

                                hbox:
                                    spacing 8
                                    text "✦ Rango:" size 17 color "#ffd6eb"
                                    text "[rango_hana]" size 17 bold True color col_hana
                                hbox:
                                    spacing 8
                                    text "✦ Misión:" size 17 color "#ffd6eb"
                                    text "[estado_mision_hana]" size 17 bold True color ("#5dfdcb" if estado_mision_hana == "Resuelto con Éxito" else "#ffd13b")
                                hbox:
                                    spacing 8
                                    text "😈 Rival Darkness:" size 17 color "#e0aaff"
                                    text "Reina ([estado_sub_reina])" size 17 bold True color ("#ff4d6d" if estado_sub_reina == "Enredado" else "#5dfdcb")


## 3B. Panel Modal de las 3 SUB-PERSONAJES (Estilo To Love-Ru Darkness: Tentación y Enredos)
screen sub_girls_modal():
    modal True
    zorder 200

    add "#14021ce8"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1700
        ysize 935
        background Frame("images/ui/modal_ecchi_tlr.png", 44, 44, 44, 44)
        padding (44, 34)

        vbox:
            spacing 16
            xfill True

            hbox:
                xfill True
                hbox:
                    spacing 12
                    yalign 0.5
                    add "images/ui/icon_tlr_heart.png" yalign 0.5
                    vbox:
                        text "😈 SUB-PERSONAJES: MODO DARKNESS, TENTACIÓN Y LUJURIA" size 30 bold True color "#e0aaff" outlines [(3, "#210233", 0, 0)]
                        text "⚠️ Si caes en sus tentaciones, DEBERÁS TERMINAR CON ELLAS antes del Festival o arruinarán tu final principal." size 17 bold True color "#ffd13b" outlines [(2, "#1f022b", 0, 0)]

                hbox:
                    xalign 1.0
                    spacing 14
                    yalign 0.5
                    textbutton "💖 Ver Principales":
                        action [Hide("sub_girls_modal"), Show("girls_status_modal")]
                        background Frame("images/ui/btn_pink_idle.png", 24, 14, 24, 14)
                        hover_background Frame("images/ui/btn_pink_hover.png", 24, 14, 24, 14)
                        padding (24, 10)
                        text_size 20
                        text_bold True
                        text_color "#ffffff"
                        text_outlines [(2, "#4a0528", 0, 0)]
                    textbutton "✖ Cerrar":
                        action Hide("sub_girls_modal")
                        background Frame("images/ui/btn_purple_idle.png", 24, 14, 24, 14)
                        hover_background Frame("images/ui/btn_purple_hover.png", 24, 14, 24, 14)
                        padding (24, 10)
                        text_size 20
                        text_bold True
                        text_color "#ffffff"
                        text_outlines [(2, "#2d0645", 0, 0)]

            hbox:
                spacing 28
                xalign 0.5

                # --- SUB 1: KUROE SAKAMOTO ---
                frame:
                    xsize 515
                    ysize 760
                    background Frame("images/ui/card_sub_tlr.png", 40, 40, 40, 40)
                    padding (28, 22)
                    vbox:
                        spacing 10
                        xfill True
                        text "🔥 Kuroe Sakamoto 🔥" size 28 bold True color "#e0aaff" outlines [(2, "#240338", 0, 0)] xalign 0.5
                        text "«La Chica Mala que Odia Estudiar»" size 18 italic True color "#ffd13b" outlines [(1, "#240338", 0, 0)] xalign 0.5

                        add "images/thumb_kuroe.png" xalign 0.5

                        text "Conectada a: Akane (Consejo).\nRebelde y provocadora. Se esconde en la Biblioteca y te exige besos prohibidos a cambio de las Actas." size 17 color "#f8e8ff"

                        frame:
                            xfill True
                            background Frame("images/ui/panel_inner_tlr.png", 24, 18, 24, 18)
                            padding (16, 10)
                            vbox:
                                spacing 6
                                hbox:
                                    xfill True
                                    text "🔥 Nivel de Lujuria:" size 18 bold True color "#e0aaff"
                                    text "[tentacion_kuroe] / 100 🔥" size 19 bold True color "#ffb703" outlines [(2, "#240338", 0, 0)] xalign 1.0
                                bar:
                                    value StaticValue(tentacion_kuroe, 100)
                                    xfill True
                                    ysize 20
                                    left_bar Frame("images/ui/bar_full_ecchi.png", 10, 4)
                                    right_bar Frame("images/ui/bar_empty_tlr.png", 10, 4)

                                hbox:
                                    spacing 8
                                    text "💋 Estado:" size 18 color "#f3d5ff"
                                    if not visitado_akane:
                                        text "🔒 Bloqueada (Avanza con Akane)" size 17 bold True color "#ff85c0"
                                    else:
                                        text "[estado_sub_kuroe]" size 18 bold True color ("#ff4d6d" if estado_sub_kuroe == "Enredado" else "#5dfdcb")

                # --- SUB 2: MIREI KANZAKI ---
                frame:
                    xsize 515
                    ysize 760
                    background Frame("images/ui/card_sub_tlr.png", 40, 40, 40, 40)
                    padding (28, 22)
                    vbox:
                        spacing 10
                        xfill True
                        text "🔥 Mirei Kanzaki 🔥" size 28 bold True color "#e0aaff" outlines [(2, "#240338", 0, 0)] xalign 0.5
                        text "«La Sempai Seductora de Ciencias»" size 18 italic True color "#ffd13b" outlines [(1, "#240338", 0, 0)] xalign 0.5

                        add "images/thumb_mirei.png" xalign 0.5

                        text "Conectada a: Yuki (Laboratorio).\nMadura, voluptuosa y susurrante. Te ofrece la Bobina Experimental a cambio de 'experimentos corporales'." size 17 color "#f8e8ff"

                        frame:
                            xfill True
                            background Frame("images/ui/panel_inner_tlr.png", 24, 18, 24, 18)
                            padding (16, 10)
                            vbox:
                                spacing 6
                                hbox:
                                    xfill True
                                    text "🔥 Nivel de Lujuria:" size 18 bold True color "#e0aaff"
                                    text "[tentacion_mirei] / 100 🔥" size 19 bold True color "#ffb703" outlines [(2, "#240338", 0, 0)] xalign 1.0
                                bar:
                                    value StaticValue(tentacion_mirei, 100)
                                    xfill True
                                    ysize 20
                                    left_bar Frame("images/ui/bar_full_ecchi.png", 10, 4)
                                    right_bar Frame("images/ui/bar_empty_tlr.png", 10, 4)

                                hbox:
                                    spacing 8
                                    text "💋 Estado:" size 18 color "#f3d5ff"
                                    if not visitado_yuki:
                                        text "🔒 Bloqueada (Avanza con Yuki)" size 17 bold True color "#ff85c0"
                                    else:
                                        text "[estado_sub_mirei]" size 18 bold True color ("#ff4d6d" if estado_sub_mirei == "Enredado" else "#5dfdcb")

                # --- SUB 3: REINA KUROKAWA ---
                frame:
                    xsize 515
                    ysize 760
                    background Frame("images/ui/card_sub_tlr.png", 40, 40, 40, 40)
                    padding (28, 22)
                    vbox:
                        spacing 10
                        xfill True
                        text "🔥 Reina Kurokawa 🔥" size 28 bold True color "#ffb703" outlines [(2, "#240338", 0, 0)] xalign 0.5
                        text "«La Capitana Ardiente de Ed. Física»" size 18 italic True color "#ffe680" outlines [(1, "#240338", 0, 0)] xalign 0.5

                        add "images/thumb_reina.png" xalign 0.5

                        text "Conectada a: Hana (Atletismo).\nAtlética, dominante y directa. Sabe el secreto de la lesión de Hana y te cita a solas en los vestuarios." size 17 color "#f8e8ff"

                        frame:
                            xfill True
                            background Frame("images/ui/panel_inner_tlr.png", 24, 18, 24, 18)
                            padding (16, 10)
                            vbox:
                                spacing 6
                                hbox:
                                    xfill True
                                    text "🔥 Nivel de Lujuria:" size 18 bold True color "#ffe680"
                                    text "[tentacion_reina] / 100 🔥" size 19 bold True color "#ffb703" outlines [(2, "#240338", 0, 0)] xalign 1.0
                                bar:
                                    value StaticValue(tentacion_reina, 100)
                                    xfill True
                                    ysize 20
                                    left_bar Frame("images/ui/bar_full_ecchi.png", 10, 4)
                                    right_bar Frame("images/ui/bar_empty_tlr.png", 10, 4)

                                hbox:
                                    spacing 8
                                    text "💋 Estado:" size 18 color "#f3d5ff"
                                    if not visitado_hana:
                                        text "🔒 Bloqueada (Avanza con Hana)" size 17 bold True color "#ff85c0"
                                    else:
                                        text "[estado_sub_reina]" size 18 bold True color ("#ff4d6d" if estado_sub_reina == "Enredado" else "#5dfdcb")


## 4. Panel Modal de Registro de Ramas, Consecuencias e Inventario (Estilo To Love-Ru Trouble Log)
screen consequences_log_modal():
    modal True
    zorder 200

    add "#160214e8"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1580
        ysize 900
        background Frame("images/ui/modal_romance_tlr.png", 44, 44, 44, 44)
        padding (44, 34)

        vbox:
            spacing 16
            xfill True

            hbox:
                xfill True
                hbox:
                    spacing 12
                    yalign 0.5
                    add "images/ui/icon_tlr_heart.png" yalign 0.5
                    vbox:
                        text "🔀 TROUBLE LOG: DECISIONES, RAMAS E INVENTARIO" size 32 bold True color "#70e4ff" outlines [(3, "#24031a", 0, 0)]
                        text "✦ Cada enredo romántico o tentación deja huella en tu historia ✦" size 17 italic True color "#ffe680"

                textbutton "✖ Cerrar":
                    xalign 1.0
                    yalign 0.5
                    action Hide("consequences_log_modal")
                    background Frame("images/ui/btn_pink_idle.png", 24, 14, 24, 14)
                    hover_background Frame("images/ui/btn_pink_hover.png", 24, 14, 24, 14)
                    padding (26, 10)
                    text_size 21
                    text_bold True
                    text_color "#ffffff"
                    text_outlines [(2, "#4a0528", 0, 0)]

            # Inventario de objetos clave con cápsulas brillantes
            frame:
                xfill True
                background Frame("images/ui/panel_inner_tlr.png", 24, 18, 24, 18)
                padding (22, 14)
                vbox:
                    spacing 8
                    text "🎒 Objetos Clave en tu Mochila ([len(inventario_items)]):" size 21 bold True color "#ffd13b" outlines [(2, "#24031a", 0, 0)]
                    if len(inventario_items) == 0:
                        text "Ninguno todavía. Explora las zonas del instituto para encontrar objetos y pistas." size 19 italic True color "#f3c4e2"
                    else:
                        hbox:
                            box_wrap True
                            spacing 10
                            box_wrap_spacing 8
                            for item in inventario_items:
                                frame:
                                    background Frame("images/ui/pill_stat_tlr.png", 24, 12, 24, 12)
                                    padding (18, 7)
                                    text "✦ [item]" size 18 bold True color "#fff0f6" outlines [(2, "#24031a", 0, 0)]

            # Lista desplazable de consecuencias
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                xfill True
                ysize 590

                vbox:
                    spacing 14
                    xfill True
                    if len(registro_consecuencias) == 0:
                        text "Aún no has tomado decisiones críticas. Tus elecciones cambiarán el rumbo de la historia." size 23 color "#ffd6eb"
                    else:
                        for item in registro_consecuencias:
                            frame:
                                xfill True
                                background Frame("images/ui/panel_inner_tlr.png", 24, 18, 24, 18)
                                padding (24, 16)
                                vbox:
                                    spacing 6
                                    hbox:
                                        xfill True
                                        text "💖 " + item["titulo"] size 23 bold True color "#ffd13b" outlines [(2, "#24031a", 0, 0)]
                                        text item["impacto"] size 20 bold True color "#5dfdcb" outlines [(2, "#190212", 0, 0)] xalign 1.0
                                    text item["descripcion"] size 19 color "#fff0f6"


## 4B. MODAL DE PROGRESO TOTAL DE LA PARTIDA (0% A 100% — QUÉ TE FALTA PARA EL JUEGO COMPLETO)
screen game_progress_modal():
    modal True
    zorder 205

    $ datos_prog = obtener_desglose_progreso_juego()
    $ porc_total = datos_prog["porcentaje"]
    $ falta_porc = 100 - porc_total
    $ num_comp = datos_prog["completados"]
    $ num_tot = datos_prog["total_hitos"]
    $ lista_hitos = datos_prog["hitos"]
    $ lista_pend = datos_prog["pendientes"]

    add "#160214eb"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1680
        ysize 930
        background Frame("images/ui/modal_romance_tlr.png", 44, 44, 44, 44)
        padding (42, 32)

        vbox:
            spacing 14
            xfill True

            # Cabecera
            hbox:
                xfill True
                hbox:
                    spacing 12
                    yalign 0.5
                    add "images/ui/icon_tlr_heart.png" yalign 0.5
                    vbox:
                        text "🏆 PROGRESO TOTAL DE TU PARTIDA: [porc_total]%% / 100%%" size 31 bold True color "#ffd13b" outlines [(3, "#24031a", 0, 0)]
                        if falta_porc > 0:
                            text "✦ Te falta un [falta_porc]%% ([len(lista_pend)] objetivos pendientes de [num_tot]) para obtener el Juego Completo al 100%% ✦" size 17 bold True color "#5dfdcb" outlines [(2, "#190212", 0, 0)]
                        else:
                            text "👑 ¡FELICIDADES! ¡Has alcanzado el 100%% del Juego Completo en el Instituto Sakura! 👑" size 18 bold True color "#5dfdcb" outlines [(2, "#190212", 0, 0)]

                textbutton "✖ Cerrar":
                    xalign 1.0
                    yalign 0.5
                    action Hide("game_progress_modal")
                    background Frame("images/ui/btn_pink_idle.png", 24, 14, 24, 14)
                    hover_background Frame("images/ui/btn_pink_hover.png", 24, 14, 24, 14)
                    padding (24, 10)
                    text_size 20
                    text_bold True
                    text_color "#ffffff"
                    text_outlines [(2, "#4a0528", 0, 0)]

            # Barra general de progreso 0% a 100% + Resumen de Estadísticas y Finales
            frame:
                xfill True
                background Frame("images/ui/panel_inner_tlr.png", 24, 18, 24, 18)
                padding (24, 14)
                vbox:
                    spacing 8
                    hbox:
                        xfill True
                        text "📊 Medidor de Juego Completo (Empieza en 0%% y sube hasta 100%%):" size 19 bold True color "#fff0f6"
                        text "[porc_total]%% Completado  |  [falta_porc]%% Restante" size 19 bold True color "#ffd13b" xalign 1.0
                    bar:
                        value StaticValue(porc_total, 100)
                        xfill True
                        ysize 22
                        left_bar Frame("images/ui/bar_full_pink.png", 10, 4)
                        right_bar Frame("images/ui/bar_empty_tlr.png", 10, 4)

                    hbox:
                        spacing 18
                        xalign 0.5
                        text "💖 Akane: [afinidad_akane]%%" size 17 bold True color "#ff85c0"
                        text "💙 Yuki: [afinidad_yuki]%%" size 17 bold True color "#70e4ff"
                        text "🌸 Hana: [afinidad_hana]%%" size 17 bold True color "#ffb3d9"
                        text "🔥 Kuroe: [tentacion_kuroe]%%" size 17 bold True color "#e0aaff"
                        text "🔥 Mirei: [tentacion_mirei]%%" size 17 bold True color "#c77dff"
                        text "🔥 Reina: [tentacion_reina]%%" size 17 bold True color "#ffb703"
                        text "🏮 Festival: [presupuesto_festival]%%" size 17 bold True color "#5dfdcb"
                        text "🎬 Finales Vistos: [len(finales_vistos)]/7" size 17 bold True color "#ffd13b"

            # Lista desplazable con todos los hitos (Qué tienes completado y qué te falta hacer)
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                xfill True
                ysize 595

                vbox:
                    spacing 10
                    xfill True
                    for h in lista_hitos:
                        frame:
                            xfill True
                            background Frame("images/ui/panel_inner_tlr.png", 24, 18, 24, 18)
                            padding (20, 12)
                            vbox:
                                spacing 4
                                hbox:
                                    xfill True
                                    if h["completado"]:
                                        text "✔ [h['titulo']]" size 19 bold True color "#5dfdcb" outlines [(2, "#190212", 0, 0)]
                                        text "+[h['peso']]%% OBTENIDO" size 18 bold True color "#5dfdcb" xalign 1.0
                                    else:
                                        text "⏳ FALTA: [h['titulo']]" size 19 bold True color "#ffd13b" outlines [(2, "#24031a", 0, 0)]
                                        text "Falta +[h['peso']]%%" size 18 bold True color "#ff85c0" xalign 1.0

                                hbox:
                                    spacing 10
                                    text "[h['categoria']]" size 15 bold True color "#e0aaff"
                                    if not h["completado"]:
                                        text "➔ Cómo lograrlo: [h['como_lograrlo']]" size 16 color "#fff0f6"
                                    else:
                                        text "➔ ¡Objetivo completado en tu partida!" size 16 italic True color "#a8e6cf"


## 5. MAPA INTERACTIVO DEL INSTITUTO SAKURA (ESTILO TO LOVE-RU)
screen school_hub_selector():
    modal True
    zorder 90

    $ info_actual = ZONAS_INSTITUTO[ubicacion_actual]
    $ zona_actual_abierta = esta_zona_desbloqueada(ubicacion_actual)
    $ misiones_listas = esta_zona_desbloqueada("festival")
    $ sub_pendientes = obtener_estado_sub_Pendiente()
    $ etapa_num, etapa_max, obj_texto, obj_zona = obtener_objetivo_actual()
    $ porc_mapa = calcular_progreso_total()

    key "K_UP" action Function(mover_en_mapa, "arriba")
    key "K_w" action Function(mover_en_mapa, "arriba")
    key "K_DOWN" action Function(mover_en_mapa, "abajo")
    key "K_s" action Function(mover_en_mapa, "abajo")
    key "K_LEFT" action Function(mover_en_mapa, "izquierda")
    key "K_a" action Function(mover_en_mapa, "izquierda")
    key "K_RIGHT" action Function(mover_en_mapa, "derecha")
    key "K_d" action Function(mover_en_mapa, "derecha")
    key "K_RETURN" action If(zona_actual_abierta, Return(info_actual["label_destino"]), Function(registrar_intento_bloqueo, ubicacion_actual))
    key "K_SPACE" action If(zona_actual_abierta, Return(info_actual["label_destino"]), Function(registrar_intento_bloqueo, ubicacion_actual))

    frame:
        xalign 0.5
        ypos 80
        xsize 1860
        ysize 985
        background Frame("images/ui/modal_map_tlr.png", 44, 44, 44, 44)
        padding (34, 24)

        vbox:
            spacing 10
            xfill True

            # Cabecera del Mapa con Objetivo Progresivo de la Trama
            hbox:
                xfill True
                hbox:
                    spacing 10
                    yalign 0.5
                    add "images/ui/icon_tlr_heart.png" zoom 0.85 yalign 0.5
                    vbox:
                        spacing 3
                        text "🗺️ MAPA DEL INSTITUTO SAKURA — PROGRESO PARTIDA: [porc_mapa]%% (ETAPA [etapa_num]/[etapa_max])" size 24 bold True color "#ffd13b" outlines [(2, "#24031a", 0, 0)]
                        text "🎯 OBJETIVO ACTUAL: [obj_texto]" size 18 bold True color "#5dfdcb" outlines [(2, "#190212", 0, 0)]
                        if len(sub_pendientes) > 0:
                            text "😈 Aventuras Darkness activas con: [', '.join(sub_pendientes)]. ¡Corta con ellas antes del Festival!" size 16 bold True color "#ff85c0" outlines [(2, "#24031a", 0, 0)]

                hbox:
                    xalign 1.0
                    spacing 10
                    yalign 0.5
                    textbutton "🏆 Qué me falta ([porc_mapa]%%)":
                        action Show("game_progress_modal")
                        background Frame("images/ui/btn_cyan_idle.png", 24, 14, 24, 14)
                        hover_background Frame("images/ui/btn_cyan_hover.png", 24, 14, 24, 14)
                        padding (18, 10)
                        text_size 17
                        text_bold True
                        text_color "#ffffff"
                        text_outlines [(2, "#062b45", 0, 0)]

                    if misiones_listas:
                        textbutton "🏮 ¡IR AL FESTIVAL NOCTURNO (CLÍMAX)!":
                            action Return("ir_climax_festival")
                            background Frame("images/ui/btn_gold_idle.png", 24, 14, 24, 14)
                            hover_background Frame("images/ui/btn_gold_hover.png", 24, 14, 24, 14)
                            padding (22, 10)
                            text_size 19
                            text_bold True
                            text_color "#2b0318"
                            text_hover_color "#000000"
                    else:
                        textbutton "🔒 Festival Bloqueado (Etapa [etapa_num]/[etapa_max])":
                            action Function(registrar_intento_bloqueo, "festival")
                            background Frame("images/ui/btn_purple_idle.png", 24, 14, 24, 14)
                            hover_background Frame("images/ui/btn_purple_hover.png", 24, 14, 24, 14)
                            padding (20, 10)
                            text_size 17
                            text_bold True
                            text_color "#fff0f6"
                            text_outlines [(2, "#24031a", 0, 0)]

            # Cuerpo Principal: Mapa Visual a la Izquierda + Panel Inspector a la Derecha
            hbox:
                spacing 20
                xfill True

                # --- LIENZO DEL MAPA DEL CAMPUS (1220x780) ---
                fixed:
                    xsize 1220
                    ysize 780

                    add "images/bg_school_map.png"

                    # Etiquetas de los edificios y Pines Interactivos
                    for clave, datos in ZONAS_INSTITUTO.items():
                        $ nx, ny = datos["pos"]
                        $ es_actual = (ubicacion_actual == clave)
                        $ abierta = esta_zona_desbloqueada(clave)
                        $ intentos_z = intentos_bloqueo_zona.get(clave, 0)

                        if not abierta:
                            if intentos_z >= 3:
                                $ badge_txt = "📊 FALTAN PUNTOS (Ver Diagnóstico)"
                                $ badge_col = "#ffd13b"
                            else:
                                $ badge_txt = f"🔒 BLOQUEADA ({intentos_z}/3 intentos)"
                                $ badge_col = "#ff85c0"
                        elif clave == "consejo":
                            if not visitado_akane:
                                $ badge_txt = "🎯 OBJETIVO: Ayudar a Akane"
                                $ badge_col = "#ffd13b"
                            elif afinidad_akane < 30:
                                $ badge_txt = f"🎯 Subir Akane a 30% ♥ (Tienes {afinidad_akane}%)"
                                $ badge_col = "#ffd13b"
                            elif not actas_entregadas_akane and "Actas Secretas Recuperadas" in inventario_items:
                                $ badge_txt = "🎯 OBJETIVO: Entregar Actas a Akane"
                                $ badge_col = "#ffd13b"
                            elif not actas_entregadas_akane:
                                $ badge_txt = "⏳ Esperando Actas de Biblioteca"
                                $ badge_col = "#ff85c0"
                            elif afinidad_akane < 50:
                                $ badge_txt = f"🎯 Subir Akane a 50% ♥ (Tienes {afinidad_akane}%)"
                                $ badge_col = "#ffd13b"
                            else:
                                $ badge_txt = "💖 Akane (Arco Completado)"
                                $ badge_col = "#5dfdcb"
                        elif clave == "biblioteca":
                            if not encuentro_sub_kuroe:
                                $ badge_txt = "🎯 OBJETIVO: Kuroe (Recuperar Actas)"
                                $ badge_col = "#ffd13b"
                            elif estado_sub_kuroe == "Enredado" and not ruptura_sub_kuroe:
                                $ badge_txt = "😈 ¡Terminar con Kuroe!"
                                $ badge_col = "#ff5ca8"
                            else:
                                $ badge_txt = "💋 Biblioteca / Kuroe (Lista)"
                                $ badge_col = "#e0aaff"
                        elif clave == "laboratorio":
                            if not visitado_yuki:
                                $ badge_txt = "🎯 OBJETIVO: Ayudar a Yuki"
                                $ badge_col = "#ffd13b"
                            elif afinidad_yuki < 35:
                                $ badge_txt = f"🎯 Subir Yuki a 35% ♥ (Tienes {afinidad_yuki}%)"
                                $ badge_col = "#ffd13b"
                            elif not encuentro_sub_mirei:
                                $ badge_txt = "🎯 OBJETIVO: Mirei (Almacén Químico)"
                                $ badge_col = "#e0aaff"
                            elif not bobina_instalada_yuki:
                                $ badge_txt = "🎯 OBJETIVO: Instalar Bobina a Yuki"
                                $ badge_col = "#ffd13b"
                            elif afinidad_yuki < 55:
                                $ badge_txt = f"🎯 Subir Yuki a 55% ♥ (Tienes {afinidad_yuki}%)"
                                $ badge_col = "#ffd13b"
                            elif estado_sub_mirei == "Enredado" and not ruptura_sub_mirei:
                                $ badge_txt = "😈 ¡Terminar con Mirei! | 💙 Yuki"
                                $ badge_col = "#ff5ca8"
                            else:
                                $ badge_txt = "💙 Yuki y Mirei (Arco Completado)"
                                $ badge_col = "#5dfdcb"
                        elif clave == "azotea":
                            if not visitado_hana:
                                $ badge_txt = "🎯 OBJETIVO: Ayudar a Hana"
                                $ badge_col = "#ffd13b"
                            elif afinidad_hana < 35:
                                $ badge_txt = f"🎯 Subir Hana a 35% ♥ (Tienes {afinidad_hana}%)"
                                $ badge_col = "#ffd13b"
                            elif not pase_entregado_hana and "Pase Oficial de Exhibición" in inventario_items:
                                $ badge_txt = "🎯 OBJETIVO: Entregar Pase a Hana"
                                $ badge_col = "#ffd13b"
                            elif not pase_entregado_hana:
                                $ badge_txt = "⏳ Esperando Pase de Reina"
                                $ badge_col = "#ff85c0"
                            else:
                                $ badge_txt = "🌸 Hana (Arco Completado)"
                                $ badge_col = "#5dfdcb"
                        elif clave == "cafeteria":
                            if not encuentro_sub_reina:
                                $ badge_txt = "🎯 OBJETIVO: Reina (Vestuarios Sur)"
                                $ badge_col = "#ffd13b"
                            elif estado_sub_reina == "Enredado" and not ruptura_sub_reina:
                                $ badge_txt = "😈 ¡Terminar con Reina!"
                                $ badge_col = "#ff5ca8"
                            else:
                                $ badge_txt = "💋 Cafetería / Reina (Lista)"
                                $ badge_col = "#ffb703"
                        else:
                            $ badge_txt = "🌸 Punto Central y Rumores"
                            $ badge_col = "#ffd13b"

                        # Botón del nodo en el mapa con cápsula To Love-Ru
                        frame:
                            xpos nx
                            ypos ny + 62
                            xanchor 0.5
                            yanchor 0.5
                            background (Frame("images/ui/btn_pink_idle.png", 24, 14, 24, 14) if es_actual else (Frame("images/ui/btn_purple_idle.png", 24, 14, 24, 14) if not abierta else Frame("images/ui/pill_stat_tlr.png", 24, 12, 24, 12)))
                            padding (16, 7)

                            $ etiqueta_nodo = datos["nombre"] if abierta else ("🔒 " + datos["nombre"])
                            textbutton etiqueta_nodo:
                                action If(abierta, If(es_actual, Return(datos["label_destino"]), SetVariable("ubicacion_actual", clave)), [SetVariable("ubicacion_actual", clave), Function(registrar_intento_bloqueo, clave)])
                                text_size 17
                                text_bold True
                                text_color ("#ffffff" if es_actual else ("#f3c4e2" if not abierta else datos["color"]))
                                text_hover_color "#ffe680"
                                text_outlines [(2, "#220318", 0, 0)]

                        # Insignia superior de estado / heroína
                        frame:
                            xpos nx
                            ypos ny - 64
                            xanchor 0.5
                            yanchor 0.5
                            background Frame("images/ui/pill_stat_tlr.png", 24, 12, 24, 12)
                            padding (14, 5)
                            text badge_txt size 14 bold True color badge_col outlines [(2, "#1c0214", 0, 0)]

                        # Área clicable sobre el círculo de vista previa
                        button:
                            xpos nx
                            ypos ny
                            xanchor 0.5
                            yanchor 0.5
                            xsize 112
                            ysize 112
                            background None
                            action If(abierta, If(es_actual, Return(datos["label_destino"]), SetVariable("ubicacion_actual", clave)), [SetVariable("ubicacion_actual", clave), Function(registrar_intento_bloqueo, clave)])

                    # Marcador animado de posición actual de Leo
                    $ lx, ly = info_actual["pos"]
                    frame:
                        at pulse_glow
                        xpos lx
                        ypos ly - 98
                        xanchor 0.5
                        yanchor 0.5
                        background Frame("images/ui/btn_gold_idle.png", 24, 14, 24, 14)
                        padding (18, 6)
                        text "💖 [nombre_prota] (AQUÍ)" size 17 bold True color "#2b0318"

                # --- PANEL INSPECTOR DE ZONA Y CONTROLES DE NAVEGACIÓN (545x780) ---
                frame:
                    xsize 545
                    ysize 780
                    background Frame("images/ui/card_akane_tlr.png", 40, 40, 40, 40)
                    padding (26, 20)

                    vbox:
                        spacing 8
                        xfill True

                        text "✦ ZONA SELECCIONADA ✦" size 16 bold True color "#ffd13b" outlines [(2, "#24031a", 0, 0)] xalign 0.5
                        text info_actual["nombre"] size 25 bold True color (info_actual["color"] if zona_actual_abierta else "#ff85c0") outlines [(2, "#24031a", 0, 0)] xalign 0.5
                        text info_actual["subtitulo"] size 16 italic True color "#ffe6eb" xalign 0.5

                        # Estado de desbloqueo y personaje presente
                        frame:
                            xfill True
                            background Frame("images/ui/panel_inner_tlr.png", 24, 18, 24, 18)
                            padding (16, 10)
                            vbox:
                                spacing 5
                                hbox:
                                    text "💖 Chicas:" size 16 bold True color "#ffb3d9"
                                    text "  " + info_actual["heroina"] size 16 bold True color info_actual["color"] outlines [(1, "#1c0214", 0, 0)]
                                hbox:
                                    text "🔑 Acceso:" size 16 bold True color "#ffb3d9"
                                    if not zona_actual_abierta:
                                        $ int_act = intentos_bloqueo_zona.get(ubicacion_actual, 0)
                                        text "  🔒 BLOQUEADA (Intentos: [int_act]/3)" size 16 bold True color "#ffd13b"
                                    elif ubicacion_actual in zonas_exploradas:
                                        text "  🔓 Desbloqueada (Visitada)" size 16 bold True color "#5dfdcb"
                                    else:
                                        text "  🔓 ¡Lista para explorar!" size 16 bold True color "#ffd13b"

                        if not zona_actual_abierta:
                            frame:
                                xfill True
                                background Frame("images/ui/panel_inner_tlr.png", 24, 18, 24, 18)
                                padding (16, 10)
                                vbox:
                                    spacing 4
                                    text "🚫 AVISO DE PROGRESO:" size 15 bold True color "#ffd13b"
                                    text obtener_motivo_bloqueo_zona(ubicacion_actual) size 15 color "#fff0f6"
                        else:
                            text info_actual["descripcion"] size 16 color "#fff0f6"

                        # Botón grande para entrar e interactuar en la zona actual
                        if zona_actual_abierta:
                            textbutton "🚪 ENTRAR A ESTA ZONA ➔":
                                xfill True
                                action Return(info_actual["label_destino"])
                                background Frame("images/ui/btn_gold_idle.png", 24, 14, 24, 14)
                                hover_background Frame("images/ui/btn_gold_hover.png", 24, 14, 24, 14)
                                padding (18, 10)
                                text_size 20
                                text_bold True
                                text_color "#2b0318"
                                text_hover_color "#000000"
                                text_xalign 0.5
                        else:
                            textbutton "🔒 INTENTAR ENTRAR (VER MODAL)":
                                xfill True
                                action Function(registrar_intento_bloqueo, ubicacion_actual)
                                background Frame("images/ui/btn_pink_idle.png", 24, 14, 24, 14)
                                hover_background Frame("images/ui/btn_pink_hover.png", 24, 14, 24, 14)
                                padding (18, 10)
                                text_size 18
                                text_bold True
                                text_color "#ffffff"
                                text_outlines [(2, "#4a0528", 0, 0)]
                                text_xalign 0.5

                        # Cruceta de Caminata por el Campus
                        frame:
                            xfill True
                            background Frame("images/ui/panel_inner_tlr.png", 24, 18, 24, 18)
                            padding (16, 10)
                            vbox:
                                spacing 6
                                xfill True
                                text "🧭 CAMINAR POR EL INSTITUTO" size 16 bold True color "#ffd13b" outlines [(2, "#24031a", 0, 0)] xalign 0.5

                                $ conex = info_actual["conexiones"]

                                if "arriba" in conex:
                                    $ c_arr = conex["arriba"]
                                    $ dest_n = ZONAS_INSTITUTO[c_arr]["nombre"]
                                    $ lock_n = "" if esta_zona_desbloqueada(c_arr) else " 🔒"
                                    textbutton "⬆️ Ir a: [dest_n][lock_n]":
                                        xfill True
                                        action Function(mover_en_mapa, "arriba")
                                        background Frame("images/ui/btn_dark_idle.png", 24, 14, 24, 14)
                                        hover_background Frame("images/ui/btn_dark_hover.png", 24, 14, 24, 14)
                                        padding (12, 6)
                                        text_size 15
                                        text_bold True
                                        text_color "#fff0f6"
                                        text_xalign 0.5

                                hbox:
                                    spacing 8
                                    xfill True
                                    if "izquierda" in conex:
                                        $ c_izq = conex["izquierda"]
                                        $ dest_o = ZONAS_INSTITUTO[c_izq]["nombre"]
                                        $ lock_o = "" if esta_zona_desbloqueada(c_izq) else " 🔒"
                                        textbutton "⬅️ [dest_o][lock_o]":
                                            xfill True
                                            action Function(mover_en_mapa, "izquierda")
                                            background Frame("images/ui/btn_dark_idle.png", 24, 14, 24, 14)
                                            hover_background Frame("images/ui/btn_dark_hover.png", 24, 14, 24, 14)
                                            padding (10, 6)
                                            text_size 14
                                            text_bold True
                                            text_color "#fff0f6"
                                            text_xalign 0.5
                                    if "derecha" in conex:
                                        $ c_der = conex["derecha"]
                                        $ dest_e = ZONAS_INSTITUTO[c_der]["nombre"]
                                        $ lock_e = "" if esta_zona_desbloqueada(c_der) else " 🔒"
                                        textbutton "[dest_e][lock_e] ➡️":
                                            xfill True
                                            action Function(mover_en_mapa, "derecha")
                                            background Frame("images/ui/btn_dark_idle.png", 24, 14, 24, 14)
                                            hover_background Frame("images/ui/btn_dark_hover.png", 24, 14, 24, 14)
                                            padding (10, 6)
                                            text_size 14
                                            text_bold True
                                            text_color "#fff0f6"
                                            text_xalign 0.5

                                if "abajo" in conex:
                                    $ c_aba = conex["abajo"]
                                    $ dest_s = ZONAS_INSTITUTO[c_aba]["nombre"]
                                    $ lock_s = "" if esta_zona_desbloqueada(c_aba) else " 🔒"
                                    textbutton "⬇️ Ir a: [dest_s][lock_s]":
                                        xfill True
                                        action Function(mover_en_mapa, "abajo")
                                        background Frame("images/ui/btn_dark_idle.png", 24, 14, 24, 14)
                                        hover_background Frame("images/ui/btn_dark_hover.png", 24, 14, 24, 14)
                                        padding (12, 6)
                                        text_size 15
                                        text_bold True
                                        text_color "#fff0f6"
                                        text_xalign 0.5

                        if misiones_listas:
                            textbutton "🏮 ¡Ir al Festival Nocturno (Clímax)!":
                                xfill True
                                action Return("ir_climax_festival")
                                background Frame("images/ui/btn_pink_idle.png", 24, 14, 24, 14)
                                hover_background Frame("images/ui/btn_pink_hover.png", 24, 14, 24, 14)
                                padding (14, 8)
                                text_size 17
                                text_bold True
                                text_color "#ffffff"
                                text_xalign 0.5
                        else:
                            textbutton "🔒 Festival Nocturno (Ver Requisitos)":
                                xfill True
                                action Function(registrar_intento_bloqueo, "festival")
                                background Frame("images/ui/btn_purple_idle.png", 24, 14, 24, 14)
                                hover_background Frame("images/ui/btn_purple_hover.png", 24, 14, 24, 14)
                                padding (14, 8)
                                text_size 16
                                text_bold True
                                text_color "#fff0f6"
                                text_xalign 0.5


## 5B. MODAL DE AVISO DE ZONA BLOQUEADA (ESTILO TO LOVE-RU TROUBLE ALERT — 3 INTENTOS)
screen locked_zone_modal():
    modal True
    zorder 210

    $ diag = obtener_diagnostico_bloqueo(zona_modal_bloqueada)
    $ num_int = diag["intentos"]
    $ revelado = diag["revelado"]

    add "#180214eb"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1120
        background Frame(("images/ui/modal_ecchi_tlr.png" if revelado else "images/ui/modal_alert_tlr.png"), 44, 44, 44, 44)
        padding (42, 34)

        vbox:
            spacing 16
            xfill True

            # Cabecera con icono To Love-Ru y botón de cierre
            hbox:
                xfill True
                hbox:
                    spacing 12
                    yalign 0.5
                    add "images/ui/icon_tlr_heart.png" yalign 0.5
                    vbox:
                        if revelado:
                            text "🔓 ¡SECRETO DE PROGRESO REVELADO! (Intento #[num_int])" size 27 bold True color "#ffd13b" outlines [(3, "#24031a", 0, 0)]
                            text "✦ Escáner de Corazones y Tentaciones del Instituto Sakura ✦" size 16 italic True color "#5dfdcb"
                        else:
                            text "🚫 ¡AÚN NO PUEDES ENTRAR ACÁ! (Intento [num_int] de 3)" size 28 bold True color "#ff5ca8" outlines [(3, "#24031a", 0, 0)]
                            text "✦ ¡Trouble Alert! Esta zona requiere avanzar en tu historia romántica ✦" size 16 italic True color "#ffe680"

                textbutton "✖ Cerrar":
                    xalign 1.0
                    yalign 0.5
                    action Hide("locked_zone_modal")
                    background Frame("images/ui/btn_pink_idle.png", 24, 14, 24, 14)
                    hover_background Frame("images/ui/btn_pink_hover.png", 24, 14, 24, 14)
                    padding (22, 8)
                    text_size 19
                    text_bold True
                    text_color "#ffffff"
                    text_outlines [(2, "#4a0528", 0, 0)]

            # Medidor visual de los 3 intentos con cápsulas brillantes
            hbox:
                spacing 14
                xalign 0.5
                frame:
                    background Frame("images/ui/pill_stat_tlr.png", 24, 12, 24, 12)
                    padding (18, 6)
                    text "📍 Zona: [diag['nombre']]" size 19 bold True color "#70e4ff" outlines [(2, "#190212", 0, 0)]

                for idx_i in [1, 2, 3]:
                    frame:
                        background (Frame("images/ui/btn_pink_idle.png", 24, 14, 24, 14) if num_int >= idx_i else Frame("images/ui/pill_stat_tlr.png", 24, 12, 24, 12))
                        padding (16, 6)
                        text ("💖 Intento [idx_i]/3" if num_int >= idx_i else "🔒 Intento [idx_i]/3") size 17 bold True color ("#ffffff" if num_int >= idx_i else "#b892b0")

            frame:
                xfill True
                background Frame("images/ui/panel_inner_tlr.png", 24, 18, 24, 18)
                padding (22, 16)
                vbox:
                    spacing 8
                    text "📢 Aviso del Instituto:" size 19 bold True color "#ffd13b" outlines [(2, "#24031a", 0, 0)]
                    text diag["aviso"] size 19 color "#fff0f6"

            if not revelado:
                frame:
                    xfill True
                    background Frame("images/ui/panel_inner_tlr.png", 24, 18, 24, 18)
                    padding (20, 14)
                    vbox:
                        spacing 6
                        text "🕵️ Radar To Love-Ru (Intentos: [num_int] / 3):" size 19 bold True color "#5dfdcb" outlines [(2, "#190212", 0, 0)]
                        text "Si intentas entrar **3 veces** a esta zona bloqueada (te faltan **[3 - num_int]** intento/s), se activará el **Diagnóstico de Amor y Lujuria** y te dirá **exactamente cuántos puntos de personaje te faltan**." size 18 color "#ffd6eb"

                hbox:
                    spacing 18
                    xalign 0.5
                    textbutton "🚪 Insistir en la Puerta ([num_int]/3 ➔ [num_int + 1]/3)":
                        action Function(registrar_intento_bloqueo, zona_modal_bloqueada)
                        background Frame("images/ui/btn_purple_idle.png", 24, 14, 24, 14)
                        hover_background Frame("images/ui/btn_purple_hover.png", 24, 14, 24, 14)
                        padding (26, 12)
                        text_size 19
                        text_bold True
                        text_color "#ffffff"
                        text_outlines [(2, "#2d0645", 0, 0)]

                    textbutton "🗺️ Volver al Mapa":
                        action Hide("locked_zone_modal")
                        background Frame("images/ui/btn_cyan_idle.png", 24, 14, 24, 14)
                        hover_background Frame("images/ui/btn_cyan_hover.png", 24, 14, 24, 14)
                        padding (26, 12)
                        text_size 19
                        text_bold True
                        text_color "#ffffff"
                        text_outlines [(2, "#062b45", 0, 0)]

            else:
                # 3+ Intentos: Muestra los puntos de personaje exactos que faltan y los hitos pendientes
                frame:
                    xfill True
                    background Frame("images/ui/panel_inner_tlr.png", 24, 18, 24, 18)
                    padding (24, 18)
                    vbox:
                        spacing 9
                        text "💖 PUNTOS DE PERSONAJE NECESARIOS SEGÚN TU PROGRESO:" size 20 bold True color "#5dfdcb" outlines [(2, "#190212", 0, 0)]
                        for p_txt in diag["faltan_puntos"]:
                            text "• " + p_txt size 19 bold True color ("#5dfdcb" if "✔" in p_txt else "#ffb3d9") outlines [(1, "#190212", 0, 0)]

                        if len(diag["faltan_trama"]) > 0:
                            null height 4
                            text "📜 EVENTOS DE LA HISTORIA PENDIENTES:" size 19 bold True color "#ffd13b" outlines [(2, "#24031a", 0, 0)]
                            for t_txt in diag["faltan_trama"]:
                                text "▸ " + t_txt size 18 color "#fff0f6"

                        null height 4
                        text diag["consejo"] size 18 italic True color "#ffe680"

                hbox:
                    spacing 18
                    xalign 0.5
                    textbutton "💖 ¡Entendido, Ir a Conseguir los Puntos!":
                        action Hide("locked_zone_modal")
                        background Frame("images/ui/btn_gold_idle.png", 24, 14, 24, 14)
                        hover_background Frame("images/ui/btn_gold_hover.png", 24, 14, 24, 14)
                        padding (30, 12)
                        text_size 20
                        text_bold True
                        text_color "#2b0318"
                        text_hover_color "#000000"


## 6. Pantalla de Decisión Rápida con Cuenta Regresiva (Estilo To Love-Ru Trouble Rush!)
screen decision_bajo_presion(titulo_alerta, tiempo_limite, resultado_timeout, lista_opciones):
    modal True
    zorder 120

    default tiempo_restante = int(tiempo_limite)

    timer 1.0 repeat True action If(tiempo_restante > 1, SetScreenVariable("tiempo_restante", tiempo_restante - 1), Return(resultado_timeout))

    frame:
        xalign 0.5
        yalign 0.22
        xsize 1140
        background Frame("images/ui/modal_alert_tlr.png", 44, 44, 44, 44)
        padding (38, 28)

        vbox:
            spacing 14
            xfill True
            hbox:
                spacing 10
                xalign 0.5
                add "images/ui/icon_tlr_heart.png" zoom 0.85 yalign 0.5
                text "💥 ¡TROUBLE RUSH! — [titulo_alerta]" size 29 bold True color "#ff5ca8" outlines [(3, "#24031a", 0, 0)] yalign 0.5

            text "⏳ ¡Decide antes de meterte en un lío mayor! ([tiempo_restante] segundos)" size 21 bold True color "#ffd13b" outlines [(2, "#24031a", 0, 0)] xalign 0.5

            bar:
                value AnimatedValue(tiempo_restante, int(tiempo_limite), 0.5)
                xfill True
                ysize 22
                left_bar Frame("images/ui/bar_full_pink.png", 10, 4)
                right_bar Frame("images/ui/bar_empty_tlr.png", 10, 4)

            null height 6

            vbox:
                spacing 12
                xfill True
                for texto_op, valor_retorno in lista_opciones:
                    textbutton "✦ " + texto_op:
                        xfill True
                        action Return(valor_retorno)
                        background Frame("images/ui/btn_dark_idle.png", 24, 14, 24, 14)
                        hover_background Frame("images/ui/btn_pink_hover.png", 24, 14, 24, 14)
                        padding (24, 14)
                        text_size 22
                        text_bold True
                        text_color "#fff0f6"
                        text_hover_color "#ffffff"
                        text_outlines [(2, "#24031a", 0, 0)]
