@echo off
set venv_dir=venv

if exist %venv_dir% (
    echo Entorno virtual ya existe. Activándolo...
) else (
    echo Creando entorno virtual...
    python -m venv %venv_dir%
)

echo Activando entorno virtual...
call %venv_dir%\Scripts\activate

dir
pause

echo Instalando dependencias...

pip install -r requirements.txt

echo Entorno virtual activado. ¡Listo para usar!
cmd
