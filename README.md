# Ejecucion del proyecto
## Configuracion del entorno
Instalar el venv y configurarlo en windows
```bash
# Crear el entorno
python -m venv .venv
# Activarlo si hace falta
.venv\Scripts\activate
# Instalar las depedencias segun el requirements
pip install -r requirements.txt
```
## Ejecutar test cases
```bash
pytest -s -v [direccionDelArchivo]
```

### Informacion importante para el captcha
** Aplicacion necesario para poder pasar el captcha, descarga directa [Tesseract](https://github.com/tesseract-ocr/tesseract/releases/download/5.5.0/tesseract-ocr-w64-setup-5.5.0.20241111.exe) **

### Informacion importante para el usuario, pin y tesseract

Crear un .env.test en la raiz del proyecto y crear las variables de entorno correspondientes al usuario, pin y la ubicacion de tesseract en el equipo.  
- TEST_USERNAME  
- TEST_PASSWORD  
- TEST_TESSERACT_PATH  

