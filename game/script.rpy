################################################################################
## CRÓNICAS DEL INSTITUTO SAKURA: ¡LÍOS EN EL FESTIVAL!
## Guion Completo: 3 Heroínas Principales + 3 Sub-Personajes de Tentación + Mapa
################################################################################

## 1. Definición de Imágenes de Fondo (1920x1080)
image bg classroom = "images/bg_classroom.png"
image bg council = "images/bg_council.png"
image bg rooftop = "images/bg_rooftop.png"
image bg festival = "images/bg_festival.png"
image bg library = "images/bg_library.png"
image bg courtyard = "images/bg_courtyard.png"

## 2. Definición de Sprites de las 3 HEROÍNAS PRINCIPALES (Historia Central)
# Akane Tachibana (Tsundere - Presidenta del Consejo Estudiantil)
image akane normal = "images/akane_normal.png"
image akane angry = "images/akane_angry.png"
image akane blush = "images/akane_blush.png"

# Yuki Shirogane (Kuudere - Genio del Club de Ciencias)
image yuki normal = "images/yuki_normal.png"
image yuki smile = "images/yuki_smile.png"
image yuki shy = "images/yuki_shy.png"

# Hana Sakuragi (Genki - Estrella de Atletismo)
image hana normal = "images/hana_normal.png"
image hana happy = "images/hana_happy.png"
image hana sad = "images/hana_sad.png"

## 3. Definición de Sprites de las 3 SUB-PERSONAJES (Lujuria y Tentación)
# Kuroe Sakamoto (La Chica Mala Rebelde - Conectada a la ruta de Akane)
image kuroe normal = "images/kuroe_normal.png"
image kuroe seductive = "images/kuroe_seductive.png"
image kuroe angry = "images/kuroe_angry.png"

# Mirei Kanzaki (La Sempai Seductora de Ciencias - Conectada a la ruta de Yuki)
image mirei normal = "images/mirei_normal.png"
image mirei seductive = "images/mirei_seductive.png"
image mirei angry = "images/mirei_angry.png"

# Reina Kurokawa (La Capitana Ardiente de Ed. Física - Conectada a la ruta de Hana)
image reina normal = "images/reina_normal.png"
image reina seductive = "images/reina_seductive.png"
image reina angry = "images/reina_angry.png"

## 4. Definición de Personajes
define leo = Character("[nombre_prota]", color="#ffd166", what_prefix="«", what_suffix="»")
# Heroínas Principales
define akane = Character("Akane Tachibana", color="#ff4d6d")
define yuki = Character("Yuki Shirogane", color="#4cc9f0")
define hana = Character("Hana Sakuragi", color="#ff85a1")
# Sub-Personajes (Tentaciones)
define kuroe = Character("Kuroe Sakamoto (Chica Mala)", color="#e0aaff")
define mirei = Character("Mirei Kanzaki (Sempai Ciencias)", color="#c77dff")
define reina = Character("Reina Kurokawa (Capitana Ed. Física)", color="#ff9e00")

define narrador = Character(None, what_italic=True, what_color="#e2eafc")


################################################################################
## INICIO DE LA HISTORIA — PRÓLOGO: EL CHICO QUE SE METE EN PROBLEMAS
################################################################################

label start:
    $ mostrar_hud = True
    show screen stats_hud

    scene bg courtyard with fade

    narrador "Instituto Privado Sakura. Último día de preparativos antes del gran Festival Cultural de Otoño."
    narrador "Para la mayoría de los estudiantes, hoy es un día de emoción, romances inocentes y puestos de comida..."
    narrador "Pero para mí, las cosas están a punto de complicarse con las seis chicas más intensas de todo el instituto."

    python:
        nombre_ingresado = renpy.input("¿Cómo te llamas, estudiante problemático?", default="Leo", length=18)
        nombre_ingresado = nombre_ingresado.strip()
        if nombre_ingresado:
            nombre_prota = nombre_ingresado

    leo "Vale, soy [nombre_prota]. Solo tenía una tarea sencilla hoy: llevar las cajas de decoraciones hasta el almacén sin meterme en líos."
    leo "Pero antes de salir corriendo por el pasillo... ¿cuál diría todo el mundo que es mi mayor virtud cuando las cosas se salen de control?"

    menu:
        "⚡ Mi mente rápida e ingenio para improvisar planes (+15%% Ingenio)":
            $ cambiar_stat("ingenio", 15, "Talento innato")
            $ registrar_rama("Talento: Mente Brillante", "Elegiste destacar por tu ingenio táctico desde el inicio.", "+15% Ingenio")
            leo "Siempre encuentro un truco o una salida lógica cuando nadie más la ve."

        "✨ Mi carisma y magnetismo con las chicas (+15%% Carisma)":
            $ cambiar_stat("carisma", 15, "Encanto natural")
            $ registrar_rama("Talento: Corazón Carismático", "Elegiste destacar por tu magnetismo y encanto personal.", "+15% Carisma")
            leo "Puede que me meta en problemas, pero ninguna chica del instituto puede ignorarme."

        "★ Mi sentido del honor para dar la cara (+15%% Reputación)":
            $ cambiar_stat("reputacion", 15, "Fama de valiente")
            $ registrar_rama("Talento: Espíritu Honorable", "Comenzaste ganándote el respeto del instituto.", "+15% Reputación")
            leo "Aunque todo salga al revés, siempre cumplo mis promesas hasta el final."

    show hana normal at enter_right
    with dissolve
    show hana normal at happy_bounce

    hana "¡Eh, [nombre_prota]! ¡Buenos días! ¿Ya estás cargando todas esas cajas tú solo?"
    leo "¡Hana! Justo a tiempo. El profesor me dijo que si no llevo esto a la Sala del Consejo en dos minutos, me castigará limpiando el gimnasio todo el mes."

    show hana happy at pos_right
    hana "¡Jajaja, típico de ti! ¡Ven, te abro las puertas del edificio principal para que tomes el atajo!"

    scene bg council at camera_shake with vpunch

    narrador "¡CRASH! ¡BUM! ¡CATAPUM!"
    narrador "Al doblar la esquina a toda velocidad, tropiezas con una alfombra recién encerada y entras volando como un meteorito directamente en la Sala del Consejo Estudiantil."

    show akane angry at enter_left
    show yuki normal at enter_center
    show hana sad at enter_right
    with dissolve

    show akane angry at anger_shake
    akane "¡¿PERO QUÉ DEMONIOS ESTÁ PASANDO AQUÍ?!"

    yuki "Alerta crítica. La torre de cajas del presupuesto, los permisos del festival y mi proyector holográfico están perdiendo el equilibrio..."

    hana "¡Cuidado, [nombre_prota]! ¡La estantería principal se viene abajo sobre nosotras!"

    ## DECISIÓN BAJO PRESIÓN CON TEMPORIZADOR (8 SEGUNDOS)
    call screen decision_bajo_presion(
        "¡LA ESTANTERÍA DEL CONSEJO SE DERRUMBA!",
        8,
        "timeout_desastre",
        [
            ("🛡️ Lanzarme para proteger a Akane y salvar los documentos del Consejo", "salvar_akane"),
            ("🔬 Saltar hacia Yuki para atrapar su proyector holográfico en el aire", "salvar_yuki"),
            ("🌸 Empujar a Hana fuera del peligro y amortiguar la caída con mi cuerpo", "salvar_hana")
        ]
    )

    $ eleccion_accidente = _return

    if eleccion_accidente == "salvar_akane":
        show akane blush at pos_left, shy_sink
        $ cambiar_afinidad("akane", 15, "¡La protegiste!")
        $ cambiar_stat("reputacion", 10, "Reflejos heroicos")
        $ cambiar_stat("festival", 5, "Documentos salvados")
        $ registrar_rama("Escudo de la Presidenta", "Protegiste a Akane del derrumbe en la Sala del Consejo.", "+15% ♥ Akane, +5% Festival")

        leo "¡Cuidado, Presidenta!"
        narrador "Rodeas a Akane con tus brazos y detienes la caja más pesada con el hombro, quedando a pocos centímetros de su rostro."
        akane "¡¿Eh?! ¡O-oye! ¡Estás demasiado cerca, idiota...! Pe-pero... gracias por salvar los documentos."

    elif eleccion_accidente == "salvar_yuki":
        show yuki shy at pos_center, shy_sink
        $ cambiar_afinidad("yuki", 15, "¡Salvaste su invento!")
        $ cambiar_stat("ingenio", 10, "Cálculo de trayectoria")
        $ cambiar_stat("festival", 5, "Lente intacta")
        $ registrar_rama("Salvador de la Ciencia", "Atrapaste el prototipo de Yuki antes de que se hiciera añicos.", "+15% ♥ Yuki, +5% Festival")

        leo "¡El proyector no toca el suelo mientras yo esté aquí!"
        narrador "Deslizas las rodillas por el parqué y atrapas el delicado cristal de Yuki a un centímetro del suelo, sosteniendo también su mano."
        yuki "Mis pulsaciones acaban de subir un 42 por ciento... Has protegido semanas de mi trabajo, [nombre_prota]."

    elif eleccion_accidente == "salvar_hana":
        show hana happy at pos_right, happy_bounce
        $ cambiar_afinidad("hana", 15, "¡La pusiste a salvo!")
        $ cambiar_stat("carisma", 10, "Valentía")
        $ cambiar_stat("festival", 5, "Hana a salvo")
        $ registrar_rama("Guardián de Hana", "Recibiste el golpe para que Hana no se lastimara antes de su exhibición.", "+15% ♥ Hana, +5% Festival")

        leo "¡Hana, detrás de mí!"
        narrador "Apartas a Hana con suavidad y recibes una lluvia de serpentinas y carpetas sobre la cabeza."
        hana "¡[nombre_prota]! ¡Estuviste increíble, como un héroe de película! ¿Estás bien?"

    else:
        scene bg council at camera_shake with hpunch
        show akane angry at pos_left, anger_shake
        show yuki normal at pos_center
        show hana sad at pos_right
        $ cambiar_afinidad("akane", 5, "Preocupación por el golpe")
        $ cambiar_afinidad("yuki", 5, "Preocupación por el golpe")
        $ cambiar_afinidad("hana", 5, "Preocupación por el golpe")
        $ registrar_rama("Tropiezo de Comedia", "Terminaste sepultado bajo una montaña de cajas, despertando la compasión de las chicas.", "+5% ♥ con todas")

        leo "¡Uwahhh! ¿A quién ayudo primero?"
        narrador "intentas protegerlas a las tres a la vez y una avalancha de papeles y purpurina te cubre de pies a cabeza."

    show akane angry at pos_left, anger_shake
    akane "¡MIRA ESTE DESASTRE, [nombre_prota!u]! ¡Los permisos se han perdido, el proyector de Yuki está dañado y la exhibición de Hana peligra!"
    akane "Escúchame bien: tienes hasta el anochecer para recorrer el instituto y resolver los problemas de nosotras tres."

    yuki "Pero ten cuidado mientras te mueves por el campus, [nombre_prota]..."
    yuki "Para resolver nuestros problemas tendrás que tratar con tres chicas muy peligrosas: **Kuroe** la rebelde, **Mirei** mi sempai del laboratorio y **Reina** la capitana de educación física."

    hana "¡Eso es! Ellas tres son súper atractivas y les encanta tentar a los chicos para meterlos en líos... ¡Si te enredas con ellas, más te vale cortar las cosas a tiempo o todo terminará en escándalo!"

    menu:
        "«¡Os prometo que os ayudaré a las tres y no dejaré que ninguna tentación me desvíe!»":
            $ consecuencia_culpa_asumida = True
            $ cambiar_stat("reputacion", 10, "Promesa firme")
            $ cambiar_afinidad("akane", 5)
            $ cambiar_afinidad("yuki", 5)
            $ cambiar_afinidad("hana", 5)
            $ registrar_rama("Promesa de Honor", "Juraste lealtad a las tres heroínas principales frente a las tentaciones.", "+10% Reputación y +5% ♥ con todas")

        "«Bueno... si tengo que usar mis encantos con esas tres chicas para salvar el festival, ¡me sacrificaré por el equipo!»":
            $ cambiar_stat("carisma", 10, "Espíritu seductor")
            $ cambiar_tentacion("kuroe", 10, "Actitud atrevida")
            $ cambiar_tentacion("mirei", 10, "Actitud atrevida")
            $ cambiar_tentacion("reina", 10, "Actitud atrevida")
            $ registrar_rama("Jugando con Fuego", "Decidiste que no te importaría tentar a la suerte con las sub-personajes.", "+10% Carisma, +10% 🔥 Lujuria")
            show akane angry at pos_left, anger_shake
            akane "¡¿Qué 'sacrificio' ni qué ocho cuartos, pervertido?! ¡Más te vale comportarte!"

    hide akane
    hide yuki
    hide hana
    with dissolve

    $ ubicacion_actual = "patio"
    jump hub_instituto


