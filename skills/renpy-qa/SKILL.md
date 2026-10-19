---
name: renpy-qa
description: Prueba y depura proyectos Ren'Py, detectando errores de sintaxis, flujo y recursos.
---

# Ren'Py QA

Verifica el proyecto de forma reproducible. Inspecciona el código y los recursos antes de editar.

## Lista de comprobación
- Sintaxis e indentación de bloques Ren'Py.
- Labels duplicados o destinos inexistentes.
- Personajes, imágenes, sonidos y música sin definir.
- Variables no inicializadas o condiciones de final imposibles.
- Menús sin salida y ciclos accidentales.
- Diferencias entre guion aprobado y escena implementada.
- Rutas y finales alcanzables.
- Textos provisionales, TODOs y recursos faltantes.

## Método
1. Identifica la ubicación del proyecto y la versión de Ren'Py.
2. Ejecuta las comprobaciones disponibles sin borrar partidas ni datos.
3. Si se puede usar el launcher o una herramienta de lint, ejecútala y conserva el resultado.
4. Corrige primero errores que impiden arrancar; después errores de flujo; al final, pulido.
5. No declares una prueba superada sin evidencia de ejecución.
6. No borres ni reemplaces recursos o archivos en lote sin autorización.

## Informe
Resume comando ejecutado, resultado, errores con archivo/línea y pasos para reproducir. Separa problemas confirmados de sospechas.
