@echo off
echo ===================================================
echo 🤖 INICIANDO MONITOREO AUTOMÁTICO DE PRECIOS...
echo ===================================================

rem El truco de privacidad: %~dp0 es la carpeta actual
cd /d "%~dp0"

py -m pip install requests beautifulsoup4 pandas --quiet
py run_market_pipeline.py

echo ===================================================
echo 📊 PIPELINE FINALIZADO CON ÉXITO.
echo ===================================================
pause