################################################################################
## ACTO 2 — NAVEGACIÓN LIBRE POR EL MAPA DEL INSTITUTO SAKURA
################################################################################

label hub_instituto:
    scene bg courtyard with dissolve

    call screen school_hub_selector
    $ destino_elegido = _return

    if destino_elegido == "ir_climax_festival":
        jump confirmar_ir_festival

    jump expression destino_elegido


label confirmar_ir_festival:
    $ pendientes_sub = obtener_estado_sub_Pendiente()

    if not (actas_entregadas_akane and bobina_instalada_yuki and pase_entregado_hana):
        $ e_num, e_max, o_txt, o_zona = obtener_objetivo_actual()
        narrador "🔒 **Aún no puedes avanzar al Festival Nocturno (Etapa [e_num]/[e_max]).**"
        narrador "🎯 **Objetivo actual de la trama:** [o_txt]."
        jump hub_instituto
    elif len(pendientes_sub) > 0:
        narrador "🔥 ¡ATENCIÓN! Te has enredado en aventuras ardientes con: **[', '.join(pendientes_sub)]**."
        narrador "Para poder finalizar la historia principal con Akane, Yuki o Hana, **debes terminar tu aventura con las sub-personajes** antes de que empiece la ceremonia (o enfrentarte a ellas ahora mismo)."
        menu:
            "🗺️ Ir por el mapa a terminar con ellas en sus zonas antes del festival":
                jump hub_instituto
            "🔥 Enfrentar a las sub-personajes ahora mismo entre bastidores antes del Festival":
                jump verificar_rupturas_antes_climax
    else:
        narrador "¡Has completado las misiones principales y tienes todos tus asuntos bajo control! ¿Listo para el gran Festival Cultural Nocturno?"
        menu:
            "🏮 ¡Sí, iniciar la Noche del Festival Cultural!":
                jump climax_festival
            "🗺️ Seguir explorando el instituto un poco más":
                jump hub_instituto


################################################################################
## ZONA 1: SALA DEL CONSEJO ESTUDIANTIL (PRINCIPAL: AKANE TACHIBANA)
################################################################################

label zona_consejo:
    $ zonas_exploradas.add("consejo")
    scene bg council with dissolve

    if visitado_akane:
        show akane normal at enter_center
    else:
        show akane angry at enter_center

    narrador "📍 Estás en la **Sala del Consejo Estudiantil** (Planta Noble). El centro de mando de **Akane Tachibana**."

    label menu_zona_consejo:
        menu:
            "❗ «ETAPA 1 — HISTORIA PRINCIPAL» Ayudar a Akane con la crisis del Consejo y el Subdirector" if not visitado_akane:
                $ visitado_akane = True
                $ turnos_dia -= 1
                jump evento_akane

            "📂 «ETAPA 3 — PROGRESO» Entregar a Akane las 'Actas Secretas Recuperadas' de Kuroe (+20 ♥ Akane, Desbloquea Laboratorio)" if ("Actas Secretas Recuperadas" in inventario_items and not actas_entregadas_akane):
                $ actas_entregadas_akane = True
                $ cambiar_afinidad("akane", 20, "¡Recuperaste los sellos de Kuroe!")
                $ cambiar_stat("festival", 15, "Permisos completos")
                $ notificar_cambio("🔓 ¡ZONA DESBLOQUEADA: Laboratorio de Ciencias (Yuki)!", "#4cc9f0")
                show akane blush at closeup_romance, happy_bounce
                leo "Akane, conseguí que Kuroe me devolviera las carpetas que faltaban del Consejo."
                akane "¡¿Qué?! ¡¿Lograste que esa rebelde imposible entrara en razón?! N-no sé cómo lo hiciste, [nombre_prota], ¡pero me has salvado la vida!"
                akane "Con esto ya tengo el permiso firmado para abrirte el **Laboratorio de Ciencias del Ala Este**. ¡Ve a ayudar a **Yuki Shirogane** con el proyector holográfico!"
                if estado_sub_kuroe == "Enredado" and not ruptura_sub_kuroe:
                    narrador "(Recuerdas los labios de Kuroe en la biblioteca... Sabes que tendrás que ir a la Biblioteca a **terminar con Kuroe** antes de que Akane descubra el trato que hiciste con ella)."
                show akane blush at reset_zoom
                jump menu_zona_consejo

            "🎁 Regalar 'Té Real de Durazno' a Akane (+15 ♥ Akane)" if ("Té Real de Durazno" in inventario_items and not regalo_entregado_akane):
                $ regalo_entregado_akane = True
                $ cambiar_afinidad("akane", 15, "¡Su bebida favorita!")
                $ registrar_rama("Detalle Dulce para la Presidenta", "Le llevaste en secreto su Té Real de Durazno favorito.", "+15 ♥ Akane")
                show akane blush at closeup_romance, happy_bounce
                leo "Pasé por la cafetería y traje tu Té Real de Durazno favorito."
                akane "¡¿C-cómo sabías que me encanta?! No pienses que con esto me tienes ganada... aunque está riquísimo. Gracias."
                show akane blush at reset_zoom
                jump menu_zona_consejo

            "💬 Conversar con Akane" if visitado_akane:
                show akane blush at pos_center
                if afinidad_akane < 50:
                    $ cambiar_afinidad("akane", 10, "Apoyo en el Consejo")
                if not actas_entregadas_akane:
                    akane "¡Date prisa, [nombre_prota]! Ve a la **Biblioteca Oeste**, recupérale las **Actas Secretas** a **Kuroe** y tráemelas para que pueda abrirte el Laboratorio de Ciencias."
                else:
                    akane "Oye, [nombre_prota]... Prométeme que no estás tonteando con Kuroe ni con ninguna otra mientras me ayudas, ¿eh? Confío en ti."
                jump menu_zona_consejo

            "🗺️ Abrir el Mapa del Instituto":
                hide akane with dissolve
                jump hub_instituto


################################################################################
## ZONA 2: LABORATORIO Y ALMACÉN QUÍMICO (PRINCIPAL: YUKI | SUB: MIREI)
################################################################################

