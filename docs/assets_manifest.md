# 🎨 Manifiesto de Recursos y Assets del Proyecto

Inventario técnico de imágenes de fondo, sprites de personajes, elementos de interfaz gráfica (UI) y recursos multimedia definidos en el código de Ren'Py.

---

## 🏞️ 1. Imágenes de Fondo (Backgrounds - 1920x1080)

| Nombre de Imagen | Archivo Referenciado | Ubicación en el Juego | Estado en Repositorio |
| :--- | :--- | :--- | :--- |
| `bg classroom` | `images/bg_classroom.png` | Laboratorio de Ciencias y Almacén | ✅ Presente en `game/images/` |
| `bg council` | `images/bg_council.png` | Sala del Consejo Estudiantil | ✅ Presente en `game/images/` |
| `bg rooftop` | `images/bg_rooftop.png` | Azotea del Instituto Sakura | ✅ Presente en `game/images/` |
| `bg festival` | `images/bg_festival.png` | Patio en Noche de Festival | ✅ Presente en `game/images/` |
| `bg library` | `images/bg_library.png` | Biblioteca Oeste | ✅ Presente en `game/images/` |
| `bg courtyard` | `images/bg_courtyard.png` | Patio Central de los Cerezos | ✅ Presente en `game/images/` |

---

## 👤 2. Sprites de Personajes (Tachi-e - Canal Alfa Transparente)

### Heroínas Principales (18 Sprites)
* **Akane Tachibana (Tsundere):**
  * `akane normal` (`images/akane_normal.png`) ✅
  * `akane angry` (`images/akane_angry.png`) ✅
  * `akane blush` (`images/akane_blush.png`) ✅
  * `akane surprised` (`images/akane_surprised.png`) ✅
  * `akane pout` (`images/akane_pout.png`) ✅
  * `akane love` (`images/akane_love.png`) ✅
* **Yuki Shirogane (Kuudere):**
  * `yuki normal` (`images/yuki_normal.png`) ✅
  * `yuki smile` (`images/yuki_smile.png`) ✅
  * `yuki shy` (`images/yuki_shy.png`) ✅
  * `yuki surprised` (`images/yuki_surprised.png`) ✅
  * `yuki thinking` (`images/yuki_thinking.png`) ✅
  * `yuki love` (`images/yuki_love.png`) ✅
* **Hana Sakuragi (Genki):**
  * `hana normal` (`images/hana_normal.png`) ✅
  * `hana happy` (`images/hana_happy.png`) ✅
  * `hana sad` (`images/hana_sad.png`) ✅
  * `hana wink` (`images/hana_wink.png`) ✅
  * `hana shy` (`images/hana_shy.png`) ✅
  * `hana love` (`images/hana_love.png`) ✅

### Sub-Personajes Darkness (18 Sprites)
* **Kuroe Sakamoto (Rebelde):** `kuroe normal`, `seductive`, `angry`, `teasing`, `blush`, `passion` ✅
* **Mirei Kanzaki (Sempai Ciencias):** `mirei normal`, `seductive`, `angry`, `teasing`, `blush`, `passion` ✅
* **Reina Kurokawa (Capitana Atletismo):** `reina normal`, `seductive`, `angry`, `teasing`, `blush`, `passion` ✅

---

## 🖼️ 3. Elementos de Interfaz de Usuario (UI / Screens Estilo To Love-Ru)

Ubicados en `game/images/ui/`:
* `hud_bar_tlr.png`: Barra superior permanente del HUD.
* `pill_stat_tlr.png`: Cápsulas de estadísticas (★ Reputación, ⚡ Ingenio, ✨ Carisma, 🏮 Festival).
* `modal_box_tlr.png`: Marco *9-slice* ornamental de ventanas modales.
* `btn_pink_idle.png` / `btn_pink_hover.png`: Botón de estado de heroínas.
* `btn_purple_idle.png` / `btn_purple_hover.png`: Botón de sub-personajes Darkness.
* `btn_cyan_idle.png` / `btn_cyan_hover.png`: Botón de registro de ramas de historia.
* `btn_gold_idle.png` / `btn_gold_hover.png`: Botón de progreso total (0% - 100%).
* `bar_heart_full.png` / `bar_heart_empty.png`: Barras de afinidad romántica.
* `bar_lust_full.png` / `bar_lust_empty.png`: Barras de tentación Darkness.
* Iconos de reacciones flotantes: `icon_reac_hearts.png`, `icon_reac_shock.png`, `icon_reac_lust.png`, `icon_reac_sparkle.png`, `icon_reac_anger.png`, etc.
* `sakura_petal1.png` / `sakura_petal2.png`: Partículas de pétalos de cerezo para el efecto de atmósfera anime flotante (`sakura_petals`).

