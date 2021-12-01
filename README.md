<h1>scrap_and_analisis_linkedin_jobs</h1>
<h3>Español</h3>
<h1>Bot para descargar vacantes de linkedin y visualización de la frecuencia con la que es demandada cierta habilidad o conocimiento</h1>
<h2>OS: Windows 10 home Edition</h2>
<h2>Lenguaje: Python 3.8.2</h2>

<h2>SCRAPER: caller.py</h2>

Este es el programa encargado de crear un archivo de excel donde descargará hasta 500 vacantes publicadas con sus respectivo, nombre, compañía, url, descripción...
El código está configurado para que selenium actue en 2do plano, pero se puede cambiar a primer plano.
Una vez creado el venv en base a requirements.txt y clonado el repositorio se debe crear en esa misma carpeta un archivo "personal_info.json" que contendrá su nombre de usuario y contraseña de linkedin de la siguiente forma: {"name":"correo_de_linkedin@correo.com","password":"contraseña_cuenta_linkedin"}, este archivo no debe ser compartido por motivos de seguridad.

Una vez se ejecuta el archivo, se deberán llenar los siguientes inputs
*Trabajo: (por defecto python)
*Ubicación: (por defecto colombia)
*Remoto, presione Y/N: (Debe presionarse "Y" o "y" para que solo tome las vacantes remotas)
*Última semana, presione Y/N: (Debe presionarse "Y" o "y" para que solo tome las vacantes de la última semana)

NOTA:
Si el scraper detecta las 500 vacantes máximo que puede detectar, puede tomar hasta dos horas para descargar toda la información.
Si el scraper no puede ingresar a la cuenta de linkedin, es probable que se hayan realizado demasiadas "requests" de ingreso, y pida que se ingrese manualmente al pasar un test de seguridad.

<h2>ANALIZADOR: word_counter_aboslute.py</h2>

Depende del archivo "inputs/description_regex_tokens.json", en donde se encuentran las REGEX de las palabras clave a buscar. Por ejemplo, si queremos ver si scikitlearn se encuentra explicito en el texto de las ofertas, este archivo usa la expresión "scikitlearn": "^[scikit|SCIKIT]{6}[l|L]?"
Así que si se buscan empleos por fuera de las habilidades anotadas en este archivo, deben ser adicionadas.

Una vez se ejecuta el archivo: 
*se abre una ventana de tkinter solicitando el archivo creado por caller.py a analizar.
*Contar por idioma?, ingrese es/en/none: Se ingresa "es" para tomar solo las vacantes en español, "en" para tomar solo las vacantes en inglés o "none" para tomar todas

El resultado son:
*Un archivo de excel con la distribución de frecuencias de cada palabra clave por texto
*Un gráfico con la frecuencia en que se repite cada habilidad o conocimiento.
___________
English
Bot to scrap jobs from linkedin and make a distribution analysis of abilities

