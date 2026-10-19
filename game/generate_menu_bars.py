# -*- coding: utf-8 -*-
"""
Generador de Assets GUI Modernos (Barras, Sliders, Scrollbars, Navegación, Slots y Preferencias)
Estilo: Anime Glassmorphism Rom-Com / Cyber-Sakura
"""

import os
import math
from PIL import Image, ImageDraw, ImageFilter

def make_dirs():
    dirs = [
        "game/gui",
        "game/gui/bar",
        "game/gui/button",
        "game/gui/overlay",
        "game/gui/scrollbar",
        "game/gui/slider",
        "game/gui/phone",
        "game/gui/phone/bar",
        "game/gui/phone/button",
        "game/gui/phone/overlay",
        "game/gui/phone/scrollbar",
        "game/gui/phone/slider",
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)

# -------------------------------------------------------------
# 1. SLIDERS HORIZONTALES Y VERTICALES
# -------------------------------------------------------------
def create_sliders():
    print("Generando Sliders Modernos...")
    w_h, h_h = 64, 28
    
    # Horizontal Idle Left (Pista llena)
    # Gradiente vibrante Cyan -> Pink con brillo superior
    img = Image.new("RGBA", (w_h, h_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # Borde redondeado suave
    draw.rounded_rectangle([1, 2, w_h - 2, h_h - 3], radius=11, fill=(240, 60, 120, 230), outline=(255, 130, 180, 255), width=2)
    # Resplandor superior
    draw.rounded_rectangle([4, 4, w_h - 5, 11], radius=4, fill=(255, 255, 255, 100))
    img.save("game/gui/slider/horizontal_idle_left.png")

    # Horizontal Hover Left (Resplandor dorado / cian intenso)
    img = Image.new("RGBA", (w_h, h_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([1, 2, w_h - 2, h_h - 3], radius=11, fill=(255, 90, 150, 250), outline=(93, 253, 203, 255), width=2)
    draw.rounded_rectangle([4, 4, w_h - 5, 11], radius=4, fill=(255, 255, 255, 160))
    img.save("game/gui/slider/horizontal_hover_left.png")

    # Horizontal Idle Right (Pista vacía de cristal oscuro)
    img = Image.new("RGBA", (w_h, h_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([1, 2, w_h - 2, h_h - 3], radius=11, fill=(20, 4, 30, 210), outline=(100, 30, 80, 180), width=2)
    # Ranura central tenue
    draw.rounded_rectangle([4, 11, w_h - 5, 15], radius=2, fill=(10, 2, 16, 230))
    img.save("game/gui/slider/horizontal_idle_right.png")

    # Horizontal Hover Right
    img = Image.new("RGBA", (w_h, h_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([1, 2, w_h - 2, h_h - 3], radius=11, fill=(26, 6, 38, 230), outline=(255, 77, 109, 140), width=2)
    draw.rounded_rectangle([4, 11, w_h - 5, 15], radius=2, fill=(14, 3, 22, 240))
    img.save("game/gui/slider/horizontal_hover_right.png")

    # Compatibilidad base_bar
    img.save("game/gui/slider/horizontal_idle_bar.png")
    img.save("game/gui/slider/horizontal_hover_bar.png")

    # Horizontal Thumbs (Joya circular con aureola luminosa)
    thumb_sz = 34
    # Idle Thumb
    img = Image.new("RGBA", (thumb_sz, thumb_sz), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # Aro exterior resplandor dorado
    draw.ellipse([1, 1, thumb_sz - 2, thumb_sz - 2], fill=(255, 209, 59, 255), outline=(255, 245, 180, 255), width=2)
    # Núcleo joya violeta profundo
    draw.ellipse([5, 5, thumb_sz - 6, thumb_sz - 6], fill=(42, 6, 56, 255), outline=(255, 77, 109, 200), width=1)
    # Estrella / Gema cian central
    draw.ellipse([10, 10, thumb_sz - 11, thumb_sz - 11], fill=(93, 253, 203, 255))
    # Brillo especular
    draw.ellipse([9, 7, 16, 14], fill=(255, 255, 255, 240))
    img.save("game/gui/slider/horizontal_idle_thumb.png")

    # Hover Thumb (Aura de luz expandida y resplandor blanco-dorado)
    img = Image.new("RGBA", (thumb_sz, thumb_sz), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.ellipse([0, 0, thumb_sz - 1, thumb_sz - 1], fill=(255, 235, 130, 255), outline=(255, 255, 255, 255), width=2)
    draw.ellipse([4, 4, thumb_sz - 5, thumb_sz - 5], fill=(255, 77, 109, 255), outline=(255, 209, 59, 240), width=1)
    draw.ellipse([9, 9, thumb_sz - 10, thumb_sz - 10], fill=(255, 255, 255, 255))
    draw.ellipse([11, 8, 17, 14], fill=(255, 255, 255, 255))
    img.save("game/gui/slider/horizontal_hover_thumb.png")

    # Vertical Sliders
    w_v, h_v = 28, 64
    # Vertical Idle Top (Pista llena superior)
    img = Image.new("RGBA", (w_v, h_v), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([2, 1, w_v - 3, h_v - 2], radius=11, fill=(240, 60, 120, 230), outline=(255, 130, 180, 255), width=2)
    draw.rounded_rectangle([4, 4, 11, h_v - 5], radius=4, fill=(255, 255, 255, 100))
    img.save("game/gui/slider/vertical_idle_top.png")

    # Vertical Hover Top
    img = Image.new("RGBA", (w_v, h_v), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([2, 1, w_v - 3, h_v - 2], radius=11, fill=(255, 90, 150, 250), outline=(93, 253, 203, 255), width=2)
    draw.rounded_rectangle([4, 4, 11, h_v - 5], radius=4, fill=(255, 255, 255, 160))
    img.save("game/gui/slider/vertical_hover_top.png")

    # Vertical Idle Bottom (Pista vacía)
    img = Image.new("RGBA", (w_v, h_v), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([2, 1, w_v - 3, h_v - 2], radius=11, fill=(20, 4, 30, 210), outline=(100, 30, 80, 180), width=2)
    draw.rounded_rectangle([11, 4, 15, h_v - 5], radius=2, fill=(10, 2, 16, 230))
    img.save("game/gui/slider/vertical_idle_bottom.png")

    # Vertical Hover Bottom
    img = Image.new("RGBA", (w_v, h_v), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([2, 1, w_v - 3, h_v - 2], radius=11, fill=(26, 6, 38, 230), outline=(255, 77, 109, 140), width=2)
    draw.rounded_rectangle([11, 4, 15, h_v - 5], radius=2, fill=(14, 3, 22, 240))
    img.save("game/gui/slider/vertical_hover_bottom.png")

    img.save("game/gui/slider/vertical_idle_bar.png")
    img.save("game/gui/slider/vertical_hover_bar.png")

    # Vertical Thumbs
    img_thumb_v_idle = Image.open("game/gui/slider/horizontal_idle_thumb.png")
    img_thumb_v_idle.save("game/gui/slider/vertical_idle_thumb.png")
    img_thumb_v_hover = Image.open("game/gui/slider/horizontal_hover_thumb.png")
    img_thumb_v_hover.save("game/gui/slider/vertical_hover_thumb.png")

# -------------------------------------------------------------
# 2. BARRAS GENERALES (gui/bar/)
# -------------------------------------------------------------
def create_bars():
    print("Generando Barras de Progreso GUI...")
    w, h = 64, 28
    
    # Left (Lleno)
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([1, 2, w - 2, h - 3], radius=10, fill=(93, 253, 203, 240), outline=(255, 255, 255, 220), width=2)
    draw.rounded_rectangle([4, 4, w - 5, 10], radius=3, fill=(255, 255, 255, 120))
    img.save("game/gui/bar/left.png")

    # Right (Vacío)
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([1, 2, w - 2, h - 3], radius=10, fill=(22, 5, 32, 210), outline=(80, 25, 70, 160), width=2)
    draw.rounded_rectangle([4, 11, w - 5, 15], radius=2, fill=(12, 3, 18, 220))
    img.save("game/gui/bar/right.png")

    # Top (Vertical Lleno)
    img = Image.new("RGBA", (h, w), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([2, 1, h - 3, w - 2], radius=10, fill=(93, 253, 203, 240), outline=(255, 255, 255, 220), width=2)
    draw.rounded_rectangle([4, 4, 10, w - 5], radius=3, fill=(255, 255, 255, 120))
    img.save("game/gui/bar/top.png")

    # Bottom (Vertical Vacío)
    img = Image.new("RGBA", (h, w), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([2, 1, h - 3, w - 2], radius=10, fill=(22, 5, 32, 210), outline=(80, 25, 70, 160), width=2)
    draw.rounded_rectangle([11, 4, 15, w - 5], radius=2, fill=(12, 3, 18, 220))
    img.save("game/gui/bar/bottom.png")

# -------------------------------------------------------------
# 3. BARRAS DE DESPLAZAMIENTO (gui/scrollbar/)
# -------------------------------------------------------------
def create_scrollbars():
    print("Generando Barras de Desplazamiento...")
    # Horizontal Bar & Thumb
    w_bar, h_bar = 1050, 16
    img = Image.new("RGBA", (w_bar, h_bar), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([0, 2, w_bar - 1, h_bar - 3], radius=6, fill=(16, 4, 25, 180), outline=(70, 20, 60, 120), width=1)
    img.save("game/gui/scrollbar/horizontal_idle_bar.png")
    
    img_h_bar_hov = Image.new("RGBA", (w_bar, h_bar), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img_h_bar_hov)
    draw.rounded_rectangle([0, 2, w_bar - 1, h_bar - 3], radius=6, fill=(24, 6, 36, 210), outline=(255, 77, 109, 100), width=1)
    img_h_bar_hov.save("game/gui/scrollbar/horizontal_hover_bar.png")

    # Horizontal Thumbs
    w_th, h_th = 120, 16
    img = Image.new("RGBA", (w_th, h_th), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([1, 1, w_th - 2, h_th - 2], radius=7, fill=(255, 77, 109, 210), outline=(255, 180, 200, 240), width=1)
    draw.rounded_rectangle([6, 3, w_th - 7, 7], radius=2, fill=(255, 255, 255, 110))
    img.save("game/gui/scrollbar/horizontal_idle_thumb.png")

    img_th_hov = Image.new("RGBA", (w_th, h_th), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img_th_hov)
    draw.rounded_rectangle([0, 0, w_th - 1, h_th - 1], radius=7, fill=(255, 209, 59, 240), outline=(255, 255, 255, 255), width=2)
    draw.rounded_rectangle([6, 3, w_th - 7, 7], radius=2, fill=(255, 255, 255, 180))
    img_th_hov.save("game/gui/scrollbar/horizontal_hover_thumb.png")

    # Vertical Bar & Thumb
    w_vbar, h_vbar = 16, 1050
    img = Image.new("RGBA", (w_vbar, h_vbar), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([2, 0, w_vbar - 3, h_vbar - 1], radius=6, fill=(16, 4, 25, 180), outline=(70, 20, 60, 120), width=1)
    img.save("game/gui/scrollbar/vertical_idle_bar.png")

    img_v_bar_hov = Image.new("RGBA", (w_vbar, h_vbar), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img_v_bar_hov)
    draw.rounded_rectangle([2, 0, w_vbar - 3, h_vbar - 1], radius=6, fill=(24, 6, 36, 210), outline=(255, 77, 109, 100), width=1)
    img_v_bar_hov.save("game/gui/scrollbar/vertical_hover_bar.png")

    # Vertical Thumbs
    w_vth, h_vth = 16, 120
    img = Image.new("RGBA", (w_vth, h_vth), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([1, 1, w_vth - 2, h_vth - 2], radius=7, fill=(255, 77, 109, 210), outline=(255, 180, 200, 240), width=1)
    draw.rounded_rectangle([3, 6, 7, h_vth - 7], radius=2, fill=(255, 255, 255, 110))
    img.save("game/gui/scrollbar/vertical_idle_thumb.png")

    img_v_th_hov = Image.new("RGBA", (w_vth, h_vth), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img_v_th_hov)
    draw.rounded_rectangle([0, 0, w_vth - 1, h_vth - 1], radius=7, fill=(255, 209, 59, 240), outline=(255, 255, 255, 255), width=2)
    draw.rounded_rectangle([3, 6, 7, h_vth - 7], radius=2, fill=(255, 255, 255, 180))
    img_v_th_hov.save("game/gui/scrollbar/vertical_hover_thumb.png")

# -------------------------------------------------------------
# 4. BOTONES DE NAVEGACIÓN Y PÁGINA (gui/button/)
# -------------------------------------------------------------
def create_navigation_and_page_buttons():
    print("Generando Botones de Navegación y Páginas...")
    # Navigation Buttons (340x50)
    w_nav, h_nav = 340, 50
    
    # Idle: Cápsula de cristal ahumado violeta con acento magenta izquierdo
    img = Image.new("RGBA", (w_nav, h_nav), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([0, 0, w_nav - 1, h_nav - 1], radius=14, fill=(24, 5, 36, 195), outline=(255, 77, 109, 65), width=2)
    # Barra de acento izquierda
    draw.rounded_rectangle([6, 8, 11, h_nav - 9], radius=3, fill=(255, 77, 109, 230))
    img.save("game/gui/button/navigation_idle_background.png")

    # Hover: Cápsula iluminada con resplandor cian y acento dorado
    img = Image.new("RGBA", (w_nav, h_nav), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([0, 0, w_nav - 1, h_nav - 1], radius=14, fill=(45, 9, 65, 225), outline=(93, 253, 203, 230), width=2)
    draw.rounded_rectangle([5, 6, 12, h_nav - 7], radius=3, fill=(255, 209, 59, 255))
    draw.rounded_rectangle([15, 3, w_nav - 15, 12], radius=4, fill=(255, 255, 255, 35))
    img.save("game/gui/button/navigation_hover_background.png")

    # Selected: Marco radiante dorado
    img = Image.new("RGBA", (w_nav, h_nav), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([0, 0, w_nav - 1, h_nav - 1], radius=14, fill=(58, 12, 54, 235), outline=(255, 209, 59, 255), width=2)
    draw.rounded_rectangle([5, 6, 12, h_nav - 7], radius=3, fill=(255, 209, 59, 255))
    img.save("game/gui/button/navigation_selected_background.png")

    # Page Buttons (52x42)
    w_p, h_p = 54, 42
    # Idle
    img = Image.new("RGBA", (w_p, h_p), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([1, 1, w_p - 2, h_p - 2], radius=10, fill=(22, 5, 34, 200), outline=(255, 77, 109, 70), width=2)
    img.save("game/gui/button/page_idle_background.png")

    # Hover
    img = Image.new("RGBA", (w_p, h_p), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([0, 0, w_p - 1, h_p - 1], radius=10, fill=(44, 9, 64, 230), outline=(93, 253, 203, 240), width=2)
    draw.rounded_rectangle([4, 3, w_p - 5, 11], radius=3, fill=(255, 255, 255, 50))
    img.save("game/gui/button/page_hover_background.png")

    # Selected
    img = Image.new("RGBA", (w_p, h_p), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([0, 0, w_p - 1, h_p - 1], radius=10, fill=(60, 15, 50, 240), outline=(255, 209, 59, 255), width=2)
    draw.rounded_rectangle([4, 3, w_p - 5, 11], radius=3, fill=(255, 255, 255, 70))
    img.save("game/gui/button/page_selected_background.png")

    # Botón Eliminar Ranura (Delete Save Button 34x34)
    sz_d = 34
    img = Image.new("RGBA", (sz_d, sz_d), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.ellipse([1, 1, sz_d - 2, sz_d - 2], fill=(40, 8, 20, 220), outline=(255, 77, 109, 180), width=2)
    draw.line([10, 10, sz_d - 11, sz_d - 11], fill=(255, 150, 170, 240), width=2)
    draw.line([sz_d - 11, 10, 10, sz_d - 11], fill=(255, 150, 170, 240), width=2)
    img.save("game/gui/button/delete_idle_background.png")

    img_d_hov = Image.new("RGBA", (sz_d, sz_d), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img_d_hov)
    draw.ellipse([0, 0, sz_d - 1, sz_d - 1], fill=(180, 20, 50, 250), outline=(255, 255, 255, 255), width=2)
    draw.line([9, 9, sz_d - 10, sz_d - 10], fill=(255, 255, 255, 255), width=3)
    draw.line([sz_d - 10, 9, 9, sz_d - 10], fill=(255, 255, 255, 255), width=3)
    img_d_hov.save("game/gui/button/delete_hover_background.png")

# -------------------------------------------------------------
# 5. RANURAS DE GUARDADO (gui/button/slot_*)
# -------------------------------------------------------------
def create_slots():
    print("Generando Ranuras de Guardado Modernas...")
    w_s, h_s = 414, 309
    
    # Idle Slot Frame: Cristal ahumado con esquinas redondeadas y borde sutil
    img = Image.new("RGBA", (w_s, h_s), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([0, 0, w_s - 1, h_s - 1], radius=18, fill=(18, 4, 28, 220), outline=(255, 77, 109, 65), width=2)
    # Cabecera superior interna
    draw.rounded_rectangle([4, 4, w_s - 5, 38], radius=12, fill=(28, 6, 42, 230))
    # Marco interior para la miniatura
    draw.rounded_rectangle([13, 44, w_s - 14, 262], radius=10, outline=(70, 20, 60, 120), width=1)
    img.save("game/gui/button/slot_idle_background.png")

    # Hover Slot Frame: Resplandor cian/oro con ribetes neón
    img = Image.new("RGBA", (w_s, h_s), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([0, 0, w_s - 1, h_s - 1], radius=18, fill=(36, 8, 54, 240), outline=(93, 253, 203, 240), width=3)
    draw.rounded_rectangle([4, 4, w_s - 5, 38], radius=12, fill=(54, 12, 76, 240))
    draw.rounded_rectangle([13, 44, w_s - 14, 262], radius=10, outline=(255, 209, 59, 220), width=2)
    # Corchetes dorados en las 4 esquinas
    bracket_len = 16
    draw.line([8, 8, 8 + bracket_len, 8], fill=(255, 209, 59, 255), width=2)
    draw.line([8, 8, 8, 8 + bracket_len], fill=(255, 209, 59, 255), width=2)
    draw.line([w_s - 9, 8, w_s - 9 - bracket_len, 8], fill=(255, 209, 59, 255), width=2)
    draw.line([w_s - 9, 8, w_s - 9, 8 + bracket_len], fill=(255, 209, 59, 255), width=2)
    draw.line([8, h_s - 9, 8 + bracket_len, h_s - 9], fill=(255, 209, 59, 255), width=2)
    draw.line([8, h_s - 9, 8, h_s - 9 - bracket_len], fill=(255, 209, 59, 255), width=2)
    draw.line([w_s - 9, h_s - 9, w_s - 9 - bracket_len, h_s - 9], fill=(255, 209, 59, 255), width=2)
    draw.line([w_s - 9, h_s - 9, w_s - 9, h_s - 9 - bracket_len], fill=(255, 209, 59, 255), width=2)
    img.save("game/gui/button/slot_hover_background.png")

# -------------------------------------------------------------
# 6. TARJETAS DE HISTORIAL, PREFERENCIAS Y TECLAS (KEYCAPS)
# -------------------------------------------------------------
def create_cards_and_keycaps():
    print("Generando Tarjetas y Keycaps...")
    # Tarjeta de Historial (1200x120)
    w_h, h_h = 1200, 120
    img = Image.new("RGBA", (w_h, h_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([0, 0, w_h - 1, h_h - 1], radius=16, fill=(18, 4, 28, 205), outline=(255, 77, 109, 50), width=1)
    # Acento lateral izquierdo
    draw.rounded_rectangle([4, 6, 9, h_h - 7], radius=3, fill=(255, 209, 59, 220))
    img.save("game/gui/history_card.png")

    # Tarjeta para Bloques de Preferencias (480x380)
    w_p, h_p = 480, 380
    img = Image.new("RGBA", (w_p, h_p), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([0, 0, w_p - 1, h_p - 1], radius=20, fill=(20, 4, 32, 215), outline=(255, 77, 109, 70), width=2)
    draw.rounded_rectangle([4, 4, w_p - 5, 46], radius=14, fill=(35, 7, 52, 230))
    img.save("game/gui/card_pref.png")

    # Tecla Física Iluminada (Keycap 120x44)
    w_k, h_k = 120, 44
    img = Image.new("RGBA", (w_k, h_k), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # Cuerpo de tecla
    draw.rounded_rectangle([1, 1, w_k - 2, h_k - 2], radius=10, fill=(30, 8, 46, 240), outline=(93, 253, 203, 200), width=2)
    # Bisel superior
    draw.rounded_rectangle([4, 3, w_k - 5, 12], radius=4, fill=(255, 255, 255, 40))
    img.save("game/gui/keycap.png")

    # NVL Background (1920x1080)
    img = Image.new("RGBA", (1920, 1080), (12, 2, 18, 235))
    draw = ImageDraw.Draw(img)
    # Gradiente de resplandor superior e inferior
    draw.rectangle([0, 0, 1920, 8], fill=(255, 77, 109, 180))
    draw.rectangle([0, 1072, 1920, 1080], fill=(93, 253, 203, 180))
    # Panel de lectura central
    draw.rounded_rectangle([200, 60, 1720, 1020], radius=24, fill=(18, 3, 28, 190), outline=(255, 77, 109, 60), width=2)
    img.save("game/gui/nvl.png")

# -------------------------------------------------------------
# 7. SINCRONIZAR VERSIÓN MÓVIL / TELÉFONO (gui/phone/)
# -------------------------------------------------------------
def sync_phone_assets():
    print("Sincronizando Assets Móviles / Phone...")
    # Copiar o generar versiones táctiles ampliadas
    # Bar Phone
    img_b_l = Image.open("game/gui/bar/left.png")
    img_b_l.save("game/gui/phone/bar/left.png")
    img_b_r = Image.open("game/gui/bar/right.png")
    img_b_r.save("game/gui/phone/bar/right.png")
    img_b_t = Image.open("game/gui/bar/top.png")
    img_b_t.save("game/gui/phone/bar/top.png")
    img_b_b = Image.open("game/gui/bar/bottom.png")
    img_b_b.save("game/gui/phone/bar/bottom.png")

    # Sliders Phone
    for f in [
        "horizontal_idle_left.png", "horizontal_idle_right.png", "horizontal_idle_thumb.png",
        "horizontal_hover_left.png", "horizontal_hover_right.png", "horizontal_hover_thumb.png",
        "horizontal_idle_bar.png", "horizontal_hover_bar.png",
        "vertical_idle_top.png", "vertical_idle_bottom.png", "vertical_idle_thumb.png",
        "vertical_hover_top.png", "vertical_hover_bottom.png", "vertical_hover_thumb.png",
        "vertical_idle_bar.png", "vertical_hover_bar.png"
    ]:
        im = Image.open(f"game/gui/slider/{f}")
        im.save(f"game/gui/phone/slider/{f}")

    # Scrollbars Phone
    for f in [
        "horizontal_idle_bar.png", "horizontal_hover_bar.png", "horizontal_idle_thumb.png", "horizontal_hover_thumb.png",
        "vertical_idle_bar.png", "vertical_hover_bar.png", "vertical_idle_thumb.png", "vertical_hover_thumb.png"
    ]:
        im = Image.open(f"game/gui/scrollbar/{f}")
        im.save(f"game/gui/phone/scrollbar/{f}")

    # Buttons Phone
    for f in [
        "check_foreground.png", "check_selected_foreground.png",
        "radio_foreground.png", "radio_selected_foreground.png",
        "choice_idle_background.png", "choice_hover_background.png",
        "idle_background.png", "hover_background.png",
        "slot_idle_background.png", "slot_hover_background.png"
    ]:
        if os.path.exists(f"game/gui/button/{f}"):
            im = Image.open(f"game/gui/button/{f}")
            im.save(f"game/gui/phone/button/{f}")

    # Overlays Phone
    for f in ["game_menu.png", "main_menu.png"]:
        if os.path.exists(f"game/gui/overlay/{f}"):
            im = Image.open(f"game/gui/overlay/{f}")
            im.save(f"game/gui/phone/overlay/{f}")

    # Textbox & NVL Phone
    im_tb = Image.open("game/gui/textbox.png")
    im_tb.save("game/gui/phone/textbox.png")
    im_nvl = Image.open("game/gui/nvl.png")
    im_nvl.save("game/gui/phone/nvl.png")

if __name__ == "__main__":
    make_dirs()
    create_sliders()
    create_bars()
    create_scrollbars()
    create_navigation_and_page_buttons()
    create_slots()
    create_cards_and_keycaps()
    sync_phone_assets()
    print("¡Todos los assets GUI de menú y barras han sido generados exitosamente!")
