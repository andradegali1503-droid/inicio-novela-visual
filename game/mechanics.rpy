################################################################################
## MECÁNICAS, PUNTUACIÓN DESDE 0%, PROGRESO TOTAL (0-100%) Y MAPA LIBRE
################################################################################

## Variables de Estado del Protagonista (Leo) — Todo empieza en 0% al iniciar
default nombre_prota = "Leo"
default reputacion = 0            # 0% a 100% ★ Reputación en el instituto
default ingenio = 0               # 0% a 100% ⚡ Ingenio para resolver líos
default carisma = 0               # 0% a 100% ✨ Carisma y magnetismo
default presupuesto_festival = 0  # 0% a 100% 🏮 Preparación del Festival Cultural
default turnos_dia = 3            # Misiones principales pendientes

## Puntos de Afinidad de las 3 HEROÍNAS PRINCIPALES (Empiezan en 0% ♥ hasta 100% ♥)
default afinidad_akane = 0        # Akane Tachibana (Tsundere - Presidenta del Consejo)
default afinidad_yuki = 0         # Yuki Shirogane (Kuudere - Genio del Club de Ciencias)
default afinidad_hana = 0         # Hana Sakuragi (Genki - Estrella de Atletismo)

## Estado de los Problemas / Misiones de cada Heroína Principal
default estado_mision_akane = "Pendiente"
default estado_mision_yuki = "Pendiente"
default estado_mision_hana = "Pendiente"

## Rutas principales completadas
default visitado_akane = False
default visitado_yuki = False
default visitado_hana = False

################################################################################
## LAS 3 SUB-PERSONAJES (TENTACIÓN, LUJURIA Y ENREDO SECUNDARIO — EMPIEZAN EN 0%)
################################################################################
default tentacion_kuroe = 0       # 0% a 100% 🔥 Nivel de lujuria/enganche con Kuroe
default tentacion_mirei = 0       # 0% a 100% 🔥 Nivel de lujuria/enganche con Mirei
default tentacion_reina = 0       # 0% a 100% 🔥 Nivel de lujuria/enganche con Reina

# Estados posibles: "Disponible", "Enredado", "Terminada"
default estado_sub_kuroe = "Disponible"
default estado_sub_mirei = "Disponible"
default estado_sub_reina = "Disponible"

# Indica si ya tuviste el encuentro picante con cada sub-heroína
default encuentro_sub_kuroe = False
default encuentro_sub_mirei = False
default encuentro_sub_reina = False

# Indica si ya terminaste/cerraste tu aventura con ellas para liberar la ruta principal
default ruptura_sub_kuroe = False
default ruptura_sub_mirei = False
default ruptura_sub_reina = False

# Banderas de entrega de objetos de las sub-personajes a las principales
default actas_entregadas_akane = False
default bobina_instalada_yuki = False
default pase_entregado_hana = False

## Estado de Exploración Libre del Mapa y Progreso Total de la Partida
default ubicacion_actual = "patio"
default zonas_exploradas = set()
default regalo_entregado_akane = False
default regalo_entregado_yuki = False
default regalo_entregado_hana = False
default entrenado_biblioteca = False
default entrenado_cafeteria = False
default entrenado_patio = False
default climax_completado = False
default finales_vistos = set()
default persistent.finales_desbloqueados = set()

## Banderas de Consecuencias (Ramas Narrativas)
default consecuencia_culpa_asumida = False
default consecuencia_jugando_con_fuego = False
default consecuencia_akane_confia = False
default consecuencia_yuki_invento_estable = False
default consecuencia_hana_secreto_guardado = False
default consecuencia_alianza_chicas = False

## Inventario de Objetos Clave obtenidos explorando el instituto
default inventario_items = []

## Historial de Decisiones y Consecuencias
default registro_consecuencias = []

## Contador de intentos en zonas bloqueadas (al 3er intento revela los puntos exactos faltantes)
default intentos_bloqueo_zona = {
    "biblioteca": 0,
    "laboratorio": 0,
    "almacen_mirei": 0,
    "azotea": 0,
    "cafeteria": 0,
    "festival": 0
}
default zona_modal_bloqueada = "biblioteca"

## Cola apilable de notificaciones flotantes y reacciones emocionales en vivo
default cola_popups = []
default mostrar_hud = False
default reaccion_actual_icono = None
default reaccion_actual_pos = "center"
default reaccion_actual_ambiente = None
default charlas_intimidad = {
    "akane": 0,
    "yuki": 0,
    "hana": 0,
    "kuroe": 0,
    "mirei": 0,
    "reina": 0
}

