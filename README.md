# API-Rest-OpenSoruce-Code-Code
Interfaz de programacion de Aplicaciones - Transferencia de Estado Representacional Cursos Online-Gratis

## ¿Como hacer las peteciones en las colecciones de Postman?

1. Primero vamos a tener que generar una clave/password.

    * [bcrypt](https://bcrypt-generator.com/)

    **Ejemplo: carlos tevez == $2a$12$GA/DJb2lHWN1YG488bgODOlpaYbfyVRjq.voOu56fM4wEUgc/Cr.q**

2. Una vez la clave este generada, vamos a cargar un usuario en la base de datos (con la clave genereda anteriormente). 

    * Puede cargar al usuario via http://127.0.0.1:8000/docs o via Postman (una vez obtenga la coleccion). 
    * Otra opcion es http://127.0.0.1:8000/redoc

    **Nota Recordar tambien el nombre de usuario (username)**

3. Ya cargamos al usurio en la base de datos, con su clave hasheada (HASH), obvio nosotros por ahora sabemos la contraseña, por que es un entorno de prueba.

    * Ahora para poder hacer las otras operaciones, como por ejemplo ver todos los usuarios, vamos a tener que generar un token. 
    * El token se genera en la coleccion de Postman, en la carpeta Authenticate/(POST)Obtener token.
    * En Body/form-data, tendria que haber un formulario con los siguientes key y values: 

        * Key:                  values: 
            * username:         tevez
            * password:         carlos tevez (la contraseña en el formulario de postman va en texto plano y no la hasheada); 
    
    * Listo, ahora hay que darle a "Send", esto va generar un token, (tienes un minuto antes de que el token caduque para poder hacer las operaciones)

4. Para poder hacer todas las restantes operaciones, tendrias que copiar el token generado y pasarselo en la barra de postman: 

    * Authorization/Bearer Token y pasar el token generado o copiarlo ahi. 
    * Le das a "Send"m y podrias hacer la operacion que necesites o quieras ver, por ejemplo la de obtener todos los usuarios.


**Capas falten más pasos pero es lo que puede hacer -_-**
