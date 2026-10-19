# 🔍 Auditoría de Continuidad y Coherencia Narrativa

Auditoría exhaustiva del proyecto realizada conforme a los principios de **Branching Continuity**.

---

## 📋 Tabla de Severidad y Hallazgos

| Severidad | Archivo / Escena | Problema Detectado | Impacto en la Jugabilidad | Corrección Aplicada |
| :--- | :--- | :--- | :--- | :--- |
| **ALTA** | `game/script.rpy:238` *(Prólogo)* | Bandera huérfana: `$ consecuencia_culpa_asumida = True` se asignaba en la Opción 1 de honor, pero nunca se leía ni tenía eco posterior. Además, la Opción 2 ("Jugando con Fuego") no fijaba ninguna bandera. | La elección inaugural no producía impacto ni reactividad en el clímax ni en las rupturas de las sub-rutas. | Se añadió `default consecuencia_jugando_con_fuego = False`, se asignó en la Opción 2, y se integró reactividad en los diálogos de Kuroe, Mirei y Reina en `verificar_rupturas_antes_climax` y de Akane en `climax_festival`. |
| **ALTA** | `game/mechanics.rpy:97` / `game/script.rpy` | Variable `charlas_intimidad` declarada en `mechanics.rpy` pero nunca actualizada ni leída en las etiquetas `charlar_con_akane`, `charlar_con_yuki`, etc. | Las visitas repetidas a las heroínas no reflejaban intimidad progresiva ni guardaban memoria del tiempo compartido. | Se implementó la función helper `registrar_charla(personaje)`, se integró en las 6 etiquetas de charla y se agregaron ramas de diálogo diferenciadas según el número de visitas. |
| **MEDIA** | `game/script.rpy:297` (`confirmar_ir_festival`) | Interpolación compleja con comillas dentro de corchetes: `**[', '.join(pendientes_sub)]**`. | Riesgo de excepción sintáctica en el evaluador AST de Ren'Py en tiempo de ejecución. | Se encapsuló la lista en la función `obtener_texto_sub_pendientes()` y se realizó la interpolación limpia con la variable `[sub_pendientes_texto]`. |
| **BAJA** | `game/mechanics.rpy:11` / `game/script.rpy` | Variable `turnos_dia` se restaba en cada visita a heroína pero no bloqueaba la libertad de movimiento en el mapa (el diseño es de exploración libre). | Riesgo de confusión conceptual sobre si existía un límite estricto de turnos. | Se documentó su rol como contador informativo de misiones principales pendientes (3 iniciales, 0 al completar las tres). |
| **BAJA** | `game/animations.rpy:88` | Error histórico corregido en el log: `repeat 2:` producía error de sintaxis en ATL Ren'Py. | El script fallaba al compilar si contenía dos puntos tras repeat. | Verificado en código actual: corregido a `repeat 2` sin dos puntos, compilando limpiamente. |

---

## 📊 Invariantes y Rangos de Variables Canónicas

| Variable | Tipo | Rango Válido | Inicialización | Propósito y Uso |
| :--- | :--- | :--- | :--- | :--- |
| `nombre_prota` | String | 1 a 18 chars | `"Leo"` | Nombre del protagonista con soporte para Ren'Py text tag `[nombre_prota]`. |
| `reputacion` | Entero | `0%` a `100%` | `0` | Respeto del profesorado y estudiantes ante resoluciones maduras. |
| `ingenio` | Entero | `0%` a `100%` | `0` | Destreza intelectual y técnica para resolver problemas sin atajos sucios. |
| `carisma` | Entero | `0%` a `100%` | `0` | Habilidad de persuasión, encanto social y magnetismo personal. |
| `presupuesto_festival` | Entero | `0%` a `100%` | `0` | Preparación general del evento; se requiere `>= 60%` para el Festival y `>= 75%` para Harem. |
| `afinidad_akane` | Entero | `0%` a `100%` | `0` | Afecto romántico de Akane; desbloquea Biblioteca (`30%`) y True End (`50%`). |
| `afinidad_yuki` | Entero | `0%` a `100%` | `0` | Afecto romántico de Yuki; desbloquea Almacén (`35%`) y True End (`50%`). |
| `afinidad_hana` | Entero | `0%` a `100%` | `0` | Afecto romántico de Hana; desbloquea Cafetería (`35%`) y True End (`50%`). |
| `tentacion_kuroe` | Entero | `0%` a `100%` | `0` | Nivel de provocación/lujuria con Kuroe; se requiere `>= 25%` para abrir Laboratorio. |
| `tentacion_mirei` | Entero | `0%` a `100%` | `0` | Nivel de provocación/lujuria con Mirei; se requiere `>= 25%` para abrir Azotea. |
| `tentacion_reina` | Entero | `0%` a `100%` | `0` | Nivel de provocación/lujuria con Reina; se requiere `>= 25%` para abrir Festival. |
| `consecuencia_culpa_asumida` | Bool | True/False | `False` | Juramento de honor en el prólogo; reconocido en diálogos de clímax. |
| `consecuencia_jugando_con_fuego` | Bool | True/False | `False` | Actitud atrevida en el prólogo; recordado por las sub-personajes en el ajuste de cuentas. |
| `consecuencia_akane_confia` | Bool | True/False | `False` | Inspección del Consejo superada con éxito. |
| `consecuencia_yuki_invento_estable` | Bool | True/False | `False` | Proyector holográfico estabilizado sin quemar fusibles. |
| `consecuencia_hana_secreto_guardado` | Bool | True/False | `False` | Tobillo vendado y espectáculo rediseñado en pareja. |
| `consecuencia_alianza_chicas` | Bool | True/False | `False` | Activada si las 3 misiones triunfaron; otorga bono histórico al Festival. |

---

## 🔒 Coherencia de Desbloqueo y Ausencia de Rutas Imposibles

1. **Ruta hacia Akane:** Siempre accesible desde el inicio en el Consejo. Proporciona los puntos necesarios para abrir la Biblioteca con Kuroe.
2. **Ruta hacia Yuki:** Las Actas entregadas a Akane otorgan `+20% ♥` asegurando el umbral de `50% ♥` en Akane y `25% 🔥` en Kuroe, desbloqueando el Laboratorio sin bloqueos blandos (*softlocks*).
3. **Ruta hacia Hana:** La Bobina Experimental instalada con Yuki otorga `+20% ♥` asegurando el umbral de `55% ♥` en Yuki y `25% 🔥` en Mirei, abriendo la Azotea de forma limpia.
4. **Acceso al Festival:** La entrega del Pase Oficial de Reina a Hana otorga los puntos necesarios para superar el umbral del 60% de Festival y desbloquear la ceremonia final.
