import os
import subprocess
import webbrowser
import time

base_dir = os.path.dirname(os.path.abspath(__file__))
manage_path = os.path.join(base_dir, 'manage.py')

# Ejecutar el servidor en segundo plano sin mostrar la ventana de CMD
server_process = subprocess.Popen(['python', manage_path, 'runserver'], creationflags=subprocess.CREATE_NO_WINDOW)

time.sleep(5)
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
try:
    webbrowser.get(chrome_path).open('http://127.0.0.1:8000')
except webbrowser.Error:
    print("No se pudo localizar el navegador Chrome. Abriendo en el navegador predeterminado.")
    webbrowser.open('http://127.0.0.1:8000')



