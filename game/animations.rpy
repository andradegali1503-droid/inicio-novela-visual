################################################################################
## ANIMACIONES Y TRANSFORMACIONES (ATL) — CORREGIDAS Y ESTABILIZADAS
################################################################################

define flash = Fade(0.1, 0.0, 0.4, color="#ffffff")

## Posiciones en pantalla con centrado exacto (xanchor 0.5, yanchor 1.0) para lienzos 700x940
transform pos_left:
    xanchor 0.5
    yanchor 1.0
    ypos 1.0
    zoom 1.0
    xoffset 0
    yoffset 0
    alpha 1.0
    easein 0.35 xpos 0.22

transform pos_center:
    xanchor 0.5
    yanchor 1.0
    ypos 1.0
    zoom 1.0
    xoffset 0
    yoffset 0
    alpha 1.0
    easein 0.35 xpos 0.50

transform pos_right:
    xanchor 0.5
    yanchor 1.0
    ypos 1.0
    zoom 1.0
    xoffset 0
    yoffset 0
    alpha 1.0
    easein 0.35 xpos 0.78

## Entradas dinámicas desde los lados
transform enter_left:
    xanchor 0.5 yanchor 1.0 xpos -0.20 ypos 1.0 alpha 0.0 zoom 1.0 xoffset 0 yoffset 0
    parallel:
        easein_cubic 0.45 xpos 0.22
    parallel:
        linear 0.3 alpha 1.0

transform enter_right:
    xanchor 0.5 yanchor 1.0 xpos 1.20 ypos 1.0 alpha 0.0 zoom 1.0 xoffset 0 yoffset 0
    parallel:
        easein_cubic 0.45 xpos 0.78
    parallel:
        linear 0.3 alpha 1.0

transform enter_center:
    xanchor 0.5 yanchor 1.0 xpos 0.50 ypos 1.04 alpha 0.0 zoom 0.96 xoffset 0 yoffset 0
    parallel:
        easein_back 0.4 ypos 1.0 zoom 1.0
    parallel:
        linear 0.3 alpha 1.0

## Salidas dinámicas
transform exit_left:
    parallel:
        easeout_cubic 0.4 xpos -0.25
    parallel:
        linear 0.35 alpha 0.0

transform exit_right:
    parallel:
        easeout_cubic 0.4 xpos 1.25
    parallel:
        linear 0.35 alpha 0.0

## Emociones de personajes
# Saltito alegre (Genki / Entusiasmo)
transform happy_bounce:
    yoffset 0 xoffset 0
    easein 0.12 yoffset -26
    easeout 0.12 yoffset 0
    easein 0.09 yoffset -14
    easeout 0.09 yoffset 0

# Doble salto de emoción
transform excited_jump:
    yoffset 0 xoffset 0
    block:
        easein 0.14 yoffset -28
        easeout 0.14 yoffset 0
        repeat 2

# Temblor de enfado (Tsundere / Furia)
transform anger_shake:
    xoffset 0 yoffset 0
    linear 0.04 xoffset -12 yoffset -4
    linear 0.04 xoffset 12 yoffset 4
    linear 0.04 xoffset -10 yoffset 2
    linear 0.04 xoffset 10 yoffset -2
    linear 0.04 xoffset -6 yoffset 0
    linear 0.04 xoffset 6 yoffset 0
    linear 0.04 xoffset 0 yoffset 0

# Hundirse por timidez o vergüenza (Kuudere / Sonrojo)
transform shy_sink:
    yoffset 0 xoffset 0 zoom 1.0
    easein 0.35 yoffset 18 zoom 0.98
    linear 0.08 xoffset -4
    linear 0.08 xoffset 4
    linear 0.08 xoffset 0
    pause 0.25
    easeout 0.3 yoffset 0 zoom 1.0

# Acercamiento íntimo / romántico centrado sin cortar la cabeza
transform closeup_romance:
    xanchor 0.5
    yanchor 1.0
    xpos 0.50
    ypos 1.0
    alpha 1.0
    xoffset 0
    easein_cubic 0.42 zoom 1.10 yoffset 28

transform reset_zoom:
    xanchor 0.5
    yanchor 1.0
    xpos 0.50
    ypos 1.0
    xoffset 0
    easeout_cubic 0.35 zoom 1.0 yoffset 0

# Sacudida de cámara / pantalla para accidentes y comedia
transform camera_shake:
    xalign 0.5 yalign 0.5
    xoffset 0 yoffset 0
    linear 0.05 xoffset -16 yoffset 10
    linear 0.05 xoffset 16 yoffset -10
    linear 0.05 xoffset -12 yoffset -8
    linear 0.05 xoffset 12 yoffset 8
    linear 0.05 xoffset -6 yoffset 4
    linear 0.05 xoffset 0 yoffset 0

# Efecto de latido para marcadores de interfaz
transform pulse_glow:
    zoom 1.0
    easein 0.25 zoom 1.04
    easeout 0.25 zoom 1.0

