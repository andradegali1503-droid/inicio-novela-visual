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

## ============================================================================
## NUEVAS REACCIONES CORPORALES Y ANIMACIONES DE CONEXIÓN EMOCIONAL (ATL)
## ============================================================================

# Latido romántico (Doki-Doki: cuando la heroína siente mariposas o amor intenso)
transform heartbeat_throb:
    yoffset 0 xoffset 0
    easein 0.14 zoom 1.05 yoffset -6
    easeout 0.14 zoom 1.0 yoffset 0
    pause 0.06
    easein 0.12 zoom 1.04 yoffset -4
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
    easein_quad 0.30 xoffset 14 yoffset -6 zoom 1.04
    easeout_quad 0.30 xoffset -10 yoffset 0 zoom 1.02
    easein_quad 0.25 xoffset 0 yoffset 0 zoom 1.0

# Sobresalto de sorpresa (¡Eh?!: brinco repentino cuando la toman desprevenida)
transform surprised_pop:
    yoffset 0 xoffset 0
    easein_back 0.14 yoffset -36 zoom 1.05
    easeout_bounce 0.24 yoffset 0 zoom 1.0

# Acercamiento susurrante ultra-cercano (Lean-in close: susurro al oído o beso)
transform lean_in_close:
    xalign 0.5
    yalign 1.0
    alpha 1.0
    xoffset 0
    easein_cubic 0.40 zoom 1.22 yoffset 60

# Suspiro / Alivio / Melancolía suave
transform sigh_sink:
    yoffset 0 xoffset 0
    easein 0.25 yoffset -8
    easeout 0.45 yoffset 16
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