label zona_laboratorio:
    if not esta_zona_desbloqueada("laboratorio"):
        $ notificar_cambio(obtener_motivo_bloqueo_zona("laboratorio"), "#ff4d6d")
        jump hub_instituto

    $ zonas_exploradas.add("laboratorio")
    scene bg classroom with dissolve

    if not visitado_yuki:
        show yuki normal at enter_center
        with dissolve
        narrador "📍 Estás en el **Laboratorio de Ciencias** (Ala Este). **Yuki Shirogane** intenta estabilizar en solitario el Proyector Holográfico."
    else:
        show yuki normal at enter_left
        show mirei seductive at enter_right
        with dissolve
        narrador "📍 Estás en el **Laboratorio de Ciencias** (Ala Este). **Yuki Shirogane** ajusta el proyector mientras la voluptuosa sempai **Mirei Kanzaki** te hace señas desde la puerta del almacén químico."

    label menu_zona_laboratorio:
        menu:
            "❗ «ETAPA 4 — HISTORIA PRINCIPAL» Ayudar a Yuki a reparar el Proyector Holográfico" if not visitado_yuki:
                $ visitado_yuki = True
                $ turnos_dia -= 1
                jump evento_yuki

            "💋 «ETAPA 5 — SUB-RUTA MIREI» Seguir a la sempai Mirei al almacén químico por la Bobina Experimental" if (esta_zona_desbloqueada("almacen_mirei") and not encuentro_sub_mirei):
                hide yuki with dissolve
                jump sub_evento_mirei

            "🔒 Almacén Químico de Mirei «Área Bloqueada»" if not esta_zona_desbloqueada("almacen_mirei"):
                $ zona_modal_bloqueada = "almacen_mirei"
                $ intentos_bloqueo_zona["almacen_mirei"] = intentos_bloqueo_zona.get("almacen_mirei", 0) + 1
                call screen locked_zone_modal
                jump menu_zona_laboratorio

            "💔 «TERMINAR CON MIREI» Cortar tu aventura secreta con Mirei para proteger tu relación con Yuki" if (estado_sub_mirei == "Enredado" and not ruptura_sub_mirei):
                hide yuki with dissolve
                jump terminar_con_mirei

            "⚡ «ETAPA 5 — PROGRESO» Instalar la 'Bobina Experimental de Mirei' en el proyector de Yuki (+20 ♥ Yuki, Desbloquea Azotea)" if ("Bobina Experimental de Mirei" in inventario_items and not bobina_instalada_yuki):
                $ bobina_instalada_yuki = True
                $ cambiar_afinidad("yuki", 20, "¡Potencia cuántica!")
                $ cambiar_stat("festival", 15, "Hologramas al 100%")
                $ notificar_cambio("🔓 ¡ZONA DESBLOQUEADA: Azotea del Instituto (Hana)!", "#ff85a1")
                show yuki smile at pos_left, happy_bounce
                leo "Yuki, conseguí la bobina superconductora del almacén de química."
                yuki "Increíble... Mirei nunca se la presta a nadie sin pedir algo turbio a cambio. Espero que no te haya hecho nada extraño, [nombre_prota]."
                yuki "Con el proyector conectado a la red principal, ya se ha desbloqueado el cierre electrónico de la **Azotea del Instituto**. ¡Sube a ayudar a **Hana Sakuragi**!"
                jump menu_zona_laboratorio

            "🎁 Regalar 'Libro de Astrofísica Poética' a Yuki (+15 ♥ Yuki)" if ("Libro de Astrofísica Poética" in inventario_items and not regalo_entregado_yuki):
                $ regalo_entregado_yuki = True
                $ cambiar_afinidad("yuki", 15, "¡Regalo inolvidable!")
                show yuki smile at pos_left, happy_bounce
                leo "Encontré esta edición especial de Astrofísica Poética en la Biblioteca para ti."
                yuki "Llevaba meses buscándolo... Mi corazón late demasiado rápido cuando estás cerca, [nombre_prota]."
                jump menu_zona_laboratorio

            "💬 Conversar con Yuki sobre el proyector" if visitado_yuki:
                show yuki smile at pos_left
                if afinidad_yuki < 60:
                    $ cambiar_afinidad("yuki", 10, "Charla científica con Yuki")
                if not bobina_instalada_yuki:
                    yuki "Necesito la **Bobina Experimental** que guarda **Mirei** en el almacén químico para poder desbloquear la red eléctrica de la Azotea..."
                else:
                    yuki "El proyector funciona a la perfección gracias a ti, [nombre_prota]. Ahora ve a la Azotea a ayudar a Hana."
                jump menu_zona_laboratorio

            "🗺️ Abrir el Mapa del Instituto":
                hide yuki
                hide mirei
                with dissolve
                jump hub_instituto


################################################################################
## ZONA 3: AZOTEA DEL INSTITUTO (PRINCIPAL: HANA SAKURAGI)
################################################################################

label zona_azotea:
    if not esta_zona_desbloqueada("azotea"):
        $ notificar_cambio(obtener_motivo_bloqueo_zona("azotea"), "#ff4d6d")
        jump hub_instituto

    $ zonas_exploradas.add("azotea")
    scene bg rooftop with dissolve

    if visitado_hana:
        show hana happy at enter_center
    else:
        show hana sad at enter_center

    narrador "📍 Estás en la **Azotea del Instituto** (Tejado Principal), donde **Hana Sakuragi** ensaya bajo el cielo dorado."

    label menu_zona_azotea:
        menu:
            "❗ «ETAPA 6 — HISTORIA PRINCIPAL» Ayudar a Hana con su lesión de tobillo y su exhibición" if not visitado_hana:
                $ visitado_hana = True
                $ turnos_dia -= 1
                jump evento_hana

            "🏅 «ETAPA 7 — PROGRESO FINAL» Entregar a Hana el 'Pase Oficial de Exhibición' firmado por Reina (+20 ♥ Hana, Desbloquea el Festival)" if ("Pase Oficial de Exhibición" in inventario_items and not pase_entregado_hana):
                $ pase_entregado_hana = True
                $ cambiar_afinidad("hana", 20, "¡Beca salvada!")
                $ cambiar_stat("festival", 15, "Apertura confirmada")
                $ notificar_cambio("🏮 ¡HISTORIA LISTA! Festival Nocturno Desbloqueado", "#ffd166")
                show hana happy at closeup_romance, excited_jump
                leo "¡Mira, Hana! Conseguí que Reina firmara el permiso para que actuemos en pareja sin que el ojeador te descalifique."
                hana "¡¿En serio?! ¡Con lo exigente y peligrosa que es Reina! ¡Gracias, [nombre_prota], eres mi salvador!"
                if estado_sub_reina == "Enredado" and not ruptura_sub_reina:
                    narrador "(Sientes un escalofrío recordando las manos de Reina en los vestuarios... Debes ir a **terminar con Reina** en la Cafetería/Vestuarios antes de que le cuente a Hana lo ocurrido)."
                show hana happy at reset_zoom
                jump menu_zona_azotea

            "🎁 Entregar 'Botiquín Deportivo Frío' a Hana (+15 ♥ Hana)" if ("Botiquín Deportivo Frío" in inventario_items and not regalo_entregado_hana):
                $ regalo_entregado_hana = True
                $ cambiar_afinidad("hana", 15, "¡Cuidado extra!")
                $ cambiar_stat("festival", 10, "Hana recuperada")
                show hana happy at closeup_romance, happy_bounce
                leo "Traje este spray frío deportivo para que tu tobillo no te moleste nada esta noche."
                hana "¡Eres el chico más atento del mundo, [nombre_prota]!"
                show hana happy at reset_zoom
                jump menu_zona_azotea

            "💬 Conversar con Hana junto a la barandilla" if visitado_hana:
                show hana happy at pos_center, happy_bounce
                if afinidad_hana < 60:
                    $ cambiar_afinidad("hana", 10, "Apoyo en la Azotea")
                if not pase_entregado_hana:
                    hana "Por favor, [nombre_prota], baja a la **Cafetería y Vestuarios Sur** y consigue que **Reina** firme nuestro **Pase Oficial de Exhibición**."
                else:
                    hana "¡Estoy deseando que llegue la noche para bailar contigo en el escenario y ver los fuegos artificiales!"
                jump menu_zona_azotea

            "🗺️ Abrir el Mapa del Instituto":
                hide hana with dissolve
                jump hub_instituto


################################################################################
## ZONA 4: BIBLIOTECA Y RINCÓN REBELDE (SUB-PERSONAJE: KUROE SAKAMOTO)
################################################################################

label zona_biblioteca:
    if not esta_zona_desbloqueada("biblioteca"):
        $ notificar_cambio(obtener_motivo_bloqueo_zona("biblioteca"), "#ff4d6d")
        jump hub_instituto

    $ zonas_exploradas.add("biblioteca")
    scene bg library with dissolve

    show kuroe seductive at enter_center
    with dissolve

    narrador "📍 Estás en la **Biblioteca y Rincón Rebelde** (Ala Oeste). Al fondo, entre las estanterías oscuras donde nadie estudia, **Kuroe Sakamoto** —la chica mala del instituto— juega con las carpetas robadas del Consejo Estudiantil con la camisa desabrochada y una sonrisa provocadora."

    label menu_zona_biblioteca:
        menu:
            "💋 «ETAPA 2 — SUB-RUTA KUROE» Enfrentar a Kuroe para recuperar las Actas del Consejo de Akane" if not encuentro_sub_kuroe:
                jump sub_evento_kuroe

            "💔 «TERMINAR CON KUROE» Poner fin a tu pacto prohibido con Kuroe para ser fiel a Akane" if (estado_sub_kuroe == "Enredado" and not ruptura_sub_kuroe):
                jump terminar_con_kuroe

            "📖 Estudiar manuales de ingeniería (+10 ⚡ Ingenio)" if not entrenado_biblioteca:
                $ entrenado_biblioteca = True
                $ cambiar_stat("ingenio", 10, "Lectura intensiva")
                narrador "Repasas un manual de circuitos ópticos y protocolos escolares bajo la mirada burlona de Kuroe."
                kuroe "Ja, mírate empollando como un niño bueno... Qué aburrido, ven aquí conmigo."
                jump menu_zona_biblioteca

            "🔎 Buscar el 'Libro de Astrofísica Poética' para Yuki" if "Libro de Astrofísica Poética" not in inventario_items:
                $ agregar_item("Libro de Astrofísica Poética")
                narrador "¡Encuentras en la sección de astronomía el 'Libro de Astrofísica Poética' que tanto quería Yuki!"
                jump menu_zona_biblioteca

            "🗺️ Abrir el Mapa del Instituto":
                hide kuroe with dissolve
                jump hub_instituto


################################################################################
## ZONA 5: PATIO CENTRAL DE LOS CEREZOS (CORAZÓN DEL CAMPUS)
################################################################################