# Animación para notificaciones emergentes de puntos
transform popup_float:
    alpha 0.0 yoffset 15 zoom 0.9
    parallel:
        easein_back 0.25 alpha 1.0 yoffset 0 zoom 1.0
    pause 2.2
    parallel:
        easeout 0.35 alpha 0.0 yoffset -20

## ============================================================================
## NUEVAS REACCIONES CORPORALES Y ANIMACIONES DE CONEXIÓN EMOCIONAL (ATL)
## ============================================================================

# Latido romántico (Doki-Doki: cuando la heroína siente mariposas o amor intenso)
transform heartbeat_throb:
    yoffset 0 xoffset 0
    easein 0.14 zoom 1.04 yoffset -5
    easeout 0.14 zoom 1.0 yoffset 0
    pause 0.06
    easein 0.12 zoom 1.03 yoffset -3
    easeout 0.18 zoom 1.0 yoffset 0

# Nerviosismo / Rubor intenso (Flustered wobble: balanceo tímido de un lado a otro)
transform fluster_wobble:
    yoffset 0 xoffset 0
    easein 0.10 xoffset -10 yoffset 4
    easeout 0.10 xoffset 10 yoffset 0
    easein 0.10 xoffset -8 yoffset 4
    easeout 0.10 xoffset 8 yoffset 0
    easein 0.08 xoffset -4 yoffset 2
    easeout 0.08 xoffset 0 yoffset 0

# Contoneo seductor (Modo Darkness: movimiento hipnótico para Kuroe, Mirei y Reina)
transform seductive_sway:
    yoffset 0 xoffset 0
    easein_quad 0.30 xoffset 12 yoffset -4 zoom 1.03
    easeout_quad 0.30 xoffset -10 yoffset 0 zoom 1.01
    easein_quad 0.25 xoffset 0 yoffset 0 zoom 1.0

# Sobresalto de sorpresa (¡Eh?!: brinco repentino cuando la toman desprevenida)
transform surprised_pop:
    yoffset 0 xoffset 0
    easein_back 0.14 yoffset -28 zoom 1.04
    easeout_bounce 0.24 yoffset 0 zoom 1.0

# Acercamiento susurrante ultra-cercano (Lean-in close: susurro al oído o beso)
transform lean_in_close:
    xanchor 0.5
    yanchor 1.0
    xpos 0.50
    ypos 1.0
    alpha 1.0
    xoffset 0
    easein_cubic 0.40 zoom 1.15 yoffset 42

# Suspiro / Alivio / Melancolía suave
transform sigh_sink:
    yoffset 0 xoffset 0
    easein 0.25 yoffset -6
    easeout 0.45 yoffset 14
    pause 0.15
    easein 0.30 yoffset 0

# Animación de aparición y flotación para los iconos de reacción anime (💕, 💢, ❗, 💧, ✨, 🔥)
transform emote_pop_anim:
    alpha 0.0 zoom 0.2 yoffset 30
    easein_back 0.28 alpha 1.0 zoom 1.12 yoffset -12
    easeout 0.14 zoom 1.0 yoffset 0
    block:
        easein 0.35 yoffset -10
        easeout 0.35 yoffset 0
        repeat 2
    easeout 0.30 alpha 0.0 yoffset -28 zoom 0.85

# Resplandor ambiental para momentos románticos o de tentación Darkness
transform mood_glow_fade:
    alpha 0.0
    easein 0.30 alpha 0.28
    pause 1.25
    easeout 0.45 alpha 0.0

## ============================================================================
## SISTEMA DE PARTÍCULAS ATMOSFÉRICAS Y CINEMÁTICA DE MENÚ
## ============================================================================

# Lluvia de pétalos de cerezo suaves y translúcidos
image sakura_petals = Fixed(
    SnowBlossom("images/ui/sakura_petal1.png", count=24, border=50, xspeed=(25, 75), yspeed=(55, 120), start=3.0, fast=True, horizontal=False),
    SnowBlossom("images/ui/sakura_petal2.png", count=16, border=50, xspeed=(35, 90), yspeed=(70, 145), start=1.5, fast=True, horizontal=False)
)

# Movimiento de cámara suave / cinemático para el Menú Principal
transform bg_menu_drift:
    zoom 1.04
    xalign 0.5 yalign 0.5
    ease 9.0 zoom 1.08 xalign 0.52 yalign 0.48
    ease 9.0 zoom 1.04 xalign 0.50 yalign 0.50
    repeat

# Sutil palpitación para el título principal
transform menu_title_pulse:
    zoom 1.0
    ease 2.5 zoom 1.015
    ease 2.5 zoom 1.0
    repeat

## ============================================================================
## TRANSICIONES CINEMÁTICAS TEMÁTICAS SEGÚN CADA ESCENA Y AMBIENTE
## ============================================================================

define loc_transition = Fade(0.18, 0.05, 0.25, color="#14021c")
define loc_fade = Fade(0.22, 0.05, 0.28, color="#14021c")
define loc_push = PushMove(0.35, "pushleft")

