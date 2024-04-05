
## crear entorno virtual
python -m venv wp_env

## iniciar entorno virtual
wp_env\Scripts\activate

## cerrar entorno virtual
deactivate

## crear repositorio en archivo .txt
python -m pip freeze > requirements.txt

## instalar repositorios desde el .txt
python -m pip install -r requirements.txt