init python:
    # Diccionario de Zonas del Instituto Sakura para el Mapa de Navegación Libre
    ZONAS_INSTITUTO = {
        "azotea": {
            "nombre": "🌅 Azotea del Instituto",
            "subtitulo": "Tejado Principal • Vista Panorámica",
            "pos": (600, 175),
            "heroina": "Principal: Hana Sakuragi 🌸",
            "color": "#ff85a1",
            "descripcion": "El lugar más alto del instituto. Aquí entrena Hana Sakuragi para su exhibición. Tus acciones aquí conectan con Reina del Club de Educación Física.",
            "conexiones": {"abajo": "consejo", "izquierda": "biblioteca", "derecha": "laboratorio"},
            "label_destino": "zona_azotea"
        },
        "consejo": {
            "nombre": "🏛️ Sala del Consejo Estudiantil",
            "subtitulo": "Planta Noble • Torre del Reloj",
            "pos": (600, 355),
            "heroina": "Principal: Akane Tachibana ❤️",
            "color": "#ff4d6d",
            "descripcion": "El centro de mando de la presidenta Akane Tachibana. Su conflicto con los permisos perdidos te llevará directo hacia Kuroe, la chica mala del instituto.",
            "conexiones": {"arriba": "azotea", "abajo": "patio", "izquierda": "biblioteca", "derecha": "laboratorio"},
            "label_destino": "zona_consejo"
        },
        "biblioteca": {
            "nombre": "📚 Biblioteca y Rincón Rebelde",
            "subtitulo": "Ala Oeste • Sub-Ruta: Kuroe Sakamoto 💋",
            "pos": (245, 430),
            "heroina": "Sub-Personaje: Kuroe (Chica Mala) 🔥",
            "color": "#c77dff",
            "descripcion": "Entre las estanterías del fondo se esconde Kuroe Sakamoto, la rebelde más seductora y peligrosa del instituto que se salta todas las clases.",
            "conexiones": {"arriba": "azotea", "derecha": "consejo", "abajo": "patio"},
            "label_destino": "zona_biblioteca"
        },
        "laboratorio": {
            "nombre": "🔬 Laboratorio y Almacén Químico",
            "subtitulo": "Ala Este • Principal: Yuki 💙 | Sub: Mirei 💋",
            "pos": (955, 430),
            "heroina": "Yuki Shirogane 💙 / Mirei Kanzaki 🔥",
            "color": "#4cc9f0",
            "descripcion": "El laboratorio donde Yuki prepara su proyector holográfico... y donde la voluptuosa sempai Mirei Kanzaki realiza sus 'experimentos privados' en la trastienda.",
            "conexiones": {"arriba": "azotea", "izquierda": "consejo", "abajo": "cafeteria"},
            "label_destino": "zona_laboratorio"
        },
        "patio": {
            "nombre": "🌸 Patio Central de los Cerezos",
            "subtitulo": "Corazón del Campus • Escenario y Rumores",
            "pos": (520, 585),
            "heroina": "Punto de Encuentro y Rumores",
            "color": "#ffd166",
            "descripcion": "El centro neurálgico donde se montan los puestos del Festival Cultural y donde circulan todos los secretos sobre las heroínas y sub-personajes.",
            "conexiones": {"arriba": "consejo", "izquierda": "biblioteca", "derecha": "cafeteria"},
            "label_destino": "zona_patio"
        },
        "cafeteria": {
            "nombre": "🍱 Cafetería y Vestuarios Sur",
            "subtitulo": "Planta Baja Sur • Sub-Ruta: Reina Kurokawa 💋",
            "pos": (855, 650),
            "heroina": "Sub-Personaje: Reina (Ed. Física) 🔥",
            "color": "#6fffe9",
            "descripcion": "Junto a la cafetería están los vestuarios del Club de Educación Física, dominados por la ardiente capitana Reina Kurokawa.",
            "conexiones": {"arriba": "laboratorio", "izquierda": "patio"},
            "label_destino": "zona_cafeteria"
        }
    }

    def esta_zona_desbloqueada(clave):
        if clave in ("patio", "consejo"):
            return True
        elif clave == "biblioteca":
            return bool(store.visitado_akane and store.afinidad_akane >= 30)
        elif clave == "laboratorio":
            return bool(store.actas_entregadas_akane and store.afinidad_akane >= 50 and store.tentacion_kuroe >= 25)
        elif clave == "almacen_mirei":
            return bool(store.visitado_yuki and store.afinidad_yuki >= 35)
        elif clave == "azotea":
            return bool(store.bobina_instalada_yuki and store.afinidad_yuki >= 55 and store.tentacion_mirei >= 25)
        elif clave == "cafeteria":
            return bool(store.visitado_hana and store.afinidad_hana >= 35)
        elif clave == "festival":
            return bool(store.pase_entregado_hana and store.presupuesto_festival >= 60 and store.tentacion_reina >= 25)
        return True

    def obtener_diagnostico_bloqueo(clave):
        intentos = store.intentos_bloqueo_zona.get(clave, 1)
        faltan_puntos = []
        faltan_trama = []
        consejo = ""
        nombre_z = ZONAS_INSTITUTO.get(clave, {}).get("nombre", "Zona Bloqueada")

        if clave == "biblioteca":
            aviso = "¡Aún no puedes entrar a la Biblioteca Oeste! La puerta está vigilada y necesitas avanzar primero en la Sala del Consejo Estudiantil."
            if not store.visitado_akane:
                faltan_trama.append("Hablar con Akane en la Sala del Consejo y superar la inspección.")
            diff_ak = max(0, 30 - store.afinidad_akane)
            if diff_ak > 0:
                faltan_puntos.append(f"Te faltan {diff_ak}% de puntos de personaje con Akane Tachibana (Tienes {store.afinidad_akane}% / Requiere 30% ♥).")
            else:
                faltan_puntos.append(f"✔ Puntos con Akane suficientes ({store.afinidad_akane}% / 30% ♥).")
            consejo = "💡 Ve a la Sala del Consejo Estudiantil y habla/ayuda a Akane (+10% ♥ por conversación) para alcanzar el 30% ♥."

        elif clave == "laboratorio":
            aviso = "¡Aún no puedes entrar al Laboratorio de Ciencias! El Ala Este permanece cerrada con llave electrónica por orden del Consejo."
            if not store.visitado_akane:
                faltan_trama.append("Completar el evento principal de Akane en la Sala del Consejo.")
            if not store.encuentro_sub_kuroe:
                faltan_trama.append("Recuperar las 'Actas Secretas' que tiene Kuroe en la Biblioteca Oeste.")
            if not store.actas_entregadas_akane:
                faltan_trama.append("Entregar las 'Actas Secretas Recuperadas' a Akane en el Consejo.")
            diff_ak = max(0, 50 - store.afinidad_akane)
            diff_ku = max(0, 25 - store.tentacion_kuroe)
            if diff_ak > 0:
                faltan_puntos.append(f"Te faltan {diff_ak}% de puntos de personaje con Akane Tachibana (Tienes {store.afinidad_akane}% / Requiere 50% ♥).")
            else:
                faltan_puntos.append(f"✔ Puntos con Akane suficientes ({store.afinidad_akane}% / 50% ♥).")
            if diff_ku > 0:
                faltan_puntos.append(f"Te faltan {diff_ku}% de puntos de sub-personaje con Kuroe Sakamoto (Tienes {store.tentacion_kuroe}% / Requiere 25% 🔥).")
            else:
                faltan_puntos.append(f"✔ Puntos con Kuroe suficientes ({store.tentacion_kuroe}% / 25% 🔥).")
            consejo = "💡 Resuelve el trato con Kuroe en la Biblioteca y conversa con Akane en la Sala del Consejo para subir sus puntos."

        elif clave == "almacen_mirei":
            nombre_z = "🧪 Almacén Químico Privado (Mirei Kanzaki)"
            aviso = "¡Aún no puedes entrar al Almacén Químico! La sempai Mirei no te abrirá la puerta hasta que avances con Yuki en el Laboratorio."
            if not store.visitado_yuki:
                faltan_trama.append("Ayudar primero a Yuki Shirogane a revisar el Proyector Holográfico.")
            diff_yu = max(0, 35 - store.afinidad_yuki)
            if diff_yu > 0:
                faltan_puntos.append(f"Te faltan {diff_yu}% de puntos de personaje con Yuki Shirogane (Tienes {store.afinidad_yuki}% / Requiere 35% ♥).")
            else:
                faltan_puntos.append(f"✔ Puntos con Yuki suficientes ({store.afinidad_yuki}% / 35% ♥).")
            consejo = "💡 Habla con Yuki en el Laboratorio (+10% ♥) o tráele el 'Libro de Astrofísica Poética' desde la Biblioteca (+15% ♥)."

        elif clave == "azotea":
            aviso = "¡Aún no puedes subir a la Azotea del Instituto! El cierre electrónico de la escalera depende del generador del Laboratorio."
            if not store.actas_entregadas_akane:
                faltan_trama.append("Cerrar primero el arco del Consejo Estudiantil con Akane y Kuroe.")
            if not store.visitado_yuki:
                faltan_trama.append("Completar el evento principal de Yuki en el Laboratorio Este.")
            if not store.encuentro_sub_mirei:
                faltan_trama.append("Conseguir la 'Bobina Experimental' con la sempai Mirei en el almacén químico.")
            if not store.bobina_instalada_yuki:
                faltan_trama.append("Instalar la 'Bobina Experimental de Mirei' en el proyector de Yuki.")
            diff_yu = max(0, 55 - store.afinidad_yuki)
            diff_mi = max(0, 25 - store.tentacion_mirei)
            if diff_yu > 0:
                faltan_puntos.append(f"Te faltan {diff_yu}% de puntos de personaje con Yuki Shirogane (Tienes {store.afinidad_yuki}% / Requiere 55% ♥).")
            else:
                faltan_puntos.append(f"✔ Puntos con Yuki suficientes ({store.afinidad_yuki}% / 55% ♥).")
            if diff_mi > 0:
                faltan_puntos.append(f"Te faltan {diff_mi}% de puntos de sub-personaje con Mirei Kanzaki (Tienes {store.tentacion_mirei}% / Requiere 25% 🔥).")
            else:
                faltan_puntos.append(f"✔ Puntos con Mirei suficientes ({store.tentacion_mirei}% / 25% 🔥).")
            consejo = "💡 Entra al almacén con Mirei, instala la Bobina con Yuki y conversa con Yuki o regálale su libro favorito."

        elif clave == "cafeteria":
            aviso = "¡Aún no puedes entrar a los Vestuarios Sur y Cafetería! El Club de Educación Física entrena a puerta cerrada."
            if not store.bobina_instalada_yuki:
                faltan_trama.append("Completar primero el arco del Laboratorio (Yuki y Mirei) para abrir la Azotea.")
            if not store.visitado_hana:
                faltan_trama.append("Subir a la Azotea del Instituto y ayudar a Hana con su exhibición.")
            diff_ha = max(0, 35 - store.afinidad_hana)
            if diff_ha > 0:
                faltan_puntos.append(f"Te faltan {diff_ha}% de puntos de personaje con Hana Sakuragi (Tienes {store.afinidad_hana}% / Requiere 35% ♥).")
            else:
                faltan_puntos.append(f"✔ Puntos con Hana suficientes ({store.afinidad_hana}% / 35% ♥).")
            consejo = "💡 Sube a la Azotea del Instituto y conversa/anima a Hana junto a la barandilla (+10% ♥) para llegar al 35% ♥."

        else:
            nombre_z = "🏮 Gran Festival Cultural Nocturno (Clímax)"
            aviso = "¡Aún no puedes iniciar la Noche del Festival! Todavía quedan preparativos y puntos de progreso por completar en el instituto."
            if not store.actas_entregadas_akane:
                faltan_trama.append("Entregar las Actas Secretas a Akane en el Consejo.")
            if not store.bobina_instalada_yuki:
                faltan_trama.append("Instalar la Bobina Experimental en el proyector de Yuki.")
            if not store.pase_entregado_hana:
                faltan_trama.append("Entregar el Pase Oficial de Exhibición firmado por Reina a Hana en la Azotea.")
            diff_pr = max(0, 60 - store.presupuesto_festival)
            diff_re = max(0, 25 - store.tentacion_reina)
            if diff_pr > 0:
                faltan_puntos.append(f"Te faltan {diff_pr}% de Preparación del Festival (Tienes {store.presupuesto_festival}% / Requiere 60% 🏮).")
            else:
                faltan_puntos.append(f"✔ Preparación del Festival suficiente ({store.presupuesto_festival}% / 60% 🏮).")
            if diff_re > 0:
                faltan_puntos.append(f"Te faltan {diff_re}% de puntos de sub-personaje con Reina Kurokawa (Tienes {store.tentacion_reina}% / Requiere 25% 🔥).")
            else:
                faltan_puntos.append(f"✔ Puntos con Reina suficientes ({store.tentacion_reina}% / 25% 🔥).")
            consejo = "💡 Negocia el Pase con Reina en los Vestuarios Sur, entrégaselo a Hana en la Azotea y ayuda en el Patio Central."

        return {
            "clave": clave,
            "nombre": nombre_z,
            "intentos": intentos,
            "revelado": (intentos >= 3),
            "aviso": aviso,
            "faltan_trama": faltan_trama,
            "faltan_puntos": faltan_puntos,
            "consejo": consejo
        }

    def obtener_motivo_bloqueo_zona(clave):
        diag = obtener_diagnostico_bloqueo(clave)
        if diag["revelado"] and len(diag["faltan_puntos"]) > 0:
            return "📊 " + " | ".join(diag["faltan_puntos"])
        return "🔒 " + diag["aviso"]

    def obtener_objetivo_actual():
        if not store.visitado_akane:
            return (1, 7, "Ve a la Sala del Consejo Estudiantil y ayuda a Akane con la inspección", "consejo")
        elif store.afinidad_akane < 30:
            return (1, 7, f"Sube tu afinidad con Akane en el Consejo a 30% ♥ (Tienes {store.afinidad_akane}% ♥) para abrir Biblioteca", "consejo")
        elif not store.encuentro_sub_kuroe:
            return (2, 7, "🔓 Biblioteca Abierta: Ve a la Biblioteca Oeste y recupera las Actas que robó Kuroe", "biblioteca")
        elif not store.actas_entregadas_akane:
            return (3, 7, "Regresa a la Sala del Consejo y entrégale las 'Actas Secretas Recuperadas' a Akane", "consejo")
        elif store.afinidad_akane < 50:
            return (3, 7, f"Conversa con Akane en el Consejo hasta llegar a 50% ♥ (Tienes {store.afinidad_akane}% ♥) para abrir Laboratorio", "consejo")
        elif not store.visitado_yuki:
            return (4, 7, "🔓 Laboratorio Abierto: Ve al Laboratorio Este y ayuda a Yuki con el Proyector", "laboratorio")
        elif store.afinidad_yuki < 35:
            return (4, 7, f"Habla con Yuki o regálale su libro hasta tener 35% ♥ (Tienes {store.afinidad_yuki}% ♥) para abrir Almacén", "laboratorio")
        elif not store.encuentro_sub_mirei:
            return (5, 7, "En el Laboratorio, entra al almacén químico con la sempai Mirei por la Bobina", "laboratorio")
        elif not store.bobina_instalada_yuki:
            return (5, 7, "En el Laboratorio, instala la 'Bobina Experimental de Mirei' en el proyector de Yuki", "laboratorio")
        elif store.afinidad_yuki < 55:
            return (5, 7, f"Conversa con Yuki o entrégale su libro hasta tener 55% ♥ (Tienes {store.afinidad_yuki}% ♥) para abrir Azotea", "laboratorio")
        elif not store.visitado_hana:
            return (6, 7, "🔓 Azotea Abierta: Sube a la Azotea del Instituto y ayuda a Hana con su exhibición", "azotea")
        elif store.afinidad_hana < 35:
            return (6, 7, f"Habla y anima a Hana en la Azotea hasta llegar a 35% ♥ (Tienes {store.afinidad_hana}% ♥) para abrir Vestuarios", "azotea")
        elif not store.encuentro_sub_reina:
            return (7, 7, "🔓 Vestuarios Sur Abiertos: Ve a la Cafetería/Vestuarios y negocia el Pase con Reina", "cafeteria")
        elif not store.pase_entregado_hana:
            return (7, 7, "Regresa a la Azotea del Instituto y entrégale el 'Pase Oficial de Exhibición' a Hana", "azotea")
        elif store.presupuesto_festival < 60:
            return (7, 7, f"Sube el progreso del Festival al 60% (Tienes {store.presupuesto_festival}%) ayudando en el Patio Central", "patio")
        else:
            pend = obtener_estado_sub_Pendiente()
            if len(pend) > 0:
                return (7, 7, f"¡Historia lista! Termina tus enredos con {', '.join(pend)} o ve al Festival Nocturno", "patio")
            return (7, 7, "¡Todas las misiones completadas! Pulsa '¡IR AL FESTIVAL NOCTURNO!' cuando estés listo", "patio")

    ############################################################################
    ## SISTEMA DE PROGRESO TOTAL DE LA PARTIDA (0% A 100%) Y CHECKLIST COMPLETO
    ############################################################################
    def obtener_desglose_progreso_juego():
        """Devuelve el porcentaje total (0 a 100%) y la lista detallada de qué tiene y qué le falta al jugador."""
        hitos = [
            # Categoría 1: Historia Principal (35%)
            {
                "categoria": "💖 Historia Principal (Heroínas)",
                "titulo": "Etapa 1: Ayudar a Akane con la inspección del Consejo",
                "completado": bool(store.visitado_akane),
                "peso": 5,
                "como_lograrlo": "Ve a la Sala del Consejo Estudiantil y completa el evento de Akane."
            },
            {
                "categoria": "💖 Historia Principal (Heroínas)",
                "titulo": "Etapa 3: Entregar las 'Actas Secretas Recuperadas' a Akane",
                "completado": bool(store.actas_entregadas_akane),
                "peso": 7,
                "como_lograrlo": "Recupera las actas con Kuroe en la Biblioteca y entrégaselas a Akane en el Consejo."
            },
            {
                "categoria": "💖 Historia Principal (Heroínas)",
                "titulo": "Etapa 4: Ayudar a Yuki con el Proyector Holográfico",
                "completado": bool(store.visitado_yuki),
                "peso": 5,
                "como_lograrlo": "Desbloquea el Laboratorio Este y ayuda a Yuki con su proyector."
            },
            {
                "categoria": "💖 Historia Principal (Heroínas)",
                "titulo": "Etapa 5: Instalar la 'Bobina Experimental' en el proyector de Yuki",
                "completado": bool(store.bobina_instalada_yuki),
                "peso": 6,
                "como_lograrlo": "Consigue la bobina con Mirei en el almacén químico e instálala en el Laboratorio."
            },
            {
                "categoria": "💖 Historia Principal (Heroínas)",
                "titulo": "Etapa 6: Asistir a Hana con su lesión en la Azotea",
                "completado": bool(store.visitado_hana),
                "peso": 5,
                "como_lograrlo": "Sube a la Azotea del Instituto y ayuda a Hana con su ensayo."
            },
            {
                "categoria": "💖 Historia Principal (Heroínas)",
                "titulo": "Etapa 7: Entregar el 'Pase Oficial de Exhibición' a Hana",
                "completado": bool(store.pase_entregado_hana),
                "peso": 7,
                "como_lograrlo": "Consigue el pase firmado por Reina en los Vestuarios Sur y llévaselo a Hana."
            },

            # Categoría 2: Sub-Rutas Darkness (25%)
            {
                "categoria": "😈 Sub-Rutas Darkness (Tentaciones)",
                "titulo": "Sub-Ruta Kuroe: Enfrentar a la chica mala en la Biblioteca",
                "completado": bool(store.encuentro_sub_kuroe),
                "peso": 5,
                "como_lograrlo": "Entra a la Biblioteca Oeste (requiere 30% ♥ con Akane) y negocia con Kuroe."
            },
            {
                "categoria": "😈 Sub-Rutas Darkness (Tentaciones)",
                "titulo": "Cerrar aventura con Kuroe (Sin ataduras para el final)",
                "completado": bool(store.ruptura_sub_kuroe),
                "peso": 3,
                "como_lograrlo": "Mantén la mente fría ante Kuroe o vuelve a la Biblioteca para terminar con ella."
            },
            {
                "categoria": "😈 Sub-Rutas Darkness (Tentaciones)",
                "titulo": "Sub-Ruta Mirei: Entrar al Almacén Químico privado",
                "completado": bool(store.encuentro_sub_mirei),
                "peso": 5,
                "como_lograrlo": "En el Laboratorio (requiere 35% ♥ con Yuki), sigue a la sempai Mirei al almacén."
            },
            {
                "categoria": "😈 Sub-Rutas Darkness (Tentaciones)",
                "titulo": "Cerrar aventura con Mirei (Sin ataduras para el final)",
                "completado": bool(store.ruptura_sub_mirei),
                "peso": 3,
                "como_lograrlo": "Resiste las feromonas de Mirei o corta tu aventura con ella en el Laboratorio."
            },
            {
                "categoria": "😈 Sub-Rutas Darkness (Tentaciones)",
                "titulo": "Sub-Ruta Reina: Negociar en los Vestuarios del Jardín Sur",
                "completado": bool(store.encuentro_sub_reina),
                "peso": 6,
                "como_lograrlo": "Ve a Cafetería y Vestuarios Sur (requiere 35% ♥ con Hana) y habla con Reina."
            },
            {
                "categoria": "😈 Sub-Rutas Darkness (Tentaciones)",
                "titulo": "Cerrar aventura con Reina (Sin ataduras para el final)",
                "completado": bool(store.ruptura_sub_reina),
                "peso": 3,
                "como_lograrlo": "Gánale el duelo deportivo a Reina o termina tu aventura con ella en los Vestuarios."
            },

            # Categoría 3: Afinidad Máxima y Regalos (25%)
            {
                "categoria": "🎁 Vínculos Románticos y Regalos",
                "titulo": f"Alcanzar 50%+ ♥ con Akane para su Final Verdadero (Actual: {store.afinidad_akane}%)",
                "completado": bool(store.afinidad_akane >= 50),
                "peso": 5,
                "como_lograrlo": "Apóyala en el Consejo, entrégale las Actas y regálale su Té Real de Durazno."
            },
            {
                "categoria": "🎁 Vínculos Románticos y Regalos",
                "titulo": f"Alcanzar 50%+ ♥ con Yuki para su Final Verdadero (Actual: {store.afinidad_yuki}%)",
                "completado": bool(store.afinidad_yuki >= 50),
                "peso": 5,
                "como_lograrlo": "Ayúdala en el Laboratorio, instala la Bobina y regálale el Libro de Astrofísica."
            },
            {
                "categoria": "🎁 Vínculos Románticos y Regalos",
                "titulo": f"Alcanzar 50%+ ♥ con Hana para su Final Verdadero (Actual: {store.afinidad_hana}%)",
                "completado": bool(store.afinidad_hana >= 50),
                "peso": 5,
                "como_lograrlo": "Cuida su tobillo en la Azotea, entrégale el Pase y dale el Botiquín Deportivo."
            },
            {
                "categoria": "🎁 Vínculos Románticos y Regalos",
                "titulo": "Regalo Secreto 1: Entregar 'Té Real de Durazno' a Akane",
                "completado": bool(store.regalo_entregado_akane),
                "peso": 3,
                "como_lograrlo": "Consigue el Té en la Cafetería Sur y entrégaselo a Akane en el Consejo (+15% ♥)."
            },
            {
                "categoria": "🎁 Vínculos Románticos y Regalos",
                "titulo": "Regalo Secreto 2: Entregar 'Libro de Astrofísica Poética' a Yuki",
                "completado": bool(store.regalo_entregado_yuki),
                "peso": 3,
                "como_lograrlo": "Busca el libro en la Biblioteca Oeste y entrégaselo a Yuki en el Laboratorio (+15% ♥)."
            },
            {
                "categoria": "🎁 Vínculos Románticos y Regalos",
                "titulo": "Regalo Secreto 3: Entregar 'Botiquín Deportivo Frío' a Hana",
                "completado": bool(store.regalo_entregado_hana),
                "peso": 4,
                "como_lograrlo": "Consigue el Botiquín en la Cafetería Sur y llévaselo a Hana en la Azotea (+15% ♥)."
            },

            # Categoría 4: Exploración, Entrenamientos y Clímax (15%)
            {
                "categoria": "🏫 Exploración y Festival Cultural",
                "titulo": f"Explorar las 6 Zonas del Instituto Sakura ({len(store.zonas_exploradas)}/6 visitadas)",
                "completado": bool(len(store.zonas_exploradas) >= 6),
                "peso": 5,
                "como_lograrlo": "Desbloquea y entra en Consejo, Biblioteca, Laboratorio, Azotea, Patio y Cafetería."
            },
            {
                "categoria": "🏫 Exploración y Festival Cultural",
                "titulo": "Completar las 3 Actividades Extra (Biblioteca, Patio y Cafetería)",
                "completado": bool(store.entrenado_biblioteca and store.entrenado_patio and store.entrenado_cafeteria),
                "peso": 5,
                "como_lograrlo": "Estudia en la Biblioteca (+Ingenio), monta farolillos en el Patio (+Reputación) y socializa en Cafetería (+Carisma)."
            },
            {
                "categoria": "🏫 Exploración y Festival Cultural",
                "titulo": "Llegar al Clímax del Festival Cultural Nocturno y ver un Final",
                "completado": bool(store.climax_completado),
                "peso": 5,
                "como_lograrlo": "Cuando tengas las 3 misiones listas y 60%+ de Festival, inicia el Festival Nocturno."
            }
        ]

        porcentaje_total = sum(h["peso"] for h in hitos if h["completado"])
        completados_count = sum(1 for h in hitos if h["completado"])
        pendientes_list = [h for h in hitos if not h["completado"]]

        return {
            "porcentaje": min(100, porcentaje_total),
            "completados": completados_count,
            "total_hitos": len(hitos),
            "hitos": hitos,
            "pendientes": pendientes_list
        }

    def calcular_progreso_total():
        return obtener_desglose_progreso_juego()["porcentaje"]

    def es_final_desbloqueado(id_final):
        if id_final in store.finales_vistos:
            return True
        if hasattr(persistent, "finales_desbloqueados") and persistent.finales_desbloqueados and id_final in persistent.finales_desbloqueados:
            return True
        return False

    def registrar_final(id_final):
        store.finales_vistos.add(id_final)
        if not hasattr(persistent, "finales_desbloqueados") or persistent.finales_desbloqueados is None:
            persistent.finales_desbloqueados = set()
        persistent.finales_desbloqueados.add(id_final)

    def obtener_catalogo_finales():
        return [
            {
                "id": "akane",
                "titulo": "Ruta Verdadera de Akane Tachibana",
                "subtitulo": "«El Corazón Secreto de la Presidenta Tsundere»",
                "tipo": "Heroína Principal ❤️",
                "color": "#ff4d6d",
                "thumb": "images/thumb_akane.png",
                "desbloqueado": es_final_desbloqueado("akane"),
                "visto": es_final_desbloqueado("akane"),
                "requisito": "50%+ ♥ Akane + Cierre con Kuroe + Festival Salvado.",
                "descripcion": "Akane confiesa su amor en el balcón del Consejo tras superar la inspección del Subdirector y salvar el Festival Cultural juntos."
            },
            {
                "id": "yuki",
                "titulo": "Ruta Verdadera de Yuki Shirogane",
                "subtitulo": "«La Ecuación Perfecta del Primer Amor»",
                "tipo": "Heroína Principal 💙",
                "color": "#4cc9f0",
                "thumb": "images/thumb_yuki.png",
                "desbloqueado": es_final_desbloqueado("yuki"),
                "visto": es_final_desbloqueado("yuki"),
                "requisito": "50%+ ♥ Yuki + Cierre con Mirei + Festival Salvado.",
                "descripcion": "Yuki experimenta la calidez del amor bajo la proyección de galaxias del proyector holográfico estabilizado en el laboratorio."
            },
            {
                "id": "hana",
                "titulo": "Ruta Verdadera de Hana Sakuragi",
                "subtitulo": "«Promesa Bajo la Lluvia de Sakura»",
                "tipo": "Heroína Principal 🌸",
                "color": "#ff85a1",
                "thumb": "images/thumb_hana.png",
                "desbloqueado": es_final_desbloqueado("hana"),
                "visto": es_final_desbloqueado("hana"),
                "requisito": "50%+ ♥ Hana + Cierre con Reina + Festival Salvado.",
                "descripcion": "Hana triunfa en su exhibición deportiva en pareja contigo frente al ojeador y se confiesan bajo el gran cerezo florecido."
            },
            {
                "id": "harem",
                "titulo": "Final Secreto Legendario",
                "subtitulo": "«El Héroe Indiscutible del Instituto Sakura (Harem)»",
                "tipo": "Final Secreto 👑",
                "color": "#ffd166",
                "thumb": "images/ui/icon_tlr_heart.png",
                "desbloqueado": es_final_desbloqueado("harem"),
                "visto": es_final_desbloqueado("harem"),
                "requisito": "50%+ ♥ con Akane, Yuki y Hana + 75%+ Festival + Sin ataduras.",
                "descripcion": "¡Las tres heroínas principales se reúnen contigo bajo los fuegos artificiales y acuerdan compartir tu amor sin ceder un solo centímetro!"
            },
            {
                "id": "kuroe",
                "titulo": "Sub-Ruta Prohibida de Kuroe Sakamoto",
                "subtitulo": "«Prisionero de la Chica Mala»",
                "tipo": "Modo Darkness 🔥",
                "color": "#e0aaff",
                "thumb": "images/thumb_kuroe.png",
                "desbloqueado": es_final_desbloqueado("kuroe"),
                "visto": es_final_desbloqueado("kuroe"),
                "requisito": "Enredado con Kuroe al comenzar el Festival.",
                "descripcion": "Sucumbes a la pasión rebelde de Kuroe y abandonas la ceremonia oficial para pasar la noche encerrado con ella entre las estanterías de la biblioteca."
            },
            {
                "id": "mirei",
                "titulo": "Sub-Ruta Prohibida de Mirei Kanzaki",
                "subtitulo": "«Experimento Nocturno de Lujuria»",
                "tipo": "Modo Darkness 🔥",
                "color": "#c77dff",
                "thumb": "images/thumb_mirei.png",
                "desbloqueado": es_final_desbloqueado("mirei"),
                "visto": es_final_desbloqueado("mirei"),
                "requisito": "Enredado con Mirei al comenzar el Festival.",
                "descripcion": "Te entregas al experimento corporal de la voluptuosa sempai Mirei en el almacén químico mientras el resto del instituto observa los fuegos."
            },
            {
                "id": "reina",
                "titulo": "Sub-Ruta Prohibida de Reina Kurokawa",
                "subtitulo": "«Entrenamiento Privado sin Límites»",
                "tipo": "Modo Darkness 🔥",
                "color": "#ff9e00",
                "thumb": "images/thumb_reina.png",
                "desbloqueado": es_final_desbloqueado("reina"),
                "visto": es_final_desbloqueado("reina"),
                "requisito": "Enredado con Reina al comenzar el Festival.",
                "descripcion": "Reina te arrastra a los vestuarios de educación física tras las duchas para una ardiente sesión de resistencia corporal hasta el amanecer."
            }
        ]

    def registrar_intento_bloqueo(clave):
        store.intentos_bloqueo_zona[clave] = store.intentos_bloqueo_zona.get(clave, 0) + 1
        store.zona_modal_bloqueada = clave
        renpy.show_screen("locked_zone_modal")
        renpy.restart_interaction()

    def intentar_entrar_zona(clave):
        if esta_zona_desbloqueada(clave):
            if clave == "festival":
                renpy.end_interaction("ir_climax_festival")
            else:
                renpy.end_interaction(ZONAS_INSTITUTO[clave]["label_destino"])
        else:
            registrar_intento_bloqueo(clave)

    def mover_en_mapa(direccion):
        zona_info = ZONAS_INSTITUTO.get(store.ubicacion_actual, {})
        conexiones = zona_info.get("conexiones", {})
        if direccion in conexiones:
            store.ubicacion_actual = conexiones[direccion]
            renpy.restart_interaction()

    def obtener_rango_relacion(puntos):
        if puntos == 0:
            return ("0% — Desconocidos", "#b892b0")
        elif puntos < 30:
            return ("Conocidos de Pasillo", "#ffaa4d")
        elif puntos < 50:
            return ("Aliado de Confianza", "#ffd166")
        elif puntos < 75:
            return ("Interés Romántico", "#4cc9f0")
        else:
            return ("Enamorada / Alma Gemela", "#ff4d8d")

    def obtener_estado_sub_Pendiente():
        pendientes = []
        if store.estado_sub_kuroe == "Enredado" and not store.ruptura_sub_kuroe:
            pendientes.append("Kuroe")
        if store.estado_sub_mirei == "Enredado" and not store.ruptura_sub_mirei:
            pendientes.append("Mirei")
        if store.estado_sub_reina == "Enredado" and not store.ruptura_sub_reina:
            pendientes.append("Reina")
        return pendientes

    def obtener_texto_sub_pendientes():
        pendientes = obtener_estado_sub_Pendiente()
        return ", ".join(pendientes)

    def registrar_charla(personaje):
        if personaje in store.charlas_intimidad:
            store.charlas_intimidad[personaje] = store.charlas_intimidad.get(personaje, 0) + 1
        return store.charlas_intimidad.get(personaje, 1)

    def limpiar_popups():
        store.cola_popups = []
        renpy.hide_screen("point_popup")

    def notificar_cambio(texto, color="#ffd166"):
        store.cola_popups.append((texto, color))
        if len(store.cola_popups) > 4:
            store.cola_popups = store.cola_popups[-4:]
        try:
            renpy.play("audio/sfx_chime.wav", channel="sound")
        except Exception:
            pass
        renpy.hide_screen("point_popup")
        renpy.show_screen("point_popup")
        renpy.restart_interaction()

    def cambiar_afinidad(chica, cantidad, motivo=""):
        if chica == "akane":
            store.afinidad_akane = max(0, min(100, store.afinidad_akane + cantidad))
            nombre = "Akane"
            actual = store.afinidad_akane
            color = "#ff4d6d" if cantidad >= 0 else "#ff3333"
        elif chica == "yuki":
            store.afinidad_yuki = max(0, min(100, store.afinidad_yuki + cantidad))
            nombre = "Yuki"
            actual = store.afinidad_yuki
            color = "#4cc9f0" if cantidad >= 0 else "#ff3333"
        elif chica == "hana":
            store.afinidad_hana = max(0, min(100, store.afinidad_hana + cantidad))
            nombre = "Hana"
            actual = store.afinidad_hana
            color = "#ff85a1" if cantidad >= 0 else "#ff3333"
        else:
            return

        signo = "+" if cantidad >= 0 else ""
        icono = "♥" if cantidad >= 0 else "💔"
        msg = f"{icono} {nombre} {signo}{cantidad}% (Total: {actual}%)"
        if motivo:
            msg += f" | {motivo}"
        notificar_cambio(msg, color)

    def cambiar_tentacion(sub_chica, cantidad, motivo=""):
        if sub_chica == "kuroe":
            store.tentacion_kuroe = max(0, min(100, store.tentacion_kuroe + cantidad))
            nombre = "Kuroe"
            actual = store.tentacion_kuroe
            color = "#e0aaff"
        elif sub_chica == "mirei":
            store.tentacion_mirei = max(0, min(100, store.tentacion_mirei + cantidad))
            nombre = "Mirei"
            actual = store.tentacion_mirei
            color = "#c77dff"
        elif sub_chica == "reina":
            store.tentacion_reina = max(0, min(100, store.tentacion_reina + cantidad))
            nombre = "Reina"
            actual = store.tentacion_reina
            color = "#ff9e00"
        else:
            return

        signo = "+" if cantidad >= 0 else ""
        msg = f"🔥 Lujuria {nombre} {signo}{cantidad}% (Total: {actual}%)"
        if motivo:
            msg += f" | {motivo}"
        notificar_cambio(msg, color)

    def cambiar_stat(stat, cantidad, motivo=""):
        signo = "+" if cantidad >= 0 else ""
        if stat == "reputacion":
            store.reputacion = max(0, min(100, store.reputacion + cantidad))
            etiqueta = "★ Reputación"
            actual = store.reputacion
            color = "#a8e6cf" if cantidad >= 0 else "#ff6b6b"
        elif stat == "ingenio":
            store.ingenio = max(0, min(100, store.ingenio + cantidad))
            etiqueta = "⚡ Ingenio"
            actual = store.ingenio
            color = "#70d6ff"
        elif stat == "carisma":
            store.carisma = max(0, min(100, store.carisma + cantidad))
            etiqueta = "✨ Carisma"
            actual = store.carisma
            color = "#ffd166"
        elif stat == "festival":
            store.presupuesto_festival = max(0, min(100, store.presupuesto_festival + cantidad))
            etiqueta = "🏮 Festival"
            actual = store.presupuesto_festival
            color = "#ff9f1c"
        else:
            return

        msg = f"{etiqueta} {signo}{cantidad}% (Total: {actual}%)"
        if motivo:
            msg += f" | {motivo}"
        notificar_cambio(msg, color)

    def registrar_rama(titulo, descripcion, impacto):
        store.registro_consecuencias.append({
            "titulo": titulo,
            "descripcion": descripcion,
            "impacto": impacto
        })

    def agregar_item(nombre_item):
        if nombre_item not in store.inventario_items:
            store.inventario_items.append(nombre_item)
            notificar_cambio(f"🎒 Objeto obtenido: {nombre_item}", "#c77dff")

    def remover_item(nombre_item):
        if nombre_item in store.inventario_items:
            store.inventario_items.remove(nombre_item)

    def limpiar_reaccion():
        store.reaccion_actual_icono = None
        store.reaccion_actual_ambiente = None
        renpy.hide_screen("reaction_overlay")

    def mostrar_reaccion(emote, posicion="center", ambiente=None):
        """Muestra un icono de reacción anime flotante (hearts, anger, shock, sweat, sparkle, lust, question, music), brillo ambiental y SFX."""
        mapa_iconos = {
            "hearts": "images/ui/emote_hearts.png",
            "anger": "images/ui/emote_anger.png",
            "shock": "images/ui/emote_shock.png",
            "sweat": "images/ui/emote_sweat.png",
            "sparkle": "images/ui/emote_sparkle.png",
            "lust": "images/ui/emote_lust.png",
            "question": "images/ui/emote_question.png",
            "music": "images/ui/emote_music.png"
        }
        mapa_sonidos = {
            "hearts": "audio/sfx_heartbeat.wav",
            "lust": "audio/sfx_heartbeat.wav",
            "anger": "audio/sfx_alert.wav",
            "shock": "audio/sfx_alert.wav",
            "sparkle": "audio/sfx_sparkle.wav",
            "music": "audio/sfx_chime.wav",
            "sweat": "audio/sfx_blush.wav",
            "question": "audio/sfx_blush.wav"
        }
        store.reaccion_actual_icono = mapa_iconos.get(emote, "images/ui/emote_hearts.png")
        store.reaccion_actual_pos = posicion
        store.reaccion_actual_ambiente = ambiente
        sfx = mapa_sonidos.get(emote)
        if sfx:
            try:
                renpy.play(sfx, channel="sound")
            except Exception:
                pass
        renpy.hide_screen("reaction_overlay")
        renpy.show_screen("reaction_overlay")
        renpy.restart_interaction()

    def anunciar_lugar(nombre_lugar, subtitulo, icono="🏫"):
        """Muestra un elegante banner animado de localización con sonido de transición cinemática."""
        renpy.hide_screen("location_splash")
        renpy.show_screen("location_splash", nombre_lugar=nombre_lugar, subtitulo=subtitulo, icono=icono)
        try:
            renpy.play("audio/sfx_swoosh.wav", channel="sound")
        except Exception:
            pass