label zona_patio:
    $ zonas_exploradas.add("patio")
    scene bg courtyard with dissolve

    narrador "📍 Estás en el **Patio Central de los Cerezos**. El escenario principal del festival ya casi está listo."

    label menu_zona_patio:
        menu:
            "🏮 Ayudar a montar los farolillos y el escenario (+10 ★ Reputación, +10%% Festival)" if not entrenado_patio:
                $ entrenado_patio = True
                $ cambiar_stat("reputacion", 10, "Trabajo comunitario")
                $ cambiar_stat("festival", 10, "Escenario reforzado")
                narrador "Ayudas a levantar las estructuras del escenario principal ante el aplauso de los clubes."
                jump menu_zona_patio

            "👂 Escuchar los rumores sobre las 3 Heroínas y las 3 Sub-Chicas":
                narrador "Un alumno te susurra: «Ten cuidado con **Kuroe** en la Biblioteca, con **Mirei** en el Laboratorio y con **Reina** en los Vestuarios Sur... Te darán lo que necesitas para ayudar a Akane, Yuki y Hana, ¡pero si caes en sus redes de lujuria tendrás que cortar con ellas antes de la noche o te arruinarán!»"
                jump menu_zona_patio

            "🗺️ Abrir el Mapa del Instituto":
                jump hub_instituto


################################################################################
## ZONA 6: CAFETERÍA Y VESTUARIOS SUR (SUB-PERSONAJE: REINA KUROKAWA)
################################################################################

label zona_cafeteria:
    if not esta_zona_desbloqueada("cafeteria"):
        $ notificar_cambio(obtener_motivo_bloqueo_zona("cafeteria"), "#ff4d6d")
        jump hub_instituto

    $ zonas_exploradas.add("cafeteria")
    scene bg courtyard with dissolve

    show reina seductive at enter_center
    with dissolve

    narrador "📍 Estás en la **Cafetería y Vestuarios del Jardín Sur**. Apoyada contra la entrada de las duchas del Club de Educación Física está **Reina Kurokawa**, luciendo su figura imponente y una sonrisa peligrosa."

    label menu_zona_cafeteria:
        menu:
            "💋 «ETAPA 7 — SUB-RUTA REINA» Negociar con Reina en los vestuarios el Pase Oficial para salvar a Hana" if not encuentro_sub_reina:
                jump sub_evento_reina

            "💔 «TERMINAR CON REINA» Cortar tu ardiente aventura con Reina para proteger el corazón de Hana" if (estado_sub_reina == "Enredado" and not ruptura_sub_reina):
                jump terminar_con_reina

            "🍵 Conseguir suministros (Té Real de Durazno y Botiquín Deportivo)" if ("Té Real de Durazno" not in inventario_items):
                $ agregar_item("Té Real de Durazno")
                $ agregar_item("Botiquín Deportivo Frío")
                narrador "Consigues el **Té Real de Durazno** (para Akane) y el **Botiquín Deportivo Frío** (para Hana)."
                jump menu_zona_cafeteria

            "✨ Socializar con los estudiantes (+10 ✨ Carisma)" if not entrenado_cafeteria:
                $ entrenado_cafeteria = True
                $ cambiar_stat("carisma", 10, "Alma de la fiesta")
                narrador "Animas a los voluntarios del festival con tu carisma."
                jump menu_zona_cafeteria

            "🗺️ Abrir el Mapa del Instituto":
                hide reina with dissolve
                jump hub_instituto


################################################################################
## SUB-RUTAS DE LUJURIA Y TENTACIÓN (INTEGRADAS CON LAS 3 PRINCIPALES)
################################################################################

## --- SUB-RUTA 1: KUROE SAKAMOTO (LA CHICA MALA QUE ODIA ESTUDIAR -> RUTA AKANE) ---
label sub_evento_kuroe:
    $ encuentro_sub_kuroe = True
    scene bg library with dissolve
    show kuroe seductive at closeup_romance

    kuroe "Vaya, vaya... Así que tú eres el famoso [nombre_prota], el chico de los recados de la estirada de Akane."
    narrador "Kuroe te empuja suavemente contra la estantería del fondo, encerrándote con un brazo mientras pasa un dedo por tu cuello y el borde de tus labios."
    kuroe "A mí me importan una basura los estudios y las normas del Consejo. Me llevé estas actas solo para ver a la 'Presidenta Perfecta' perder los papeles..."
    kuroe "Pero tú me gustas. Tienes mirada de chico malo aunque finjas ser bueno. Si dejas que me divierta contigo aquí mismo entre las estanterías, las actas son tuyas."

    menu:
        "🔥 Ceder a la lujuria de Kuroe y dejarme besar por la chica mala (+50%% 🔥 Kuroe, Obtienes Actas, Quedas ENREDADO)":
            $ estado_sub_kuroe = "Enredado"
            $ cambiar_tentacion("kuroe", 50, "¡Pacto carnal en la biblioteca!")
            $ cambiar_stat("carisma", 10, "Seducción prohibida")
            $ agregar_item("Actas Secretas Recuperadas")
            $ registrar_rama("Tentación Rebelde con Kuroe", "Cediste al deseo con Kuroe entre las estanterías para conseguir las actas de Akane. ¡Debes terminar con ella antes del final!", "🔥 Enredado con Kuroe")

            show kuroe seductive at happy_bounce
            narrador "El perfume intenso de Kuroe te envuelve mientras sus labios atrapan los tuyos con un calor salvaje y adictivo en la penumbra de la biblioteca."
            kuroe "Mmm... Sabes mucho mejor de lo que imaginaba, [nombre_prota]. Toma tus dichosas carpetas para Akane... pero recuerda que esta noche eres mío, ¿entendido?"
            show kuroe seductive at reset_zoom

        "🛡️ Mantener la sangre fría, seducirla con labia sin cruzar la línea y quitarle las carpetas (+25%% 🔥 Kuroe, +15%% ⚡ Ingenio, Obtienes Actas)":
            $ estado_sub_kuroe = "Terminada"
            $ ruptura_sub_kuroe = True
            $ cambiar_tentacion("kuroe", 25, "Tensión controlada")
            $ cambiar_stat("ingenio", 15, "Astucia ante la tentación")
            $ cambiar_afinidad("akane", 10, "Lealtad a Akane")
            $ agregar_item("Actas Secretas Recuperadas")
            $ registrar_rama("Domador de la Chica Mala", "Conseguiste las actas de Kuroe sin caer en su trampa, manteniendo tu lealtad hacia Akane.", "+10% ♥ Akane, Sin ataduras")

            show kuroe angry at reset_zoom
            leo "Eres peligrosamente atractiva, Kuroe, pero hoy no pienso ser el juguete de nadie. Te cambio las carpetas por guardarte el secreto de que te saltaste el examen."
            kuroe "Tsk... Qué chico tan difícil. Toma las carpetas y lárgate con tu querida presidenta antes de que te ate a esta silla."

    jump menu_zona_biblioteca


label terminar_con_kuroe:
    scene bg library with dissolve
    show kuroe seductive at closeup_romance

    narrador "Te acercas a Kuroe en el rincón oscuro de la biblioteca. Sabes que si quieres cerrar la historia con Akane, tienes que **terminar con Kuroe** ahora mismo."
    kuroe "Je, sabía que volverías a por más, [nombre_prota]... ¿Listo para dejar plantada a la presidenta y escaparte conmigo?"

    menu:
        "💔 «Lo nuestro fue increíble, Kuroe, pero mi corazón pertenece a Akane. Tenemos que terminar aquí.»":
            $ ruptura_sub_kuroe = True
            $ estado_sub_kuroe = "Terminada"
            $ cambiar_stat("reputacion", 10, "Cerraste tu pasado")
            $ cambiar_afinidad("akane", 10, "Camino libre hacia Akane")
            $ registrar_rama("Ruptura con Kuroe", "Terminaste cara a cara tu aventura prohibida con Kuroe para poder entregarte a la historia principal.", "✔ Libre de Kuroe")

            show kuroe angry at reset_zoom, anger_shake
            kuroe "¡¿Me estás dejando después de cómo me hiciste sentir aquí mismo?!"
            show kuroe seductive at pos_center
            narrador "Kuroe te agarra de la corbata, te roba un último roce en la mejilla y suspira con una sonrisa orgullosa."
            kuroe "Bah... Supongo que una chica mala como yo no está hecha para los cuentos de hadas. Ve con Akane, idiota. No le diré ni una palabra de lo nuestro."

        "🔥 «No puedo resistirme a ti, Kuroe... Al diablo con las reglas.» (Seguir enredado)":
            $ cambiar_tentacion("kuroe", 25, "¡Adicto al peligro!")
            show kuroe seductive at happy_bounce
            kuroe "Así me gusta... Sabía que mi veneno ya corría por tus venas."
            show kuroe seductive at reset_zoom

    jump menu_zona_biblioteca


