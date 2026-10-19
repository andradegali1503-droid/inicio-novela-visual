---
name: gemini-vn-producer
description: Coordina Gemini como productor de una novela visual y delega escritura, código y QA en tareas pequeñas.
---

# Gemini VN Producer

Coordina el trabajo de una novela visual mediante entregas pequeñas, verificables y compatibles con el contexto disponible del modelo.

## Principios
- El modelo configurado en OpenClaw puede ser Gemini; esta skill no cambia por sí sola el modelo ni configura credenciales.
- Trata la biblia narrativa y los archivos del proyecto como fuente de verdad.
- Divide proyectos grandes en tareas acotadas: un capítulo, una ruta o un sistema cada vez.
- Antes de modificar archivos, inspecciona la estructura actual y el estado del repositorio si está disponible.
- Nunca inventes que una herramienta, modelo, test o comando se ejecutó.
- Solicita aprobación antes de operaciones destructivas, publicar, comprar servicios o exponer secretos.

## Pipeline
1. Arquitectura: actualiza biblia, personajes, rutas y cronología.
2. Guion: produce una escena con objetivo y consecuencias explícitas.
3. Implementación: traduce el guion a `.rpy` y enumera los assets necesarios.
4. Auditoría: comprueba continuidad y ramas.
5. QA: ejecuta pruebas disponibles y corrige errores confirmados.
6. Revisión humana: presenta cambios, riesgos y decisiones pendientes.

Al cerrar cada tarea, informa de archivos modificados, pruebas realizadas, resultado y siguiente paso recomendado. Mantén un changelog del canon y no combines cambios narrativos grandes con refactorizaciones técnicas en una sola modificación.
