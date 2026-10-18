################################################################################
## ANIMACIONES Y TRANSFORMACIONES (ATL) — CORREGIDAS Y ESTABILIZADAS
################################################################################

define flash = Fade(0.1, 0.0, 0.4, color="#ffffff")

## Posiciones en pantalla con entrada suave y reseteo limpio de escala/offset
transform pos_left:
    yalign 1.0
    zoom 1.0
    xoffset 0
    yoffset 0
    alpha 1.0
    easein 0.35 xalign 0.15

transform pos_center:
    yalign 1.0
    zoom 1.0
    xoffset 0
    yoffset 0
    alpha 1.0
    easein 0.35 xalign 0.5

transform pos_right:
    yalign 1.0
    zoom 1.0
    xoffset 0
    yoffset 0
    alpha 1.0
    easein 0.35 xalign 0.85

## Entradas dinámicas desde los lados
transform enter_left:
    xalign -0.3 yalign 1.0 alpha 0.0 zoom 1.0 xoffset 0 yoffset 0
    parallel:
        easein_cubic 0.45 xalign 0.16
    parallel:
        linear 0.3 alpha 1.0

transform enter_right:
    xalign 1.3 yalign 1.0 alpha 0.0 zoom 1.0 xoffset 0 yoffset 0
    parallel:
        easein_cubic 0.45 xalign 0.84
    parallel:
        linear 0.3 alpha 1.0

transform enter_center:
    xalign 0.5 yalign 1.05 alpha 0.0 zoom 0.95 xoffset 0 yoffset 0
    parallel:
        easein_back 0.4 yalign 1.0 zoom 1.0
    parallel:
        linear 0.3 alpha 1.0

## Salidas dinámicas
transform exit_left:
    parallel:
        easeout_cubic 0.4 xalign -0.3
    parallel:
        linear 0.35 alpha 0.0

transform exit_right:
    parallel:
        easeout_cubic 0.4 xalign 1.3
    parallel:
        linear 0.35 alpha 0.0

## Emociones de personajes
# Saltito alegre (Genki / Entusiasmo)
transform happy_bounce:
    yoffset 0 xoffset 0
    easein 0.12 yoffset -28
    easeout 0.12 yoffset 0
    easein 0.09 yoffset -15
    easeout 0.09 yoffset 0

# Doble salto de emoción
transform excited_jump:
    yoffset 0 xoffset 0
    block:
        easein 0.14 yoffset -32
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
    easein 0.35 yoffset 22 zoom 0.97
    linear 0.08 xoffset -4
    linear 0.08 xoffset 4
    linear 0.08 xoffset 0
    pause 0.25
    easeout 0.3 yoffset 0 zoom 1.0

# Acercamiento íntimo / romántico (SIEMPRE asegura xalign 0.5 e yalign 1.0)
transform closeup_romance:
    xalign 0.5
    yalign 1.0
    alpha 1.0
    xoffset 0
    easein_cubic 0.45 zoom 1.14 yoffset 35

transform reset_zoom:
    xalign 0.5
    yalign 1.0
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