## --- SUB-RUTA 2: MIREI KANZAKI (CLUB DE CIENCIAS -> RUTA YUKI) ---
label sub_evento_mirei:
    $ encuentro_sub_mirei = True
    scene bg classroom with dissolve
    show mirei seductive at closeup_romance

    mirei "Ara, ara~ Cierra la puerta del almacén con seguro, [nombre_prota]. Yuki está tan concentrada en sus ecuaciones que no escuchará nada..."
    narrador "La sempai Mirei Kanzaki se acerca contoneando las caderas, sosteniendo la **Bobina Experimental** contra su escote mientras te acorrala contra la mesa de laboratorio."
    mirei "Sé cuánto deseas ayudar a la pequeña y fría Yuki. Pero en el Club de Ciencias todo es cuestión de intercambio equivalente..."
    mirei "Mi investigación trata sobre la química del deseo y el calor corporal masculino. Déjame usar tu cuerpo para mi experimento privado ahora mismo y te daré la bobina."

    menu:
        "🔥 Dejarme llevar por las manos de Mirei en el almacén (+50%% 🔥 Mirei, Obtienes Bobina, Quedas ENREDADO)":
            $ estado_sub_mirei = "Enredado"
            $ cambiar_tentacion("mirei", 50, "¡Experimento ardiente!")
            $ cambiar_stat("ingenio", 10)
            $ agregar_item("Bobina Experimental de Mirei")
            $ registrar_rama("Química Prohibida con Mirei", "Te entregaste al experimento seductor de Mirei en la trastienda mientras Yuki estaba al otro lado de la pared. ¡Debes terminar con ella antes del final!", "🔥 Enredado con Mirei")

            show mirei seductive at happy_bounce
            narrador "Las manos suaves de Mirei recorren tu pecho mientras susurra junto a tu oído, haciendo que el cristal de las probetas se empañe con vuestro aliento."
            mirei "Fascinante... Tu pulso está a 140 pulsaciones por minuto, cariño. Toma la bobina para Yuki, pero esta noche continuaremos la fase dos del experimento a solas."
            show mirei normal at reset_zoom

        "🛡️ Demostrarle con Ingenio que conozco la clave del inventario y tomar la bobina sin caer en su red (+25%% 🔥 Mirei, +15%% ⚡ Ingenio)":
            $ estado_sub_mirei = "Terminada"
            $ ruptura_sub_mirei = True
            $ cambiar_tentacion("mirei", 25, "Tensión científica")
            $ cambiar_stat("ingenio", 15, "Mente fría")
            $ cambiar_afinidad("yuki", 10, "Fidelidad a Yuki")
            $ agregar_item("Bobina Experimental de Mirei")
            $ registrar_rama("Inmune a las Feromonas de Mirei", "Obtuviste la Bobina Experimental sin traicionar la confianza de Yuki.", "+10% ♥ Yuki, Sin ataduras")

            show mirei angry at reset_zoom
            leo "Tus encantos son letales, sempai, pero esta bobina figura a nombre del proyecto oficial del festival. No jugaré con los sentimientos de Yuki."
            mirei "Mmm, qué fuerza de voluntad tan admirable... Está bien, llévatela antes de que duplique la dosis de seducción."

    jump zona_laboratorio


label terminar_con_mirei:
    scene bg classroom with dissolve
    show mirei seductive at closeup_romance

    narrador "Entras al almacén químico para hablar a solas con Mirei. Para poder cerrar la historia principal con Yuki, debes **terminar con Mirei** definitivamente."
    mirei "Hola, mi conejillo de indias favorito~ ¿Vienes a repetir la sesión práctica antes de que Yuki se dé cuenta?"

    menu:
        "💔 «Mirei, nuestro experimento en el almacén termina hoy. Quiero estar con Yuki de verdad.»":
            $ ruptura_sub_mirei = True
            $ estado_sub_mirei = "Terminada"
            $ cambiar_stat("ingenio", 10, "Decisión madura")
            $ cambiar_afinidad("yuki", 10, "Lealtad a Yuki")
            $ registrar_rama("Ruptura con Mirei", "Pusiste punto final a tu relación secreta con la sempai Mirei para proteger el corazón de Yuki.", "✔ Libre de Mirei")

            show mirei angry at reset_zoom
            mirei "Vaya... Así que la fría Yuki logró derretir tu corazón de verdad."
            show mirei seductive at pos_center
            mirei "Está bien, cariño. Una buena científica sabe cuándo dar por concluido un experimento. Nuestro pequeño secreto del almacén quedará bajo llave. Cuídala bien."

        "🔥 «Tus experimentos son demasiado adictivos, Mirei... No quiero terminar contigo.» (Seguir enredado)":
            $ cambiar_tentacion("mirei", 25, "¡Rendición al deseo!")
            show mirei seductive at happy_bounce
            mirei "Jejeje, sabía que tu cuerpo pediría otra dosis de mi laboratorio..."
            show mirei seductive at reset_zoom

    jump zona_laboratorio


## --- SUB-RUTA 3: REINA KUROKAWA (CLUB DE EDUCACIÓN FÍSICA -> RUTA HANA) ---
label sub_evento_reina:
    $ encuentro_sub_reina = True
    scene bg courtyard with dissolve
    show reina seductive at closeup_romance

    reina "Vaya, [nombre_prota]... Justo el chico que estaba buscando. Entra un momento a los vestuarios, no muerdo... a menos que me lo pidas."
    narrador "Reina Kurokawa, la capitana del Club de Educación Física, cierra la puerta del vestuario tras de ti. Su piel bronceada brilla aún por el entrenamiento mientras te acorrala contra las taquillas."
    reina "Sé perfectamente que Hana tiene el tobillo hinchado. Como capitana de Educación Física, basta una palabra mía para quitarle su puesto estelar hoy mismo..."
    reina "Pero si me demuestras aquí mismo cuánta resistencia física tienes tú dándome un 'masaje privado', firmaré su Pase Oficial en pareja."

    menu:
        "🔥 Ceder a la pasión de Reina en los vestuarios (+50%% 🔥 Reina, Obtienes Pase Oficial, Quedas ENREDADO)":
            $ estado_sub_reina = "Enredado"
            $ cambiar_tentacion("reina", 50, "¡Vapor en los vestuarios!")
            $ cambiar_stat("carisma", 10, "Pasión desbordante")
            $ agregar_item("Pase Oficial de Exhibición")
            $ registrar_rama("Tentación en los Vestuarios con Reina", "Caíste en la ardiente provocación de Reina para conseguir el pase de Hana. ¡Debes terminar con ella antes del final!", "🔥 Enredado con Reina")

            show reina seductive at happy_bounce
            narrador "Entre el vapor de las duchas y el calor de su piel atlética, tus manos recorren la cintura de Reina mientras ella ahoga un suspiro contra tu cuello."
            reina "Uff... Tienes unas manos increíbles, [nombre_prota]. Aquí tienes el Pase firmado para Hana... pero más tarde te espero en el gimnasio solo para mí."
            show reina seductive at reset_zoom

        "🛡️ Desafiarla a una prueba deportiva justa y ganarle el Pase sin traicionar a Hana (+25%% 🔥 Reina, +15%% ★ Reputación)":
            $ estado_sub_reina = "Terminada"
            $ ruptura_sub_reina = True
            $ cambiar_tentacion("reina", 25, "Respeto atlético")
            $ cambiar_stat("reputacion", 15, "Honor deportivo")
            $ cambiar_afinidad("hana", 10, "Lealtad a Hana")
            $ agregar_item("Pase Oficial de Exhibición")
            $ registrar_rama("Honor en los Vestuarios", "Conseguiste el Pase de Reina con determinación sin caer en la tentación.", "+10% ♥ Hana, Sin ataduras")

            show reina angry at reset_zoom
            leo "No necesito atajos sucios en los vestuarios, Reina. Hana y yo demostraremos en el escenario que somos el mejor dúo del instituto."
            reina "¡Ja! Tienes agallas, chico. Pocos hombres me dicen que no estando tan cerca. Toma el pase, os lo habéis ganado."

    jump menu_zona_cafeteria


label terminar_con_reina:
    scene bg courtyard with dissolve
    show reina seductive at closeup_romance

    narrador "Buscas a Reina junto a los vestuarios del Jardín Sur. Sabes que para culminar tu historia con Hana, debes **terminar con Reina** antes de que empiece el espectáculo."
    reina "Hola, campeón~ ¿Vienes al vestuario para el segundo asalto antes de salir al escenario?"

    menu:
        "💔 «Reina, lo que pasó en el vestuario no puede repetirse. Voy a jugármelo todo por Hana.»":
            $ ruptura_sub_reina = True
            $ estado_sub_reina = "Terminada"
            $ cambiar_stat("carisma", 10, "Sinceridad valiente")
            $ cambiar_afinidad("hana", 10, "Corazón limpio para Hana")
            $ registrar_rama("Ruptura con Reina", "Terminaste de frente tu ardiente aventura con Reina para no herir a Hana.", "✔ Libre de Reina")

            show reina angry at reset_zoom, anger_shake
            reina "¡¿Me dejas con las ganas después de encenderme así en las taquillas?!"
            show reina seductive at pos_center
            reina "Jajaja... Está bien, [nombre_prota]. Me gustan los hombres que saben proteger a su chica. Sal ahí fuera con Hana y brillad. Nuestro secreto muere conmigo."

        "🔥 «Tu piel me vuelve loco, Reina... No puedo decirte adiós.» (Seguir enredado)":
            $ cambiar_tentacion("reina", 25, "¡Fuego imparable!")
            show reina seductive at happy_bounce
            reina "Sabía que una vez que probaras a una mujer de verdad no podrías escapar..."
            show reina seductive at reset_zoom

    jump menu_zona_cafeteria


################################################################################
## EVENTO PRINCIPAL 1: AKANE TACHIBANA (CONEXIÓN CON KUROE)
################################################################################

