@echo off
title Servidor Web Local - Cronicas del Instituto Sakura
echo ===============================================================
echo   Iniciando Servidor Web Local en http://127.0.0.1:8042
echo   Abriendo el navegador automaticamente...
echo   (Cierra esta ventana para detener el servidor)
echo ===============================================================
start "" "http://127.0.0.1:8042/index.html"
"D:\renpy\renpy-8.5.3-sdk\lib\py3-windows-x86_64\python.exe" -m http.server 8042 --bind 127.0.0.1 --directory "%~dp0web-build"