### Interfaz del Sistema Principal (Modern Glassmorphism GUI Completo)
Ubicados en `game/gui/`:
* `textbox.png`: Caja de texto moderna flotante (1920x280) con degradado nocturno, bordes redondeados y línea superior de neón.
* `namebox.png`: Cápsula de nombre flotante (450x58) con relieve de joya y bordes dorados/rosas.
* `button/choice_idle_background.png` & `choice_hover_background.png`: Botones de elección interactivos (1185x56) con iluminación dorada al pasar el ratón.
* `button/navigation_idle_background.png`, `hover`, `selected`: Cápsulas de navegación lateral (340x50) con borde neón cian/rosa y relieve dorado.
* `button/page_idle_background.png`, `hover`, `selected`: Botones de paginación de guardado (54x42) con estados iluminados activos.
* `button/delete_idle_background.png`, `hover`: Botón circular con aspa de eliminación rápida de partidas guardadas (34x34).
* `button/slot_idle_background.png` & `slot_hover_background.png`: Tarjetas para ranuras de guardado y carga (414x309) con corchetes dorados angulares.
* `frame.png`: Ventana modal oscura moderna (900x375) con doble borde de neón y efecto glassmorphism.
* `game_menu.png`: Fondo para menús de guardado, carga y configuración (1920x1080) con viñeta y resplandores ambientales.
* `history_card.png`: Tarjetas de diálogo individuales para el historial de mensajes (1200x120) con acento dorado.
* `card_pref.png`: Bloques modulares de cristal para las opciones de pantalla y sonido (480x380).
* `keycap.png`: Teclas físicas iluminadas para la guía visual de controles de teclado y ratón (120x44).
* `bar/left.png` & `bar/right.png`: Barras de nivel y progreso en degradado neón (64x28).
* `slider/horizontal_*.png`: Deslizadores con pista llena iluminada (`horizontal_idle_left.png`), pista vacía de cristal (`horizontal_idle_right.png`) y perilla circular de joya brillante (`horizontal_idle_thumb.png`).
* `scrollbar/horizontal_*.png` y `vertical_*.png`: Barras de desplazamiento estilizadas con guías de cristal ahumado y pulgares con borde rosa/oro.
* `notify.png`: Barra de notificaciones emergente estilizada (1383x64).
* `gui/phone/`: Sincronización completa de toda la suite de textboxes, sliders táctiles, barras y botones para dispositivos móviles y web.

---


## 🎵 4. Recursos de Audio y Música (BGM y SFX)

Ubicados en `game/audio/`:

| Archivo | Tipo | Canal | Uso en el Juego | Estado |
| :--- | :--- | :--- | :--- | :--- |
| `bgm_campus.wav` | Música (Loop 16s) | `music` | Tema diurno del campus y música del menú principal | ✅ Generado y configurado |
| `bgm_festival.wav` | Música (Loop 16s) | `music` | Tema festivo nocturno del clímax del festival | ✅ Generado y configurado |
| `sfx_click.wav` | Efecto (50ms) | `sound` | Clic interactivo en todos los botones y menús | ✅ Generado y configurado |
| `sfx_chime.wav` | Efecto (1.6s) | `sound` | Notificación de puntos, afinidad y objetos obtenidos | ✅ Generado y configurado |
| `sfx_heartbeat.wav` | Efecto (0.9s) | `sound` | Latido romántico / Doki-Doki en momentos de intimidad y seducción | ✅ Generado y configurado |
| `sfx_alert.wav` | Efecto (0.75s) | `sound` | Alarma de Trouble Rush (QTEs) y sobresaltos cómicos | ✅ Generado y configurado |
| `sfx_blush.wav` | Efecto (0.45s) | `sound` | Glissando tierno para sonrojos y timidez de las chicas | ✅ Generado y configurado |
| `sfx_success.wav` | Efecto (1.8s) | `sound` | Fanfarria de victoria en los Finales Principales y Harem | ✅ Generado y configurado |
| `sfx_swoosh.wav` | Efecto (0.28s) | `sound` | Transiciones rápidas y deslizamientos de escena | ✅ Generado y configurado |
| `sfx_bell.wav` | Efecto (2.4s) | `sound` | Campana escolar de apertura matutina y cambios de hora | ✅ Generado y configurado |
| `sfx_sparkle.wav` | Efecto (1.2s) | `sound` | Destello romántico ascendente para miradas tiernas y sonrisas | ✅ Generado y configurado |
| `sfx_applause.wav` | Efecto (2.5s) | `sound` | Aplausos y ovación de la multitud en el Festival y Finales Verdaderos | ✅ Generado y configurado |
| `sfx_paper.wav` | Efecto (0.5s) | `sound` | Crujido de papeles, permisos del Consejo e informes científicos | ✅ Generado y configurado |