label evento_akane:
    $ estado_mision_akane = "En Progreso"
    scene bg council with fade

    show akane normal at enter_center
    with dissolve

    akane "El club de teatro y el comité de cocina han perdido sus sellos de presupuesto, y además **Kuroe Sakamoto**, esa rebelde que nunca entra a clase, se llevó la carpeta maestra a la Biblioteca."
    akane "Y por si fuera poco, el subdirector viene hacia aquí en cinco minutos para inspeccionar las cuentas."

    leo "Espera un momento, Akane. Tienes ojeras. ¿Llevas toda la semana haciendo el trabajo de todo el comité tú sola?"

    show akane angry at pos_center, anger_shake
    akane "¡E-eso a ti no te importa! ¡Soy la Presidenta del Consejo, es mi deber ser perfecta!"

    narrador "Al ponerse de pie bruscamente, Akane se marea por el cansancio y está a punto de tropezar contra el escritorio."

    menu:
        "Sujetarla por la cintura y obligarla con dulzura a sentarse a descansar (+20%% ♥ Akane)":
            $ cambiar_afinidad("akane", 20, "Cuidado cercano")
            $ cambiar_stat("carisma", 10)
            show akane blush at closeup_romance
            leo "Ni hablar. Incluso la presidenta más fuerte necesita apoyarse en alguien. Siéntate, yo organizaré las actas contigo."
            akane "¡¿Q-qué haces sujetándome así?! Mi corazón... digo, ¡suéltame! Aunque... está bien, solo cinco minutos."
            show akane blush at reset_zoom

        "Usar mi Ingenio para reconstruir el registro de facturas rápidamente «Requiere 15%%+ Ingenio»" if ingenio >= 15:
            $ cambiar_afinidad("akane", 20, "Admiró tu intelecto")
            $ cambiar_stat("festival", 15, "Cuentas cuadradas")
            show akane blush at pos_center, happy_bounce
            leo "Mira esto: las copias carbón siguen en el bloc de recibos. Si cruzamos los códigos numéricos, podemos reconstruir las autorizaciones en dos minutos."
            akane "¡¿Eh?! ¡Increíble! ¿Cómo se te ocurrió eso tan rápido? Quizá... te había subestimado, [nombre_prota]."

        "Decirle que yo mismo iré a la Biblioteca a lidiar con la rebelde Kuroe (+15%% ♥ Akane, +10%% 🔥 Kuroe)":
            $ cambiar_afinidad("akane", 15, "Te ofreciste a ayudarla")
            $ cambiar_tentacion("kuroe", 10, "Interés por la chica mala")
            show akane angry at pos_center
            akane "¡Ten mucho cuidado con Kuroe en la Biblioteca! Es una manipuladora descarada que usa su cuerpo para meter a los chicos en problemas."

    narrador "De pronto, se escuchan pasos pesados en el pasillo. ¡El estricto Subdirector está abriendo la puerta antes de tiempo!"

    call screen decision_bajo_presion(
        "¡EL SUBDIRECTOR ENTRA A INSPECCIONAR!",
        7,
        "timeout_subdirector",
        [
            ("🎭 Distraer al Subdirector con un discurso apasionado mientras Akane sella las actas", "distraer_subdirector"),
            ("🗂️ Escondernos juntos bajo el gran escritorio de caoba con las carpetas", "esconderse_escritorio")
        ]
    )

    $ accion_akane = _return

    if accion_akane == "distraer_subdirector":
        $ consecuencia_akane_confia = True
        $ estado_mision_akane = "Resuelto con Éxito"
        $ cambiar_afinidad("akane", 20, "¡Salvaste su puesto!")
        $ cambiar_stat("reputacion", 15, "Impresionaste a la dirección")
        $ cambiar_stat("festival", 20, "Presupuesto aprobado")
        $ agregar_item("Sello Dorado del Consejo")
        $ registrar_rama("Salvador del Consejo Estudiantil", "Distrajiste al subdirector con brillantez y Akane aprobó los fondos del festival.", "+20% ♥ Akane, +20% Festival")

        show akane blush at pos_center, happy_bounce
        akane "Gracias a ti hemos superado la inspección. Toma el Sello Dorado del Consejo... y si vas a la Biblioteca a ver a Kuroe por las carpetas restantes, ¡no dejes que te seduzca!"

    elif accion_akane == "esconderse_escritorio":
        $ consecuencia_akane_confia = True
        $ estado_mision_akane = "Resuelto con Éxito"
        $ cambiar_afinidad("akane", 25, "¡Momento íntimo bajo la mesa!")
        $ cambiar_stat("festival", 20, "Inspección esquivada")
        $ agregar_item("Sello Dorado del Consejo")
        $ registrar_rama("Secreto Bajo el Escritorio", "Te escondiste con Akane bajo la mesa del Consejo, creando una tensión romántica inolvidable.", "+25% ♥ Akane, +20% Festival")

        show akane blush at closeup_romance, shy_sink
        narrador "Bajo el escritorio del Consejo, hombro con hombro en la penumbra, escuchas la respiración acelerada de Akane hasta que el subdirector se marcha."
        akane "E-estabas tan cerca que pensé que escucharías los latidos de mi corazón... Toma este sello y prométeme que si ves a Kuroe en la Biblioteca no caerás en sus provocaciones."
        show akane blush at reset_zoom

    else:
        $ estado_mision_akane = "Complicado"
        $ cambiar_afinidad("akane", 15, "Diste la cara ante el subdirector")
        $ cambiar_stat("festival", 10, "Aprobación parcial")
        $ registrar_rama("Inspección Accidentada", "El subdirector os pilló con los papeles revueltos, pero defendiste a Akane. ¡Recupera las Actas de Kuroe en la Biblioteca!", "+15% ♥ Akane, +10% Festival")

        show akane angry at pos_center
        akane "¡Casi nos suspenden, pero gracias por defenderme! ¡Ve a la Biblioteca y recupérale las Actas a Kuroe como sea!"

    $ notificar_cambio("🔓 ¡ZONA DESBLOQUEADA: Biblioteca Oeste (Kuroe)!", "#c77dff")
    jump menu_zona_consejo


################################################################################
## EVENTO PRINCIPAL 2: YUKI SHIROGANE (CONEXIÓN CON MIREI)
################################################################################

label evento_yuki:
    $ estado_mision_yuki = "En Progreso"
    scene bg classroom with fade

    show yuki normal at enter_center
    with dissolve

    yuki "El golpe de esta mañana desalineó la matriz óptica del proyector holográfico, [nombre_prota]."
    yuki "Además, mi sempai del Club de Ciencias, **Mirei Kanzaki**, guardó bajo llave la Bobina Experimental en el almacén químico y dice que solo te la entregará a ti en privado..."

    menu:
        "Tomar las manos frías de Yuki y prometerle que ella es la única que me importa (+20%% ♥ Yuki)":
            $ cambiar_afinidad("yuki", 20, "Tocaste su corazón")
            $ cambiar_stat("carisma", 10)
            show yuki shy at closeup_romance, shy_sink
            leo "Quien diga que eres fría no te ha mirado a los ojos, Yuki. Ni Mirei ni nadie hará que me olvide de nuestra promesa."
            yuki "Temperatura corporal aumentando... [nombre_prota], cuando me hablas así, mis algoritmos lógicos dejan de funcionar por completo."
            show yuki smile at reset_zoom

        "Usar el Sello Dorado del Consejo para abrir la vitrina de repuestos (+20%% ♥ Yuki, +10%% ⚡ Ingenio)" if "Sello Dorado del Consejo" in inventario_items:
            $ cambiar_afinidad("yuki", 20, "¡Solución maestra!")
            $ cambiar_stat("ingenio", 10)
            $ cambiar_stat("reputacion", 10)
            show yuki smile at pos_center, happy_bounce
            leo "¡Con el Sello Dorado de Akane podemos usar el condensador oficial del Consejo!"
            yuki "Eso resuelve el problema con una eficiencia extraordinaria, [nombre_prota]."

        "Decirle que hablaré con la sempai Mirei en la trastienda para conseguir la bobina (+15%% ♥ Yuki, +10%% 🔥 Mirei)":
            $ cambiar_afinidad("yuki", 15, "Dispuesto a arriesgarse")
            $ cambiar_tentacion("mirei", 10, "Curiosidad por la sempai")
            yuki "Ten cuidado con Mirei... Le gusta jugar con el pulso y las hormonas de los chicos jóvenes."

    narrador "El reactor óptico emite un chispazo azulado. ¡Hay que elegir la frecuencia final antes de que se sobrecargue!"

    menu:
        "Sintonizar la frecuencia 'Luz de Luna' (+20%% ♥ Yuki, +20%% 🏮 Festival)":
            $ consecuencia_yuki_invento_estable = True
            $ estado_mision_yuki = "Resuelto con Éxito"
            $ cambiar_afinidad("yuki", 20, "¡Armonía perfecta!")
            $ cambiar_stat("festival", 20, "Espectáculo garantizado")
            $ agregar_item("Núcleo Holográfico Estelar")
            $ registrar_rama("Estrellas en el Aula", "Estabilizaste el proyector de Yuki y viste su primera sonrisa sincera.", "+20% ♥ Yuki, +20% Festival")

            show yuki smile at closeup_romance
            yuki "Dicen que el amor es solo una reacción química... pero estando aquí contigo, prefiero creer que es magia. Guarda este Núcleo Estelar para esta noche."
            show yuki smile at reset_zoom

        "Forzar la sobrecarga máxima al 200%% para impresionar a todos":
            if ingenio >= 20 or "Bobina Experimental de Mirei" in inventario_items:
                $ consecuencia_yuki_invento_estable = True
                $ estado_mision_yuki = "Resuelto con Éxito"
                $ cambiar_afinidad("yuki", 25, "¡Genio audaz!")
                $ cambiar_stat("festival", 25, "¡Potencia récord!")
                $ agregar_item("Núcleo Holográfico Estelar")
                $ registrar_rama("Sobrecarga Triunfal", "Lograste dominar la sobrecarga al 200% en el laboratorio.", "+25% ♥ Yuki, +25% Festival")

                show yuki shy at pos_center, happy_bounce
                yuki "¡Imposible! ¡Has estabilizado la sobrecarga máxima sin quemar el núcleo!"
            else:
                $ estado_mision_yuki = "Complicado"
                $ cambiar_afinidad("yuki", 20, "Protegiste a Yuki del chispazo")
                $ cambiar_stat("festival", 15, "Batería auxiliar")
                $ registrar_rama("Cortocircuito Parcial", "Se quemó el fusible secundario, pero protegiste a Yuki. ¡Consigue la Bobina con Mirei en el almacén!", "+20% ♥ Yuki, +15% Festival")

                scene bg classroom at camera_shake with flash
                show yuki shy at pos_center
                yuki "Puf... Gracias por cubrirme del chispazo. Si consigues la Bobina de Mirei podremos recuperar toda la potencia..."

    $ notificar_cambio("🔓 ¡SUB-RUTA DESBLOQUEADA: Almacén Químico (Sempai Mirei)!", "#c77dff")
    jump zona_laboratorio


