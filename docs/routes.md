# 🗺️ Mapa Completo de Rutas, Ramas y Finales

Este documento desglosa todas las trayectorias posibles desde el inicio del juego hasta los 8 finales canónicos.

---

## 🧭 Diagrama General de Ramificaciones

```
                      [INICIO: PRÓLOGO]
                              │
          ┌───────────────────┴───────────────────┐
   [Promesa de Honor]                      [Jugando con Fuego]
(+10 Rep, +5% con todas)                 (+10 Carisma, +10% Lujuria)
          │                                       │
          └───────────────────┬───────────────────┘
                              ▼
                      [HUB: CAMPUS LIBRE]
                              │
            ┌─────────────────┼─────────────────┐
            ▼                 ▼                 ▼
     [Arco 1: Akane]   [Arco 2: Yuki]    [Arco 3: Hana]
       (Consejo)        (Laboratorio)       (Azotea)
            │                 │                 │
            ▼                 ▼                 ▼
     [Sub: Kuroe]      [Sub: Mirei]      [Sub: Reina]
     (Biblioteca)     (Almacén Químico)   (Vestuarios)
            │                 │                 │
            └─────────────────┼─────────────────┘
                              ▼
               [¿QUEDASTE ENREDADO EN SUB-RUTAS?]
                              │
               ┌──────────────┴──────────────┐
              SÍ                             NO
               │                              │
     [Ajuste de Cuentas]                      │
    ┌──────────┴──────────┐                   │
    ▼                     ▼                   ▼
[Ceder a Lujuria]    [Romper Pacto] ────► [CLÍMAX DEL FESTIVAL]
        │                                     │
   3 FINALES                                  ├──────────────────────────────┐
 DE TENTACIÓN                                 │                              │
                                   [Festival Salvado]             [Catástrofe: Sanción]
                                              │                              │
                                    [ELECCIÓN DE CONFESIÓN]                  │
                               ┌──────────────┼──────────────┬───────────────┤
                               ▼              ▼              ▼               ▼
                           [Akane]         [Yuki]         [Hana]       [HAREM TOTAL]
                          (True/Norm)    (True/Norm)    (True/Norm)      (Secreto)
```

---

## 🌟 1. Las Rutas de las Heroínas Principales

### A. Ruta Akane Tachibana (Tsundere)
* **Detonante:** Ayudarla en el Consejo (`evento_akane`) y recuperar las Actas con Kuroe en la Biblioteca.
* **Hitos de Ruta:**
  1. Superar la inspección del Subdirector mediante distracción o refugio bajo el escritorio.
  2. Entregarle las Actas Secretas en el Consejo (`+20% ♥`).
  3. *(Opcional)* Regalarle el Té Real de Durazno de la Cafetería (`+15% ♥`).
* **Condiciones de Final:**
  * **Final Verdadero («El Corazón Secreto de la Presidenta Tsundere»):** Afinidad Akane `>= 50%` + Romper cualquier pacto con Kuroe + Festival salvado.
  * **Final Normal («Aliados del Consejo Estudiantil»):** Afinidad Akane `< 50%` + Libre de Kuroe.

### B. Ruta Yuki Shirogane (Kuudere)
* **Detonante:** Desbloquear el Laboratorio Este y ayudarla con el Proyector Holográfico (`evento_yuki`).
* **Hitos de Ruta:**
  1. Estabilizar el reactor óptico en frecuencia Luz de Luna o dominar la sobrecarga.
  2. Conseguir la Bobina Experimental de Mirei e instalarla en el laboratorio.
  3. *(Opcional)* Regalarle el Libro de Astrofísica Poética de la Biblioteca (`+15% ♥`).
* **Condiciones de Final:**
  * **Final Verdadero («La Ecuación Perfecta del Primer Amor»):** Afinidad Yuki `>= 50%` + Romper cualquier pacto con Mirei + Festival salvado.
  * **Final Normal («Compañeros de Laboratorio»):** Afinidad Yuki `< 50%` + Libre de Mirei.

### C. Ruta Hana Sakuragi (Genki)
* **Detonante:** Subir a la Azotea (`evento_hana`) y descubrir su lesión de tobillo.
* **Hitos de Ruta:**
  1. Vendar su tobillo y comprometerse como su pareja de coreografía o adaptar el show a acrobacia ligera.
  2. Negociar con Reina en los Vestuarios y entregar el Pase Oficial a Hana.
  3. *(Opcional)* Entregarle el Botiquín Deportivo Frío (`+15% ♥`).
* **Condiciones de Final:**
  * **Final Verdadero («Promesa Bajo la Lluvia de Sakura»):** Afinidad Hana `>= 50%` + Romper cualquier pacto con Reina + Festival salvado.
  * **Final Normal («Mejores Amigos para Siempre»):** Afinidad Hana `< 50%` + Libre de Reina.

---

## 👑 2. Final Secreto Legendario: Ruta Harem Principal
* **Título:** «El Héroe Indiscutible del Instituto Sakura»
* **Requisitos Estrictos:**
  1. Afinidad con Akane `>= 50% ♥`.
  2. Afinidad con Yuki `>= 50% ♥`.
  3. Afinidad con Hana `>= 50% ♥`.
  4. Presupuesto del Festival `>= 75% 🏮`.
  5. Haber cerrado todas las tentaciones secundarias (`ruptura_sub_kuroe`, `ruptura_sub_mirei`, `ruptura_sub_reina` = `True`).
  6. Haber cumplido las 3 misiones con éxito activando la `consecuencia_alianza_chicas`.

---

## 😈 3. Las Rutas Prohibidas de Tentación (Modo Darkness)
Si el jugador decide no terminar con las sub-personajes y sucumbe a su deseo en el ajuste de cuentas:

| Final | Sub-Personaje | Ubicación de Desenlace | Título del Final y Consecuencia |
| :--- | :--- | :--- | :--- |
| **Tentación 1** | Kuroe Sakamoto | Biblioteca Oeste | **«Prisionero de la Chica Mala»:** Abandonas la ceremonia oficial para pasar la noche encerrado con Kuroe entre las estanterías oscuras. |
| **Tentación 2** | Mirei Kanzaki | Laboratorio Este | **«Experimento Nocturno de Lujuria»:** Te encierras con la sempai Mirei en el almacén químico realizando estudios biológicos privados toda la noche. |
| **Tentación 3** | Reina Kurokawa | Vestuarios Sur | **«Entrenamiento Privado sin Límites»:** Reina te arrastra a los vestuarios vacíos para una sesión de resistencia corporal hasta el amanecer. |