# 1. Transición Romántica Flor de Cerezo / Akane (Rosa pasión)
define trans_romance_pink = Fade(0.22, 0.06, 0.32, color="#ff4d6d")
define trans_doki = Fade(0.18, 0.05, 0.28, color="#ff758f")

# 2. Transición Ciencia Serena / Laboratorio / Yuki (Azul cian brillante)
define trans_romance_cyan = Fade(0.22, 0.06, 0.32, color="#00b4d8")
define trans_lab = Fade(0.20, 0.05, 0.30, color="#061b2e")

# 3. Transición Dorada Enérgica / Sol de Mañana / Hana (Ámbar brillante)
define trans_romance_gold = Fade(0.22, 0.06, 0.32, color="#ffb703")

# 4. Transición Modo Darkness Seductor / Biblioteca / Tentación (Púrpura noche)
define trans_darkness = Fade(0.26, 0.08, 0.36, color="#1c0028")
define trans_darkness_lab = Fade(0.24, 0.07, 0.34, color="#250338")
define trans_darkness_gym = Fade(0.24, 0.07, 0.34, color="#341200")

# 5. Transición Dorada Crepúsculo / Azotea / Atardecer
define trans_sunset = Fade(0.28, 0.08, 0.38, color="#ff7b00")

# 6. Transición Nocturna del Festival y Fuegos Artificiales
define trans_festival = Fade(0.32, 0.10, 0.42, color="#090622")
define trans_fireworks_flash = Fade(0.08, 0.04, 0.30, color="#ffd166")

# 7. Transición de Sala del Consejo / Akane
define trans_council = Fade(0.22, 0.06, 0.30, color="#2b0318")

# 8. Transiciones de Comedia / Tropezón Ecchi / Alerta
define trans_shock_flash = Fade(0.06, 0.03, 0.20, color="#ffffff")
define trans_disaster = Fade(0.12, 0.08, 0.28, color="#d90429")

# 9. Transiciones de Navegación de Mapa y Capítulos
define trans_map_slide_left = PushMove(0.32, "pushleft")
define trans_map_slide_right = PushMove(0.32, "pushright")
define trans_iris_out = CropMove(0.40, "irisout")
define trans_iris_in = CropMove(0.40, "irisin")
define trans_cinematic_dissolve = Dissolve(0.42)

## ============================================================================
## TRANSFORMACIONES ATL DINÁMICAS PARA SITUACIONES ESPECÍFICAS
## ============================================================================

# Tropiezo cómico de frente estilo anime ecchi (To Love-Ru fall)
transform comic_trip:
    xalign 0.5 yalign 0.5
    yoffset 0 xoffset 0 zoom 1.0
    easein 0.08 yoffset -18 xoffset 8 zoom 1.02
    easeout 0.12 yoffset 24 xoffset -12 zoom 0.98
    linear 0.04 xoffset 14 yoffset -6
    linear 0.04 xoffset -10 yoffset 4
    linear 0.04 xoffset 0 yoffset 0 zoom 1.0

# Embestida Tsundere: Akane da un paso agresivo al frente y se detiene avergonzada
transform tsundere_strike:
    yoffset 0 xoffset 0
    easein_back 0.16 yoffset -16 xoffset 10 zoom 1.04
    easeout 0.20 yoffset 0 xoffset 0 zoom 1.0

# Salto alegre genki: Hana dando saltitos de emoción
transform genki_hop:
    yoffset 0 xoffset 0
    easein 0.11 yoffset -32 xoffset 4
    easeout 0.11 yoffset 0 xoffset 0
    easein 0.09 yoffset -18 xoffset -4
    easeout 0.09 yoffset 0 xoffset 0

# Inclinación reflexiva Kuudere: Yuki ladea la cabeza analizando una situación
transform kuudere_tilt:
    yoffset 0 xoffset 0
    easein 0.24 yoffset 6 xoffset -6
    easeout 0.24 yoffset 0 xoffset 0

# Respiración seductora / Contoneo tentación Darkness: Kuroe, Mirei, Reina
transform sway_temptation:
    yoffset 0 xoffset 0
    easein 0.35 xoffset 14 yoffset -4 zoom 1.03
    easeout 0.35 xoffset -14 yoffset 0 zoom 1.01
    easein 0.30 xoffset 0 yoffset 0 zoom 1.0

# Doki-Zoom: Acercamiento repentino por latido acelerado
transform doki_zoom:
    yoffset 0 zoom 1.0
    easein 0.16 zoom 1.06 yoffset 14
    easeout 0.22 zoom 1.0 yoffset 0

# Animación para el banner de ubicación / escena
transform location_banner_anim:
    xoffset -700 alpha 0.0
    easein_cubic 0.38 xoffset 0 alpha 1.0
    pause 2.2
    easeout_cubic 0.35 xoffset -700 alpha 0.0