################################################################################
## EVENTO PRINCIPAL 3: HANA SAKURAGI (CONEXIÓN CON REINA)
################################################################################

label evento_hana:
    $ estado_mision_hana = "En Progreso"
    scene bg rooftop with fade

    show hana sad at enter_center
    with dissolve

    hana "¡¿Eh?! ¡[nombre_prota]! N-no es lo que parece, ¡solo me estaba atando los cordones!"
    leo "Hana... tienes el tobillo hinchado. Te hiciste daño esta mañana evitando el choque en el pasillo, ¿verdad?"

    show hana sad at pos_center, shy_sink
    hana "No quería que nadie se preocupara... Hoy viene el ojeador deportivo a ver la exhibición, y encima **Reina Kurokawa**, la capitana del Club de Educación Física, sospecha que estoy lesionada."
    hana "Si Reina no firma el permiso para adaptar la rutina en los vestuarios del Jardín Sur, me descalificarán..."

    menu:
        "Arrodillarme frente a ella, vendarle el tobillo con cuidado y ofrecerme como su compañero (+25%% ♥ Hana, +20%% 🏮 Festival)":
            $ consecuencia_hana_secreto_guardado = True
            $ estado_mision_hana = "Resuelto con Éxito"
            $ cambiar_afinidad("hana", 25, "¡Su héroe incondicional!")
            $ cambiar_stat("carisma", 10, "Empatía total")
            $ cambiar_stat("festival", 20, "Coreografía en pareja")
            $ agregar_item("Amuleto de Sakura de Hana")
            $ registrar_rama("Promesa al Atardecer", "Cuidaste la lesión de Hana y adaptasteis la exhibición como un dúo inolvidable.", "+25% ♥ Hana, +20% Festival")

            show hana happy at closeup_romance, happy_bounce
            leo "No tienes que cargar con todo tú sola, Hana. Yo haré la parte de fuerza contigo en el escenario y hablaré con Reina si hace falta."
            hana "¡[nombre_prota]...! ¡Prométeme que no dejarás que Reina te robe para su club y que veremos los fuegos artificiales juntos!"
            show hana happy at reset_zoom

        "Convencerla con lógica de cambiar la acrobacia por un número musical con las luces de Yuki (+20%% ♥ Hana, +20%% 🏮 Festival)":
            $ consecuencia_hana_secreto_guardado = True
            $ estado_mision_hana = "Resuelto con Éxito"
            $ cambiar_afinidad("hana", 20, "Cuidaste su salud")
            $ cambiar_stat("ingenio", 10)
            $ cambiar_stat("festival", 20)
            $ agregar_item("Amuleto de Sakura de Hana")
            $ registrar_rama("Brillo sin Riesgo", "Rediseñaste el espectáculo de Hana para proteger su beca deportiva.", "+20% ♥ Hana, +20% Festival")

            show hana normal at pos_center, happy_bounce
            hana "¡Tienes razón! ¡Y si además consigues el Pase Oficial de Reina en la Cafetería/Vestuarios Sur, será un éxito total!"

        "Decirle que iré directo a los vestuarios a negociar a solas con Reina (+20%% ♥ Hana, +15%% 🔥 Reina)":
            $ estado_mision_hana = "Complicado"
            $ cambiar_afinidad("hana", 20, "Prometiste conseguirle el pase")
            $ cambiar_tentacion("reina", 15, "Cita en los vestuarios")
            $ cambiar_stat("festival", 15, "Plan en marcha")
            show hana sad at pos_center
            hana "T-ten mucho cuidado en los vestuarios con Reina, [nombre_prota]... Cuando le gusta un chico, no acepta un 'no' por respuesta."

    $ notificar_cambio("🔓 ¡ZONA DESBLOQUEADA: Cafetería y Vestuarios Sur (Reina)!", "#ff9e00")
    jump menu_zona_azotea


################################################################################
## FASE DE AJUSTE DE CUENTAS: TERMINAR CON LAS SUB-PERSONAJES ANTES DEL FINAL
################################################################################

label verificar_rupturas_antes_climax:
    scene bg festival with fade

    # 1. Si sigue enredado con Kuroe sin haber terminado con ella:
    if estado_sub_kuroe == "Enredado" and not ruptura_sub_kuroe:
        show kuroe seductive at enter_center
        narrador "Antes de que puedas llegar al escenario principal con Akane, **Kuroe Sakamoto** te intercepta detrás de las carpas del festival y te acorrala contra la pared."
        kuroe "¿A dónde crees que vas, [nombre_prota]? Después de lo que hicimos en la biblioteca, no pensarás irte con la presidenta como si nada..."
        menu:
            "💔 Terminar con Kuroe ahora mismo con firmeza para poder ir con las heroínas principales":
                $ ruptura_sub_kuroe = True
                $ estado_sub_kuroe = "Terminada"
                $ registrar_rama("Cierre de Última Hora con Kuroe", "Terminaste tu aventura con Kuroe justo antes de la ceremonia del festival.", "✔ Libre de Kuroe")
                show kuroe angry at pos_center
                leo "Kuroe, te agradezco la ayuda con las actas, pero lo nuestro termina aquí. Tengo que cumplir mi promesa en el escenario."
                kuroe "Tsk... Eres un rompecorazones, ¿lo sabías? Anda, vete antes de que me arrepienta y te deje marca de carmín en el cuello."
                hide kuroe with dissolve

            "🔥 Rendirme a la lujuria de Kuroe y abandonar la ceremonia para irme con ella «FINAL TENTACIÓN KUROE»":
                jump final_tentacion_kuroe

    # 2. Si sigue enredado con Mirei sin haber terminado con ella:
    if estado_sub_mirei == "Enredado" and not ruptura_sub_mirei:
        show mirei seductive at enter_center
        narrador "Al pasar junto a la carpa de control técnico, la sempai **Mirei Kanzaki** te toma de la mano y tira de ti hacia las sombras."
        mirei "Ara, ara~ ¿De verdad pensabas dejar a tu sempai sola después de nuestro pequeño experimento en el almacén químico?"
        menu:
            "💔 Terminar con Mirei definitivamente para proteger a Yuki y la historia principal":
                $ ruptura_sub_mirei = True
                $ estado_sub_mirei = "Terminada"
                $ registrar_rama("Cierre de Última Hora con Mirei", "Cortaste tu vínculo secreto con Mirei antes de que Yuki lo descubriera.", "✔ Libre de Mirei")
                show mirei angry at pos_center
                leo "Mirei, no podemos seguir con esto. Yuki confía en mí y voy a estar a su lado esta noche."
                mirei "Suspiro... Qué chico tan leal. Está bien, te libero de mi laboratorio, cariño."
                hide mirei with dissolve

            "🔥 Ceder al deseo de Mirei y encerrarme con ella en el laboratorio toda la noche «FINAL TENTACIÓN MIREI»":
                jump final_tentacion_mirei

    # 3. Si sigue enredado con Reina sin haber terminado con ella:
    if estado_sub_reina == "Enredado" and not ruptura_sub_reina:
        show reina seductive at enter_center
        narrador "Detrás de las gradas deportivas, **Reina Kurokawa** te cierra el paso con una sonrisa ardiente y dominante."
        reina "Eh, campeón. Te di el pase para Hana en los vestuarios, y ahora toca cobrarme la segunda parte de nuestro trato a solas."
        menu:
            "💔 Terminar con Reina con determinación para no traicionar a Hana":
                $ ruptura_sub_reina = True
                $ estado_sub_reina = "Terminada"
                $ registrar_rama("Cierre de Última Hora con Reina", "Terminaste tu aventura de vestuario con Reina justo a tiempo para la actuación.", "✔ Libre de Reina")
                show reina angry at pos_center
                leo "Reina, lo del vestuario quedó atrás. Esta noche mi lugar está en el escenario con Hana."
                reina "Ja... Qué desperdicio de cuerpo, pero respeto a un hombre que cumple su palabra. Ve con ella, campeón."
                hide reina with dissolve

            "🔥 Dejarme arrastrar por Reina a los vestuarios vacíos durante el festival «FINAL TENTACIÓN REINA»":
                jump final_tentacion_reina

    jump climax_festival


################################################################################
## ACTO 3 — EL CLÍMAX: LA NOCHE DEL FESTIVAL CULTURAL (HISTORIA PRINCIPAL)
################################################################################

label climax_festival:
    $ pendientes_check = obtener_estado_sub_Pendiente()
    if len(pendientes_check) > 0:
        jump verificar_rupturas_antes_climax

    $ climax_completado = True
    scene bg festival with fade

    narrador "La noche cae sobre el Instituto Sakura. Cientos de farolillos de papel iluminan el patio mientras la multitud se reúne frente al escenario principal."

    show akane normal at enter_left
    show yuki normal at enter_center
    show hana normal at enter_right
    with dissolve

    akane "Ha llegado el momento de la ceremonia principal, [nombre_prota]. Todo el instituto nos está mirando."

    if consecuencia_akane_confia and consecuencia_yuki_invento_estable and consecuencia_hana_secreto_guardado:
        $ consecuencia_alianza_chicas = True
        $ cambiar_stat("reputacion", 25, "¡Trinidad Perfecta!")
        $ cambiar_stat("festival", 20, "¡Sinergia total!")
        $ registrar_rama("¡Milagro en el Festival Sakura!", "Resolviste los problemas de las 3 heroínas principales y cerraste todas las tentaciones secundarias a tiempo.", "¡Festival al 100%!")

        show akane blush at pos_left, happy_bounce
        show yuki smile at pos_center, happy_bounce
        show hana happy at pos_right, excited_jump

        narrador "¡Con las misiones de Akane, Yuki y Hana completadas y tras haber cerrado tus peligrosos enredos con las sub-personajes, el Festival Cultural estalla en un triunfo histórico!"
        hana "¡Miren a la multitud! ¡Todo el instituto está coreando tu nombre, [nombre_prota]!"
        yuki "Probabilidad de éxito superada. Has demostrado una lealtad y un ingenio admirables."
        akane "B-bueno... supongo que tendré que retirar tu orden de expulsión y darte una medalla de honor."

    elif presupuesto_festival >= 55:
        $ cambiar_stat("reputacion", 10, "Festival salvado")
        narrador "A pesar de las tentaciones y los contratiempos de última hora, tus esfuerzos logran salvar el Festival Cultural y el público aplaude entusiasmado."
        akane "No ha sido perfecto, pero sin tu ayuda habría sido una catástrofe. Buen trabajo, [nombre_prota]."

    else:
        scene bg festival at camera_shake with vpunch
        show akane angry at pos_left, anger_shake
        show hana sad at pos_right
        narrador "De repente, las luces parpadean y parte del decorado se viene abajo en mitad de la ceremonia..."
        akane "¡Sabía que faltaban preparativos! ¡[nombre_prota], prepárate para limpiar el instituto durante todo el semestre!"


