# Prueba-Logyca

*

* Como ejecutar cada Punto
  
  Para ejecutar el primer punto en consola pararse sobre la carpeta PruebaLogyca y escribir el comando python Punto1.py se ejecutara el programa en consola.
  
  Para ejecutar el segundo punto en consola pararse sobre la carpeta PruebaLogyca y escribir el comando python Punto2.py se ejecutara el programa en consola.
  
  Para ejecutar los puntos 3 4 y 5, se debe posicionar en consola sobre la carpeta que se llama punto3-4-5 y acontinuación ejecutar el comando pip install -r requirements.txt 
  
  A continuación cambiar de directorio al del proyecto django el cual lleva por nombre punto345 y ejecutar el comando python manage.py runserver
  
  Para el punto 3
  
  Abrir postman o Talend API Tester, seleccionar el metodo GET y escribir la url como sigue para ejecutar cada endppoint. 
  
  Para ejecutar el endpoint  que contiene los primeros n numero primos se debe escribir http://(URL del servidor local)/numeroprimo?numero=(el numero que se desea consultar)
  Para ejecutar el endpoint  que contiene los primeros n pares de numero primos gemelos se debe escribir http://(URL del servidor local)/primosgemelos?numero=(el numero que se desea consultar)
  
  Se mostrará en el body de la herramienta utilizada los numeros calculados en formato json.
  
  Los Puntos 4 y 5 los uni en uno solo por lo que simplemente hay que correr el servidor y copiar en una pestaña de chrome la IP del servidor local esto renderizará la "pagina Principal" con la posibilida
  de ejecutar los dos endpoints. Dependiendo del numero a consultar se debe cambiar el numero por defecto que aparece en la url 
  ejemplo:
  en chrome poner
  http://127.0.0.1:8000
  
  y hacer click en alguno de los links 
  
  se mostrara en la url de n numeros primos algo asi 
  http://127.0.0.1:8000/numerosprimos?numero=1
  
  se debe variar el valor de numero al valor que se desee consultar.
  
  si la consulta no existe aparece un mensaje diciendo que los datos se almacenaron correctamente en la base de datos 
  
  para el endpoint n pares de numeros primos gemelos lo mismo. 
  
  Advierto que para este ultimo endpoint tuve un bug que no alcancé a solucionar  y es que si ya se consultó ese numero renderiza todos los valores almacenados en la base de datos.