################################################################################
## ACTO 4 — ELECCIÓN DE LAS HEROÍNAS PRINCIPALES Y FINALES
################################################################################

label eleccion_final:
    narrador "Cuando comienzan a estallar los fuegos artificiales en el cielo estrellado, tu teléfono vibra."
    narrador "Tras haber superado las pruebas y dejado atrás las tentaciones secundarias, las **tres heroínas principales** quieren confesarse contigo..."

    menu:
        "❤️ Ir al balcón del Consejo con Akane Tachibana (Afinidad: [afinidad_akane]%% ♥)":
            jump final_akane

        "💙 Ir al observatorio iluminado con Yuki Shirogane (Afinidad: [afinidad_yuki]%% ♥)":
            jump final_yuki

        "🩷 Ir bajo el gran cerezo del patio con Hana Sakuragi (Afinidad: [afinidad_hana]%% ♥)":
            jump final_hana

        "👑 «FINAL SECRETO HAREM PRINCIPAL» ¡Reunir a Akane, Yuki y Hana bajo los fuegos artificiales!" if (afinidad_akane >= 50 and afinidad_yuki >= 50 and afinidad_hana >= 50 and presupuesto_festival >= 75):
            jump final_harem


label final_akane:
    $ climax_completado = True
    $ finales_vistos.add("akane")
    scene bg festival with dissolve
    hide yuki
    hide hana
    if afinidad_akane >= 50:
        show akane blush at enter_center
        show akane blush at closeup_romance
        akane "Pensé que no vendrías, tonto... Y me alegra saber que ni siquiera una rebelde como Kuroe pudo apartarte de mi lado."
        akane "Siempre creí que tenía que llevar todo el peso del instituto yo sola... hasta que llegaste tú y me enseñaste a confiar."
        akane "N-no te confundas... ¡solo te nombro mi vicepresidente personal porque te quiero solo para mí!"
        leo "Acepto el cargo encantado, mi querida Presidenta."
        narrador "✨ FINAL PRINCIPAL DESBLOQUEADO: RUTA VERDADERA DE AKANE — «El Corazón Secreto de la Presidenta Tsundere» ✨"
    else:
        show akane normal at enter_center
        akane "Has trabajado duro hoy, [nombre_prota]. Todavía te falta mucho para ganarte toda mi confianza, pero te perdono el desastre de esta mañana."
        narrador "🌟 FINAL DESBLOQUEADO: RUTA NORMAL DE AKANE — «Aliados del Consejo Estudiantil» 🌟"
    jump pantalla_resumen_final


label final_yuki:
    $ climax_completado = True
    $ finales_vistos.add("yuki")
    scene bg festival with dissolve
    hide akane
    hide hana
    if afinidad_yuki >= 50:
        show yuki smile at enter_center
        show yuki shy at closeup_romance
        yuki "He analizado mil variables distintas esta noche, [nombre_prota], y todas llegan a la misma conclusión."
        yuki "Ni siquiera los juegos de seducción de Mirei pudieron alterar la química real que existe entre tú y yo. No quiero que nuestra historia termine nunca."
        leo "Entonces sigamos escribiendo nuestra historia juntos, Yuki."
        narrador "✨ FINAL PRINCIPAL DESBLOQUEADO: RUTA VERDADERA DE YUKI — «La Ecuación Perfecta del Primer Amor» ✨"
    else:
        show yuki smile at enter_center
        yuki "Gracias por ayudarme con el proyector hoy. Eres una anomalía estadística muy interesante, [nombre_prota]."
        narrador "🌟 FINAL DESBLOQUEADO: RUTA NORMAL DE YUKI — «Compañeros de Laboratorio» 🌟"
    jump pantalla_resumen_final


label final_hana:
    $ climax_completado = True
    $ finales_vistos.add("hana")
    scene bg festival with dissolve
    hide akane
    hide yuki
    if afinidad_hana >= 50:
        show hana happy at enter_center
        show hana happy at closeup_romance, happy_bounce
        hana "¡Viniste, [nombre_prota]! ¡Sabía que cumplirías nuestra promesa a pesar de las tentaciones de Reina!"
        hana "Dicen que si estás con la persona que amas cuando estalla el último fuego artificial del festival, estaréis juntos para siempre..."
        hana "¡Y yo no cambiaría este abrazo contigo por ningún trofeo del mundo!"
        leo "Yo tampoco, Hana. Tu sonrisa es lo mejor de todo el instituto."
        narrador "✨ FINAL PRINCIPAL DESBLOQUEADO: RUTA VERDADERA DE HANA — «Promesa Bajo la Lluvia de Sakura» ✨"
    else:
        show hana normal at enter_center
        hana "¡Muchas gracias por todo lo de hoy, [nombre_prota]! ¡Eres el mejor amigo que podría pedir!"
        narrador "🌟 FINAL DESBLOQUEADO: RUTA NORMAL DE HANA — «Mejores Amigos para Siempre» 🌟"
    jump pantalla_resumen_final


label final_harem:
    $ climax_completado = True
    $ finales_vistos.add("harem")
    scene bg festival with flash
    show akane blush at enter_left
    show yuki shy at enter_center
    show hana happy at enter_right
    with dissolve

    hana "¡¿Eh?! ¡¿Akane y Yuki también tenían una cita contigo aquí?!"
    akane "¡¿Q-qué significa esto, [nombre_prota]?! ¡Al menos cortaste con las tres tentadoras del instituto, pero ahora nos tienes a nosotras tres aquí!"
    yuki "Interesante. Parece que ninguno de nuestros corazones está dispuesto a cederte."
    hana "¡Pues entonces tendremos que compartirlo! ¡Después de todo, nos salvó a las tres hoy!"

    narrador "👑 FINAL SECRETO LEGENDARIO DESBLOQUEADO: «El Héroe Indiscutible del Instituto Sakura (Ruta Harem Principal)» 👑"
    jump pantalla_resumen_final


################################################################################
## FINALES ALTERNATIVOS DE TENTACIÓN (SI NO TERMINAS CON LAS SUB-PERSONAJES)
################################################################################

label final_tentacion_kuroe:
    $ climax_completado = True
    $ finales_vistos.add("kuroe")
    scene bg library with fade
    show kuroe seductive at enter_center, closeup_romance
    kuroe "Sabía que no podrías decirme adiós, chico malo... Deja que Akane se ocupe de su aburrido festival."
    kuroe "Esta noche la biblioteca entera es solo para nosotros dos..."
    narrador "🔥 FINAL DE TENTACIÓN DESBLOQUEADO: RUTA PROHIBIDA DE KUROE — «Prisionero de la Chica Mala» 🔥\n(Para ver los Finales Principales, recuerda terminar con las sub-personajes a tiempo)."
    jump pantalla_resumen_final

label final_tentacion_mirei:
    $ climax_completado = True
    $ finales_vistos.add("mirei")
    scene bg classroom with fade
    show mirei seductive at enter_center, closeup_romance
    mirei "Ara, ara~ Qué decisión tan deliciosa, [nombre_prota]. Mientras el resto del instituto mira los fuegos artificiales, tú y yo haremos saltar chispas en el laboratorio toda la noche."
    narrador "🔥 FINAL DE TENTACIÓN DESBLOQUEADO: RUTA PROHIBIDA DE MIREI — «Experimento Nocturno de Lujuria» 🔥\n(Para ver los Finales Principales, recuerda terminar con las sub-personajes a tiempo)."
    jump pantalla_resumen_final

label final_tentacion_reina:
    $ climax_completado = True
    $ finales_vistos.add("reina")
    scene bg courtyard with fade
    show reina seductive at enter_center, closeup_romance
    reina "¡Así me gusta, campeón! Sabía que no podrías olvidar el calor de los vestuarios. Esta noche vas a necesitar toda tu resistencia física conmigo."
    narrador "🔥 FINAL DE TENTACIÓN DESBLOQUEADO: RUTA PROHIBIDA DE REINA — «Entrenamiento Privado sin Límites» 🔥\n(Para ver los Finales Principales, recuerda terminar con las sub-personajes a tiempo)."
    jump pantalla_resumen_final


label pantalla_resumen_final:
    narrador "Haz clic en el botón **🏆 Progreso ([calcular_progreso_total()]%%)** de la barra superior para ver exactamente qué te falta para obtener el **100%% del Juego Completo**."

    menu:
        "🏆 Abrir Panel de Progreso Total de la Partida ([calcular_progreso_total()]%% / 100%%)":
            call screen game_progress_modal
            jump pantalla_resumen_final

        "🔄 Volver a la elección de confesiones de las Heroínas Principales":
            $ ruptura_sub_kuroe = True
            $ ruptura_sub_mirei = True
            $ ruptura_sub_reina = True
            $ estado_sub_kuroe = "Terminada"
            $ estado_sub_mirei = "Terminada"
            $ estado_sub_reina = "Terminada"
            jump eleccion_final

        "🗺️ Volver al Mapa Libre del Instituto para completar objetivos o regalos pendientes":
            jump hub_instituto

        "🏁 Terminar partida y volver al Menú Principal":
            $ mostrar_hud = False
            hide screen stats_hud
            return
